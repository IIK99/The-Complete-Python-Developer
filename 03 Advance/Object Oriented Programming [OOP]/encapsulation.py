print("\nEncapsulation")


class Mahasiswa:
    def __init__(self, nama, umur):
        self.__nama = nama
        self.__umur = umur

    def get_nama(self):
        return self.__nama, self.__umur

    def set_nama(self, nama, umur):
        self.__nama = nama
        self.__umur = umur


mahasiswa3 = Mahasiswa("Cici", 21)
print(mahasiswa3.get_nama())
mahasiswa3.set_nama("Dewi", 22)
print(mahasiswa3.get_nama())
