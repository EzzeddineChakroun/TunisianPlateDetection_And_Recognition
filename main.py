import easyocr
import os

from detect_plate import detect_plate
from ocr_plate import plate_ocr

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("testing_images", help="Path to the folder containing the images to test", default="images")
args = parser.parse_args()

#Testing Folder 
for image_name in os.listdir(args.testing_images):
    image_path = os.path.join(args.testing_images,image_name)
    detected_plate = detect_plate(image_path)
    if (detected_plate is None):
        print("image_name: ",image_name,". No plate detected ")
    else:
        plate_number = plate_ocr(detected_plate)
        print("image_name: ",image_name,". plate_number : ",plate_number)
