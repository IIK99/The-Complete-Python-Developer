# walrus :=
# Menghitung dan mengeluarkan elemen dari list sampai kosong
data = [1, 2, 3, 4, 5]
while (n := len(data)) > 0:
    print(f"Masih ada {n} elemen yang tersisa.")
    data.pop()

# Memproses dan memfilter data
print("\nList Comprehension")
data = [1, 2, None, 4, None, 5]
processed_data = [y for x in data if (y := x) is not None]
print(processed_data)  # Output: [1, 2, 4, 5]

# if
# Mengecek panjang list dan mencetak jika lebih dari 10
print("\nIf")
items = range(15)
if (count := len(items)) > 10:
    print(f"Terlalu banyak item: {count}")
