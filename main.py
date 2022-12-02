from detect_plate import detect_plate
from ocr_plate import plate_ocr
import os

#Testing Folder 
testing_images = "images" 
for image_name in os.listdir(testing_images):
    image_path = os.path.join(testing_images,image_name)
    detected_plate = detect_plate(image_path)
    if (detected_plate is None):
        print("image_name: ",image_name,". No plate detected ")
    else:
        plate_number = plate_ocr(detected_plate)
        print("image_name: ",image_name,". plate_number : ",plate_number)
