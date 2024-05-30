import serial
import time
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))

time.sleep(5)
write_read('1160')
#
#
# is_start = True
#
# while True:
#     data = arduino.readlines()
#     if len(data) == 0:
#         time.sleep(0.05)
#     else:
#         [print(a.decode('utf-8'), end='') for a in data]
#         break
#
#
# while True:
#     num = input("Enter a number: ")  # Taking input from user
#     write_read(num)
#     while True:
#         data = arduino.readlines()
#         if len(data) == 0:
#             time.sleep(0.05)
#         else:
#             [print(a.decode('utf-8'), end='') for a in data]
#             break

