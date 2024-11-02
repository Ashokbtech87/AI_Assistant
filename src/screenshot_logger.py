# src/screenshot_logger.py

import os
import time
import threading
import logging
import pyautogui
import openpyxl
from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
from config import EXCEL_LOG_FILE, TEMP_STORAGE_PATH, SCREENSHOT_INTERVAL

recording = False

def start_recording():
    global recording
    recording = True
    thread = threading.Thread(target=record_screenshots)
    thread.start()
    logging.info("Recording started.")

def stop_recording():
    global recording
    recording = False
    logging.info("Recording stopped.")

def record_screenshots():
    wb = Workbook()
    ws = wb.active
    ws.title = "Activity Log"
    ws.append(["Timestamp", "Application", "Activity Description", "Screenshot"])

    while recording:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        screenshot_path = os.path.join(TEMP_STORAGE_PATH, f'screenshot_{timestamp}.png')
        pyautogui.screenshot(screenshot_path)

        app_name = get_active_window_title()
        activity_desc = "Recorded activity"

        img = ExcelImage(screenshot_path)
        img.width, img.height = img.width * 0.5, img.height * 0.5

        ws.append([timestamp, app_name, activity_desc])
        ws.add_image(img, f'D{ws.max_row}')

        time.sleep(SCREENSHOT_INTERVAL)

    wb.save(EXCEL_LOG_FILE)

def get_active_window_title():
    try:
        from win32gui import GetWindowText, GetForegroundWindow
        return GetWindowText(GetForegroundWindow())
    except ImportError:
        return "Unknown"
