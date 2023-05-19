import time
from collections import deque

import matplotlib.pyplot as plt
from pylsl import StreamInlet, resolve_stream

last_print = time.time()
fps_counter = deque(maxlen=150)
duration = 20

# first resolve an EEG stream on the lab network
print("Looking for an EEG stream...")
streams = resolve_stream('name', 'obci_eeg1')
# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

channel_data = {}

for i in range(duration):  # how many iterations. Eventually this would be a while True

    for i in range(16):  # each of the 16 channels here
        sample, timestamp = inlet.pull_sample()
        if i not in channel_data:
            channel_data[i] = sample
        else:
            channel_data[i].append(sample)

    fps_counter.append(time.time() - last_print)
    last_print = time.time()
    cur_raw_hz = 1 / (sum(fps_counter) / len(fps_counter))
    print(cur_raw_hz)

for chan in channel_data:
    plt.plot(channel_data[chan][:60])
plt.show()
