# Public Variables: Dapat diakses dari mana saja, baik dari dalam maupun luar kelas.
# Dalam Python, variabel publik biasanya tidak di awali dengan garis bawah.

# Private Variables: Hanya dapat diakses dari dalam kelas itu sendiri.
# Dalam Python, variabel privat di awali dengan dua garis bawah (__).


class Mobil:
    def __init__(self, merek, model):
        self.merek = merek  # Public
        self.__model = model  # Private

    def tampilkan_model(self):
        return self.__model


mobil = Mobil("Toyota", "Corolla")
print(mobil.merek)  # Output: Toyota
print(mobil.tampilkan_model())  # Output: Corolla
# print(mobil.__model)  # Akan menyebabkan error karena __model adalah private
