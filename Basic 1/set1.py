# Set adalah tipe data yang tidak terurut dan bersifat mutable,
# artinya elemen dalam set bisa diubah (ditambah atau dihapus). Set tidak mengizinkan elemen duplikat.

# Membuat set
fruit_set = {"apple", "banana", "cherry"}

# Menambahkan elemen ke set
fruit_set.add("orange")
print(fruit_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# Menghapus elemen dari set
fruit_set.remove("banana")
print(fruit_set)  # Output: {'apple', 'cherry', 'orange'}

# Menggunakan metode discard untuk menghapus elemen tanpa menyebabkan error jika elemen tidak ada
fruit_set.discard("banana")

# Menggabungkan dua set
another_set = {"mango", "grape"}
combined_set = fruit_set.union(another_set)
print(combined_set)  # Output: {'apple', 'cherry', 'orange', 'mango', 'grape'}

# Operasi irisan
common_set = fruit_set.intersection(another_set)
print(common_set)  # Output: set() (karena tidak ada elemen yang sama)

# Operasi selisih
difference_set = fruit_set.difference(another_set)
print(difference_set)  # Output: {'apple', 'cherry', 'orange'}

# Memeriksa elemen dalam set
print("apple" in fruit_set)  # Output: True
print("banana" in fruit_set)  # Output: False

print("\n")
my_list = [1, 2, 3, 4, 5]
print(set(my_list))  # Output: changed to set

my_set = {1, 2, 3, 4, 5}
print(list(my_set))  # Output: changed to list
new_set = my_set.copy()
my_set.clear()
print(new_set)  # Output: copied {1, 2, 3, 4, 5}
print(my_set)  # Output: set()

print("\nNew set1")
# Membuat set awal
my_set = {1, 2, 3}
print(my_set) 

# Menambahkan elemen ke set
my_set.add(4)
print("Set setelah add(4):", my_set)

# Menghapus elemen dari set dengan remove()
my_set.remove(3)
print("Set setelah remove(3):", my_set)

# Menghapus elemen dari set dengan discard()
my_set.discard(5)  # Tidak ada elemen 5, jadi tidak ada perubahan
print("Set setelah discard(5):", my_set)

# Menghapus dan mengembalikan elemen acak dari set
element = my_set.pop()
print("Elemen yang dihapus dengan pop():", element)
print("Set setelah pop():", my_set)

# Menghapus semua elemen dari set
my_set.clear()
print("Set setelah clear():", my_set)
