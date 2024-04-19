import glob
import logging
import os

from flask import Flask, request
from pyxdf import pyxdf

import ssvep_online_process

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

log = app.logger
ssvep_online_process.log = log


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
def process__trial():
    data = request.json
    log.info(f"Process trial: {data}")
    markers: list = data['markers']
    target_frequency: int = data['targetFrequency']
    trial_result = ssvep_online_process.run_process_and_get_results_for_trial((markers[0], markers[1]), target_frequency)
    return trial_result
