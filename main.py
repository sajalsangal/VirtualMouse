import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    if not success:
        break

    flip_img = cv2.flip(img,1)
    rgbImg = cv2.cvtColor(flip_img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgbImg)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id,lms in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = lms.x * h , lms.y * w
                print([id,cx,cy])

            mpDraw.draw_landmarks(flip_img,handLms,mphands.HAND_CONNECTIONS)


    cv2.imshow("Image", flip_img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
