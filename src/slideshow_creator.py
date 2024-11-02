# srcslideshow_creator.py

import cv2
import os
import logging
from config import TEMP_STORAGE_PATH

def create_slideshow():
    images = [img for img in os.listdir(TEMP_STORAGE_PATH) if img.endswith('.png') or img.endswith('.jpg')]
    images.sort()

    if not images:
        logging.warning("No images found for slideshow.")
        return

    for img_name in images:
        img_path = os.path.join(TEMP_STORAGE_PATH, img_name)
        img = cv2.imread(img_path)
        cv2.imshow('Slideshow', img)
        cv2.waitKey(2000)  # Display each image for 2 seconds

    cv2.destroyAllWindows()
    logging.info("Slideshow completed.")
