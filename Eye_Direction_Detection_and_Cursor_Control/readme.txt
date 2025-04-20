Overview
This project allows users to control their mouse cursor using their eye movements. By using computer vision and facial landmark detection, the system tracks specific landmarks on the face, particularly around the eyes, and moves the mouse cursor accordingly. This project utilizes the MediaPipe library for face and landmark detection, OpenCV for real-time video processing, and PyAutoGUI for controlling the mouse.

Requirements
To run this project, the following libraries and tools are required:

Python 3.x

OpenCV: For real-time video capturing and image processing.

MediaPipe: For face and landmark detection.

PyAutoGUI: For simulating mouse movements and actions.

Installation
Install the required libraries by running the following commands:

bash
Copy
Edit
pip install opencv-python
pip install mediapipe
pip install pyautogui
How it Works
Face Detection: The code uses the MediaPipe Face Mesh model to detect the user's face and extract landmark points that represent various facial features.

Eye Movement Tracking: The eye movements are tracked based on the landmarks of the eyes. Specifically, landmarks from MediaPipe’s FaceMesh model are used to detect the position of the eyes in the video frame.

Mouse Control: The pyautogui library is used to control the mouse cursor. The x and y coordinates of the detected landmarks are mapped to the screen dimensions, and the cursor is moved accordingly.

Double-click Action: The system can perform a double-click action when the user’s eye movement indicates that a double-click should occur. This is based on the relative movement of the user's eye in the frame.

Code Explanation
1. Setup and Initialization
cv2.VideoCapture(0): Initializes the webcam to capture video feed.

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True): Loads the MediaPipe face mesh model with refined landmarks for better accuracy.

pyautogui.size(): Retrieves the screen width and height for mapping the eye landmarks to the screen coordinates.

2. Main Loop
cv2.flip(frame, 1): Flips the video frame horizontally to mirror the webcam image, making the interaction more intuitive.

cv2.cvtColor(frame, cv2.COLOR_BGR2RGB): Converts the captured frame from BGR (OpenCV format) to RGB (required by MediaPipe).

face_mesh.process(rgb_frame): Processes the frame using MediaPipe to detect facial landmarks.

landmarks = landmark_points[0].landmark: Extracts the facial landmarks for the detected face.

3. Eye Movement Tracking
The specific landmarks (ID 474 to 478) are used to track the eye's movement.

The pyautogui.moveTo(screen_x, screen_y) function is used to move the mouse cursor based on the x and y position of the eye landmark.

4. Double-Click Detection
The code tracks the vertical distance between the two landmarks (ID 145 and 159) around the left eye. If the difference in their y-coordinates is very small (below 0.004), a double-click is triggered by pyautogui.doubleClick().

5. Real-Time Video Display
The landmarks and movements are displayed on the video feed with cv2.circle(), which draws circles on the landmarks to visualize the detected eye positions.

The frame is shown in a window titled Eye Controlled Mouse.

6. Closing the Program
The program keeps running until the user presses a key, monitored by cv2.waitKey(1).

Features
Real-time Eye Tracking: Tracks eye movement and moves the mouse cursor accordingly.

Double-click Action: Allows users to double-click by adjusting their eyes.

Face Mesh Landmark Detection: Uses MediaPipe for precise facial landmark detection.

Usage
Run the code: Execute the script in your Python environment.

Position yourself in front of the camera: Ensure your face is fully visible to the camera.

Move your eyes: The mouse cursor will follow your eye movements.

Perform a double-click: To simulate a double-click, slightly adjust the vertical position of your eyes.

Exit the program: Close the OpenCV window or press any key to stop the program.

Notes
Ensure that the lighting conditions are optimal for better detection accuracy.

This implementation is based on a webcam, so a good-quality camera is recommended for accurate eye tracking.

pyautogui uses screen resolution, so make sure your screen resolution is accurate for proper mouse movement.

Troubleshooting
The cursor is not moving smoothly: Ensure the lighting is good, and your face is properly centered in the webcam frame.

The double-click doesn't work: This could be due to the eye movement threshold being too strict. Adjust the condition for detecting the double-click in the code.

Future Improvements
Eye Gesture Recognition: Add more gestures for different mouse actions like right-click or scroll.

Enhanced Accuracy: Improve the algorithm to detect more precise eye movements.

User Calibration: Allow users to calibrate the system for their specific eye movements.

