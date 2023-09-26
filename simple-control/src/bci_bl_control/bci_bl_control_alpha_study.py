import serial
from pylsl import StreamInlet, resolve_stream

directions = {"FORWARD": b'1',
              "BACK": b'2',
              "LEFT": b'3',
              "RIGHT": b'4'}

# Connecting to Model's Bluetooth
print("Connecting to RC(BL) model...")
ser = serial.Serial('COM6', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
print("Connected to RC(BL) model!")

print("Looking for alpha-active-result stream...")
streams_result = resolve_stream('name', 'alpha-active-result')
print("Stream alpha-active-result found!")

# Create a new inlet to read from the stream
inlet_result = StreamInlet(streams_result[0])

command_sample_threshold = 2
forward_sample_counter = [0]


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
    sample_result, _ = inlet_result.pull_sample()

    if sample_result[0] > 0.8:  # Close your eyes (spike in 8-14 Hz range)
        move_in_direction("FORWARD", forward_sample_counter)
