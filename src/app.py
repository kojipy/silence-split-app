import streamlit as st
from pydub import AudioSegment, silence

# 音声ファイルのアップロード
audio_file = st.file_uploader(
    "音声ファイルをアップロードしてください",
    type=["m4a", "mp3", "webm", "mp4", "mpga", "wav"],
)

if audio_file:
    audio = AudioSegment.from_file(audio_file)
    audio_pieces = silence.split_on_silence(
        audio, min_silence_len=100, silence_thresh=-70, keep_silence=100
    )

    for audio_pice in audio_pieces:
        audio_data = audio_pice.export()
        st.audio(audio_data.read())
