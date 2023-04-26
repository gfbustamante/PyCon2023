"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2019 REPO!
Copy the "space.wav" file to your CIRCUITPY drive.

Once the file is copied, this example plays a wav file using the speaker on the CPX, the grey
square located next to the picture of musical notes on the board."""
import board
import audioio
import audiocore
import digitalio
import touchio

from adafruit_circuitplayground.express import cpx
from random import sample

cpx.pixels.brightness = 0.3
cpx.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!


# if cpx.button_a:
#     cpx.pixels[0:5] = [(255, 0, 0)] * 5
# else:
#     cpx.pixels[0:5] = [(0, 0, 0)] * 5

# if cpx.button_b:
#     cpx.pixels[5:10] = [(0, 255, 0)] * 5
# else:
#     cpx.pixels[5:10] = [(0, 0, 0)] * 5

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)
touch_A3 = touchio.TouchIn(board.A3)
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
touch_A6 = touchio.TouchIn(board.A6)
touch_A7 = touchio.TouchIn(board.A7)

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

wav_files = audiocore.WaveFile(open("3.wav", "rb")), \
            audiocore.WaveFile(open("2.wav", "rb")), \
            audiocore.WaveFile(open("1.wav", "rb")), \
            audiocore.WaveFile(open("start.wav", "rb"))

a = audioio.AudioOut(board.SPEAKER)

print("Playing file.")

for wav in wav_files: a.play(wav)

while a.playing: pass

game = True
while game:
    for i in cpx.pixels:
        if i == (255, 0, 0):
            game = False
            break
    rands = sample(range(11), 3)
    for r in rands: cpx.pixels[r] = (255, 0, 0)
    i = 100
    while i > 0:
        if touch_A1.value:
            if cpx.pixels[0] != (255, 0, 0): break
            cpx.pixel[0] = (0, 0, 0)
        if touch_A2.value:
            if cpx.pixels[1] != (255, 0, 0): break
            cpx.pixel[1] = (0, 0, 0)
        if touch_A3.value:
            if cpx.pixels[2] != (255, 0, 0): break
            cpx.pixel[2] = (0, 0, 0)
        if touch_A4.value:
            if cpx.pixels[3] != (255, 0, 0): break
            cpx.pixel[3] = (0, 0, 0)
        if touch_A5.value:
            if cpx.pixels[4] != (255, 0, 0): break
            cpx.pixel[4] = (0, 0, 0)
        if touch_A6.value:
            if cpx.pixels[5] != (255, 0, 0): break
            cpx.pixel[5] = (0, 0, 0)
        if touch_A7.value:
            if cpx.pixels[6] != (255, 0, 0): break
            cpx.pixel[6] = (0, 0, 0)

        i -= 1


print("Playing file stopped.")
