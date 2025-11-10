import os
from google import genai
from dotenv import load_dotenv

# --- Load API Key ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY belum diatur. Jalankan: export GOOGLE_API_KEY='API_KEY_KAMU' atau isi file .env")

# --- Inisialisasi Klien ---
client = genai.Client(api_key=api_key)

print("=====================================")
print("🤖  Gemini Gaul Chat CLI")
print("Ketik pertanyaanmu (atau 'exit' untuk keluar)")
print("=====================================\n")

while True:
    user_input = input("💬 Pertanyaan: ")
    if user_input.strip().lower() in ["exit", "keluar", "quit"]:
        print("👋 Oke, sampai jumpa lagi!")
        break

    # --- Prompt dikombinasikan dengan instruksi gaya bahasa ---
    style_prompt = (
        "Jawab pertanyaan berikut dengan gaya bahasa yang santai, mudah dipahami, dan sedikit gaul.\n"
        "Gunakan istilah sehari-hari yang familiar, tapi tetap sopan.\n\n"
        f"Pertanyaan pengguna: {user_input}"
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=style_prompt
    )

    print("\n🧠 Gemini Gaul:", response.text.strip(), "\n")
