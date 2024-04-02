import os
import time
from pathlib import Path

import yaml


def init_log_cfg(file):
    log_folder = os.path.join(Path(os.path.dirname(os.path.abspath(__file__))).parents[1], 'logs')
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logconfig.yaml')
    with open(config_file, 'r') as f:
        log_cfg = yaml.safe_load(f.read())
        log_cfg['handlers']['file']['filename'] = os.path.join(
            log_folder, f"log_{os.path.basename(file)[:-3]}_{time.strftime('%Y-%m-%d_%H-%M-%S')}.log"
        )
        return log_cfg