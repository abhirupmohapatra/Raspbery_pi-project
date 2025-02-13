import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin for the servo motor
servo_pin = 22
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms period)

# Define the servo range
servo_min = 2.5  # Minimum pulse width (in ms)
servo_max = 12.5  # Maximum pulse width (in ms)

# Function to convert angle to duty cycle
def angle_to_duty_cycle(angle):
    return (angle / 180.0) * (servo_max - servo_min) + servo_min

try:
    while True:
        # Move the servo to the right (90 degrees)
        pwm.start(angle_to_duty_cycle(90))
        time.sleep(1)

        # Wait for 10 seconds
        time.sleep(10)

        # Move the servo back to its original position (0 degrees)
        pwm.start(angle_to_duty_cycle(0))
        time.sleep(10)

except KeyboardInterrupt:
    # Clean up
    pwm.stop()
    GPIO.cleanup()