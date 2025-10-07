import speech_recognition as sr
from googlesearch import search
import webbrowser as wb
import time 
# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source: 
    print("Say something...")
    r.adjust_for_ambient_noise(source)

    while True:
        
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)

            query = text
            for url in search(query):
                print("Opening:", url)
                wb.open(url)
                time.sleep(2)
                
            
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            continue

        if text.lower() == "exit":
            print("Exiting...")
            break

# hope this shows up in git