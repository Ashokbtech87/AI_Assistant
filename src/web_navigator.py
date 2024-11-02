# src/web_navigator.py

import os
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from config import TEMP_STORAGE_PATH

def navigate_and_save_images(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        images = driver.find_elements_by_tag_name('img')
        img_urls = [img.get_attribute('src') for img in images if img.get_attribute('src')]

        for idx, img_url in enumerate(img_urls):
            driver.get(img_url)
            driver.save_screenshot(os.path.join(TEMP_STORAGE_PATH, f'image_{idx}.png'))
            logging.info(f"Saved image {idx} from {img_url}")

        driver.quit()
    except Exception as e:
        logging.error(f"Failed to navigate and save images from {url}: {e}")
