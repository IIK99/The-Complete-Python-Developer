print("\nClass and Object")


class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def perkenalan(self):
        print(
            f"Nama saya {self.nama}, umur saya {self.umur} tahun, dan saya belajar di jurusan {self.jurusan}."
        )


# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Andi", 20, "Informatika")
mahasiswa1.perkenalan()
