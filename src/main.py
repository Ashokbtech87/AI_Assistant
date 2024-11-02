# src/main.py

import os
import time
import threading
import logging
from utils import setup_logging, cleanup_temp_storage, ensure_directories
from application_manager import open_application, close_application, switch_application
from web_navigator.py import navigate_and_save_images
from slideshow_creator import create_slideshow
from office_operations import create_word_document, create_excel_workbook, create_powerpoint_presentation
from screenshot_logger import start_recording, stop_recording
from config import TEMP_STORAGE_PATH, DATA_DIR

def main():
    setup_logging()
    ensure_directories([TEMP_STORAGE_PATH, DATA_DIR])
    cleanup_temp_storage(TEMP_STORAGE_PATH)

    print("Welcome to the AI-Powered Virtual Assistant")
    print("1. Open Application")
    print("2. Close Application")
    print("3. Switch Application")
    print("4. Navigate Web and Create Slideshow")
    print("5. Office Operations")
    print("6. Start Recording")
    print("7. Stop Recording")
    print("8. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            app_path = input("Enter the application path: ")
            open_application(app_path)
        elif choice == '2':
            process_name = input("Enter the process name: ")
            close_application(process_name)
        elif choice == '3':
            app_title = input("Enter the application title: ")
            switch_application(app_title)
        elif choice == '4':
            url = input("Enter the URL of the image gallery: ")
            navigate_and_save_images(url)
            create_slideshow()
            cleanup_temp_storage(TEMP_STORAGE_PATH)
        elif choice == '5':
            print("Office Operations:")
            print("a. Create Word Document")
            print("b. Create Excel Workbook")
            print("c. Create PowerPoint Presentation")
            op_choice = input("Enter your choice: ")
            if op_choice == 'a':
                content = input("Enter content for the Word document: ")
                save_path = input("Enter save path for the document: ")
                create_word_document(content, save_path)
            elif op_choice == 'b':
                data = input("Enter data for Excel workbook (comma-separated): ").split(',')
                save_path = input("Enter save path for the workbook: ")
                create_excel_workbook(data, save_path)
            elif op_choice == 'c':
                slides_content = input("Enter content for slides (comma-separated): ").split(',')
                save_path = input("Enter save path for the presentation: ")
                create_powerpoint_presentation(slides_content, save_path)
        elif choice == '6':
            start_recording()
        elif choice == '7':
            stop_recording()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
