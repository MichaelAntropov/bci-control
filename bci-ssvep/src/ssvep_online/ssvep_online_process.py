import math
import operator

import numpy as np
from pyxdf import pyxdf
import logging

from scipy import signal
from sklearn.cross_decomposition import CCA

from src.process.it_cca import ITCCA

log: logging.Logger

frequencies = [8, 9, 13, 14, 15, 16]
cutoff = [7, 49]
sampling_rate = 125
electrode_index = 13
seconds = [0.14, 3]
filter_design = signal.firwin(70, [cutoff[0] / sampling_rate, cutoff[1] / sampling_rate], pass_zero=False)

xdf_file_path = ""
calibrations = {}
result = {'calculations': []}


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


def calculate_itcca(ts_1, ts_2):
    X = ts_1
    Y = ts_2
    itcca = ITCCA(n_components=2, alpha=0.5)
    itcca.fit(X, Y)
    X_transformed = itcca.transform(X)
    Y_transformed = itcca.transform(Y)
    correlation_coefficient = itcca.correlation_
    canonical_corr = np.corrcoef(X_transformed.T, Y_transformed.T)[0, 1]
    return canonical_corr


def process_calibration_trials():
    log.info(f"Process calibration trials in XDF file: {xdf_file_path}")

    streams, file_header = pyxdf.load_xdf(xdf_file_path)

    data_raw = {'eeg': {}, 'markers': {}}
    for stream in streams:
        if stream['info']['name'] == ['eeg']:
            data_raw['eeg']['time_series'] = stream['time_series'].T[electrode_index]
            data_raw['eeg']['time_stamps'] = stream['time_stamps']
        if stream['info']['name'] == ['markers']:
            data_raw['markers']['names'] = stream['time_series']
            data_raw['markers']['time_stamps'] = stream['time_stamps']

    filtered_data = signal.convolve(data_raw['eeg']['time_series'], filter_design, mode='same')

    filtered_data = filtered_data
    time_stamps = data_raw['eeg']['time_stamps']

    markers = {}
    for fr in frequencies:
        markers[f'{fr}hz'] = []
        start = 0
        for time, name in zip(data_raw['markers']['time_stamps'], data_raw['markers']['names']):
            if str(fr) in name[0] and 'start' in name[0] and 'test' in name[0]:
                start = time
            if str(fr) in name[0] and 'end' in name[0] and 'test' in name[0]:
                markers[f'{fr}hz'].append((start, time))

    for key in markers:
        calibrations[key] = []
        for start, end in markers[key]:
            raw_start_index = np.where(time_stamps >= start)[0][0]
            start_index = raw_start_index + math.ceil(seconds[0] * sampling_rate)
            end_index = raw_start_index + sampling_rate * seconds[1]
            calibrations[key].append(filtered_data[start_index:end_index])

    for key, val in calibrations.items():
        log.info(f"Processed calibration frequency {key}: {len(calibrations[key])}")


def run_process_and_get_results_for_trial(markers: tuple, target_frequency: int):
    log.info(f"Start process and get result for trial")
    trial_start, trial_end = markers

    streams, file_header = pyxdf.load_xdf(xdf_file_path)
    data_raw = {'eeg': {}, 'markers': {}}
    for stream in streams:
        if stream['info']['name'] == ['eeg']:
            data_raw['eeg']['time_series'] = stream['time_series'].T[electrode_index]
            data_raw['eeg']['time_stamps'] = stream['time_stamps']
        if stream['info']['name'] == ['markers']:
            data_raw['markers']['names'] = stream['time_series']
            data_raw['markers']['time_stamps'] = stream['time_stamps']

    start, end = None, None
    for time, name in zip(data_raw['markers']['time_stamps'], data_raw['markers']['names']):
        if trial_start == name[0]:
            start = time
        if trial_end == name[0]:
            end = time

    start_index_raw = np.where(data_raw['eeg']['time_stamps'] >= start)[0][0]
    end_index = start_index_raw + sampling_rate * seconds[1]

    filtered_data = signal.convolve(data_raw['eeg']['time_series'][start_index_raw:end_index], filter_design, mode='same')

    filtered_data = filtered_data[math.ceil(seconds[0] * sampling_rate):]

    trial_results_cca = {}
    trial_results_itcca = {}
    trial_results_mix = {}

    for key, calibration_list in calibrations.items():
        trial_results_cca[key] = 0
        trial_results_itcca[key] = 0

        for calibration_trial in calibration_list:
            trial_results_cca[key] += calculate_cca(calibration_trial, filtered_data)
            trial_results_itcca[key] += calculate_itcca(calibration_trial, filtered_data)

        trial_results_mix[key] = trial_results_cca[key] + trial_results_itcca[key]

    guessed_frequency = max(trial_results_cca.items(), key=operator.itemgetter(1))[0]
    guessed_frequency_itcca = max(trial_results_itcca.items(), key=operator.itemgetter(1))[0]
    guessed_frequency_mix = max(trial_results_mix.items(), key=operator.itemgetter(1))[0]

    trial_result = {'targetFrequency': target_frequency,
                    'calculationsResultsCCA': trial_results_cca,
                    'calculationsResultsITCCA': trial_results_itcca,
                    'calculationsResultsMix': trial_results_mix,
                    'guessedFrequencyCCA': guessed_frequency,
                    'guessedFrequencyITCCA': guessed_frequency_itcca,
                    'guessedFrequencyMix': guessed_frequency_mix,
                    'isCorrectCCA': 1 if guessed_frequency == target_frequency else 0,
                    'isCorrectITCCA': 1 if guessed_frequency_itcca == target_frequency else 0,
                    'isCorrectMix': 1 if guessed_frequency_mix == target_frequency else 0}

    log.info(f"Trial result: {trial_result}")
    result['calculations'].append(trial_result)

    return trial_result
