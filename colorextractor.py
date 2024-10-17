import cv2
import numpy as np

# Function to adjust and print the lower and upper bounds for HSV
def get_hsv_bounds(hsv_value, h_range=10, s_range=40, v_range=40):
    h, s, v = hsv_value
    # Ensure the hue wraps around at 179 for OpenCV
    lower_bound = np.array([max(h - h_range, 0), max(s - s_range, 0), max(v - v_range, 0)])
    upper_bound = np.array([min(h + h_range, 179), min(s + s_range, 255), min(v + v_range, 255)])

    return lower_bound, upper_bound

# Callback function to capture HSV values at the point where the mouse is clicked
def get_hsv_value(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Left click to capture HSV values
        hsv_value = hsv_frame[y, x]
        print(f"HSV Value at ({x},{y}): {hsv_value}")

        # Get lower and upper bounds for the clicked HSV value
        lower_bound, upper_bound = get_hsv_bounds(hsv_value)

        print(f"Lower HSV Bound: {lower_bound}")
        print(f"Upper HSV Bound: {upper_bound}")

# Initialize webcam
cap = cv2.VideoCapture(0)

# Set the mouse callback function to capture HSV on click
cv2.namedWindow('Webcam Feed')
cv2.setMouseCallback('Webcam Feed', get_hsv_value)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the frame
    cv2.imshow('Webcam Feed', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
