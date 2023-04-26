from adafruit_circuitplayground import cp
import time


cp.pixels.brightness = 0.3
while cp.switch == False:
    for i in range(9):
        cp.pixels[i] = (100, 100, 200)
        cp.clearPixels()

while cp.switch == True:
    cp.clearPixels()
    if cp.button_a:
        cp.pixels[0] = (255, 0, 0)
        cp.pixels[1] = (235, 0, 0)
        cp.pixels[2] = (210, 45, 0)
        cp.pixels[3] = (210, 100, 0)
        cp.pixels[4] = (210, 150, 0)
        cp.play_file("audio/BassDrum.wav")
        time.sleep(0.1)
    if cp.button_b:
        cp.pixels[5] = (210, 150, 0)
        cp.pixels[6] = (210, 100, 0)
        cp.pixels[7] = (210, 45, 0)
        cp.pixels[8] = (235, 0, 0)
        cp.pixels[9] = (255, 0, 0)
        cp.play_file("audio/CrashCymbal1.wav")
        time.sleep(0.1)
    
