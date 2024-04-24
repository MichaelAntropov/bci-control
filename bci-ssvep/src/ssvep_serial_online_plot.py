from datetime import datetime
import threading
import time


import numpy as np

import matplotlib.pyplot as plt
import pylsl
import serial
from matplotlib.animation import FuncAnimation

COM_PORT = 'COM8'
BAUD_RATE = 9600

ser = None

x_time_from_start = []
x_time_timestamp = []
x_time_local_clock = []
y_values = []

values_standardized = False
standardized_threshold = 500

now = datetime.now()
csv_filepath = f'C:\\recordings\\.META\\ssvep_check_{now.strftime("%Y-%m-%d_%H-%M-%S")}.csv'


def read_serial():
    time_start = time.time()
    while True:
        timestamp = time.time()
        local_clock_time = pylsl.local_clock()
        value = ser.readline().decode().strip()

        if value:
            try:
                int_value = 1024 - int(value)
            except ValueError:
                continue

            x_time_timestamp.append(timestamp)
            x_time_from_start.append((timestamp - time_start))
            x_time_local_clock.append(local_clock_time)

            if values_standardized:
                y_values.append(1 if int_value > standardized_threshold else 0)
            else:
                y_values.append(int_value)

            # print(timestamp - time_start)
            # print(f'{str(timestamp)[:14]}: {value}')


def update(frame):
    line.set_data(x_time_from_start[-600:], y_values[-600:])
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,


if __name__ == '__main__':
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=0.008)

    figure = plt.figure()
    figure.canvas.manager.set_window_title(f'Light intensity(Online), COM={COM_PORT}, BAUD={BAUD_RATE}')
    figure.legend()
    figure.set_size_inches(10, 3)

    line, = plt.plot(x_time_from_start, y_values, '-')
    if values_standardized:
        plt.ylim(-0.2, 1.2)
    else:
        plt.ylim(0, 1024)

    plt.xlabel('Time(s)')
    plt.ylabel('Light intensity')

    data_acquisition = threading.Thread(target=read_serial, daemon=True)
    data_acquisition.start()

    animation = FuncAnimation(figure, update, interval=17)
    plt.show()

    data = np.column_stack((x_time_timestamp, x_time_from_start, x_time_local_clock, y_values))
    print(data)
    np.savetxt(csv_filepath, data,
               delimiter=',',
               header="timestamp,timestamp_from_start,local_clock,value",
               comments='')

