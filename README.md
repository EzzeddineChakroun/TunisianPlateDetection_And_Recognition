# TunisianPlateDetection_And_Recognition <br>
This repository contains an implementation of Tunisian Plate Detection and Recognition<br>
The project contains three parts:<br><br>
1) detect_plate.py: <br>
The script defines several functions for detecting and processing license plates in images.<br>
The make_prediction function takes an image and two objects, a feature extractor and a model, and uses them to detect objects in the image. <br>
The detect_objects function uses a model name to load a specific object detection model, along with its associated feature extractor, and uses them to detect objects in an image. If the function detects a license plate in the image, it crops the image to just include the plate. <br>Finally, the preprocess_plate function takes the cropped license plate image and rotates it so that it is aligned properly.<br>
The detect_plate function is the main entry point for using these functions; it takes an image file path and an optional model index and returns the processed license plate image.<br><br>
2) ocr_plate.py:<br>
This script defines a function for performing optical character recognition (OCR) on an image of a license plate. The function uses the easyocr library to do the OCR. The function takes the license plate image and a list of languages to recognize as input and returns a list of detected text strings in the image. The detail parameter in the reader.readtext method is set to 0, which means that the function will only return the text strings and not the bounding boxes of the detected text. This can be useful for simplifying the output and just extracting the detected text without any additional information.<br><br>
3) main.py:<br>
This code defines a simple script for testing the license plate detection and OCR functions. The script loops through all the images in a specified folder and applies the detect_plate function to each image to detect the license plate. If the function detects a license plate in the image, the script applies the plate_ocr function to the detected license plate to perform OCR on it and extract the plate number. The script then prints the name of the image and the detected plate number. This code is useful for testing the performance of the license plate detection and OCR functions on a set of images and ensuring that they are working correctly.
<br><br> Usage:<br>
1)Install the requirements :pip install -r requirement<br>
2)To use this script, you need to provide the path to the folder containing the images to test as an argument to the script. For example, if the images are in a folder named "images" in the current directory, you can run the script as follows:<br>
python main.py images<br>
Alternatively, you can specify a different path to the folder containing the images, like this:<br>
python script.py /path/to/images<br>
Once the script is running, it will detect the license plates in the images and print the plate numbers for each image. If no license plate is detected in an image, it will print a message saying "No plate detected".
