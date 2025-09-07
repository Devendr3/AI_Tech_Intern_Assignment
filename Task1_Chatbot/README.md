
# Task 1: Iron Lady Chatbot

## Features
- Answers FAQs about Iron Lady programs.
- Optional AI fallback using OpenAI GPT (if API key is set).
- Simple web interface.

## Setup
```bash
cd Task1_Chatbot
pip install -r requirements.txt
setx OPENAI_API_KEY "your_api_key_here"   # Windows
python chatbot_app.py
Open http://127.0.0.1:5000/
