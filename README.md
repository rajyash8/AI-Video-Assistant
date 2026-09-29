# 🎬 AI Video Assistant

An AI-powered meeting and video intelligence assistant that converts YouTube videos or local audio/video files into structured, searchable insights.

The system combines **Whisper-based transcription, LLM-powered summarization, information extraction, and Retrieval-Augmented Generation (RAG)** to help users understand and interact with long-form meeting content.

---

## 🚀 Features

- 🎥 **YouTube & Local File Support**
  - Process YouTube video URLs
  - Process local audio/video files

- 🎙️ **Automatic Transcription**
  - Local Whisper-based speech-to-text
  - Supports English transcription
  - Hinglish processing using Sarvam AI

- 📝 **AI Meeting Summarization**
  - Generates concise meeting summaries
  - Automatically creates a professional meeting title

- ✅ **Action Item Extraction**
  - Identifies tasks discussed during the meeting
  - Extracts responsible owners and deadlines when mentioned

- 🔑 **Key Decision Extraction**
  - Identifies important decisions made during the meeting

- ❓ **Open Question Detection**
  - Finds unresolved questions and follow-up topics

- 🧠 **RAG-powered Meeting Chat**
  - Ask questions about the transcript
  - Retrieves relevant transcript sections using semantic search
  - Answers only from the available meeting context

- 💻 **Streamlit Interface**
  - Interactive dashboard
  - Pipeline status tracking
  - Transcript viewer
  - AI insights
  - Conversational RAG interface

---

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │   YouTube / Local    │
                    │      Audio/Video     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Audio Processing   │
                    │  yt-dlp / FFmpeg     │
                    │      / pydub         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Transcription    │
                    │      Whisper /        │
                    │      Sarvam AI        │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
          ┌─────────────────┐    ┌──────────────────┐
          │   LLM Analysis  │    │   Vector Store   │
          │                 │    │                  │
          │ Title           │    │ HuggingFace      │
          │ Summary         │    │ Embeddings       │
          │ Action Items    │    │ + ChromaDB       │
          │ Decisions       │    │                  │
          │ Questions       │    └────────┬─────────┘
          └─────────────────┘             │
                                          ▼
                                ┌──────────────────┐
                                │    RAG Engine     │
                                │                  │
                                │ Retrieve context │
                                │ + Groq LLM       │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │    Streamlit UI   │
                                │                  │
                                │ Summary           │
                                │ Transcript        │
                                │ Insights          │
                                │ Meeting Chat      │
                                └──────────────────┘




⚙️ How It Works
1. Input

The user provides either:

A YouTube URL
A local audio/video file
2. Audio Processing

YouTube audio is downloaded using yt-dlp and converted into WAV format.

Long audio files are divided into smaller chunks for efficient processing.

3. Transcription

The audio is transcribed using:

Whisper for English
Sarvam AI for Hinglish
4. AI Analysis

The transcript is processed using a Groq-powered LLM to generate:

Meeting title
Summary
Action items
Key decisions
Open questions
5. Vector Database

The transcript is split into smaller chunks and converted into embeddings using Hugging Face Sentence Transformers.

These embeddings are stored in ChromaDB.

6. RAG Chat

When the user asks a question:

User Question
      ↓
Semantic Search
      ↓
Relevant Transcript Chunks
      ↓
Context + Question
      ↓
Groq LLM
      ↓
Answer

The assistant is instructed to answer based only on the retrieved meeting context.

🔑 Environment Variables

Create a .env file locally:

GROQ_API_KEY=your_groq_api_key
SARVAM_API_KEY=your_sarvam_api_key

WHISPER_MODEL=base
SARVAM_STT_MODEL=saaras:v2.5
