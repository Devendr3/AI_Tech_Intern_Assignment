
from flask import Flask, render_template, request, redirect
import sqlite3, os
from openai import OpenAI

app = Flask(__name__)

# OpenAI client (optional)
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None

# DB setup
def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return render_template("todo.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form["task"]
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete(task_id):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/suggest")
def suggest():
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a productivity assistant."},
                    {"role": "user", "content": "Suggest a simple productive task."}
                ],
                max_tokens=30
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"
    else:
        return "AI suggestions disabled (no API key)."

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
