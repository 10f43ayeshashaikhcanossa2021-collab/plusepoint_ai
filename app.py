import streamlit as st
import os
from utils.transcribe import transcribe_video
from utils.video_cut import cut_reel

st.title("🎯 PulsePoint AI")

uploaded = st.file_uploader("Upload a long video", type=["mp4"])

if uploaded:
    with open("temp.mp4", "wb") as f:
        f.write(uploaded.read())

    st.success("Video uploaded!")

    if st.button("Generate Reels"):
        segments = transcribe_video("temp.mp4")

        os.makedirs("outputs/reels", exist_ok=True)

        for i, seg in enumerate(segments[:5]):
            output = f"outputs/reels/reel_{i+1}.mp4"
            cut_reel("temp.mp4", seg["start"], 30, output)
            st.video(output)
