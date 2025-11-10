from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

# --- Setup ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY belum diatur. Tambahkan di file .env")

client = genai.Client(api_key=api_key)
app = Flask(__name__)

# --- Prompt generator ---
def make_prompt(question, mode):
    if mode == "SMP":
        return f"""
        Jawablah pertanyaan berikut dengan gaya tutor SMP yang santai, logis, dan mudah dimengerti.
        Hindari istilah teknis yang terlalu tinggi. Beri contoh dari kehidupan sehari-hari,
        dan tetap gunakan gaya bahasa yang asik dan friendly.
        
        Pertanyaan: {question}
        """
    else:
        return f"""
        Jawablah pertanyaan berikut dengan gaya guru SD yang ceria dan penuh semangat 🎉
        Gunakan kalimat pendek, banyak emoji, dan contoh nyata yang mudah dimengerti anak SD.
        
        Pertanyaan: {question}
        """

# --- Route utama ---
@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    theme = request.form.get("theme", "SD")  # default SD

    if request.method == "POST":
        question = request.form["question"]
        prompt = make_prompt(question, theme)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        answer = response.text.strip()

    return render_template("index.html", answer=answer, theme=theme)

if __name__ == "__main__":
    app.run(debug=True)
