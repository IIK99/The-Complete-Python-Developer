# class method and statistic methods
print("\nClass methods")


class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def set_species(cls, species):
        cls.species = species

    def cat(self):
        print(f"{self.name} is {self.age} years old and is a {self.species}")


# Menggunakan class method
Cat.set_species("feline")
my_cat = Cat("Cat1", 5)
my_cat.cat()  # Output: Cat1 is 5 years old and is a feline

print("\nStatistics method")


class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 1

    def cat(self):
        adult_status = "an adult" if self.is_adult(self.age) else "a kitten"
        print(f"{self.name} is {self.age} years old and is {adult_status}")


# Menggunakan static method
my_cat = Cat("Cat1", 5)
my_cat.cat()  # Output: Cat1 is 5 years old and is an adult

print("\nAnother exam")


class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        Mahasiswa.total_mahasiswa += 1

    @classmethod
    def dari_tahun_lahir(cls, nama, tahun_lahir):
        umur = 2024 - tahun_lahir
        return cls(nama, umur)

    @staticmethod
    def apakah_dewasa(umur):
        return umur >= 18

    def tampilkan_info(self):
        status_dewasa = "dewasa" if self.apakah_dewasa(self.umur) else "belum dewasa"
        print(f"{self.nama}, umur {self.umur} tahun, adalah {status_dewasa}.")


# Menggunakan classmethod untuk membuat instance
mahasiswa1 = Mahasiswa.dari_tahun_lahir("Budi", 2000)
mahasiswa2 = Mahasiswa.dari_tahun_lahir("Siti", 2010)

# Menggunakan staticmethod untuk memeriksa apakah mahasiswa sudah dewasa
print(Mahasiswa.apakah_dewasa(20))  # Output: True

# Menampilkan informasi mahasiswa
mahasiswa1.tampilkan_info()  # Output: Budi, umur 24 tahun, adalah dewasa.
mahasiswa2.tampilkan_info()  # Output: Siti, umur 14 tahun, adalah belum dewasa.
