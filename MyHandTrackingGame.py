import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

cTime = 0
pTime = 0
cap = cv2.VideoCapture(0)  # Open video capture
detector = htm.handDetector()  # Initialize hand detector

while True:
    success, img = cap.read()  # Read frame from the camera
    img = detector.findHands(img)  # Process the frame and draw hand landmarks
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    # Calculate Frames per Second (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on the image
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display the processed image
    cv2.imshow("Hand Tracking", img)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()