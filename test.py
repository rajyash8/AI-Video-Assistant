import time
from dotenv import load_dotenv

load_dotenv()   # MUST be before any core/ imports

from utils.audio_processor import process_input_audio
from core.transcriber import transcribe_all
from core.summarize import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions
)


source = "https://www.youtube.com/watch?v=_Q-e_nczWqM&t=223s"
language = "english"   # "english" → Whisper, "hinglish" → Sarvam


# ---------------------------------------------------------
# AUDIO PROCESSING
# ---------------------------------------------------------

chunks = process_input_audio(source)


# ---------------------------------------------------------
# TRANSCRIPTION
# ---------------------------------------------------------

transcript = transcribe_all(chunks, language=language)

print("\n" + "=" * 60)
print("📝 TRANSCRIPT")
print("=" * 60)
print(transcript[:500] + "..." if len(transcript) > 500 else transcript)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

title = generate_title(transcript)

time.sleep(2)


# ---------------------------------------------------------
# SUMMARY
# ---------------------------------------------------------

summary = summarize(transcript)

print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)

print("\n📋 SUMMARY")
print("-" * 60)
print(summary)


# ---------------------------------------------------------
# MEETING ANALYSIS
# Limit transcript size to reduce Groq token usage
# ---------------------------------------------------------

analysis_transcript = transcript[:12000]


# ACTION ITEMS

time.sleep(2)

action_items = extract_action_items(analysis_transcript)


# KEY DECISIONS

time.sleep(2)

decisions = extract_key_decisions(analysis_transcript)


# OPEN QUESTIONS

time.sleep(2)

questions = extract_questions(analysis_transcript)


# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------

print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)


print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)


print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)