# nested loops
# perkalian 1 - 100
for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

print("\nNested loops 2")
for i in [1, 2, 3]:
    for j in ("a", "b", "c"):
        print(i, j)

# Membuat piramida angka kiri
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Membuat piramida angka di kanan
rows = 5

for i in range(1, rows + 1):
    # Menambahkan spasi di sebelah kiri
    for j in range(rows - i):
        print(" ", end=" ")

    # Mencetak angka
    for k in range(1, i + 1):
        print(k, end=" ")

    print()

# Membuat piramida angka kerucut di tengah
rows = 5

for i in range(1, rows + 1):
    # Menambahkan spasi di sebelah kiri
    for j in range(rows - i):
        print(" ", end=" ")

    # Mencetak angka
    for k in range(1, i + 1):
        print(k, end=" ")

    # Mencetak angka menurun
    for m in range(i - 1, 0, -1):
        print(m, end=" ")

    print()
