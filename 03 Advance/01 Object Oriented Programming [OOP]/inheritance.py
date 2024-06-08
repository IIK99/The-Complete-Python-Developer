class User:
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrow: arrow left- {self.num_arrows}")


wizard1 = Wizard("Merlin", 80)
archer1 = Archer("Robin", 100)
wizard1.attack()
archer1.attack()
print(isinstance(wizard1, Wizard))
print(isinstance(archer1, object))


print("\nInheritance")


class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def perkenalan(self):
        print(f"Nama saya {self.nama}, umur saya {self.umur} tahun.")


class MahasiswaInformatika(Mahasiswa):
    def __init__(self, nama, umur, bahasa_pemrograman):
        super().__init__(nama, umur)  # khusus yang akan di output
        self.bahasa_pemrograman = bahasa_pemrograman

    def perkenalan(self):
        super().perkenalan()  # khusus yang akan di output
        print(f"Saya suka bahasa pemrograman {self.bahasa_pemrograman}.")


mahasiswa2 = MahasiswaInformatika("Budi", 22, "Python")
mahasiswa2.perkenalan()

print("\nObject introspection")
print(dir(mahasiswa2))
