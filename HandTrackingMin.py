import cv2
import mediapipe as mp
import time

from streamlit import success

cap=cv2.VideoCapture(0) # 1 fails so use 0

mpHands= mp.solutions.hands
hands=mpHands.Hands() # Hands class uses only RGB images so convert all images to RGB
mpDraw=mp.solutions.drawing_utils # drawing_utils method helps us drawing line between 21 point of hand.

cTime=0
pTime=0

while True:
    success,img=cap.read()

    #CONVERT IMAGE TO RGB
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB) # hand object created from mpHands.Hands() above
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks: # if multi_hand_landmarks true (hands shows)
        for handLms in results.multi_hand_landmarks:
            # to get the information within a hand we need id_number and landmark_information(gave x and y coordinates)
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                # Get the height, width, and channels of the image
                h, w, c = img.shape
                # Convert landmark coordinates to pixels(they are in ratios)
                cx, cy = int(lm.x * w), int(lm.y * h)# fetch x and y coordinates by(lm.x or lm.y) then multiply with width and height to get x and y.
                print(f"Landmark {id}: ({cx}, {cy})")
                cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    cTime=time.time()
    fps=1/(cTime-pTime)# frame per second
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
