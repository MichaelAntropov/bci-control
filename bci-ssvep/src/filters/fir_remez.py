import logging.config
import math
import os.path
from pathlib import Path

import numpy as np
import pyxdf
from scipy import signal

from src.logconfig import log_init


logging.config.dictConfig(log_init.init_log_cfg(__file__))
log = logging.getLogger(__name__)


def apply_fir_remez_and_save_csv(xdf_file_path, dir_to_save_csv, frequencies: list, seconds: tuple,
                                 sampling_rate=125, band=(1, 45), numtaps=70, desired=(0, 1, 0),
                                 electrode_index=13):

    streams, file_header = pyxdf.load_xdf(xdf_file_path)

    data_raw = {'eeg': {}, 'markers': {}}
    for stream in streams:
        if stream['info']['name'] == ['eeg']:
            data_raw['eeg']['time_series'] = stream['time_series'].T[electrode_index]
            data_raw['eeg']['time_stamps'] = stream['time_stamps']
        if stream['info']['name'] == ['markers']:
            data_raw['markers']['names'] = stream['time_series']
            data_raw['markers']['time_stamps'] = stream['time_stamps']

    edges = [0, band[0] - 0.5, band[0], band[1], band[1] + 5, sampling_rate * 0.5]

    # Design the FIR filter using remez algorithm
    filter_design = signal.remez(numtaps, edges, desired, fs=sampling_rate)

    filtered_data = signal.convolve(data_raw['eeg']['time_series'], filter_design, mode='same')

    filtered_data = filtered_data
    time_stamps = data_raw['eeg']['time_stamps']

    markers = {}
    for fr in frequencies:
        markers[f'{fr}hz'] = []
        start = 0
        for time, name in zip(data_raw['markers']['time_stamps'], data_raw['markers']['names']):
            if str(fr) in name[0] and 'start' in name[0]:
                start = time
            if str(fr) in name[0] and 'end' in name[0]:
                markers[f'{fr}hz'].append((start, time))

    final = {}
    for key in markers:
        final[key] = []
        for start, end in markers[key]:
            start_index = np.where(time_stamps >= start)[0][0] + math.ceil(seconds[0] * sampling_rate)
            end_index = start_index + sampling_rate * seconds[1]
            final[key].append(filtered_data[start_index:end_index])

    Path(dir_to_save_csv).mkdir(parents=True, exist_ok=True)
    for key in final:
        full_csv_file_path = os.path.join(dir_to_save_csv, f'{key}.csv')
        np.savetxt(full_csv_file_path, final[key], delimiter=',')
