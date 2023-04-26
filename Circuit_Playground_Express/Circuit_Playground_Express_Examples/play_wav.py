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

wav_files = audiocore.WaveFile(open("3.wav", "rb")), \
            audiocore.WaveFile(open("2.wav", "rb")), \
            audiocore.WaveFile(open("1.wav", "rb")), \
            audiocore.WaveFile(open("start.wav", "rb"))

a = audioio.AudioOut(board.SPEAKER)

print("Playing file.")

for wav in wav_files: a.play(wav)

while a.playing: pass

print("Playing file stopped.")
