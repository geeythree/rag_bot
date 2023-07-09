import streamlit as st
from audio_recorder_streamlit import audio_recorder
from rag.query import query_doc
from rag.audio_prompt import audio_to_text
import pyttsx3

st.title("Retrieval Augmented Generation (RAG)")
st.subheader("You may ask questions about PAN card")

text_prompt = st.text_input("Write a text prompt")

audio_prompt = audio_recorder("To start recording click on the mic icon, click on it again to stop recording: ")
if audio_prompt:
    st.audio(audio_prompt, format="audio/wav")
    text = audio_to_text(audio_prompt)
    st.write(text)
    if not text.startswith('Sorry'):
        response = query_doc(text)
        st.subheader(f"Answer:\n:green[{response}]")
        engine = pyttsx3.init()
        engine.say(response)
        # st.audio(response,format="audio/wav")
        
        engine.runAndWait()
        
        if engine._inLoop:
            engine.endLoop()
elif text_prompt:
    response = query_doc(text_prompt)
    st.subheader(f"Answer:\n:green[{response}]")
