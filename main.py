import RPi.GPIO as GPIO
from datetime import datetime

red_pin = 22
green_pin = 16
blue_pin = 10


# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Define a function to set the LED to a specific color
def set_color(color):
  if color == "yellow":
    # Set the LED to yellow by turning on the red and green channels
    GPIO.output(red_pin, True)
    GPIO.output(green_pin, True)
    GPIO.output(blue_pin, False)
  elif color == "blue":
    # Set the LED to blue by turning on the blue channel
    GPIO.output(red_pin, False)
    GPIO.output(green_pin, False)
    GPIO.output(blue_pin, True)
  else:
    # Turn off the LED
    GPIO.output(red_pin, False)
    GPIO.output(green_pin, False)
    GPIO.output(blue_pin, False)

# List of days to set the LED to yellow
yellow_days = [
  (1, 9),
  (12, 25),
]

# List of days to set the LED to blue
blue_days = [
  (7, 4),  
  (9, 11),  
]

# Set the LED to the appropriate color based on the current date
while True:
  now = datetime.now()
  if (now.month, now.day) in yellow_days:
    set_color("yellow")
  elif (now.month, now.day) in blue_days:
    set_color("blue")
  else:
    set_color("off")
    