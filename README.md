# Archery-Posture-Analysis

Archery Posture Analysis: A computer vision-based tool to evaluate an archer's form and technique using pose estimation, biomechanical analysis, and real-time visual feedback!

This repository contains a Python-based system for analyzing an archer's shooting form using pose estimation and video analysis. The system identifies biomechanical inefficiencies throughout the entire shot cycle and generates dynamic, frame-by-frame feedback to assist athletes, coaches, and sports researchers.

#### Key Features:

1. **Pose Estimation Integration:**
   * **Purpose:** Leverages MediaPipe for accurate body landmark detection from video input.
   * **Use Cases:** Provides the foundation for analyzing posture and motion in archery training.

2. **Multi-Phase Analysis:**
   * **Stance & Posture:** Evaluates shoulder alignment, foot placement, and center of gravity balance.
   * **Nocking & Set-up:** Assesses arrow placement, bow grip, and string hand positioning.
   * **Draw Phase:** Detects elbow path symmetry and shoulder posture.
   * **Anchor & Aiming:** Monitors head stability, anchor point consistency, and bow canting.
   * **Release:** Tracks hand motion and smoothness of release.
   * **Follow-through:** Evaluates post-release posture and arrow flight detection.

3. **Real-time Feedback Overlay:**
   * **Purpose:** Annotates each video frame with posture trails, feedback text, and visual cues.
   * **Use Cases:** Delivers immediate visual feedback for coaches and athletes to assess form.

4. **Custom Arrow Tip Detection:**
   * **Purpose:** Uses simple image processing (HSV masking) to detect and track the arrow during release.
   * **Use Cases:** Tracks arrow behavior during release to assess precision and form quality.

5. **Modular & Reusable Codebase:**
   * **Purpose:** Each analysis phase and utility is separated into clean, maintainable Python modules.
   * **Use Cases:** Easily extendable for other sports or motion analysis applications.

#### Included Components:

1. **posture_analysis.py**
   * **Purpose:** Core analysis logic for each shot phase.

2. **pose_utils.py**
   * **Purpose:** Functions for extracting and analyzing body landmarks.

3. **draw_utils.py**
   * **Purpose:** Visualization overlays for pose trails, arrow tip, and feedback.

4. **arrow_utils.py**
   * **Purpose:** Arrow detection logic using basic color segmentation.

5. **ArcheryEvaluation.ipynb**
   * **Purpose:** End-to-end pipeline to process videos and generate annotated output.

6. **videos/**
   * **Purpose:** Folder for input videos (MP4 format).

7. **outputs/**
   * **Purpose:** Folder where annotated videos with feedback are saved.

8. **requirements.txt**
   * **Purpose:** Contains required Python packages for setting up the environment.

#### Requirements:

Install dependencies with:

```bash
pip install -r requirements.txt
```

#### Applications & Use Cases:

1. **Athlete Coaching & Training:**
   * Identify and correct subtle form errors for archers at all skill levels.
   * Deliver data-backed insights to improve shooting consistency.

2. **Biomechanics & Sports Science:**
   * Study body mechanics and joint movement patterns in real-world conditions.
   * Useful for research in human movement and performance optimization.

3. **Computer Vision Projects:**
   * Showcase applied pose estimation for action feedback systems.
   * Ideal for students and developers exploring AI in sports.

4. **Performance Evaluation Tools:**
   * Adaptable to other sports or activities involving precision and posture.
   * Can be modified for golf, baseball, or martial arts analysis.

#### Why Use This Tool?

This project bridges the gap between sports performance and artificial intelligence, offering an intelligent visual feedback system for archery training using Python and computer vision. With its real-time posture tracking and modular architecture, this tool empowers coaches, athletes, and researchers to push the boundaries of biomechanical analysis in a practical, accessible way.
