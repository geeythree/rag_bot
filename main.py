from termcolor import cprint
from rag.query import query_doc
from rag.audio_prompt import listen
import pyttsx3


if __name__ == '__main__':
    
    audio = input("Want to use microphone? [types Y/n]: ")
    if audio.lower() == 'y':
        ques = listen()
    elif audio.lower() == 'n':
        ques = input("Type your question here: ")
    else:
        raise ValueError(f'Unknown option {audio}')
   
    if not ques.startswith('Sorry'):
        answer = query_doc(query=ques)
        cprint(f"{answer}", 'blue')
        if audio.lower() == 'y':
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
    else:
        cprint("Please try again", 'red')
        