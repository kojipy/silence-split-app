import librosa
import pandas as pd
import streamlit as st
from pydub import AudioSegment, silence


def pitch_chart(audio_segment):
    audio_data = audio_segment.export()
    y, sr = librosa.load(audio_data)

    f0, _, _ = librosa.pyin(y, fmin=50, fmax=2000, sr=sr, center=False)

    times = librosa.times_like(f0, sr=sr)
    data = pd.DataFrame({"pitch": f0, "times": times})

    st.line_chart(data, x="times", y="pitch")


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

    pice_ids = list(map(str, range(1, len(audio_pieces) + 1)))
    tabs = st.tabs(pice_ids)
    for piece_id, tab in enumerate(tabs):
        with tab:
            audio_segment = audio_pieces[piece_id]

            pitch_chart(audio_segment)

            audio_data = audio_segment.export()
            st.audio(audio_data.read())
