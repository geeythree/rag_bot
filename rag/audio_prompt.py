import speech_recognition as sr

def listen() -> str:
    """
    Converts speech to text

    Code adapted from -> https://python.langchain.com/docs/use_cases/chatbots/voice_assistant.html 

    Returns
    -------
    text: str
          Audio converted to text format
    """
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
    
def audio_to_text(audio_bytes):
    """
    Converts recorded audio to text when using web interface

    Returns
    -------
    text: str
          Audio converted to text format
    """
    r = sr.Recognizer()
    audio = sr.AudioData(audio_bytes, 36000, 4)
    # with audio as source:
    #     audio_data = r.record(source)
    try:
        text = "Text: "+r.recognize_google(audio)
        print(text)
    except Exception as e:
        unrecognized_speech_text = (
            f"Sorry, I didn't catch that. Exception was: {e}s"
        )
        text = unrecognized_speech_text
    return text