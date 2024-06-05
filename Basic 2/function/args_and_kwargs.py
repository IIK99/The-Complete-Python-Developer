# *args dan **kwargs digunakan dalam fungsi Python untuk menangani
# sejumlah argumen yang tidak ditentukan jumlahnya. Mereka membuat
# fungsi lebih fleksibel dengan memungkinkan menerima berbagai jumlah argumen.

# *args digunakan untuk mengirim sejumlah argumen non-keyword variabel
# ke dalam sebuah fungsi. Argumen ini diubah menjadi tuple dalam fungsi.

print("\n*Args")


def tambah_semua(*args):
    """
    Menambahkan semua argumen yang diberikan.

    Parameters:
    *args (int, float): Angka-angka yang akan dijumlahkan.

    Returns:
    int, float: Hasil penjumlahan dari semua angka yang diberikan.
    """
    return sum(args)


print(tambah_semua(1, 2, 3, 4))  # Output: 10
print(tambah_semua(5, 10))  # Output: 15

# **kwargs digunakan untuk mengirim sejumlah argumen keyword
# variabel ke dalam sebuah fungsi. Argumen ini diubah menjadi
# dictionary dalam fungsi.

print("\n**Kwargs")


def cetak_info(**kwargs):
    """
    Mencetak informasi yang diberikan sebagai keyword arguments.

    Parameters:
    **kwargs (dict): Informasi yang akan dicetak dalam bentuk key-value pairs.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


cetak_info(nama="John", umur=25, kota="New York")
# Output:
# nama: John
# umur: 25
# kota: New York

# Menggabungkan *args dan **kwargs
# Anda juga bisa menggunakan *args dan **kwargs
# dalam fungsi yang sama untuk menangani argumen posisi dan keyword variabel.

print("\nGabungan *Args dan **kwargs")


def contoh_gabung(*args, **kwargs):
    """
    Mencetak argumen posisi dan keyword yang diberikan.

    Parameters:
    *args (tuple): Argumen posisi.
    **kwargs (dict): Argumen keyword.
    """
    print("Args:", args)
    print("Kwargs:", kwargs)


contoh_gabung(1, 2, 3, nama="Alice", umur=30)
# Output:
# Args: (1, 2, 3)
# Kwargs: {'nama': 'Alice', 'umur': 30}

print("\nCoba *Args")


def super_func(*args):
    print(*args)
    print(args)  # without * is tuple type ()
    return sum(args)


print(super_func(1, 2, 3, 4, 5))

print("\nGabungan *Args dan **Kwargs")


def super_functions(*args, **kwargs):
    print(*args)
    print(args)  # without * is tuple type ()
    print(*kwargs)
    print(kwargs)  # without * is dict type {}
    total = 0
    for i in kwargs.values():
        total += i
    return sum(args) + total


print(super_functions(1, 2, 3, 4, 5, num1=5, num2=10))

print(help(tambah_semua))
print(help(cetak_info))
print(help(contoh_gabung))
