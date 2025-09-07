# Task 2: To-Do Manager

## Features
- Add, view, and delete tasks.
- SQLite database for persistence.
- Bonus: AI-generated task suggestions (if API key is set).

## Setup
```bash
cd Task2_TodoApp
pip install -r requirements.txt
setx OPENAI_API_KEY "your_api_key_here"   # Windows
export OPENAI_API_KEY="your_api_key_here" # Linux/Mac
python todo_app.py
Open http://127.0.0.1:5000/
