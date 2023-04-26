from adafruit_circuitplayground import cp
import time


cp.pixels.brightness = 0.3

while True:
    if cp.button_a:
        cp.pixels[5] = (255, 0, 0)
        cp.pixels[6] = (255, 0, 0)
        cp.pixels[7] = (210, 45, 0)
        cp.pixels[8] = (210, 100, 0)
        cp.pixels[9] = (210, 150, 0)
        cp.play_file("audio/BassDrum.wav")
    if cp.button_b:
        cp.pixels[0] = (255, 0, 0)
        cp.pixels[1] = (255, 0, 0)
        cp.pixels[2] = (210, 45, 0)
        cp.pixels[3] = (210, 100, 0)
        cp.pixels[4] = (210, 150, 0)
        cp.play_file("audio/CrashCymbal.wav")
    time.sleep(0.1)
