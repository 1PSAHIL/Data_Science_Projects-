import cv2#Cv2 library is used for image processing
import numpy as np#Numpy is used of for numerical operations and handling arrays
import joblib#
import pyautogui  # Library for controlling the mouse cursor

# Paths
svm_model_path = 'eye_direction_svm_model.pkl'  # Path to your saved SVM model

# Load the trained SVM model
svm_model = joblib.load(svm_model_path)

# Haar cascade for eye detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Function to preprocess eye region
def preprocess_eye(eye_img, img_size=64):
    eye_img = cv2.resize(eye_img, (img_size, img_size))
    eye_img = eye_img.flatten()
    return eye_img

# Function to predict eye direction
def predict_eye_direction(eye_img):
    eye_img = preprocess_eye(eye_img)
    eye_img = eye_img.reshape(1, -1)  # Reshape for the SVM model
    prediction = svm_model.predict(eye_img)[0]
    directions = ['left', 'right', 'up', 'down']
    return directions[prediction]

# Function to move the cursor based on eye direction
def move_cursor(direction):
    screen_width, screen_height = pyautogui.size()
    current_x, current_y = pyautogui.position()
    step = 20  # Number of pixels to move the cursor
    if direction == 'left' and current_x > step:
        pyautogui.moveRel(-step, 0)
    elif direction == 'right' and current_x < screen_width - step:
        pyautogui.moveRel(step, 0)
    elif direction == 'up' and current_y > step:
        pyautogui.moveRel(0, -step)
    elif direction == 'down' and current_y < screen_height - step:
        pyautogui.moveRel(0, step)

# Video capture
cap = cv2.VideoCapture('v1.mp4')  # Replace with 0 for webcam
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        eye_img = gray[ey:ey+eh, ex:ex+ew]
        direction = predict_eye_direction(eye_img)    
        # Draw rectangle around the eyes and put the direction text
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
        cv2.putText(frame, f'Eyes direction: {direction}', (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        # Move cursor based on detected eye direction
        move_cursor(direction)
    cv2.imshow('Eye Direction', frame)#Display the frame with the rectangle and direction    
    if cv2.waitKey(1) & 0xFF == ord('q'):#Waits for ms for a key press,exits the loop if q is pressed.
        break
cap.release()#Release the video capture
cv2.destroyAllWindows()#Close all OpenCv Windows
