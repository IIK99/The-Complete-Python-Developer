# Ini membantu dalam mengurangi kerumitan dan meningkatkan efisiensi.
# Contohnya, saat kita menggunakan mobil, kita hanya perlu tahu cara mengemudi,
# bukan bagaimana mesin bekerja.

from abc import ABC, abstractmethod


class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


persegi = Persegi(4)
print(persegi.luas())  # Output: 16, (4 * 4)
