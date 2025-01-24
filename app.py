import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
MEDIA_DIR = BASE_DIR.joinpath("media")
CSS_DIR = BASE_DIR.joinpath("css")
speech_file_path = MEDIA_DIR / "tts-output.mp3"

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_tts_model = os.getenv("OPENAI_TTS_MODEL", default="tts-1")
openai_tts_voice = "ash"

client = OpenAI(
  api_key=openai_api_key
)

def log_msg(msg: str):

    now = datetime.now()
    print(f"[{now:%Y-%m-%d %H:%M:%S}] ", msg)

def local_css(file_name: str) -> bool:
    # Load local CSS for additional styling
    try:
        with open(CSS_DIR.joinpath(file_name)) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        return True
    except Exception as e:
        return False

def convert(text: str, voice: str = "ash"):

    log_msg(f"Selected voice: {voice} : TTS Convert > {text}")

    try:

        with client.audio.speech.with_streaming_response.create(
            model=openai_tts_model,
            voice=voice,
            input=text
        ) as response:
            response.stream_to_file(speech_file_path)

        return True
    except Exception as e:
        print("Exception occured :", e)
        return False

def streamlit_app():

    st.set_page_config(page_title="Text-to-Speech Converter", layout="wide")
    st.title("Text-to-Speech Converter")
    # load and apply local CSS for additional styling
    local_css("style.css")

    alert_box = st.empty()
    left_top_col, right_top_col = st.columns([1,8])
    voice_option = st.selectbox(
        "Which voice would you like to use?",
        ("Alloy", "Ash", "Coral", "Echo", "Fable", "Onyx", "Nova", "Sage", "Shimmer"),
        index=1
    )

    text = st.text_area(
        "Enter text that you would like to convert to speech:"
    )
    if st.button("Convert"):
        if text:
            result = convert(text, voice_option.lower())

            if result:

                alert_box.success("Audio file created successfully!  You can now play or download your audio file.")

                encoded_file_path = str(speech_file_path).encode('utf-8')

                with open(encoded_file_path, "rb") as file:
                    audio_bytes = file.read()
                    right_top_col.audio(audio_bytes, format="audio/mpeg")

                    # create a download button to download newly created audio file
                    left_top_col.download_button(
                            label="Download",
                            data=file,
                            file_name="tts-output.mp3"
                        )

        else:
            st.write("Please enter text")

def main():
    streamlit_app()

if __name__ == "__main__":
    main()
