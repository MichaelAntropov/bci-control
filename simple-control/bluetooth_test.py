import serial

# Sends command to arduino via Bluetooth: 0 or 1

ser = serial.Serial('COM7', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

while True:
    cmd = input("LED command: ")
    if cmd == "1":
        ser.write(b'1')

    if cmd == "0":
        ser.write(b'0')
