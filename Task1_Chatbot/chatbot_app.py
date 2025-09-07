from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client with env variable
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_KEY) if OPENAI_KEY else None

# Predefined FAQs
faqs = {
    "programs": "Iron Lady offers Leadership Development, Career Accelerator, and Confidence Coaching programs.",
    "duration": "Most programs run between 6 weeks to 3 months depending on the track.",
    "mode": "Programs are primarily online, with some offline workshops in Bengaluru.",
    "certificate": "Yes, participants receive certificates upon completion.",
    "mentors": "Mentors include experienced leaders, coaches, and corporate professionals."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").lower()

    # Check FAQs first
    for key, answer in faqs.items():
        if key in user_msg:
            return jsonify({"response": answer})

    # If API key exists → AI fallback
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant about Iron Lady programs."},
                    {"role": "user", "content": user_msg}
                ],
                max_tokens=100
            )
            return jsonify({"response": response.choices[0].message.content.strip()})
        except Exception:
            return jsonify({"response": "Sorry, AI service not available now."})
    else:
        return jsonify({"response": "I can only answer FAQs like programs, duration, mode, certificates, and mentors."})

if __name__ == "__main__":
    app.run(debug=True)

