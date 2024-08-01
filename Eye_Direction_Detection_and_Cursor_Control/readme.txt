Overview
This project uses a trained SVM model and OpenCV to detect eye direction from
video frames and control the mouse cursor based on the detected direction.

Features
Real-time Eye Detection: Uses Haar cascades to detect eyes in video frames.
Direction Prediction: Predicts eye movement direction using a trained SVM model.
Cursor Control: Moves the mouse cursor based on the detected eye direction.
Requirements
OpenCV
NumPy
Joblib
Pyautogui
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/eye-direction-cursor-control.git
Install the required libraries:
bash
Copy code
pip install opencv-python numpy joblib pyautogui
Run the script:
bash
Copy code
python eye_direction_cursor_control.py
Files
eye_direction_cursor_control.py: Main script to run the project.
eye_direction_svm_model.pkl: Trained SVM model.
v1.mp4: Sample video file for testing (replace with 0 for webcam input).
License
This project is licensed under the MIT License.

