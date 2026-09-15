# Automated Active Alignment, Optical Sensor Quality Assurance, and Deep Learning Defect Detection

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://github.com/ultralytics/ultralytics)
[![Database](https://img.shields.io/badge/SQL_Server-pyodbc-orange.svg)](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-red.svg)](https://opencv.org/)

## Academic Project Overview
* **Author:** Vatsla Adhikari (UID: 20BCS5064)
* **Degree:** Bachelor of Engineering in Computer Science & Engineering, Chandigarh University
* **Module:** Senior Undergraduate Capstone Research & Industrial Dissertation (Semester 7: 15 Credits, Grade A+)
* **Supervision:** Chu-Shou Yang, Ph.D., Associate Professor & Prof. Shao
* **Fellowship:** Taiwan Experience Education Program (TEEP)

---

## Abstract
This repository contains the software codebase, algorithmic workflows, technical reports, and experimental visualizations developed for the undergraduate capstone dissertation. The research resolves two central challenges in optoelectronic sensor manufacturing: automated spatial active alignment along the optical Z-axis using Modulation Transfer Function (MTF) analysis, and real-time microscopic defect localization using deep learning (YOLOv8) and morphological image processing.

---

## System Architecture & Modules

### 1. Active Alignment & Delta-Z Curve Fitting (`/analysis`)
* **MTF vs. Z Analysis:** Extracts spatial Modulation Transfer Function values across 5 designated coordinates (Center, UL, UR, LL, LR) to model focal plane curvature.
* **$\Delta Z$ Computation:** Determines the focal deviation between the optical center ($Z_1$) and composite peripheral averages ($Z_2$):
  $$\Delta Z = \vert{}Z_1 - Z_2\vert{}$$
* Automated parametric tracking and histogram visualizers built using `pandas`, `matplotlib`, and `pyodbc` directly interfacing with SQL Server (`REC_DB`).

### 2. Deep Learning Defect Detection (`/yolo_defect_detection`)
* Microscopic particle and scratch localization on optical sensor dies using a custom-trained **YOLOv8s** network.
* Dataset curated, annotated, and augmented with Roboflow.
* **Validation Performance:** Achieved **92.0% Precision**, **77.0% Recall**, and **68.7% mAP@0.5**.

### 3. Morphological Signal Processing (`/image_processing`)
* Channel-wise histogram equalization (`equalizeHist`) across multi-folder RGB captures.
* Adaptive Gaussian thresholding and contour isolation (`minEnclosingCircle`, `pointPolygonTest`) to measure particle radius and centroid coordinates down to single-pixel resolutions.

---

## Repository Structure
```text
├── reports/                 # Weekly research reports submitted to faculty supervisors
│   ├── Weekly_Report_Nov_1.pdf
│   ├── Weekly_Report_Nov_2.pdf
│   ├── Weekly_Report_Dec_1.pdf
│   ├── Weekly_Report_Dec_2.pdf
│   ├── Weekly_Report_Dec_3.pdf
│   └── Weekly_Report_Dec_4.pdf
├── scripts/                 # Core Python processing pipelines
│   ├── TTU.py               # Channel histogram equalization & batch processing
│   ├── db_mtf_pipeline.py   # SQL Server connection and MTF extraction functions
│   └── yolo_inference.py    # Defect prediction and bounding box visualization
├── visualizations/          # Empirical output plots and detection results
│   ├── mtf_vs_z_curves/
│   ├── delta_z_histograms/
│   └── yolo_sample_outputs/
└── README.md
