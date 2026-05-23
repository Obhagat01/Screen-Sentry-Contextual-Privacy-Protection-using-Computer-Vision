#  Screen Sentry – Contextual Privacy Protection Using Computer Vision

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-red?style=for-the-badge)
![PyQt5](https://img.shields.io/badge/PyQt5-GUI-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

### AI-Powered Real-Time Laptop Privacy Protection System

An intelligent desktop application that protects users from shoulder surfing and unauthorized screen recording using Computer Vision and Deep Learning.

</div>

---

#  Overview

Screen Sentry is a real-time AI-powered privacy protection desktop application developed using Python, OpenCV, YOLOv8, and PyQt5.

The system continuously monitors the surroundings through the laptop webcam and automatically protects sensitive screen content whenever a privacy threat is detected.

The application detects:

-  Multiple unauthorized viewers near the screen.
-  Smartphone cameras attempting to record the display.
-  Shoulder surfing threats in public environments.

Whenever a threat is detected, Screen Sentry instantly activates a fullscreen blur overlay to hide sensitive information from unauthorized viewers.

---

#  Problem Statement

Laptop users working in:

- Libraries
- Cafés
- Airports
- Offices
- Classrooms
- Co-working spaces

are vulnerable to:

##  Shoulder Surfing
Unauthorized people viewing confidential screen content.

##  Smartphone Recording
Attackers secretly recording laptop screens using mobile devices.

Traditional privacy filters:
- Reduce brightness
- Reduce viewing angles
- Are expensive
- Are inconvenient

Screen Sentry solves this problem intelligently using AI-powered real-time threat detection.

---

#  Features

✅ Real-time webcam monitoring

✅ Face detection using Haar Cascade Classifier

✅ Smartphone detection using YOLOv8 Nano

✅ Automatic fullscreen blur overlay

✅ Smart alert popup system

✅ User-controlled privacy protection

✅ Lightweight CPU-based execution

✅ Approximately 30 FPS real-time performance

✅ No additional hardware required

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| OpenCV | Webcam capture & image processing |
| YOLOv8 Nano | Smartphone detection |
| Haar Cascade | Face detection |
| PyQt5 | Desktop GUI |
| NumPy | Frame processing |
| PyTorch (CPU) | YOLO inference backend |
| PyAutoGUI | Screenshot capture |

---

#  Project Structure

```text
ScreenSentry/
│
├── core/
│   ├── face_detector.py
│   ├── phone_detector.py
│   └── screen_blur.py
│
├── ui/
│   ├── main_window.py
│   ├── blur_overlay.py
│   └── alert_popup.py
│
├── models/
│   ├── haarcascade_frontalface_default.xml
│   └── yolov8n.pt
│
├── main.py
└── requirements.txt
```

---

#  Working Methodology

## 1️⃣ Webcam Monitoring
The webcam continuously captures frames using OpenCV.

---

## 2️⃣ Face Detection
Haar Cascade detects multiple faces near the laptop screen.

If:
```python
face_count > 1
```

➡️ Privacy threat detected.

---

## 3️⃣ Smartphone Detection
YOLOv8 detects nearby mobile phones in real time.

---

## 4️⃣ Threat Decision Logic

```python
privacy_risk = (face_count > 1) or (phone_detected == True)
```

---

## 5️⃣ Blur Overlay Activation
PyQt5 creates a fullscreen blurred overlay above the screen.

---

## 6️⃣ User Alert Popup
User can:
- Keep Blur Active
- Remove Blur Temporarily

---

#  Performance Metrics

| Metric | Value |
|---|---|
| Processing Speed | ~30 FPS |
| Threat Detection Latency | < 1 second |
| CPU Usage | 15–35% |
| RAM Usage | 350–500 MB |
| Blur Kernel | 51x51 Gaussian Blur |

---

#  Application Screenshots

##  Main Dashboard

```markdown
![Dashboard](images/dashboard.png)
```

---

##  Multiple Face Detection

```markdown
![Face Detection](images/faces_detected.png)
```

---

##  Smartphone Detection

```markdown
![Phone Detection](images/phone_detected.png)
```

---

#  Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Screen-Sentry.git
```

---

## 2️⃣ Open Project Folder

```bash
cd Screen-Sentry
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run Application

```bash
python main.py
```

---

#  Requirements

```text
Python 3.11
OpenCV
PyQt5
Ultralytics YOLOv8
PyTorch CPU
NumPy < 2.0
PyAutoGUI
```

---

#  Test Results

| Test Scenario | Status |
|---|---|
| Multiple Faces Detection | ✅ PASS |
| Smartphone Detection | ✅ PASS |
| Blur Activation | ✅ PASS |
| Blur Removal | ✅ PASS |
| Real-Time Monitoring | ✅ PASS |

---

#  Strengths of the System

✅ Context-aware privacy protection

✅ No additional hardware required

✅ Real-time AI-based detection

✅ Lightweight CPU-based implementation

✅ User-friendly interface

✅ Automatic blur recovery

✅ Practical and deployable solution

---

#  Limitations

- Reduced accuracy in low lighting
- Limited side-angle face detection
- Windows-focused implementation
- Full-screen blur instead of selective blur

---

#  Future Scope

##  Gaze Detection
Detect whether someone is actually looking at the screen.

##  Window-Specific Blur
Blur only sensitive windows instead of the full screen.

##  Multi-Platform Support
Extend compatibility to Linux and macOS.

##  Deep Learning Face Detection
Replace Haar Cascade with RetinaFace or MTCNN.

##  Threat Logging
Maintain session-wise privacy threat logs.

---

#  Team Members

| Name |
|---|
| Manya Mokhalgaya |
| Ojasvi Bhagat |
| Palak Ganwani |
| Rashi Pawar |

---

#  Institution

**Shri Ramdeobaba College of Engineering & Management, Nagpur**  
Department of Data Science  
Bachelor of Technology (B.Tech) – Computer Science & Engineering (Data Science)



<div align="center">

##  “Privacy is not a feature — it’s a necessity.”

</div>
