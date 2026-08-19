import math
import numpy as np
from pose_utils import *

def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def analyze_posture(landmarks):
    if landmarks is None:
        return "No pose detected"
    feedback = []
    if abs(landmarks.landmark[11].y - landmarks.landmark[12].y) > 0.05:
        feedback.append("Uneven shoulders")
    if abs(landmarks.landmark[23].y - landmarks.landmark[24].y) > 0.05:
        feedback.append("Unstable hip alignment")

    heel_l = landmarks.landmark[27]
    heel_r = landmarks.landmark[28]
    toe_l = landmarks.landmark[31]
    toe_r = landmarks.landmark[32]

    stance_width = calculate_distance(heel_l, heel_r)
    toe_angle_diff = abs(toe_l.y - toe_r.y)

    if stance_width < 0.2:
        feedback.append("Feet too close")
    elif stance_width > 0.6:
        feedback.append("Feet too wide")
    else:
        feedback.append("Good stance width")

    if toe_angle_diff > 0.05:
        feedback.append("Uneven toe angle")

    if estimate_center_of_gravity(landmarks) > 0.1:
        feedback.append("Unbalanced center of gravity")

    return " | ".join(feedback) if feedback else "Posture: Good"

def analyze_nocking_and_setup(landmarks, arrow_tip=None, image_shape=None):
    if landmarks is None:
        return "No pose detected"
    result = []
    result.append("Bow grip: OK" if is_bow_grip_vertical(landmarks) else "Bow grip not vertical")
    result.append("String hand anchor: OK" if is_string_hand_aligned_with_face(landmarks) else "String hand not aligned with face")
    if arrow_tip and image_shape:
        result.append("Arrow nocked: OK" if is_arrow_nocked_properly(arrow_tip, landmarks, image_shape) else "Arrow not correctly placed")
    else:
        result.append("Arrow nocking: Not visible")
    return " | ".join(result)

def analyze_draw_phase(landmarks, elbow_path=None):
    if landmarks is None:
        return "No pose detected"
    feedback = []
    if get_shoulder_alignment_diff(landmarks) > 0.05:
        feedback.append("Shoulders not level during draw")
    if get_elbow_draw_distance(landmarks) < 0.15:
        feedback.append("Elbow not fully drawn")
    if elbow_path and len(elbow_path) > 5:
        x_coords = [pt[0] for pt in elbow_path[-5:]]
        if np.std(x_coords) > 10:
            feedback.append("Draw path symmetry inconsistent")
    return " | ".join(feedback) if feedback else "Draw phase: Good"

def analyze_anchor_and_aiming(landmarks):
    if landmarks is None:
        return "No pose detected"
    feedback = []
    if not is_anchor_point_consistent(landmarks):
        feedback.append("Inconsistent anchor point")
    if not is_head_stable(landmarks):
        feedback.append("Head not stable")
    if is_bow_canted(landmarks):
        feedback.append("Bow is canted")
    return " | ".join(feedback) if feedback else "Anchor & Aiming: Good"

def analyze_release(prev, curr):
    if not prev or not curr:
        return "No pose detected"
    feedback = []
    move = calculate_distance(prev.landmark[16], curr.landmark[16])
    dx = curr.landmark[16].x - prev.landmark[16].x
    if move < 0.01:
        feedback.append("Release appears stiff")
    else:
        direction = "backward" if dx > 0 else "sideways"
        feedback.append(f"Release: Smooth ({direction})")
    bow_move = calculate_distance(prev.landmark[15], curr.landmark[15])
    if bow_move > 0.05:
        feedback.append("Bow hand reaction too aggressive")
    return " | ".join(feedback)

def analyze_follow_through(landmarks, arrow_tip=None):
    if not landmarks:
        return "No pose detected"
    feedback = []
    head = landmarks.landmark[0]
    mid_x = (landmarks.landmark[11].x + landmarks.landmark[12].x) / 2
    if abs(head.x - mid_x) > 0.1:
        feedback.append("Head moved after release")
    if landmarks.landmark[15].y - landmarks.landmark[13].y > 0.15:
        feedback.append("Bow arm dropped after shot")
    feedback.append("Arrow flight: Detected" if arrow_tip else "Arrow flight: Not detected")
    return " | ".join(feedback) if feedback else "Follow-through: Good"