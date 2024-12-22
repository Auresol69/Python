import sounddevice as sd
import numpy as np

# Hàm tạo âm thanh cho từng nốt
def play_tone(frequency, duration, amplitude=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate)
    sd.wait()

# Nốt nhạc (đơn giản hóa giai điệu Daisy Bell)
notes = [
    (262, 0.4), (294, 0.4), (330, 0.4), (262, 0.4),  # "Dai-sy, Dai-sy"
    (294, 0.4), (330, 0.4), (349, 0.6), (294, 0.6),  # "give me your an-swer, do."
]

# Phát từng nốt nhạc
for freq, dur in notes:
    play_tone(freq, dur)

import pyttsx3

engine = pyttsx3.init()
lyrics = "Daisy, Daisy, give me your answer, do. I'm half crazy, all for the love of you."

engine.say(lyrics)
engine.runAndWait()
