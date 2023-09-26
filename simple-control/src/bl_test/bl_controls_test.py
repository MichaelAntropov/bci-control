# import tkinter module
from tkinter import *
from tkinter.ttk import *

import serial

running = False
jobid = ""
directions = {"FORWARD": b'1',
              "BACK": b'2',
              "LEFT": b'3',
              "RIGHT": b'4'}


def start_motor(direction):
    print("starting motor...(%s)" % direction)
    move(direction)


def stop_motor():
    global jobid
    root.after_cancel(jobid)
    print("stopping motor...")


def move(direction):
    global jobid
    print(f"Moving ({direction}[{directions[direction]}])")
    ser.write(directions[direction])
    jobid = root.after(70, move, direction)


# Connecting to Model's Bluetooth
ser = serial.Serial('COM7', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
# creating main tkinter window/toplevel
root = Tk()
root.geometry("400x300")
root.title("Simple Control")
root.resizable(False, False)

# this will create a label widget
b_f = Button(text="FORWARD")
b_b = Button(text="BACK")
b_l = Button(text="LEFT")
b_r = Button(text="RIGHT")

# grid method to arrange labels in respective
# rows and columns as specified
b_f.place(x=160, y=10, width=80, height=80)
b_b.place(x=160, y=210, width=80, height=80)
b_l.place(x=60, y=110, width=80, height=80)
b_r.place(x=260, y=110, width=80, height=80)

b_f.bind('<ButtonPress-1>', lambda event, direction="FORWARD": start_motor(direction))
b_f.bind('<ButtonRelease-1>', lambda event: stop_motor())

b_b.bind('<ButtonPress-1>', lambda event, direction="BACK": start_motor(direction))
b_b.bind('<ButtonRelease-1>', lambda event: stop_motor())

b_l.bind('<ButtonPress-1>', lambda event, direction="LEFT": start_motor(direction))
b_l.bind('<ButtonRelease-1>', lambda event: stop_motor())

b_r.bind('<ButtonPress-1>', lambda event, direction="RIGHT": start_motor(direction))
b_r.bind('<ButtonRelease-1>', lambda event: stop_motor())

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
