import webbrowser
import speech_recognition as sr
import os
from fucns import *
recognizer = sr.Recognizer()
def open_chrome():
    os.system('start chrome')
    return
def open_spotify():
    os.system('start spotify')
    return
def search_in_chrome():
    mic = sr.Microphone()
    rec = sr.Recognizer()
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        print("What would you like to search for?")
        while(True):
            audio = rec.listen(source)
            response = {'success':True,
                        "error": None,
                        "sent": None
                        }
            try:
                response["transcription"] = recognizer.recognize_google(audio)
            except sr.RequestError:
                response["success"] = False
                response["error"] = "API unavailable/unresponsive"
            except sr.UnknownValueError:
                response['success'] = False
                response["error"] = "Unable to recognize speech"
            if response['success'] != False :
                search_url = f"https://www.google.com/search?q={response["transcription"]}"
                webbrowser.open(search_url, new=2)
                return
            else:
                print(response['error'])

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
    return response
