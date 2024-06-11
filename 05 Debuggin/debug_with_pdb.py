import pdb


def divide(a, b):
    pdb.set_trace()  # Memulai sesi debugging
    return a / b


num1 = 10
num2 = 0  # Mengubah nilai untuk menghindari ZeroDivisionError
result = divide(num1, num2)
print(result)

# n (next): Melanjutkan eksekusi ke baris berikutnya.
# c (continue): Melanjutkan eksekusi hingga breakpoint berikutnya.
# p (print): Mencetak nilai variabel. Contoh: p a atau p b.
# q (quit): Keluar dari sesi debugging.
# help
