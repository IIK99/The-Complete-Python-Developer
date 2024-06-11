# file I/O
import os

print("hai ini lokasi file nya", os.getcwd())
file = open("test.txt")
print(file.readline())  # membaca 1 line
print(file.readlines())  # membaca semua line
file.close()

# buka dengan cmd biasa jika error dengan, buka file location lalu ketik python nama_file.py
# 'r': Baca (default).
# 'w': Tulis (mengganti isi file).
# 'a': Tambah (menambahkan ke akhir file).
# 'b': Binary mode (digunakan bersamaan dengan mode lain seperti 'rb' atau 'wb').
