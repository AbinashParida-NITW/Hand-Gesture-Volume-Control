import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon  # detection confidence
        self.trackCon = trackCon  # tracking confidence

        # Initialize Mediapipe Hands solution
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils  # Drawing utility for hand landmarks

    def findHands(self, img, draw=True):
        # Convert image to RGB as Mediapipe processes RGB images
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        # Check if hand landmarks are detected
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    # Draw hand landmarks and connections
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo=0,draw=True):
        lmList=[]

        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                # Get the height, width, and channels of the image
                h, w, c = img.shape
                # Convert landmark coordinates to pixels(they are in ratios)
                cx, cy = int(lm.x * w), int(lm.y * h)  # fetch x and y coordinates by(lm.x or lm.y) then multiply with width and height to get x and y.
                #print(f"Landmark {id}: ({cx}, {cy})")
                lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        return lmList

def main():
    cTime = 0
    pTime = 0
    cap = cv2.VideoCapture(0)  # Open video capture
    detector = handDetector()  # Initialize hand detector

    while True:
        success, img = cap.read()  # Read frame from the camera
        img = detector.findHands(img)  # Process the frame and draw hand landmarks
        lmList=detector.findPosition(img)
        if len(lmList)!=0:
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

if __name__ == "__main__":
    main()
