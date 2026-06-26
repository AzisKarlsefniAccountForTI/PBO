# ==================== Tahap 1 & 2 ====================
# Enkapsulasi, Inheritance, dan Polimorfisme


# Superclass
class Aset:
    def __init__(self, kode, nama, tahun_pengadaan):
        self.__kode = kode
        self.__nama = nama
        self.__tahun_pengadaan = tahun_pengadaan
        self.__status = "Tersedia"
        self.__peminjam = None

    # Enkapsulasi
    @property
    def kode(self):
        return self.__kode

    @property
    def nama(self):
        return self.__nama

    @property
    def status(self):
        return self.__status

    @property
    def peminjam(self):
        return self.__peminjam

    def pinjam(self, peminjam_obj):
        if self.__status == "Tersedia":
            self.__status = "Dipinjam"
            self.__peminjam = peminjam_obj
            print(f"✅ Aset '{self.nama}' berhasil dipinjam oleh {peminjam_obj.nama}.")
            return True
        else:
            print(f"❌ GAGAL: Aset '{self.nama}' saat ini berstatus '{self.status}'.")
            return False

    def kembalikan(self):
        if self.__status == "Dipinjam":
            peminjam_sebelumnya = self.__peminjam.nama
            self.__status = "Tersedia"
            self.__peminjam = None
            print(f"✅ Aset '{self.nama}' telah dikembalikan oleh {peminjam_sebelumnya}.")
            return True
        else:
            print(f"❌ GAGAL: Aset '{self.nama}' tidak sedang dipinjam.")
            return False

    def set_pemeliharaan(self):
        if self.__status != "Dipinjam":
            self.__status = "Dalam Pemeliharaan"
            print(f"✅ Status aset '{self.nama}' diubah menjadi 'Dalam Pemeliharaan'.")
        else:
            print(f"❌ GAGAL: Aset yang sedang dipinjam tidak bisa diubah statusnya.")

    # Polimorfisme (Method Dasar)
    def hitung_biaya_sewa(self, durasi_hari):
        biaya_dasar = 5000
        return biaya_dasar * durasi_hari

    def __str__(self):
        info_peminjam = self.peminjam.nama if self.peminjam else "-"
        return f"Kode: {self.kode:<10} | Nama: {self.nama:<20} | Status: {self.status:<20} | Peminjam: {info_peminjam}"

# Inheritance
class Elektronik(Aset):
    def __init__(self, kode, nama, tahun_pengadaan, merk):
        super().__init__(kode, nama, tahun_pengadaan)
        self.__merk = merk

    # Polimorfisme
    def hitung_biaya_sewa(self, durasi_hari):
        return 30000 * durasi_hari

    def __str__(self):
        return f"[Elektronik] {super().__str__()} | Merk: {self.__merk}"

# Inheritance
class Furnitur(Aset):
    def __init__(self, kode, nama, tahun_pengadaan, material):
        super().__init__(kode, nama, tahun_pengadaan)
        self.__material = material

    # Polimorfisme
    def hitung_biaya_sewa(self, durasi_hari):
        return 10000 * durasi_hari

    def __str__(self):
        return f"[Furnitur]   {super().__str__()} | Material: {self.__material}"

# Inheritance
class Kendaraan(Aset):
    def __init__(self, kode, nama, tahun_pengadaan, nopol):
        super().__init__(kode, nama, tahun_pengadaan)
        self.__nopol = nopol

    # Polimorfisme
    def hitung_biaya_sewa(self, durasi_hari):
        return 200000 * durasi_hari

    def __str__(self):
        return f"[Kendaraan]  {super().__str__()} | No. Polisi: {self.__nopol}"

class Peminjam:
    def __init__(self, id_peminjam, nama, unit):
        self.__id_peminjam = id_peminjam
        self.__nama = nama
        self.__unit = unit

    # Enkapsulasi
    @property
    def id_peminjam(self):
        return self.__id_peminjam

    @property
    def nama(self):
        return self.__nama

    def __str__(self):
        return f"ID: {self.id_peminjam:<12} | Nama: {self.nama:<25} | Unit: {self.__unit}"

# Kelas Manajer
class SistemInventaris:
    def __init__(self, nama_fakultas):
        self.nama_fakultas = nama_fakultas

        # Agregasi
        self.__daftar_aset = []
        self.__daftar_peminjam = []

    def tambah_aset(self, aset_obj):
        if not self.cari_aset_by_kode(aset_obj.kode):
            self.__daftar_aset.append(aset_obj)
            print(f"✅ Aset '{aset_obj.nama}' berhasil ditambahkan.")
        else:
            print(f"❌ GAGAL: Aset dengan kode '{aset_obj.kode}' sudah ada.")

    def tambah_peminjam(self, peminjam_obj):
        if not self.cari_peminjam_by_id(peminjam_obj.id_peminjam):
            self.__daftar_peminjam.append(peminjam_obj)
            print(f"✅ Peminjam '{peminjam_obj.nama}' berhasil ditambahkan.")
        else:
            print(f"❌ GAGAL: Peminjam dengan ID '{peminjam_obj.id_peminjam}' sudah ada.")

    def cari_aset_by_kode(self, kode):
        for aset in self.__daftar_aset:
            if aset.kode == kode:
                return aset
        return None

    def cari_peminjam_by_id(self, id_peminjam):
        for peminjam in self.__daftar_peminjam:
            if peminjam.id_peminjam == id_peminjam:
                return peminjam
        return None

    def tampilkan_semua_aset(self):
        print("\n" + "=" * 80)
        print(f"DAFTAR ASET INVENTARIS - {self.nama_fakultas.upper()}")
        print("=" * 80)

        if not self.__daftar_aset:
            print("Inventaris kosong.")
        else:
            # Polimorfisme
            for aset in self.__daftar_aset:
                print(aset)

        print("=" * 80)

    def tampilkan_semua_peminjam(self):
        print("\n" + "=" * 60)
        print("DAFTAR PEMINJAM")
        print("=" * 60)

        if not self.__daftar_peminjam:
            print("Tidak ada peminjam terdaftar.")
        else:
            for peminjam in self.__daftar_peminjam:
                print(peminjam)

        print("=" * 60)
