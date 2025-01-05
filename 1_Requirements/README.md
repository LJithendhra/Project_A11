## Requirements

### High-Level Requirements (HLRs)
These requirements describe the overall goals and features of the system:
1. The system must detect emergency vehicles (e.g., ambulances, fire engines) in real-time using deep learning models.
2. It must analyze the density of vehicles at traffic lanes to dynamically adjust signal timings.
3. The system should integrate with existing traffic signal infrastructure to enable automatic signal control.
4. It should be capable of processing live video feeds from cameras installed at traffic intersections.
5. The system must prioritize emergency vehicles by dynamically allocating signal time based on proximity.

### Low-Level Requirements (LLRs)
These requirements describe the specific functionalities and technical details:
1. Implement YOLOv11 for object detection, trained with custom datasets including emergency vehicles and standard traffic scenarios.
2. Apply data augmentation techniques such as greyscale conversion, noise addition, and blurring for better model robustness.
3. Develop a software interface (e.g., Flask or FastAPI) for real-time processing of video feeds.
4. Use OpenCV for pre-processing video feeds, including frame extraction and resizing.
5. Include a distance measurement mechanism (e.g., pixel-based or LiDAR) to calculate the proximity of vehicles to the traffic signals.
6. Design APIs or hardware-compatible modules for controlling traffic signal timers dynamically.

### Non-Functional Requirements (NFRs)
These requirements focus on the quality attributes and performance of the system:
1. **Performance:** 
   - The system must detect and process vehicles with at least 90% accuracy.
   - Signal adjustments should occur within 2 seconds of emergency vehicle detection.
2. **Scalability:** 
   - The system should handle video feeds from multiple traffic intersections simultaneously.
3. **Reliability:**
   - The system should function 24/7 with minimal downtime (<1%).
4. **Security:** 
   - Secure communication between the system and traffic signal controllers using encrypted channels.
5. **Usability:** 
   - Provide a simple dashboard for traffic operators to monitor the system's performance and logs.
6. **Maintainability:**
   - The system should have modular code to allow easy updates and integration of new features (e.g., adding new vehicle types for detection).
7. **Compliance:**
   - The system must comply with local traffic regulations and data privacy laws (e.g., not storing personally identifiable information from video feeds).

### Summary of Requirements
| Type                     | Description                                                                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **High-Level**           | Overall system goals and features (e.g., detecting emergency vehicles, real-time signal control).                                           |
| **Low-Level**            | Specific technical details (e.g., using YOLOv11, OpenCV, APIs for signal control).                                                         |
| **Non-Functional**       | Quality attributes (e.g., performance, scalability, security, reliability, and maintainability). 
