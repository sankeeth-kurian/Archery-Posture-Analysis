import numpy as np
import cv2
from arrow_utils import detect_arrow_tip

def extract_pose_landmarks(image, pose_model):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = pose_model.process(image_rgb)
    return result.pose_landmarks if result.pose_landmarks else None

def get_arrow_tip_position(image):
    return detect_arrow_tip(image)

def is_bow_grip_vertical(landmarks):
    return abs(landmarks.landmark[15].x - landmarks.landmark[13].x) < 0.05

def is_string_hand_aligned_with_face(landmarks):
    return abs(landmarks.landmark[16].x - landmarks.landmark[0].x) < 0.1

def is_arrow_nocked_properly(arrow_tip, landmarks, image_shape):
    if not arrow_tip:
        return False
    h, w, _ = image_shape
    right_hand = landmarks.landmark[16]
    rh_px = (int(right_hand.x * w), int(right_hand.y * h))
    distance = ((arrow_tip[0] - rh_px[0]) ** 2 + (arrow_tip[1] - rh_px[1]) ** 2) ** 0.5
    return distance < 50

def get_shoulder_alignment_diff(landmarks):
    return abs(landmarks.landmark[11].y - landmarks.landmark[12].y)

def get_elbow_draw_distance(landmarks):
    le = landmarks.landmark[13]
    ls = landmarks.landmark[11]
    return ((le.x - ls.x)**2 + (le.y - ls.y)**2)**0.5

def is_anchor_point_consistent(landmarks):
    rh = landmarks.landmark[16]
    mouth = landmarks.landmark[9]
    return abs(rh.x - mouth.x) < 0.08 and abs(rh.y - mouth.y) < 0.08

def is_head_stable(landmarks):
    head = landmarks.landmark[0]
    mid_x = (landmarks.landmark[11].x + landmarks.landmark[12].x) / 2
    return abs(head.x - mid_x) < 0.1

def is_bow_canted(landmarks):
    return abs(landmarks.landmark[15].x - landmarks.landmark[13].x) > 0.1

def estimate_center_of_gravity(landmarks):
    hip_mid_x = (landmarks.landmark[23].x + landmarks.landmark[24].x) / 2
    heel_mid_x = (landmarks.landmark[27].x + landmarks.landmark[28].x) / 2
    return abs(hip_mid_x - heel_mid_x)

def get_left_elbow_pixel(landmarks, image_shape):
    h, w, _ = image_shape
    elbow = landmarks.landmark[13]
    return (int(elbow.x * w), int(elbow.y * h))