import concurrent.futures
import functools
import logging.config
import operator
import os

import numpy as np
from sklearn.cross_decomposition import CCA
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.db_entities import Recording, ProcessParameters, ProcessResult
from src.filters import fir_remez
from src.logconfig import log_init

logging.config.dictConfig(log_init.init_log_cfg(__file__))
log = logging.getLogger(__name__)


max_threads = os.cpu_count()

database_url = 'sqlite:///../../database/data/ssvep-db.sqlite'
database_recordings_folder = os.path.abspath(r'../../database/data/recordings')
database_temp_folder = os.path.abspath(r'../../database/data/temp')

engine = create_engine(database_url)


def calculate_cca(ts_1, ts_2):
    time_series_1 = ts_1
    time_series_2 = ts_2

    cca = CCA(n_components=1)
    X = time_series_1.reshape(-1, 1)
    Y = time_series_2.reshape(-1, 1)
    cca.fit(X, Y)

    X_c, Y_c = cca.transform(X, Y)

    canonical_corr = np.corrcoef(X_c.T, Y_c.T)[0, 1]
    return canonical_corr


def export_csv_for_recording(xdf_file, save_dir, frequencies, seconds, numtaps, desired, sampling_rate, band, electrode_index):
    fir_remez.apply_fir_remez_and_save_csv(xdf_file, save_dir, frequencies,
                                           seconds=seconds,
                                           numtaps=numtaps,
                                           desired=desired,
                                           sampling_rate=sampling_rate,
                                           band=band,
                                           electrode_index=electrode_index)


def get_recordings(session: Session) -> list[Recording]:
    stmt = select(Recording).where(
        (Recording.parameters['duration_s'].as_float() == 6.0)
        & (Recording.parameters['frequencies'].as_string() == '["9","16","13"]')
    )

    result = list(session.scalars(stmt).all())
    log.info(f"Selected {len(result)} recordings to be processed")
    return result


def run_process_and_get_results_for_recording(recording: Recording, params: dict) -> (dict, str, dict):
    result = {'calculations': []}
    frequencies_timeseries = {}

    folder_to_csv = os.path.join(database_temp_folder, recording.xdf_file_path[:-4])

    for i in params['frequencies']:
        #  [1:, 1:] needed to cut header and first column
        frequencies_timeseries[f'{i}hz'] = np.loadtxt(os.path.join(folder_to_csv, f'{i}hz.csv'), delimiter=",", dtype=str)

    calibrations = {}
    for i in params['frequencies']:
        calibrations[f'{i}hz_1'] = frequencies_timeseries[f'{i}hz'][0]
        calibrations[f'{i}hz_2'] = frequencies_timeseries[f'{i}hz'][1]

    trials_to_test = {}
    for key in frequencies_timeseries.keys():
        trials_to_test[key] = frequencies_timeseries[key][2:]

    for freq_key, freq_time_series_arrays in trials_to_test.items():
        for freq_key_time_series in freq_time_series_arrays:
            trial_results = {}
            for i in params['frequencies']:
                trial_results[f'{i}hz'] = (calculate_cca(calibrations[f'{i}hz_1'],
                                                         freq_key_time_series) + calculate_cca(
                    calibrations[f'{i}hz_2'], freq_key_time_series)) / 2

            guessed_frequency = max(trial_results.items(), key=operator.itemgetter(1))[0]
            result['calculations'].append({'targetFrequency': freq_key,
                                           'calculationsResults': trial_results,
                                           'guessedFrequency': guessed_frequency,
                                           'isCorrect': 1 if guessed_frequency == freq_key else 0})

    result['total_trials_tested'] = len(result['calculations'])
    result['total_correct'] = functools.reduce(lambda current_total, k: current_total + k['isCorrect'],
                                               result['calculations'], 0)
    result['accuracy'] = result['total_correct'] / result['total_trials_tested']

    notes = None
    meta = None
    return result, notes, meta


def run_cca_np_fir():
    log.info("Start processing...")

    with Session(engine) as session, session.begin():
        process_parameters = ProcessParameters.find_proc_params_by_params(parameters, session=session)
        if process_parameters is None:
            process_parameters = ProcessParameters(parameters=parameters)
            session.add(process_parameters)
            session.flush()
            log.info(f"Process parameters did not exist. Created {process_parameters}")
        else:
            log.info(f"Found existing process parameters - {process_parameters}")

        # Prepare csv files after segmentation in temp folder
        recordings = get_recordings(session)

        with concurrent.futures.ProcessPoolExecutor(max_workers=max_threads) as executor:
            log.info(f"Submit {len(recordings)} *.xdf files to be processed into CSV through custom filter")
            for recording in recordings:
                abs_xdf_file_path = os.path.join(database_recordings_folder, recording.xdf_file_path)
                folder_name = recording.xdf_file_path[:-4]
                folder_to_save_csv = os.path.join(database_temp_folder, folder_name)
                executor.submit(export_csv_for_recording,
                                #  export_csv_for_recording arguments:
                                #  parameters have to be provided directly because in executor parameters scope changes
                                abs_xdf_file_path,
                                folder_to_save_csv,
                                parameters['frequencies'],
                                tuple(parameters['segmentTimeLimits']),
                                parameters['firParams']['numtaps'],
                                tuple(parameters['firParams']['desired']),
                                parameters['firParams']['samplingRate'],
                                tuple(parameters['firParams']['band']),
                                parameters['firParams']['electrodeIndex'])

            log.info(f"Wait for executor to finish export of CSVs")
            executor.shutdown(wait=True)
            log.info(f"CSVs exported and saved into: {database_temp_folder}")

        future_results = {}
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_threads) as executor:
            for recording in recordings:
                future_result = executor.submit(run_process_and_get_results_for_recording,
                                                #  run_process_and_get_results_for_recording arguments:
                                                #  parameters have to be provided because in executor parameters scope changes
                                                recording, parameters)
                future_results[recording] = future_result

            log.info(f"Wait for executor to finish CCA analysis on each recording ({len(recordings)} items)")
            executor.shutdown(wait=True)
            log.info(f"CCA analysis for each recording is finished, processed {len(future_results)} recordings")

        updated = 0
        inserted = 0
        for recording, future_result in future_results.items():
            result, notes, meta = future_result.result()
            process_result = ProcessResult.find_proc_result_by_params_id_and_recording_id(process_parameters.id,
                                                                                          recording.id,
                                                                                          session=session)
            if process_result is None:
                process_result = ProcessResult()
                process_result.parameters_id = process_parameters.id
                process_result.recording_id = recording.id
                process_result.results = result
                process_result.notes = notes
                process_result.meta = meta
                session.add(process_result)
                inserted = inserted + 1
            else:
                process_result.results = result
                process_result.notes = notes
                process_result.meta = meta
                updated = updated + 1

        session.flush()
        log.info(f"Inserted new {inserted} results. Updated {updated} results")


if __name__ == '__main__':
    log.info("=" * 160)
    log.info("Init processing...")
    parameters = {
        'method': 'sklearn CCA, n_components=1, first 2 vs rest averaged, fir custom',
        'firParams': {
            'design': 'remez',
            'band': [1, 45],
            'samplingRate': 125,
            'numtaps': 70,
            'desired': [0, 1, 0],
            'electrodeIndex': 13
        },
        'frequencies': [9, 16, 13],
        'segmentTimeLimits': [0.14, 6],
        'trialSequence': [9, 16, 13] * 8
    }
    log.info(f"Database recordings folder: {database_recordings_folder}")
    log.info(f"Database temp folder: {database_temp_folder}")
    log.info(f"Max threads: {max_threads}")
    log.info(f"Parameters: {parameters}")
    run_cca_np_fir()
