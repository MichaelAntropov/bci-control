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

print("Looking for a FOCUS stream...")
streams_focus = resolve_stream('name', 'obci_eeg2')
print("FOCUS stream found!")

# create a new inlet to read from the stream
inlet_emg = StreamInlet(streams_emg[0])
inlet_focus = StreamInlet(streams_focus[0])

command_sample_threshold = 20

focus_sample_counter = [0]
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


while True:
    sample_emg, _ = inlet_emg.pull_sample()
    sample_focus, _ = inlet_focus.pull_sample()

    if sample_emg[2] > 0.8:  # Move jaw left
        move_in_direction("LEFT", left_sample_counter)
    elif sample_emg[3] > 0.8:  # Move jaw right
        move_in_direction("RIGHT", right_sample_counter)
    elif sample_emg[1] > 0.8:  # Blink several times
        move_in_direction("BACK", back_sample_counter)
    elif sample_focus[0] > 0.8:  # Concentrate
        move_in_direction("FORWARD", focus_sample_counter)
