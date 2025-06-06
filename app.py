import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import tempfile
import os
from utils.transcript import transcribe_video
from utils.alignment import match_script_to_transcript
from utils.cutter import cut_clips

st.set_page_config(page_title="Video Summary Cutter", layout="centered")
st.title("🎬 Tự động cắt video theo kịch bản")

video_file = st.file_uploader("📹 Upload video (.mp4)", type=["mp4"])
script_file = st.file_uploader("📄 Upload kịch bản (.txt)", type=["txt"])

if video_file and script_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_vid:
        tmp_vid.write(video_file.read())
        video_path = tmp_vid.name

    script_text = script_file.read().decode("utf-8")
    st.video(video_path)
    st.markdown("### ✏️ Kịch bản tóm tắt")
    st.code(script_text.strip())

    if st.button("▶️ Bắt đầu phân tích và cắt video"):
        with st.spinner("Đang xử lý transcript..."):
            transcript_text, segments = transcribe_video(video_path)
        with st.spinner("Đang so khớp nội dung..."):
            matches = match_script_to_transcript(script_text, segments)
        with st.spinner("Đang cắt video..."):
            clips = cut_clips(video_path, matches)

        st.success("✅ Hoàn tất! Các đoạn cắt được hiển thị bên dưới:")
        for i, (text, path) in enumerate(clips):
            st.markdown(f"**Đoạn {i+1}:** {text}")
            st.video(path)
else:
    st.info("Vui lòng upload cả video và file kịch bản để bắt đầu.")
