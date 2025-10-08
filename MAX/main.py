import speech_recognition as sr
from googlesearch import search
import webbrowser as wb
import time 
# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source: 
    while True:
         print("Say something...")
         r.adjust_for_ambient_noise(source)
         listener = r.listen(source)
         audio = r.recognize_google(listener)
         print(audio)

# hope this shows up in git