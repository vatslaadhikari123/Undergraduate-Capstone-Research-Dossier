```markdown
# Automated Active Alignment & Deep Learning Defect Inspection for Optical Camera Sensors

[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=flat)](https://github.com/ultralytics/ultralytics)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-CC292B?style=flat&logo=microsoftsqlserver&logoColor=white)](https://www.microsoft.com/sql-server)

* **Candidate:** Vatsla Adhikari (UID: 20BCS5064)
* **Module:** Senior Undergraduate Capstone Research & Industrial Project (Semester 7, 15 Credits, Grade A+)
* **Academic Supervisors:** Chu-Shou Yang, Ph.D., Associate Professor & Prof. Shao
* **Fellowship & Industry Host:** Taiwan Experience Education Program (TEEP) | REC Technology Corporation

---

## 1. Project Overview

In automotive safety cameras (such as electronic digital rearview mirrors and backup cameras), assembly requires bonding an optical lens directly over an electronic image sensor chip. During production, two common defects occur:
1. **Optical Tilt (Misalignment):** Adhesive shrinkage tilts the lens relative to the chip, causing the center of the image to remain sharp while the corners become blurry.
2. **Microscopic Contamination:** Tiny airborne dust specks or scratches on the sensor glass block incoming light, leaving permanent dark spots on video feeds.

This project provides an automated computer-vision and telemetry pipeline to calculate physical tilt alignment and detect microscopic defects in real time.

---

## 2. Part 1: Optical Tilt & Active Alignment

### The Physical Problem
A camera lens and its image sensor chip must sit flat and parallel:
* When the lens tilts, the center acts like a seesaw pivot and stays at the proper focus distance.
* One corner tilts **too far away** from the lens (light converges in mid-air before reaching the sensor).
* The opposite corner tilts **too close** to the lens (light hits the sensor before converging).
* As a result, the corners blur, preventing reliable wide-angle lane and obstacle detection.

```text
LENS (Tilted):          \=======================/
                       /            |            \
                      /             |             \
                     v (Focal Point)|              v (Focal Point)
                    *               |               *
                   / \              v (Focal Point)/ \
SENSOR: ======[=======]============[=]============[=======]======
              Corner 1            Center          Corner 2
          (Sensor Too Far)    (In Focus: Z1)  (Sensor Too Close)
              [BLURRY]           [SHARP]          [BLURRY]

```

---

### The Solution & Tilt Math

A motorized stage moves the lens up and down along the focus axis ($Z$) in steps of $0.002\text{ mm}$, measuring the sharpness score (MTF) across 5 regions: Center, Upper-Left, Upper-Right, Lower-Left, and Lower-Right.

Instead of complex equations, the software determines focus using three simple values:

* **$Z_1$:** The lens height where the **Center** reaches peak sharpness.
* **$Z_2$:** The average lens height where the **4 Corners** reach peak sharpness.
* **$\Delta Z$ (Focal Offset):** The physical gap between center focus and corner focus:

$$\Delta Z = \vert{}Z_1 - Z_2\vert{}$$

```text
Sharpness (MTF)
  ^
50|                   Center (Z1) Peak
  |                         /\               Corners Avg (Z2) Peak
40|                        /  \                     / \
  |                       /    \                   /   \
  |                      /      \                 /     \
 0+---------------------/--------\---------------/-------\--------> Z Position (mm)
                       |          |             |         |
                               ^                         ^
                         Z1 = -0.160 mm             Z2 = -0.141 mm
                               
                               |<----- Delta Z ----->|
                                    |Z1 - Z2| = 19 um

```

* **Pass Criterion:** If $\Delta Z \le 0.006\text{ mm}\ (6\text{ \mu m})$, the lens is parallel and passes inspection.
* **Database Automation:** A Python script connects to SQL Server (`REC_DB`) using `pyodbc` to pull batch records (`find_MTF_oneLot`, `find_MTF_latestNLots`) and plot distribution histograms across assembly stations.

---

## 3. Part 2: Microscopic Defect Detection

### The Problem

Tiny dust particles or scratches (invisible to the human eye) on the sensor glass block light and ruin camera quality. Manual inspection under microscopes is slow and prone to fatigue.

---

### The Software Pipeline

```text
[Sensor Image] -> [YOLOv8 Detection Box] -> [Equalize Histogram] -> [Adaptive Threshold] -> [Find Radius & Center]

```

1. **AI Spotter (YOLOv8 & Roboflow):**
A YOLOv8 model was trained on annotated microscopic images from Roboflow to locate candidate dust specks and place bounding boxes around them.
2. **Image Processing & Measurement (OpenCV):**
* **Histogram Equalization (`equalizeHist`):** Increases image contrast to pull faint particles out of dark sensor backgrounds.
* **Adaptive Thresholding:** Converts the region into pure black and white (particle = black, clean sensor = white).
* **Circle Fitting (`minEnclosingCircle`):** Wraps a tight circle around the particle to extract its exact pixel coordinates $(X, Y)$ and radius ($R$).
* **Boundary Check (`pointPolygonTest`):** Verifies the particle perimeter to confirm size and eliminate lighting shadows.



---

## 4. End-to-End Production Flow

```text
 [1. Active Alignment]       [2. UV Curing]       [3. Vision Inspection]       [4. Final Gate]
  Motor sweeps Z-axis    ->  UV light hardens ->  Camera captures image   ->   Pass: Pack & Ship
  Calculates Delta Z         glue permanently     YOLOv8 spots dust            Fail: Scrap / Air Clean
  Aligns until <= 6 um                     OpenCV measures radius

```

---

## 5. Quantitative Results

| Metric / Parameter | Value Achieved | Operational Meaning |
| --- | --- | --- |
| **YOLOv8 Detection Precision** | **92.0%** | High accuracy with minimal false alarms on clean chips |
| **YOLOv8 Defect Recall** | **77.0%** | Catches foreign contaminants reliably before packaging |
| **Alignment Tolerance ($\Delta Z$)** | **$\le 0.006\text{ mm}$ ($6\text{ \mu m}$)** | Enforces clear, edge-to-edge optical sharpness |
| **Inspection Latency** | **$< 20\text{ ms}$ / frame** | Operates inline without slowing conveyor movement |
| **Academic Defense** | **Grade A+ (15 Credits)** | Defended and evaluated before academic supervisors |

---

## 6. Repository Structure

```text
├── reports/                 # Faculty progress reports (Nov–Dec 2023 validating my thesis)
└── README.md

```

```

```
