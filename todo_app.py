# todo_app.py
from flask import Flask, render_template, request, redirect
import sqlite3, openai

from openai import OpenAI
client = OpenAI(api_key="sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx")

app = Flask(__name__)
openai.api_key = "sk-abc123..."

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
    prompt = "Suggest a simple productive task."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",   # or "gpt-4o-mini"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=30
        )
        suggestion = response.choices[0].message.content.strip()
        return suggestion
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
