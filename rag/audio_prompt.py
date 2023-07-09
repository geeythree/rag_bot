import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening now...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=30)
            print("Recognizing...")
            
            text = "Text: "+r.recognize_google(audio)
            print(text)
        except Exception as e:
            unrecognized_speech_text = (
                f"Sorry, I didn't catch that. Exception was: {e}s"
            )
            text = unrecognized_speech_text
        
        return text