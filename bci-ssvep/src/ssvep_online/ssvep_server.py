import glob
import logging
import os

import serial
from flask import Flask, request

import ssvep_online_process

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

log = app.logger
ssvep_online_process.log = log

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
# arduino = None

direction_types = {
    "ROTATE_LEFT": {"servo": 1, "amount": 20},
    "ROTATE_RIGHT": {"servo": 1, "amount": -20},
    "EXTEND_HORIZONTAL": {"servo": 2, "amount": 15},
    "RETRACT_HORIZONTAL": {"servo": 2, "amount": -15},
    "EXTEND_VERTICAL": {"servo": 3, "amount": 15},
    "RETRACT_VERTICAL": {"servo": 3, "amount": -15},
    "GRAB": {"servo": 4, "amount": -15},
    "RELEASE": {"servo": 4, "amount": 15},
}


@app.route("/api/configure/xdf-file-folder", methods=["POST"])
def configure_xdf_file_name():
    data = request.json
    xdf_folder_path = data['xdfFileFolderPath']
    list_of_files = glob.glob(os.path.join(xdf_folder_path, "*.xdf"))
    latest_file = max(list_of_files, key=os.path.getctime)
    ssvep_online_process.xdf_file_path = latest_file
    return f"XDF File Configured: {str(ssvep_online_process.xdf_file_path)}"


@app.route("/api/xdf-file", methods=["GET"])
def get_xdf_file_name():
    app.logger.info(f"XDF File Folder: {ssvep_online_process.xdf_file_path}")
    return f"{ssvep_online_process.xdf_file_path}"


@app.route("/api/process/calibration-trials", methods=["POST"])
def process_calibration_trials():
    ssvep_online_process.process_calibration_trials()
    return "OK"


@app.route("/api/process/process-trial", methods=["POST"])
def process_trial():
    data = request.json
    log.info(f"Process trial: {data}")
    markers: list = data['markers']
    target_frequency: int = data['targetFrequency']
    trial_result = ssvep_online_process.run_process_and_get_results_for_trial((markers[0], markers[1]), target_frequency)
    return trial_result


@app.route("/api/process/process-trial/guess-only", methods=["POST"])
def process_trial_guess_only():
    data = request.json
    log.info(f"Process trial(guess only): {data}")
    markers: list = data['markers']
    trial_result = ssvep_online_process.run_process_and_get_guessed_frequency_only((markers[0], markers[1]))
    return trial_result


@app.route("/api/process/process-trial/guess-only/result/<result_type>", methods=["POST"])
def process_trial_guess_only_result(result_type):
    log.info(f"Received result type: {result_type}")
    ssvep_online_process.record_result_for_last_trial(result_type)
    return result_type


@app.route("/api/arm-control/move-servo/<servo_number>/<degrees>", methods=["POST"])
def arm_control_servo(servo_number, degrees):
    log.info(f'{servo_number}, {degrees}')
    command = 10_000 + int(servo_number) * 1000 + int(degrees)
    arduino.write(bytes(str(command), 'utf-8'))
    return "OK"


@app.route("/api/arm-control/move/direction/<direction_type>", methods=["POST"])
def arm_control_directional(direction_type):
    log.info(f'Direction type: {direction_type}')

    if direction_type in direction_types.keys():
        servo_num = direction_types[direction_type]["servo"]
        amount = direction_types[direction_type]["amount"]
        command = 20_000 + servo_num * 1_000 + (180 + amount)
        log.info(f'Command: {command}')
        arduino.write(bytes(str(command), 'utf-8'))
    return "OK"
