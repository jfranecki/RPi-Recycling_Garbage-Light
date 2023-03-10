import RPi.GPIO as GPIO
import logging
import time
from datetime import datetime

yellow_led_pin = 24
blue_led_pin = 15

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(yellow_led_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)

# Define a function to turn an LED on or off
def set_led(led_pin, state):
  GPIO.output(led_pin, state)

# All dates are set 1 day prior
# List of days to set the yellow LED on: Garbage
yellow_days = [
  (1, 10),
  (1, 18),
  (1, 25),
  (2, 1),
  (2, 8),
  (2, 15),
  (2, 22),
  (3, 1),
  (3, 8),
  (3, 15),
  (3, 22),
  (3, 29),
]

# All dates are set 1 day prior
# List of days to set the blue LED on: Recycling
blue_days = [
  (1, 19),
  (2, 2),
  (2, 16),
  (3, 2),
  (3, 16),
  (3, 30),
]

logging.info("Starting LED control program")

# Set the LED to the appropriate color based on the current date
while True:
  now = datetime.now()
  if (now.month, now.day) in yellow_days:
    set_led(yellow_led_pin, True)
    logging.info("Turning yellow LED on")
  else:
    set_led(yellow_led_pin, False)
  if (now.month, now.day) in blue_days:
    set_led(blue_led_pin, True)
    logging.info("Turning blue LED on")
  else:
    set_led(blue_led_pin, False)
    logging.info("Current Date is " + str(now.month) + "/" + str(now.day) + ". No day found for light activation.")
  time.sleep(60)  # Delay for 1m
