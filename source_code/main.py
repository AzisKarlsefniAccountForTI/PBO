from class_models import *
from menu_cli import *

# Program Utama
if __name__ == "__main__":
    sistem_ft = SistemInventaris("Fakultas Teknik")

    print("Memuat data awal...")

    sistem_ft.tambah_aset(
        Elektronik(
            "EL-001",
            "Proyektor InFocus",
            2022,
            "InFocus"
        )
    )

    sistem_ft.tambah_aset(
        Furnitur(
            "FN-001",
            "Meja Rapat",
            2019,
            "Kayu Jati"
        )
    )

    sistem_ft.tambah_aset(
        Kendaraan(
            "KD-001",
            "Toyota Avanza",
            2021,
            "B 1234 FT"
        )
    )

    sistem_ft.tambah_peminjam(
        Peminjam(
            "19900101",
            "Dr. Budi Santoso",
            "Teknik Informatika"
        )
    )

    sistem_ft.tambah_peminjam(
        Peminjam(
            "19850505",
            "Prof. Citra Lestari",
            "Teknik Elektro"
        )
    )

    jalankan_cli(sistem_ft)
