# 🚀 PANDUAN INSTALASI - AI COPYWRITING PRO (GROQ EDITION)

## 🎉 VERSI 100% GRATIS DENGAN GROQ API!

Groq adalah AI super cepat dan **GRATIS UNLIMITED**! Perfect untuk copywriting!

---

## ✨ Keunggulan Groq:

✅ **100% GRATIS** - Tidak perlu kartu kredit
✅ **Unlimited** - Generate sebanyak yang Anda mau
✅ **Super Cepat** - Respon dalam 1-2 detik
✅ **Kualitas Tinggi** - Menggunakan Llama 3.1 70B
✅ **Tanpa Kredit** - Tidak perlu top up

---

## 📦 LANGKAH 1: Install Dependencies

Buka Command Prompt dan jalankan:

```bash
cd "C:\Users\Revitha Vebiola\Documents\website AI\ai-copywriting-project"
pip install -r requirements.txt
```

---

## 🔑 LANGKAH 2: Dapatkan API Key Groq (GRATIS!)

### 2.1 Daftar di Groq

1. **Buka browser:** https://console.groq.com/
2. **Klik "Sign Up"** atau langsung login dengan Google
3. **Verifikasi email** Anda (jika diminta)
4. **SELESAI!** Anda langsung dapat akses gratis

### 2.2 Buat API Key

1. Setelah login, klik menu **"API Keys"** di sidebar kiri
2. Klik tombol **"Create API Key"**
3. Beri nama: **"AI Copywriting"**
4. Klik **"Submit"** atau **"Create"**
5. **COPY API key** yang muncul (format: `gsk_xxxxxxxxxxxxxxxxxxxxx`)

⚠️ **SIMPAN BAIK-BAIK!** API key hanya muncul sekali!

---

## ⚙️ LANGKAH 3: Setting API Key

### CARA A: Menggunakan File .env (RECOMMENDED)

1. **Buka folder project di File Explorer:**
   ```
   C:\Users\Revitha Vebiola\Documents\website AI\ai-copywriting-project
   ```

2. **Copy file `.env.example` menjadi `.env`:**
   - Klik kanan `.env.example` → Copy
   - Klik kanan di folder → Paste
   - Rename hasil copy menjadi `.env` (hapus semua kecuali .env)

3. **Edit file `.env` dengan Notepad:**
   - Klik kanan file `.env` → Open with → Notepad
   - Ganti:
   ```
   GROQ_API_KEY=your-groq-api-key-here
   ```
   Menjadi:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   (Paste API key Groq Anda)

4. **Save** (Ctrl+S) dan tutup Notepad

### CARA B: Set Environment Variable (ALTERNATIF)

Di Command Prompt, jalankan setiap kali sebelum menjalankan app:

```bash
set GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
python app.py
```

---

## 🚀 LANGKAH 4: Jalankan Website

1. **Buka Command Prompt**

2. **Masuk ke folder project:**
   ```bash
   cd "C:\Users\Revitha Vebiola\Documents\website AI\ai-copywriting-project"
   ```

3. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```

4. **Tunggu sampai muncul:**
   ```
   🚀 AI COPYWRITING PRO - GROQ EDITION (100% GRATIS!)
   * Running on http://0.0.0.0:5000
   ```

5. **Buka browser:**
   ```
   http://localhost:5000
   ```

---

## ✅ LANGKAH 5: Test Website

1. **Pilih:**
   - Jenis Konten: **Slogan / Tagline**
   - Topik: **Kafe kopi dengan WiFi cepat dan suasana nyaman**
   - Tone: **Friendly**
   - Bahasa: **Bahasa Indonesia**

2. **Klik "Generate Copywriting"**

3. **Tunggu 2-3 detik**

4. **BOOM! 🎉** Hasil copywriting muncul!

---

## 🔧 TROUBLESHOOTING

### Error: "API key belum diatur"

**Solusi:**
1. Cek file `.env` ada di folder project
2. Pastikan isinya: `GROQ_API_KEY=gsk_xxx...`
3. Restart aplikasi

### Error: "API key tidak valid"

**Solusi:**
1. Cek API key di https://console.groq.com/keys
2. Copy paste dengan benar (tidak ada spasi)
3. Buat API key baru jika perlu

### Error: "Rate limit tercapai"

**Solusi:**
- Groq gratis: 30 request per menit
- Tunggu 1 menit, lalu coba lagi
- Atau buat akun Groq baru dengan email berbeda

### Website tidak bisa diakses

**Solusi:**
1. Pastikan `python app.py` tidak ada error
2. Cek port 5000 tidak dipakai aplikasi lain
3. Coba ganti port (edit app.py, ubah 5000 jadi 8000)

---

## 💡 TIPS & TRIK

### Groq API Gratis:
- ✅ **30 requests per menit** (lebih dari cukup!)
- ✅ **6,000 tokens per menit**
- ✅ **14,400 requests per hari**
- ✅ **Tidak perlu kartu kredit**
- ✅ **Tidak ada expired kredit**

### Optimasi Penggunaan:
1. **Deskripsi detail** → Hasil lebih baik
2. **Pilih tone yang sesuai** → Lebih natural
3. **Coba beberapa kali** → Dapatkan variasi
4. **Edit hasil** → Sesuaikan dengan kebutuhan

### Model Groq yang Digunakan:
- **Llama 3.1 70B Versatile** (model default)
- Sangat bagus untuk copywriting
- Cepat dan akurat
- Gratis unlimited!

---

## 📊 Perbandingan Groq vs Claude

| Fitur | Groq | Claude/Anthropic |
|-------|------|------------------|
| Harga | **100% GRATIS** | $5 minimum top up |
| Kecepatan | ⚡ Super cepat (1-2 detik) | 🐢 Agak lambat (5-10 detik) |
| Limit | 30 req/menit | Tergantung kredit |
| Kualitas | ⭐⭐⭐⭐ Sangat bagus | ⭐⭐⭐⭐⭐ Excellent |
| Setup | ✅ Mudah | ✅ Mudah |
| Kredit Card | ❌ Tidak perlu | ✅ Perlu untuk top up |

**Verdict:** Untuk belajar dan testing, Groq **JAUH LEBIH BAIK** karena GRATIS!

---

## 🎯 KESIMPULAN

Dengan Groq API:
- ✅ Tidak perlu bayar sepeser pun
- ✅ Generate unlimited copywriting
- ✅ Kecepatan super cepat
- ✅ Kualitas tetap bagus
- ✅ Perfect untuk portfolio & belajar

---

## 🆘 BUTUH BANTUAN?

Jika ada masalah:
1. Screenshot error yang muncul
2. Cek semua langkah sudah benar
3. Pastikan Python 3.7+ terinstall

---

**Selamat mencoba! Generate copywriting sebanyak yang Anda mau! 🎉**

**#GratisTapiBerkualitas #GroqAI #AICopywriting**
