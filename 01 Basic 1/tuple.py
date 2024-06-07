# tuple like list but unlike list, because tuple can't be the changed immutable
my_tuple = (1,2,3,4,5,5)
# my_tuple[1] = 'z' got error cannot reassign tuple
print(my_tuple[3], 1 in my_tuple) # output 4, true
print(my_tuple.count(5)) # output 2, because 5 have 2
print(len(my_tuple)) # output 6

x,y,z, *other = (1,2,3,4,5)
print(y, other)

print('\n')
# Membuat tuple
fruit_tuple = ("apple", "banana", "cherry")

# Mengakses elemen tuple
print(fruit_tuple[0])  # Output: apple
print(fruit_tuple[1])  # Output: banana

# Menambahkan tuple (menghasilkan tuple baru)
new_tuple = fruit_tuple + ("orange",)
print(new_tuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Menggunakan slicing pada tuple
print(fruit_tuple[0:2])  # Output: ('apple', 'banana')

# Tuple bisa berisi berbagai tipe data
mixed_tuple = (1, "hello", 3.14)

# Tuple bersarang
nested_tuple = (fruit_tuple, mixed_tuple)
print(nested_tuple)  # Output: (('apple', 'banana', 'cherry'), (1, 'hello', 3.14))
