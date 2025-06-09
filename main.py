import streamlit as st
import asyncio
import edge_tts
import os

# Voice options
VOICES = [
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-GB-RyanNeural",
    "en-GB-SoniaNeural"
]

async def convert_text_to_speech(text, voice, filename="output.mp3"):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

def run_tts(text, voice):
    asyncio.run(convert_text_to_speech(text, voice))

# Streamlit UI
st.set_page_config(page_title="Edge TTS App", layout="centered")
st.title("🎤 Text to Speech Converter (Edge TTS)")

text_input = st.text_area("Enter the text to convert to speech:", height=150)
selected_voice = st.selectbox("Choose a voice:", VOICES)

if st.button("🔊 Convert to Speech"):
    if text_input.strip():
        with st.spinner("Generating audio..."):
            run_tts(text_input, selected_voice)
        st.success("Audio generated successfully!")

        # Play audio
        audio_bytes = open("output.mp3", "rb").read()
        st.audio(audio_bytes, format="audio/mp3")
        st.download_button("📥 Download MP3", audio_bytes, file_name="output.mp3")
    else:
        st.warning("Please enter some text.")
