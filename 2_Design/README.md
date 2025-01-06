# Architecture
![Screenshot 2025-01-05 121433](https://github.com/user-attachments/assets/b75fba65-a62d-4da2-8b97-6fdf76788425)

# Methodology
![image](https://github.com/user-attachments/assets/5043d6cc-b0b1-44c4-a490-cef80260f99b)


## Component Design

### 1. Input Module
- **Functionality:** Captures video feed from cameras and preprocesses it using OpenCV.
- **Key Features:**
  - Resizes video frames for efficient processing.
  - Removes noise for better object detection accuracy.

### 2. Object Detection Module
- **Functionality:** Detects and classifies vehicles in video frames using YOLOv11.
- **Key Features:**
  - Bounding boxes for detected vehicles.
  - Classification of high-priority vehicles.

### 3. Traffic Analysis Module
- **Functionality:** Analyzes vehicle density and prioritizes high-priority vehicles.
- **Key Features:**
  - Calculates lane-wise vehicle density.
  - Identifies the proximity of high-priority vehicles to traffic signals.

### 4. Signal Control Module
- **Functionality:** Adjusts traffic signal timings dynamically.
- **Key Features:**
  - Allocates timing based on lane density and vehicle priority.
  - Communicates with signal controllers via APIs.

### 5. Monitoring Dashboard
- **Functionality:** Displays real-time traffic conditions and system status.
- **Key Features:**
  - Live video feed with detected vehicles.
  - Lane density and signal timing visualization.


