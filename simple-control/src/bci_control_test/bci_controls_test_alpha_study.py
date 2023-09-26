from pylsl import StreamInlet, resolve_stream

print("Looking for alpha-active-result stream...")
streams_result = resolve_stream('name', 'alpha-active-result')
# create a new inlet to read from the stream
inlet_result = StreamInlet(streams_result[0])
print("Stream alpha-active-result found!")

command_sample_threshold = 5
forward_sample_counter = [0]


def move_in_direction(direction, sample_counter):
    if sample_counter[0] > 0:
        if sample_counter[0] > command_sample_threshold:
            sample_counter[0] = 0
        else:
            sample_counter[0] += 1
    else:
        print(direction)
        sample_counter[0] += 1


while True:
    sample_result, _ = inlet_result.pull_sample()

    if sample_result[0] > 0.8:  # Close your eyes (spike in 8-14 Hz range)
        move_in_direction("FORWARD", forward_sample_counter)
