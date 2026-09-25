# 🚂 Honkai: Web Rail

Selamat datang di **Honkai: Web Rail**! Proyek ini adalah aplikasi web interaktif yang terinspirasi dari game populer Honkai: Star Rail. 

## ✨ Fitur Utama

- **Antarmuka Futuristik**: Desain UI/UX khas Honkai dengan nuansa _Dark Mode_ dan aksen _Gold/Blue_.
- **Sistem Leaderboard**: Skrip Python (`build_leaderboard.py`) untuk memproses dan menampilkan peringkat pemain.
- **Data Extractor**: Modul `extract.py` untuk mengambil/memproses data-data in-game.
- **Auto Patching**: Dilengkapi dengan berbagai skrip _patching_ otomatis (seperti `patch_bugs.py`, `patch_ui.py`) untuk memudahkan pembaruan sistem dan antarmuka.

## 🛠️ Teknologi yang Digunakan

- **Frontend**: HTML5, CSS3, Vanilla JavaScript.
- **Backend & Scripting**: Python (untuk ekstraksi data dan sistem pembaruan).
- **Font**: Orbitron & Rajdhani dari Google Fonts untuk tampilan Sci-Fi yang autentik.

## 🚀 Cara Menjalankan Proyek (Lokal)

1. **Clone Repository**
   ```bash
   git clone https://github.com/Azriel121212/honkairail.git
   cd honkairail
   ```

2. **Jalankan Skrip Data (Opsional, jika diperlukan)**
   Jalankan file ekstraksi atau _rebuild_ jika kamu ingin memperbarui data:
   ```bash
   python extract.py
   python rebuild.py
   ```

3. **Buka Aplikasi Web**
   Buka file `index.html` menggunakan browser favoritmu, atau jalankan local server jika kamu menggunakan environment seperti Laragon/XAMPP:
   ```bash
   http://localhost/honkairail/index.html
   ```

## 📂 Struktur Folder Utama

- `index.html` - File utama untuk antarmuka web.
- `extract.py` - Skrip untuk mengekstrak atau memperbarui aset/data.
- `build_leaderboard.py` - Skrip untuk memproses _Leaderboard_.
- `patch_*.py` - Kumpulan skrip patching & autobuild untuk memudahkan pemeliharaan proyek.
- `test.js` - Skrip JavaScript untuk logika web / testing.

## 🤝 Kontribusi

Pull request selalu terbuka! Jika kamu ingin menambahkan fitur baru, memperbaiki _bug_, atau mempercantik _User Interface_, jangan ragu untuk membuat _fork_ dan mengirimkan PR.

## 📜 Lisensi

Proyek ini dibuat untuk tujuan hiburan dan pembelajaran. Segala aset yang berkaitan dengan Honkai: Star Rail adalah hak cipta dari HoYoverse (Cognosphere).
