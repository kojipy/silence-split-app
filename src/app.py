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

    for piece_id, audio_pice in enumerate(audio_pieces):
        id_col, audio_col = st.columns([1, 9], vertical_alignment="top", gap="small")
        audio_data = audio_pice.export()

        with id_col:
            st.subheader(piece_id + 1, divider="gray")

        with audio_col:
            st.audio(audio_data.read())
