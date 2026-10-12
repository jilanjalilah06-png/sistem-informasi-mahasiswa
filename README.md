# Sistem Informasi Mahasiswa

## Deskripsi
Sistem Informasi Mahasiswa adalah aplikasi berbasis terminal yang dibuat menggunakan Python untuk mengelola data mahasiswa.

## Identitas
- Nama: Jilan Jalilah
- Program Studi: Sistem Informasi
- Angkatan: 2024

## Fitur
- Menambahkan data mahasiswa.
- Menampilkan seluruh data mahasiswa.
- Mencari mahasiswa berdasarkan NIM.
- Menghapus data mahasiswa.
- Memvalidasi NIM, nama, dan rentang IPK.
- Mencegah penggunaan NIM yang duplikat.

## Teknologi
- Python
- Rich
- Pytest

## Persyaratan
- Python 3.10 atau lebih baru
- Git (opsional, untuk pengelolaan versi)

## Instalasi

1. Clone repository:
   ```bash
   git clone URL_REPOSITORY
   ```
2. Masuk ke folder proyek:
   ```bash
   cd sim-mahasiswa
   ```
3. Buat virtual environment:
   ```bash
   python -m venv venv
   ```
4. Aktifkan virtual environment di Windows CMD:
   ```bat
   venv\Scripts\activate.bat
   ```
5. Instal dependensi:
   ```bash
   python -m pip install -r requirements.txt
   ```

## Menjalankan Program

```bash
python -m src.main
```

## Menjalankan Pengujian

```bash
python -m pytest tests/ -v
```

## Struktur Proyek

```text
sim-mahasiswa/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── .gitignore
├── README.md
└── requirements.txt
```

## Catatan
Aplikasi ini merupakan proyek praktikum Python untuk mempelajari struktur proyek, pengelolaan data, pengujian, dan penggunaan Git.