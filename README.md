# Face Detection using Haar Cascades (OpenCV)

##  Overview
This project implements **real-time face and eye detection** using **Haar Cascade classifiers** provided by OpenCV.  
It demonstrates a **classical computer vision pipeline** for object detection using handcrafted features and cascade classifiers.

The project focuses on understanding **traditional face detection techniques** rather than deep learning–based approaches.

---

##  Key Concepts Covered
- Haar Cascade classifiers
- Classical object detection
- Region of Interest (ROI) processing
- Real-time video capture using webcam
- Face and eye detection pipeline

---

##  Tech Stack
- **Python**
- **OpenCV**
- **NumPy**

---

##  Project Structure
face-detection-haar-cascades/
├── face_detection.py
├── haarcascade_frontalface_default.xml
├── haarcascade_eye.xml
└── README.md

---

## Detection Pipeline
1. Capture video frames from webcam
2. Convert frames to grayscale
3. Detect faces using Haar Cascade classifier
4. Define face region as ROI
5. Detect eyes within the face ROI
6. Draw bounding boxes on detected regions

---

## How to Run
1. Install dependencies
   ```bash
   pip install opencv-python numpy

---

## Results
	•	Successfully detects faces and eyes in real time
	•	Performs well under good lighting conditions
	•	Demonstrates fast inference suitable for real-time applications

---

## Notes
•	This is a classical computer vision / foundational project
•	Haar Cascades use handcrafted features and are sensitive to lighting and pose
•	The project is intended for learning purposes, not production deployment