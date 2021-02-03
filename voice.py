import speech_recognition as sr 

# code pulled from:
# https://www.activestate.com/blog/how-to-build-a-digital-virtual-assistant-in-python/
def getCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError as e:
        print("UNKNOWN VALUE ERROR: Speech recognition engine did not understand the audio")
    except sr.RequestError as e:
        print(f"REQUEST ERROR: {e}")
    return data 