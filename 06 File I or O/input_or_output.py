# file I/O
import os

print("hai ini lokasi file nya", os.getcwd())
file = open(
    "test.txt",
    encoding="utf-8",  # penyebab err ternyata karena pakai emoticon jadi gak ke baca
    errors="ignore",
)
print(file.readline())  # membaca 1 line
print(file.readlines())  # membaca semua line
file.close()



# 'r': Baca (default).
# 'w': Tulis (mengganti isi file).
# 'a': Tambah (menambahkan ke akhir file).
# 'b': Binary mode (digunakan bersamaan dengan mode lain seperti 'rb' atau 'wb').