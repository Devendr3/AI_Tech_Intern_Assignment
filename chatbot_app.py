
# chatbot_app.py
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set your OpenAI API Key
openai.api_key = "sk-abc123..."

# Predefined FAQ database
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
    user_msg = request.json.get("message").lower()

    # Check FAQs first
    for key, answer in faqs.items():
        if key in user_msg:
            return jsonify({"response": answer})

    # Default response if no match found
    return jsonify({"response": "I can only answer FAQs like programs, duration, mode, certificates, and mentors."})

if __name__ == "__main__":
    app.run(debug=True)

