# 📦 Sistem Pengelolaan Inventaris Barang Milik Negara (BMN)

## Tentang Proyek
Sistem Pengelolaan Inventaris Barang Milik Negara (BMN) merupakan aplikasi berbasis Command Line Interface (CLI) yang dikembangkan menggunakan bahasa pemrograman Python dengan menerapkan konsep Pemrograman Berorientasi Objek (Object-Oriented Programming/OOP).

Program ini dirancang untuk membantu proses pengelolaan inventaris di lingkungan fakultas, khususnya dalam pencatatan data aset, pengelolaan data peminjam, proses peminjaman dan pengembalian aset, serta pemantauan status aset secara lebih terstruktur dan mudah digunakan.

Pengembangan sistem ini bertujuan untuk mengurangi kesalahan pencatatan yang sering terjadi pada pengelolaan inventaris secara manual serta memberikan pengalaman penerapan konsep OOP melalui pengembangan aplikasi berbasis teks.

---

## Identitas Proyek

| Keterangan | Informasi |
|------------|------------|
| Mata Kuliah | Praktikum Pemrograman Berorientasi Objek |
| Program Studi | Teknologi Informasi (S1) |
| Fakultas | Sains dan Teknologi |
| Universitas | Universitas Islam Negeri Salatiga |
| Jenis Aplikasi | Command Line Interface (CLI) |
| Bahasa Pemrograman | Python |
| Kelompok | 6 |

---

## Anggota Kelompok

1. Azis Khoirul Setiawan
2. Oryza Alpha Azzukhruf
3. Silfia Ulkhaq Fitriannisa'
4. Muhammad Syaikhul Umam

---

## Pembagian Tugas

### Pengembangan Program
- Silfia Ulkhaq Fitriannisa'
- Muhammad Syaikhul Umam

Bertanggung jawab dalam perancangan class, implementasi konsep Object-Oriented Programming (OOP), pengembangan logika program, implementasi antarmuka Command Line Interface (CLI), validasi input, proses debugging, pengujian, dan finalisasi program.

### Penyusunan Laporan
- Oryza Alpha Azzukhruf
- Azis Khoirul Setiawan

Bertanggung jawab dalam penyusunan isi laporan, dokumentasi, pengaturan format dan tata letak dokumen, pembuatan daftar isi dan daftar gambar, pengaturan penomoran, serta finalisasi laporan proyek akhir praktikum.

---

## Fitur Sistem

✅ Menampilkan daftar aset inventaris fakultas

✅ Menambahkan data aset baru

✅ Menambahkan data peminjam

✅ Melakukan proses peminjaman aset

✅ Melakukan proses pengembalian aset

✅ Mengubah status aset menjadi dalam pemeliharaan

✅ Menampilkan daftar peminjam

✅ Melakukan validasi input pengguna

✅ Menghitung biaya sewa berdasarkan jenis aset

---

## Konsep Object-Oriented Programming (OOP)

Program ini menerapkan beberapa konsep utama dalam Pemrograman Berorientasi Objek, yaitu:

- Encapsulation
- Inheritance
- Polymorphism
- Aggregation

---

## Struktur Project

```text
inventaris_bmn/
│
├── class_models.py
├── menu_cli.py
├── main.py
└── README.md
```

### Penjelasan File

#### class_models.py
Berisi implementasi seluruh class pada sistem, yaitu:

- Aset
- Elektronik
- Furnitur
- Kendaraan
- Peminjam
- SistemInventaris

File ini juga mengimplementasikan konsep Encapsulation, Inheritance, Polymorphism, dan Aggregation.

#### menu_cli.py
Berisi seluruh fungsi antarmuka berbasis teks (CLI), meliputi:

- Menu utama sistem
- Menu penambahan aset
- Menu peminjaman aset
- Menu pengembalian aset
- Menu pengelolaan peminjam
- Menu perubahan status pemeliharaan
- Validasi input pengguna

#### main.py
Berisi program utama (entry point) yang digunakan untuk:

- Membuat objek SistemInventaris
- Menginisialisasi data awal
- Menambahkan contoh data aset dan peminjam
- Menjalankan antarmuka Command Line Interface (CLI)

---

## Cara Menjalankan Program

1. Pastikan Python telah terinstal pada komputer.
2. Buka folder project menggunakan Visual Studio Code atau Terminal.
3. Jalankan perintah berikut:

```bash
python main.py
```

---

## Tujuan Pengembangan

Project ini dikembangkan sebagai pemenuhan tugas Proyek Akhir Praktikum Pemrograman Berorientasi Objek Program Studi Teknologi Informasi Fakultas Sains dan Teknologi Universitas Islam Negeri Salatiga sekaligus sebagai implementasi penerapan konsep Object-Oriented Programming (OOP) dalam pembangunan sistem informasi berbasis Command Line Interface (CLI).
