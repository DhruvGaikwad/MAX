import speech_recognition as sr
from googlesearch import search
import webbrowser as wb
import time 
# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source: 
    r.adjust_for_ambient_noise(source)

    while True:
        try:
         print("Say something...")
         listener = r.listen(source)
         aud = r.recognize_google(listener)
         audio = aud.lower()
         print(audio)
         
         if "google" in audio:
            print("enter your query here")
            time.sleep(1)
            r.pause_threshold = 1x
            googie= r.listen(source)  # reuse the same source
            a = r.recognize_google(googie)
            
            for j in search(a, num_results=1):
                wb.open(j)
                
        except sr.UnknownValueError:
            print("Could not understand audio")
        

# hope this shows up in git