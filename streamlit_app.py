import streamlit as st
import numpy as np
import os
# from audio_recorder_streamlit import audio_recorder
from rag.query import query_doc
from rag.audio_prompt import audio_to_text
import pyttsx3
from io import BytesIO
import streamlit.components.v1 as components

def st_audiorec():

    # get parent directory relative to current directory
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    try:
         # Custom REACT-based component for recording client audio in browser
        build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
        # specify directory and initialize st_audiorec object functionality
        st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    except:
        # Custom REACT-based component for recording client audio in browser
        # build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
        build_dir = "/app/rag_bot/st_audiorec/frontend/build"
        # specify directory and initialize st_audiorec object functionality
        st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    # Create an instance of the component: STREAMLIT AUDIO RECORDER
    raw_audio_data = st_audiorec()  # raw_audio_data: stores all the data returned from the streamlit frontend
    wav_bytes = None                # wav_bytes: contains the recorded audio in .WAV format after conversion

    # the frontend returns raw audio data in the form of arraybuffer
    # (this arraybuffer is derived from web-media API WAV-blob data)

    if isinstance(raw_audio_data, dict):  # retrieve audio data
        with st.spinner('retrieving audio-recording...'):
            ind, raw_audio_data = zip(*raw_audio_data['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            raw_audio_data = np.array(raw_audio_data)  # convert to np array
            sorted_ints = raw_audio_data[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            # wav_bytes contains audio data in byte format, ready to be processed further
            wav_bytes = stream.read()

    return wav_bytes

st.title("Retrieval Augmented Generation (RAG)")
st.subheader("You may ask questions about PAN card")

text_prompt = st.text_input("Write a text prompt")
st.write('Or record an audio prompt: ')
audio_prompt = st_audiorec()
# audio_prompt = audio_recorder("To start recording click on the mic icon, click on it again to stop recording: ")

if audio_prompt is not None:
    # st.audio(audio_prompt, format="audio/wav")
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

