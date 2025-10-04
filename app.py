from flask import Flask, render_template, request, jsonify
import json
import difflib

app = Flask(__name__)

with open("static/qna.json", "r", encoding="utf-8") as f:
    qna = json.load(f)

greetings = {
    "hi": "Hello gorgeous 💕! I’m your Makeup Assistant.",
    "hello": "Hi beauty ✨! Ask me about products, tips, or routines.",
    "hey": "Hey glam queen 👑! Ready to glow?",
    "good morning": "Good morning ☀️! Shall we talk skincare or makeup?",
    "good evening": "Good evening 🌙! Let’s chat about beauty essentials.",
    "thanks": "You’re welcome 💖. Stay fabulous!"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "").lower().strip()

    # Normalize short forms
    replacements = {
        "spf": "sunscreen",
        "lipstick recs": "lipstick recommendations",
        "best foundation": "foundation recommendation"
    }
    for k, v in replacements.items():
        user_question = user_question.replace(k, v)

    # Check greetings
    for key, reply in greetings.items():
        if user_question.startswith(key):
            return jsonify({"answer": reply})

    # Fuzzy matching
    questions = [qa["question"].lower() for qa in qna]
    match = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.4)

    if match:
        for qa in qna:
            if qa["question"].lower() == match[0]:
                return jsonify({"answer": qa["answer"]})

    return jsonify({"answer": "Hmm 🤔 I don’t know that one yet. But I can help with makeup tips, product suggestions, and skincare basics!"})

if __name__ == "__main__":
    app.run(debug=True)
