import time
import simpleaudio as sa
import sys

def PlaySound(sound):
    wave_obj = sa.WaveObject.from_wave_file(sound)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def StartPlay(timerNumber):
   # countdown(timerNumber)
    PlaySound('Sound/GLaDOS-564474.wav')



