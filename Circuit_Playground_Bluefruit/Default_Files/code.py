"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2023 REPO!
Copy the "ring.wav" and "think.wav" files into a folder named "audio" on your CIRCUITPY drive.

Once the files are copied, this example plays a different wav file for each button pressed!"""
from adafruit_circuitplayground import cp
import pygame
import random

while True:
    if pygame.mouse.get_pressed():
        cp.pixels.fill((round(random.random() * 255, 2), round(random.random() * 255, 2), round(random.random() * 255), 2))
        time.sleep(0.001)
