import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Say something...")
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source) 


try:
    text = r.recognize_google(audio)
    print("You said:", text)
    
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
