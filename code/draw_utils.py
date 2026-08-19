import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def smooth_path(path, window_size=5):
    if len(path) < window_size:
        return path
    smoothed = []
    for i in range(len(path)):
        x_vals = [pt[0] for pt in path[max(0, i - window_size + 1):i + 1]]
        y_vals = [pt[1] for pt in path[max(0, i - window_size + 1):i + 1]]
        smoothed.append((int(np.mean(x_vals)), int(np.mean(y_vals))))
    return smoothed

def draw_annotations(image, pose_landmarks, arrow_tip=None, arrow_path=None, elbow_path=None):
    if pose_landmarks:
        annotated_image = image.copy()
        overlay = image.copy()

        # Default pose drawing by MediaPipe
        mp_drawing.draw_landmarks(
            image=annotated_image,
            landmark_list=pose_landmarks,
            connections=mp_pose.POSE_CONNECTIONS
        )

        # Draw arrow tip if present
        if arrow_tip:
            cv2.circle(overlay, arrow_tip, 5, (0, 255, 0), -1)
            cv2.putText(overlay, "ARROW DETECTED", (arrow_tip[0] + 5, arrow_tip[1] - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 2)

        # Draw arrow trail
        if arrow_path and len(arrow_path) > 1:
            smoothed_arrow = smooth_path(arrow_path)
            for i in range(1, len(smoothed_arrow)):
                cv2.line(overlay, smoothed_arrow[i - 1], smoothed_arrow[i], (0, 200, 0), 2)

        # Draw elbow trail
        if elbow_path and len(elbow_path) > 1:
            smoothed_elbow = smooth_path(elbow_path)
            for i in range(1, len(smoothed_elbow)):
                cv2.line(overlay, smoothed_elbow[i - 1], smoothed_elbow[i], (255, 0, 255), 2)

        # Blend overlay with annotations
        cv2.addWeighted(overlay, 0.4, annotated_image, 0.6, 0, annotated_image)

        return annotated_image
    return image