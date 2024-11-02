# src/application_manager.py

import subprocess
import psutil
import logging
from pywinauto import Application

def open_application(app_path):
    try:
        subprocess.Popen(app_path)
        logging.info(f"Opened application: {app_path}")
    except Exception as e:
        logging.error(f"Failed to open application {app_path}: {e}")

def close_application(process_name):
    try:
        for proc in psutil.process_iter():
            if proc.name().lower() == process_name.lower():
                proc.kill()
                logging.info(f"Closed application: {process_name}")
    except Exception as e:
        logging.error(f"Failed to close application {process_name}: {e}")

def switch_application(app_title):
    try:
        app = Application().connect(title_re=app_title)
        app.top_window().set_focus()
        logging.info(f"Switched to application: {app_title}")
    except Exception as e:
        logging.error(f"Failed to switch to application {app_title}: {e}")
