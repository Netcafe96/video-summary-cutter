from faster_whisper import WhisperModel

def transcribe_video(video_path):
    model = WhisperModel("base", compute_type="int8")
    segments, _ = model.transcribe(video_path)
    
    full_text = []
    segment_list = []
    for seg in segments:
        full_text.append(seg.text)
        segment_list.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text
        })
    
    return " ".join(full_text), segment_list
