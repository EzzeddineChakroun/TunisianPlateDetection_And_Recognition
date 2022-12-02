
from transformers import AutoFeatureExtractor, YolosForObjectDetection, DetrForObjectDetection
import torch
import numpy as np
from PIL import Image
import cv2
from skimage.color import rgb2gray
from skimage.feature import canny
from skimage.transform import hough_line, hough_line_peaks
from skimage.transform import rotate

#Define needed functions

#prediction function of plate detection models  
def make_prediction(img, feature_extractor, model):
    inputs = feature_extractor(img, return_tensors="pt")
    outputs = model(**inputs)
    img_size = torch.tensor([tuple(reversed(img.size))])
    processed_outputs = feature_extractor.post_process(outputs, img_size)
    return processed_outputs[0]

#Detect plate and crop it  
def detect_objects(model_name,image,threshold):
    try:
        #Extract model and feature extractor
        feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
        if "yolos" in model_name:
            model = YolosForObjectDetection.from_pretrained(model_name)
        elif "detr" in model_name:
            model = DetrForObjectDetection.from_pretrained(model_name)    
        #Make prediction
        processed_outputs = make_prediction(image, feature_extractor, model)
        keep = processed_outputs["scores"] > threshold
        boxes = processed_outputs["boxes"][keep].tolist()
        labels = processed_outputs["labels"][keep].tolist()
        labels = [model.config.id2label[x] for x in labels]
        output=None
        for (xmin, ymin, xmax, ymax), label in zip( boxes, labels):
            if label == 'license-plates':
                output = image.crop((xmin, ymin, xmax, ymax))
        return output
    except Exception as e:
        print("Error",e)
        return None

#Alignment of plate 
def preprocess_plate(plate):
    cv2_img = np.array(plate)
    image_opencv = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    grayscale = rgb2gray(image_opencv)
    edges = canny(grayscale, sigma=3.0)
    out, angles, distances = hough_line(edges)
    #Searching for rotating angle
    _, angles_peaks,_ = hough_line_peaks(out, angles, distances, num_peaks=20)
    angle=np.mean(np.rad2deg(angles_peaks))  
    if 0 <= angle <= 90:
        rot_angle = angle - 90
    elif -45 <= angle < 0:
        rot_angle = angle - 90
    elif -90 <= angle < -45:
        rot_angle = 90 + angle
    if abs(rot_angle)>20:
        rot_angle=0
    rotated = rotate(image_opencv, rot_angle, resize=True)*255
    rotated =rotated.astype(np.uint8)
    return rotated

#Main Function 
def detect_plate(image_path,model_index=0):
    models = ["nickmuchi/yolos-small-finetuned-license-plate-detection","nickmuchi/detr-resnet50-license-plate-detection"]
    #Choose_model 
    model_name = models[model_index]
    # yolos
    threshold=0.5
    image = Image.open(image_path)
    cropped_plate = detect_objects(model_name,image,threshold)
    if(cropped_plate is None):
        return None
    rotated_plate = preprocess_plate(cropped_plate)
    return rotated_plate