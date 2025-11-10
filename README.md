# 🤖 Gemini Kids Chatbot (SD & SMP Edition)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)
![Gemini](https://img.shields.io/badge/Google-Gemini%20API-yellow?logo=google)
![Theme](https://img.shields.io/badge/Theme-SD%20%7C%20SMP-brightgreen)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🎯 Deskripsi

**Gemini Kids Chatbot** adalah chatbot edukatif berbasis **Flask + Google Gemini API**  
yang dirancang untuk membantu anak **SD hingga SMP** memahami konsep sains, teknologi, dan pelajaran sekolah dengan **cara yang seru, mudah dipahami, dan ramah anak.**

💬 Chatbot ini bisa **berubah gaya bicara dan warna tampilan** sesuai mode:
- 🎨 **Mode SD** → gaya ceria, banyak emoji, warna cerah
- 🧠 **Mode SMP** → gaya santai, logis, dan edukatif dengan warna biru kalem  

---

## 🧱 Struktur Project
<img width="188" height="243" alt="struktur" src="https://github.com/user-attachments/assets/1d692c35-3caf-4fdb-9e8d-5373e2c3ed58" />



---

## ⚙️ Instalasi dan Setup

### 1️⃣ Pastikan sudah terinstal **uv**
`uv` adalah pengganti modern untuk `pip` dan `virtualenv` (lebih cepat & aman).

curl -LsSf https://astral.sh/uv/install.sh | sh

## Buat  environment project
cd chatbot-SD_SMP
uv init
uv add flask google-genai python-dotenv

## Buat file .env
GOOGLE_API_KEY="ISI_API_KEY_KAMU_DI_SINI"

## Menjalankan Aplikasi
uv run app.py

Buka browser dan akses
http://127.0.0.1:5000


### Mode Tema
Kamu bisa mengganti mode di pojok kanan atas:
🌈 Mode SD → Bahasa ceria, warna pastel
🧩 Mode SMP → Bahasa logis, warna biru keabu-abuan
Tema disimpan otomatis di browser, jadi tidak hilang saat reload.


### Fitur Utama
🧠 Integrasi dengan Google Gemini API
💬 Interaktif langsung dari browser
🎨 Dual mode tema (SD ↔ SMP)
🔐 Aman: API key disimpan di file .env
🪄 Tampilan responsif dan ramah anak

### Contoh Penggunaan
Input:
Jelaskan bagaimana awan terbentuk.

Output (Mode SD):
☁️ Jadi gini, awan tuh terbentuk waktu udara yang lembab naik ke langit dan jadi dingin! Uap airnya berubah jadi butiran air kecil deh, terus ngumpul jadi awan. Seru kan? 🌤️

Output (Mode SMP):
Awan terbentuk saat uap air di udara naik ke atmosfer dan mendingin hingga mengalami kondensasi menjadi butiran air kecil. Proses ini terjadi karena perbedaan suhu antara permukaan bumi dan lapisan udara atas.

### Lisensi
Proyek ini dirilis di bawah lisensi MIT — bebas digunakan dan dimodifikasi untuk keperluan edukatif dan non-komersial.

###Kontributor
Dibuat oleh: Wahyu Budi
📫 Email: wbudi75@gmail.com

