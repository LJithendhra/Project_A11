import cv2
import numpy as np
import torch
from ultralytics import YOLO
import pygame
import os
import time

# Load YOLO model
MODEL_PATH = "runs/detect/train6/weights/best.pt"
model = YOLO(MODEL_PATH)

# Confidence threshold for detection
CONFIDENCE_THRESHOLD = 0.5

# Define class names
CLASS_NAMES = {
    0: "Accident", 1: "Auto Rickshaw", 2: "Bicycle", 3: "Bus",
    4: "Car", 5: "Emergency", 6: "Motorcycle", 7: "Truck"
}

# Define colors for different classes
CLASS_COLORS = {
    0: (255, 0, 0), 1: (0, 255, 0), 2: (0, 0, 255), 3: (255, 255, 0),
    4: (255, 165, 0), 5: (0, 0, 255), 6: (0, 255, 255), 7: (255, 192, 203)
}

# Initialize pygame mixer for alert sound
pygame.mixer.init()
ALERT_SOUND = os.path.abspath("static/alert.mp3")

# Track detected unique vehicles
unique_vehicles = {class_name: set() for class_name in CLASS_NAMES.values()}

# Alert system tracking
detection_start_time = None
DETECTION_DURATION = 3  # How long an emergency vehicle needs to be detected before alert triggers

def play_alert():
    """Plays an alert sound if not already playing."""
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(ALERT_SOUND)
        pygame.mixer.music.play()

def stop_alert():
    """Stops the alert sound."""
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def update_detection(is_detected):
    """Manages emergency vehicle detection timing."""
    global detection_start_time
    if is_detected:
        if detection_start_time is None:
            detection_start_time = time.time()
        elif time.time() - detection_start_time >= DETECTION_DURATION:
            play_alert()
    else:
        detection_start_time = None
        stop_alert()

def calculate_distance(y1, y2, frame_height):
    """Estimates distance of emergency vehicle from the camera."""
    relative_position = (y2 + y1) / (2 * frame_height)
    max_distance = 100
    return max_distance * (1 - relative_position)

def estimate_time(distance, num_vehicles):
    """Estimates time for emergency vehicle to reach the camera."""
    base_speed = 10  # Approximate speed in m/s
    congestion_factor = 1 + (num_vehicles * 0.1)
    return round(distance / (base_speed / congestion_factor), 2)

def process_frame(frame):
    """Processes a single video frame and detects vehicles."""
    results = model(frame)[0]
    detections = []
    emergency_detected = False
    frame_height, frame_width, _ = frame.shape

    if results.boxes:
        for box in results.boxes:
            conf = box.conf.item()
            cls_id = int(box.cls.item())
            if conf >= CONFIDENCE_THRESHOLD:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                class_name = CLASS_NAMES.get(cls_id, "Unknown")

                # Create a unique identifier for the object (based on bounding box)
                obj_id = (x1, y1, x2, y2)

                # Count unique vehicles
                if obj_id not in unique_vehicles[class_name]:
                    unique_vehicles[class_name].add(obj_id)

                # Draw bounding box and label
                color = CLASS_COLORS.get(cls_id, (0, 255, 0))
                label = f"{class_name} {int(conf * 100)}%"
                detections.append({"class": class_name, "confidence": round(conf, 2), "bbox": (x1, y1, x2, y2)})

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

                if cls_id == 5:  # Emergency vehicle detected
                    emergency_detected = True
                    distance = calculate_distance(y1, y2, frame_height)
                    estimated_time = estimate_time(distance, len(unique_vehicles[class_name]))

                    cv2.putText(frame, f"Dist: {distance:.1f}m Time: {estimated_time}s", (x1, y2 + 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2, cv2.LINE_AA)

                    detections[-1]["distance"] = round(distance, 2)
                    detections[-1]["estimated_time"] = estimated_time

    return frame, detections, emergency_detected

def process_video(video_path, output_path):
    """Processes a video file, detects vehicles, tracks unique ones, and plays alert if needed."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Error: Could not open video.")
        return []

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    global unique_vehicles
    unique_vehicles = {class_name: set() for class_name in CLASS_NAMES.values()}  # Reset for each video

    emergency_detected = False
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame, detections, emergency_detected_frame = process_frame(frame)

        if emergency_detected_frame:
            emergency_detected = True

        # Update the alert system
        update_detection(emergency_detected_frame)

        out.write(processed_frame)
        cv2.imshow("Processed Frame", processed_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Get final vehicle counts
    final_counts = {vehicle: len(unique_vehicles[vehicle]) for vehicle in unique_vehicles}

    print(f"✅ Processed video saved at: {output_path}")
    print(f"🚗 Final Unique Vehicle Counts: {final_counts}")

    if emergency_detected:
        print("🚨 Emergency vehicle detected at least once!")

    return final_counts
