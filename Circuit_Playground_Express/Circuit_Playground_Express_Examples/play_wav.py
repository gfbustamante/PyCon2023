"""THIS EXAMPLE REQUIRES A WAV FILE FROM THE ADDITIONAL_CONTENT FOLDER IN THE PyCon2019 REPO!
Copy the "space.wav" file to your CIRCUITPY drive.

Once the file is copied, this example plays a wav file using the speaker on the CPX, the grey
square located next to the picture of musical notes on the board."""
import board
import audioio
import audiocore
import digitalio

speaker_enable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
speaker_enable.switch_to_output(value=True)

data1, data2 = open("space.wav", "rb"), open("cyberpunk.wav", "rb")
wav1, wav2 = audiocore.WaveFile(data1), audiocore.WaveFile(data2)
a = audioio.AudioOut(board.SPEAKER)

print("Playing file.")
a.play(wav2)
while a.playing:
    pass
print("Playing file stopped.")
