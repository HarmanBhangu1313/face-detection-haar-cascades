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
##  Mathematical Intuition (Haar Cascade Face Detection)

###  Haar-Like Features
Haar Cascade face detection works by measuring **intensity differences** between adjacent rectangular regions of an image.

A Haar feature simply subtracts the sum of pixel values in one region from another.  
These differences capture basic visual patterns such as:
- Edges
- Lines
- Center–surround contrasts  

Human faces have consistent intensity patterns (for example, eyes are usually darker than cheeks), which makes these features effective.

---

###  Integral Image (Why Detection Is Fast)
To compute rectangular intensity sums efficiently, an **integral image** is used.

The integral image stores cumulative pixel sums so that the total intensity of any rectangular region can be calculated in **constant time**, regardless of its size.

This allows thousands of Haar features to be evaluated extremely quickly, enabling **real-time face detection**.

---

###  Boosted Weak Classifiers (AdaBoost)
Each Haar feature on its own is a **weak classifier**, meaning it performs only slightly better than random guessing.

AdaBoost combines many such weak classifiers into a **strong classifier** by:
- Selecting the most informative features
- Assigning higher importance to features that classify faces more accurately

This results in a robust face detector built from simple components.

---

###  Cascade of Classifiers
Instead of applying all classifiers everywhere, Haar Cascades use a **cascade structure**:

- Early stages use a small number of features to quickly reject non-face regions
- Later stages apply more features only to promising regions

A detection window is accepted as a face only if it passes **all stages** of the cascade, making the algorithm both fast and efficient.

---

### Multi-Scale Detection
Faces appear at different sizes in images.  
To handle this, the detector scans the image at multiple scales using a sliding window approach.

---

### Key Limitations
Haar Cascade face detection is sensitive to:
- Lighting variations
- Pose changes
- Occlusions

Despite these limitations, it remains a fast and effective method for face detection in controlled environments.

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
