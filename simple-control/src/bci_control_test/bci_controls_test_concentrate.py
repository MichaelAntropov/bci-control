from pylsl import StreamInlet, resolve_stream

# Gets data from BCI GUI LSL stream and outputs directions
# Best to use 8 channels when Focus Widget is used

print("Looking for an EEG stream...")
streams_emg = resolve_stream('name', 'obci_eeg1')
streams_focus = resolve_stream('name', 'obci_eeg2')
# create a new inlet to read from the stream
inlet_emg = StreamInlet(streams_emg[0])
inlet_focus = StreamInlet(streams_focus[0])

command_sample_threshold = 20
focus_sample_counter = 0


while True:
    sample_emg, _ = inlet_emg.pull_sample()
    sample_focus, _ = inlet_focus.pull_sample()

    if sample_emg[2] > 0.8:  # Move jaw left
        print("LEFT")
    elif sample_emg[3] > 0.8:  # Move jaw right
        print("RIGHT")
    elif sample_emg[1] > 0.8:  # Blink several times
        print("BACK")
    elif sample_focus[0] > 0.8: # Concentrate
        if focus_sample_counter > 0:
            if focus_sample_counter > command_sample_threshold:
                focus_sample_counter = 0
            else:
                focus_sample_counter += 1
        else:
            print("FORWARD")
            focus_sample_counter += 1
