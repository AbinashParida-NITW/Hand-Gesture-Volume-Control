This project uses computer vision and hand tracking to control the system volume through simple hand gestures.
By tracking the position of the thumb and index finger, the distance between them is used to adjust the system's audio volume in real-time. 
The project utilizes OpenCV, Mediapipe, NumPy, and Pycaw libraries to achieve this functionality.

How it Works
Hand Tracking: Mediapipe's hand landmarks are used to detect and track the position of the thumb and index finger in real-time.
Volume Adjustment: The distance between the thumb and index finger is calculated using basic geometry, and the volume is adjusted based on this distance. The closer the fingers, the lower the volume, and vice versa.
Volume Feedback: A volume bar is displayed on the screen to provide visual feedback on the current volume level.
Features
Real-time hand gesture recognition
Smooth volume adjustment using finger movements
Visual feedback with a dynamic volume bar
Frame-per-second (FPS) counter for performance tracking
Technologies & Libraries Used

OpenCV: For video capture and image processing.
Mediapipe: For hand landmark detection and tracking.
NumPy: For mathematical operations and coordinate mapping.
Pycaw: For controlling the system audio volume on Windows.
Math: For calculating distances between hand landmarks.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/AbinashParida-NITW/Hand-Gesture-Volume-Control.git
cd hand-gesture-volume-control
Install the required dependencies: You can install all required Python libraries using the following:

bash
Copy code
pip install opencv-python mediapipe numpy pycaw comtypes
Run the project:

bash
Copy code
python VolumeHandControl.py
Usage
Ensure your webcam is connected and running.
The volume is controlled by adjusting the distance between your thumb and index finger.
Move your fingers closer to decrease the volume, or farther apart to increase it.
A visual volume bar on the screen will provide feedback as you change the volume.
Project Files
HandTrackingModule.py: Contains the handDetector class for detecting and tracking hand landmarks.
VolumeHandControl.py: Main file that integrates hand tracking with system volume control using Pycaw.
Future Enhancements
Add support for other operating systems (currently works on Windows only).
Improve gesture recognition for more control options (e.g., mute/unmute, play/pause).
Enhance hand tracking accuracy in various lighting conditions.
Contribution
Feel free to fork this repository and contribute by submitting pull requests. Any contributions that enhance the project are welcome!
