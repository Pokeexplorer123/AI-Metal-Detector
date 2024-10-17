import cv2
import numpy as np

# Function to detect colors based on HSV values
def detect_color(hsv_frame, color_ranges):
    for color_name, (lower_bound, upper_bound) in color_ranges.items():
        # Create a mask for each color
        temp_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        # Find contours to highlight the detected color
        contours, _ = cv2.findContours(temp_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter small areas
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Adjusted narrower HSV ranges
color_ranges = {
    'Lead': (np.array([110, 223, 37]), np.array([124, 55, 123])),  # Narrower range for Lead (Gray tones)
    'Gold': (np.array([9, 96, 101]), np.array([27, 162, 174])),  # Gold (working)
    'Redstone': (np.array([166, 90, 86]), np.array([179, 170, 166])),  # Redstone (working)
    'Lapis': (np.array([95, 94, 112]), np.array([115, 174, 192])),  # Narrower range for Lapis (Deep Blue)
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert to HSV

    # Call function to detect colors
    detect_color(hsv_frame, color_ranges)

    # Show the result
    cv2.imshow('Specialized Color Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
