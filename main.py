import cv2
import mediapipe
import time

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    flip_img = cv2.flip(img,1)
