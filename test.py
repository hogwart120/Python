import snowboydecoder
import sys
import signal

def detected_callback():

detector = snowboydecoder.HotwordDetector('alexa.umdl', sensitivity=0.8, audio_gain=1)

detector.start(detected_callback, sleep_time=0.01)
detector.terminate()
