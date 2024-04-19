import math
import os
from pathlib import Path

import mne
import numpy as np
from pyxdf import pyxdf


def apply_fir_firwin_and_save_csv(xdf_file_path, dir_to_save_csv, frequencies: list, seconds: tuple,
                                  sampling_rate=125, cutoff=(5, 49), electrode_index=13):

    streams, file_header = pyxdf.load_xdf(xdf_file_path)

    data_raw = {'eeg': {}, 'markers': {}}
    for stream in streams:
        if stream['info']['name'] == ['eeg']:
            data_raw['eeg']['time_series'] = stream['time_series'].T[electrode_index]
            data_raw['eeg']['time_stamps'] = stream['time_stamps']
        if stream['info']['name'] == ['markers']:
            data_raw['markers']['names'] = stream['time_series']
            data_raw['markers']['time_stamps'] = stream['time_stamps']

    filtered_data = mne.filter.filter_data(data_raw['eeg']['time_series'].astype(np.float64), sfreq=sampling_rate,
                                           l_freq=cutoff[0], h_freq=cutoff[1], verbose=0, method='fir')

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
