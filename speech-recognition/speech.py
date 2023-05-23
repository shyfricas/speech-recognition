# pip install speechrecognition and pyttsx3

import speech_recognition
import pyttsx3

# could also: import speech_recognition as sr

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)
            # i prefer using google since it is most common
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            # make sure to add f, will not work if otherwise
            print(f"You said: {text}")
    
    # usually rare for this but if does not work it will restart
    
    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        print("Could not get reuslts")
        continue
    
# open with python or command terminal 