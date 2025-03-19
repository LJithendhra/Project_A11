## 🚦 Requirements

### 🎯 High-Level Requirements (HLRs)
These requirements describe the overall goals and features of the system:
- ✅ **The system must detect emergency vehicles** (e.g., ambulances, fire engines) in real-time using deep learning models.
- ✅ **It must analyze the density of vehicles** at traffic lanes to dynamically adjust signal timings.
- ✅ **The system should integrate with existing traffic signal infrastructure** to enable automatic signal control.
- ✅ **It should process live video feeds** from cameras installed at traffic intersections.
- ✅ **The system must prioritize emergency vehicles** by dynamically allocating signal time based on proximity.

### ⚙️ Low-Level Requirements (LLRs)
These requirements describe the specific functionalities and technical details:
- 🔍 **Implement YOLOv11** for object detection, trained with custom datasets including emergency vehicles and standard traffic scenarios.
- 🎨 **Apply data augmentation techniques** such as greyscale conversion, noise addition, and blurring for better model robustness.
- 💻 **Develop a software interface** (e.g., Flask or FastAPI) for real-time processing of video feeds.
- 🎥 **Use OpenCV for video pre-processing**, including frame extraction and resizing.
- 📏 **Include a distance measurement mechanism** (e.g., pixel-based or LiDAR) to calculate vehicle proximity to traffic signals.
- 🔗 **Design APIs or hardware-compatible modules** for controlling traffic signal timers dynamically.

### 📊 Non-Functional Requirements (NFRs)
These requirements focus on the quality attributes and performance of the system:
- 🚀 **Performance:**  
  - 🔹 The system must detect and process vehicles with at least **90% accuracy**.  
  - 🔹 Signal adjustments should occur **within 2 seconds** of emergency vehicle detection.  
- 📈 **Scalability:**  
  - 🔹 The system should handle **video feeds from multiple traffic intersections** simultaneously.  
- 🔧 **Reliability:**  
  - 🔹 The system should function **24/7 with minimal downtime (<1%)**.  
- 🔒 **Security:**  
  - 🔹 Secure communication between the system and traffic signal controllers **using encrypted channels**.  
- 🖥️ **Usability:**  
  - 🔹 Provide a **simple dashboard** for traffic operators to monitor the system’s performance and logs.  
- 🛠️ **Maintainability:**  
  - 🔹 The system should have **modular code** to allow easy updates and feature additions.  
- 📜 **Compliance:**  
  - 🔹 The system must comply with **local traffic regulations and data privacy laws** (e.g., not storing personally identifiable information from video feeds).  

### 📝 Summary of Requirements
| 🔰 **Type**             | 📝 **Description**                                                                                                   |
|------------------------|-------------------------------------------------------------------------------------------------------------------|
| 🎯 **High-Level**       | Overall system goals and features (e.g., detecting emergency vehicles, real-time signal control).                 |
| ⚙️ **Low-Level**        | Specific technical details (e.g., using YOLOv11, OpenCV, APIs for signal control).                               |
| 📊 **Non-Functional**   | Quality attributes (e.g., performance, scalability, security, reliability, and maintainability).                |

