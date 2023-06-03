import numpy as np
from pylsl import StreamInlet, resolve_stream

import serial

directions = {"FORWARD": b'1',
              "BACK": b'2',
              "LEFT": b'3',
              "RIGHT": b'4'}

# Setup:

# 1. Connecting to Model's Bluetooth
print("Connecting to RC(BL) model...")
ser = serial.Serial('COM7', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
print("Connected to RC(BL) model!")

# 2. Get data from BCI GUI LSL streams
print("Looking for an EMG stream...")
streams_emg = resolve_stream('name', 'obci_eeg1')
print("EMG stream found!")

print("Looking for a EEG(FFT) stream...")
streams_fft = resolve_stream('name', 'obci_eeg2')
print("EEG(FFT) stream found!")

# create a new inlet to read from the stream
inlet_emg = StreamInlet(streams_emg[0])
inlet_fft = StreamInlet(streams_fft[0])

command_sample_threshold = 20

forward_sample_counter = [0]
back_sample_counter = [0]
left_sample_counter = [0]
right_sample_counter = [0]


def move_in_direction(direction, sample_counter):
    if sample_counter[0] > 0:
        if sample_counter[0] > command_sample_threshold:
            sample_counter[0] = 0
        else:
            sample_counter[0] += 1
    else:
        print(direction)
        ser.write(directions[direction])
        sample_counter[0] += 1


channel_data = {}

while True:
    sample_emg, _ = inlet_emg.pull_sample()

    for i in range(8):
        sample, _ = inlet_fft.pull_sample()
        channel_data[i] = sample

    avg_channel = np.mean(np.array([channel_data[5][5:15],
                                    channel_data[6][5:15],
                                    channel_data[7][5:15]]), axis=0)
    value = np.std(avg_channel)

    if sample_emg[2] > 0.8:  # Move jaw left
        move_in_direction("LEFT", left_sample_counter)
    elif sample_emg[3] > 0.8:  # Move jaw right
        move_in_direction("RIGHT", right_sample_counter)
    elif sample_emg[1] > 0.8:  # Blink several times
        move_in_direction("BACK", back_sample_counter)
    elif value > 1.8:  # Close your eyes (spike in 8-12 Hz range)
        move_in_direction("FORWARD", forward_sample_counter)
