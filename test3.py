import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode

GPIO.setmode(GPIO.BOARD)
# Set the GPIO pin for the servo motor
servo_pin = 22
GPIO.setup(servo_pin, GPIO.OUT)
# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)

# Define the servo range
servo_min = 2.5  # Minimum pulse width (in ms)
servo_max = 12.5  # Maximum pulse width (in ms)
authorized_detected = False
count = 0

def angle_to_duty_cycle(angle):
    return (angle / 180.0) * (servo_max - servo_min) + servo_min

def rotate_motor():
    pwm.start(angle_to_duty_cycle(90))
    time.sleep(1)

    # Open the gate
    # You may need to adjust the delay based on your gate mechanism
    time.sleep(10)
    pwm.start(angle_to_duty_cycle(0))
    time.sleep(10)
    # Move the servo back to its original position (0 degrees)
    return

# Define the ROI (region of interest) coordinates
roi_x = 160  # X-coordinate of the top-left corner of the ROI
roi_y = 120  # Y-coordinate of the top-left corner of the ROI
roi_width = 320  # Width of the ROI
roi_height = 240  # Height of the ROI

# Calculate the coordinates for the green square boundary
boundary_thickness = 2
boundary_color = (0, 255, 0)  # Green color
boundary_x1 = roi_x
boundary_y1 = roi_y
boundary_x2 = roi_x + roi_width
boundary_y2 = roi_y + roi_height

#img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
allowed_printed = False

with open('Authorized_vehicle.txt') as f:
    myDataList = f.read().splitlines()

while True:
    success, img = cap.read()
    # Draw the green square boundary
    cv2.rectangle(img, (boundary_x1, boundary_y1), (boundary_x2, boundary_y2), boundary_color, boundary_thickness)
    # Extract the region of interest (ROI) for QR code detection
    roi = img[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]
    for barcode in decode(roi):
        myData = barcode.data.decode('utf-8')
        if myData in myDataList and not authorized_detected:
            rotate_motor()
            print("Allowed", count)
            count += 1
            authorized_detected = True
            # Add a delay to prevent continuous gate openings
            time.sleep(5)  # Adjust the delay as needed

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Result', img)
    if authorized_detected:
        authorized_detected = False

cap.release()
cv2.destroyAllWindows()