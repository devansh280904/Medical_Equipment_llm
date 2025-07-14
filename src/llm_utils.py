from llama_cpp import Llama
import streamlit as st
import pyttsx3


@st.cache_resource
def get_llm():
    return Llama(model_path="models/phi2-medical-merged-q8.gguf", n_ctx=2048, n_threads=8)

def tts_speak(text):
    import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Zira" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150) 
    engine.say(text)
    engine.runAndWait()
