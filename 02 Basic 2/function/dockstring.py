print("\nTesting")


def test(a):
    """
    Info: this function tests and print param a
    """
    print(a)


print(test.__doc__)

print("\nDef function")


def tambah(a, b):
    """
    Mengembalikan hasil penjumlahan dari dua angka a dan b.

    Parameters:
    a (int or float): Angka pertama.
    b (int or float): Angka kedua.

    Returns:
    int or float: Hasil penjumlahan a dan b.
    """
    return a + b


hasil = tambah(5, 3)
print(hasil)  # Output: 8

print("\nClass")


class PersegiPanjang:
    """
    Kelas yang merepresentasikan persegi panjang.

    Attributes:
    panjang (float): Panjang persegi panjang.
    lebar (float): Lebar persegi panjang.
    """

    def __init__(self, panjang, lebar):
        """
        Inisialisasi atribut panjang dan lebar.

        Parameters:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.
        """
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        """
        Menghitung dan mengembalikan luas persegi panjang.

        Returns:
        float: Luas persegi panjang.
        """
        return self.panjang * self.lebar


# Membuat objek persegi panjang
pp = PersegiPanjang(10, 5)
print(pp.hitung_luas())  # Output: 50

print(help(tambah))
print(help(PersegiPanjang))

# Docstrings sangat berguna untuk mendokumentasikan kode
# sehingga mudah dipahami oleh orang lain atau oleh diri
# sendiri di masa depan. Anda dapat menggunakan alat seperti
# help() di Python untuk menampilkan docstrings.
