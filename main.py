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

def set_led(led_pin, state, color):
    GPIO.output(led_pin, state)
    if state:
        logging.info(f"Turning {color} LED on")
    else:
        logging.info(f"Turning {color} LED off")

def set_yellow_led(state):
    set_led(yellow_led_pin, state, 'yellow')

def set_blue_led(state):
    set_led(blue_led_pin, state, 'blue')

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

blue_days = [
  (1, 19),
  (2, 2),
  (2, 16),
  (3, 2),
  (3, 16),
  (3, 30),
]


logging.info("Starting LED control program")

while True:
    now = datetime.now()
    if (now.month, now.day) in yellow_days:
        set_yellow_led(True)
    else:
        set_yellow_led(False)
        
    if (now.month, now.day) in blue_days:
        set_blue_led(True)
    else:
        set_blue_led(False)
        logging.info(f"Current Date is {now.month}/{now.day}. No day found for light activation.")
        
    time.sleep(60)  # Delay for 1m
