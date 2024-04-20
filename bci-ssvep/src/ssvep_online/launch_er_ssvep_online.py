import configparser
import os
import subprocess
import time

import requests

server_url = "http://localhost:5000"

recordings_dir = r"C:\recordings"
group_id = "ssvep_sequenced_6_online"
subject_id = "1"
session_id = "1"

experiment_recorder_cmd = r"D:\ProgramFiles\Intheon\NeuroPype Academic Suite\Experiment Recorder\experiment-recorder.cmd"
er_file = r"D:\ProgramFiles\Intheon\NeuroPype Academic Suite\Experiment Recorder\settings\custom\ssvep_sequenced_6_online.er"


if __name__ == '__main__':
    # Parameters like 'group_id', 'subject_id' and 'session_id' passed as cmd command parameters because
    # in that case 'session_id' is ignored and not set properly
    config = configparser.ConfigParser()
    config.read(er_file)

    config.set("Output", option="recordings_dir", value=recordings_dir)
    config.set("Output", option="group_id", value=group_id)
    config.set("Output", option="subject_id", value=subject_id)
    config.set("Output", option="session_id", value=session_id)

    with open(er_file, "w") as f:
        config.write(f)

    # project_folder = os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parents[1])
    # venv_activate = os.path.join(project_folder, "venv", "Scripts", "activate")
    server = subprocess.Popen('flask --app="ssvep_server" run', stdout=subprocess.PIPE)
    er_recorder = subprocess.Popen(f""""{experiment_recorder_cmd}" /console --settings="{er_file}" --nogui=true""", stdout=subprocess.PIPE)

    time.sleep(7)
    requests.post(f"{server_url}/api/configure/xdf-file-folder", json={"xdfFileFolderPath": os.path.join(recordings_dir, group_id, subject_id, session_id)})

    server.wait()  # wait, otherwise the server is terminated
