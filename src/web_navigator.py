# src/web_navigator.py

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from config import TEMP_STORAGE_PATH

def navigate_and_save_images(url):
    print(f"Starting navigation to URL: {url}")  # Debugging statement
    try:
        # Set up Chrome options for headless browsing
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (optional)
        
        # Initialize the Chrome driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        print("Page loaded successfully.")  # Debugging statement
        time.sleep(3)  # Give time for images to load

        # Locate image elements on the page
        images = driver.find_elements(By.TAG_NAME, 'img')
        if not images:
            print("No images found on the page.")  # Debugging statement
            return
        
        img_urls = [img.get_attribute('src') for img in images if img.get_attribute('src')]
        print(f"Found {len(img_urls)} images on the page.")  # Debugging statement

        # Ensure temp storage path exists
        if not os.path.exists(TEMP_STORAGE_PATH):
            os.makedirs(TEMP_STORAGE_PATH)
        
        # Save each image temporarily
        for idx, img_url in enumerate(img_urls):
            try:
                driver.get(img_url)
                screenshot_path = os.path.join(TEMP_STORAGE_PATH, f'image_{idx}.png')
                driver.save_screenshot(screenshot_path)
                print(f"Saved image {idx + 1}/{len(img_urls)} to {screenshot_path}")  # Debugging statement
            except Exception as e:
                logging.error(f"Failed to save image {idx} from {img_url}: {e}")

        driver.quit()
        print("Navigation and image saving completed.")  # Debugging statement

    except Exception as e:
        logging.error(f"Failed to navigate and save images from {url}: {e}")
        print(f"An error occurred: {e}")  # Print error for visibility
    finally:
        if 'driver' in locals():
            driver.quit()
            print("Web driver closed.")  # Confirm driver is closed
