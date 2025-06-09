from flask import Flask, render_template, request, send_file
import asyncio
import edge_tts
import os

app = Flask(__name__)

VOICES = [
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-GB-SoniaNeural",
    "en-GB-RyanNeural"
]

OUTPUT_FILE = "static/output.mp3"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        voice_index = int(request.form['voice'])
        voice = VOICES[voice_index]

        # Run edge-tts asynchronously
        asyncio.run(text_to_speech(text, voice))

        return render_template("index.html", voices=VOICES, success=True, audio_file=OUTPUT_FILE)

    return render_template("index.html", voices=VOICES)

async def text_to_speech(text, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(OUTPUT_FILE)

if __name__ == '__main__':
    # Make sure static folder exists
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
