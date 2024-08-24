import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    audio = r.listen(source)

    try:
        # Using Google Web Speech API to recognize the speech
        text = r.recognize_google(audio)
        print(f"You said: {text}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")
