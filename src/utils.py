# src/utils.py

import os
import shutil
import logging

def setup_logging():
    logging.basicConfig(
        filename='assistant.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

def cleanup_temp_storage(temp_path):
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.makedirs(temp_path)

def ensure_directories(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
