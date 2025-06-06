from difflib import SequenceMatcher

def match_script_to_transcript(script_text, segments):
    matches = []
    script_lines = [line.strip() for line in script_text.split('\n') if line.strip()]
    
    for line in script_lines:
        best = None
        best_score = 0
        for seg in segments:
            score = SequenceMatcher(None, line.lower(), seg["text"].lower()).ratio()
            if score > best_score:
                best = seg
                best_score = score
        if best:
            matches.append({
                "script": line,
                "start": best["start"],
                "end": min(best["end"], best["start"] + 10)  # giới hạn 10s
            })
    return matches
