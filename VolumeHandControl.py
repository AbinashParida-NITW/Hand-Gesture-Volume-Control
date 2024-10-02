import numpy as np
import cv2
import time
import HandTrackingModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


##############################################
wCam,hCam=600,480
##############################################

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.8)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange=volume.GetVolumeRange() #get range between -96 t0 0
minVol=volRange[0]   #-96
maxVol=volRange[1]   #0
vol=0
volBar=400

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        print(lmList[4],lmList[8]) # 8 index finger top and 4 thumb top

        x1,y1=lmList[4][1],lmList[4][2] # give x1 and y1 positions respectively of thumb
        x2, y2 = lmList[8][1], lmList[8][2]  # give x1 and y1 positions respectively of index finger
        cx,cy=(x1+x2)//2,(y1+y2)//2 #ceter points


        cv2.circle(img,(x1,y1),10,(255, 0, 255),cv2.FILLED) # circle the tip of thumb
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)# circle the tip of index finger
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)  # circle the tip of index finger
        cv2.line(img,(x1,y1),(x2,y2),(0,255,255),3) # draw line between points

        length=math.hypot(x2-x1,y2-y1)
        #print(length)
        #Hand Range = 50-300
        #volume range = -65 to 0
        vol=np.interp(length,[30,230],[minVol,maxVol])
        volBar = np.interp(length, [30, 230], [400, 150])
        print(f'length:{int(length)} vol:{vol}')
        volume.SetMasterVolumeLevel(vol, None)


        if length<30:
            cv2.circle(img, (cx, cy), 10, (0,255, 0 ), cv2.FILLED)  # circle the tip of index finger


    cv2.rectangle(img, (30, 150), (65, 400), (0, 0, 255),3)
    cv2.rectangle(img, (30, int(volBar)), (65, 400), (0, 0, 255), cv2.FILLED)


    # Calculate Frames per Second (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on the image
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()