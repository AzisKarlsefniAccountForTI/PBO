from class_models import *

# ==================== Tahap 4 & 5 ====================
# CLI dan Validasi Input

# CLI
def jalankan_cli(sistem):
    while True:
        print("\n===== MENU UTAMA SISTEM INVENTARIS BMN =====")
        print("1. Tampilkan Semua Aset")
        print("2. Tambah Aset Baru")
        print("3. Proses Peminjaman Aset")
        print("4. Proses Pengembalian Aset")
        print("5. Kelola Peminjam")
        print("6. Ubah Status Aset (Pemeliharaan)")
        print("0. Keluar")

        pilihan = input("▶ Masukkan pilihan Anda: ")

        if pilihan == '1':
            sistem.tampilkan_semua_aset()
        elif pilihan == '2':
            menu_tambah_aset(sistem)
        elif pilihan == '3':
            menu_pinjam_aset(sistem)
        elif pilihan == '4':
            menu_kembalikan_aset(sistem)
        elif pilihan == '5':
            menu_kelola_peminjam(sistem)
        elif pilihan == '6':
            menu_set_pemeliharaan(sistem)
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan sistem. Sampai jumpa!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.")

def menu_tambah_aset(sistem):
    print("\n--- Tambah Aset Baru ---")
    print("Tipe Aset: [1] Elektronik, [2] Furnitur, [3] Kendaraan")

    tipe = input("▶ Pilih tipe: ")
    kode = input("▶ Kode Aset: ")
    nama = input("▶ Nama Aset: ")
    tahun = input("▶ Tahun Pengadaan: ")

    # Validasi Input
    if not tahun.isdigit():
        print("❌ GAGAL: Tahun harus berupa angka.")
        return

    if tipe == '1':
        merk = input("▶ Merk: ")
        aset = Elektronik(kode, nama, int(tahun), merk)
    elif tipe == '2':
        material = input("▶ Material: ")
        aset = Furnitur(kode, nama, int(tahun), material)
    elif tipe == '3':
        nopol = input("▶ Nomor Polisi: ")
        aset = Kendaraan(kode, nama, int(tahun), nopol)
    else:
        print("❌ GAGAL: Tipe aset tidak dikenal.")
        return

    sistem.tambah_aset(aset)

def menu_pinjam_aset(sistem):
    print("\n--- Proses Peminjaman Aset ---")

    kode_aset = input("▶ Masukkan Kode Aset yang akan dipinjam: ")
    id_peminjam = input("▶ Masukkan ID Peminjam: ")

    aset = sistem.cari_aset_by_kode(kode_aset)
    peminjam = sistem.cari_peminjam_by_id(id_peminjam)

    # Validasi Logika Bisnis
    if aset and peminjam:
        durasi_str = input("▶ Durasi peminjaman (hari): ")

        # Validasi Input
        if not durasi_str.isdigit() or int(durasi_str) <= 0:
            print("❌ GAGAL: Durasi harus berupa angka positif.")
            return

        if aset.pinjam(peminjam):
            # Polimorfisme
            biaya = aset.hitung_biaya_sewa(int(durasi_str))
            print(f"💰 Estimasi biaya sewa: Rp {biaya:,.0f}")

    elif not aset:
        print(f"❌ GAGAL: Aset dengan kode '{kode_aset}' tidak ditemukan.")
    else:
        print(f"❌ GAGAL: Peminjam dengan ID '{id_peminjam}' tidak terdaftar.")

def menu_kembalikan_aset(sistem):
    print("\n--- Proses Pengembalian Aset ---")

    kode_aset = input("▶ Masukkan Kode Aset yang dikembalikan: ")
    aset = sistem.cari_aset_by_kode(kode_aset)

    if aset:
        aset.kembalikan()
    else:
        print(f"❌ GAGAL: Aset dengan kode '{kode_aset}' tidak ditemukan.")

def menu_set_pemeliharaan(sistem):
    print("\n--- Ubah Status Aset ke Pemeliharaan ---")

    kode_aset = input("▶ Masukkan Kode Aset: ")
    aset = sistem.cari_aset_by_kode(kode_aset)

    if aset:
        aset.set_pemeliharaan()
    else:
        print(f"❌ GAGAL: Aset dengan kode '{kode_aset}' tidak ditemukan.")

def menu_kelola_peminjam(sistem):
    while True:
        print("\n--- Kelola Peminjam ---")
        print("1. Tampilkan Semua Peminjam")
        print("2. Tambah Peminjam Baru")
        print("0. Kembali ke Menu Utama")

        pilihan = input("▶ Pilih opsi: ")

        if pilihan == '1':
            sistem.tampilkan_semua_peminjam()

        elif pilihan == '2':
            id_peminjam = input("▶ ID Peminjam (NIP/NIM): ")
            nama = input("▶ Nama Lengkap: ")
            unit = input("▶ Unit/Prodi: ")

            sistem.tambah_peminjam(
                Peminjam(id_peminjam, nama, unit)
            )

        elif pilihan == '0':
            break

        else:
            print("❌ Pilihan tidak valid.")
