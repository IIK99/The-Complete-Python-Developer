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

print("\nInheritance")


class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Nama saya {self.nama}, umur saya {self.umur} tahun.")


class MahasiswaInformatika(Mahasiswa):
    def __init__(self, nama, umur, bahasa_pemrograman):
        super().__init__(nama, umur)
        self.bahasa_pemrograman = bahasa_pemrograman

    def perkenalan(self):
        super().perkenalan()
        print(f"Saya suka bahasa pemrograman {self.bahasa_pemrograman}.")


mahasiswa2 = MahasiswaInformatika("Budi", 22, "Python")
mahasiswa2.perkenalan()

print("\nEncapsulation")


class Mahasiswa:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama


mahasiswa3 = Mahasiswa("Cici", 21)
print(mahasiswa3.get_nama())
mahasiswa3.set_nama("Dewi")
print(mahasiswa3.get_nama())
