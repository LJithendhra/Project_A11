import cv2
import numpy as np
from ultralytics import YOLO

model_path = "runs/detect/train6/weights/best.pt"
model = YOLO(model_path)

def process_video(video_path):
    video = cv2.VideoCapture(video_path)
    detections = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        results = model(frame)[0]
        frame_detections = []
        for result in results:
            if result.boxes:
                for box in result.boxes:
                    conf = box.conf.item()
                    cls_id = box.cls.item()
                    if conf >= 0.5:
                        bbox = list(map(int, box.xyxy[0].tolist()))
                        class_name = get_class_name(cls_id)
                        frame_detections.append({"class": class_name, "confidence": conf, "bbox": bbox})
        detections.append(frame_detections)
    video.release()
    return detections

def get_class_name(cls_id):
    class_name_dict = {
        0: "Accident", 1: "Auto Rickshaw", 2: "Bicycle", 3: "Bus",
        4: "Car", 5: "Emergency", 6: "Motorcycle", 7: "Truck"
    }
    return class_name_dict.get(cls_id, "Unknown")

def calculate_distance(bbox):
    x1, y1, x2, y2 = bbox
    object_width_pixels = x2 - x1
    focal_length = 800  # Adjust based on your camera calibration
    real_width_meters = 2.0  # Approximate width of an emergency vehicle
    distance = (focal_length * real_width_meters) / object_width_pixels
    estimated_time = max(5, distance / 5)  # Assume an average speed of 5 m/s
    return round(distance, 2), round(estimated_time, 2)
