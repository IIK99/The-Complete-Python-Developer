print("\nSet 2")
# Membuat dua set baru
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1, set2)

# Union dari set1 dan set2
set3 = set1.union(set2)
print("Union set1 dan set2:", set3)

# Intersection dari set1 dan set2
set4 = set1.intersection(set2)
print("Intersection set1 dan set2:", set4)

# Difference dari set1 dan set2
set5 = set1.difference(set2)
print("Difference set1 dan set2:", set5)

# Mengecek apakah set1 adalah subset dari set2
is_subset = set1.issubset(set2)
print("Apakah set1 subset dari set2?", is_subset)

# Mengecek apakah set1 adalah superset dari set2
is_superset = set1.issuperset(set2)
print("Apakah set1 superset dari set2?", is_superset)

# Mengecek apakah set1 dan set2 disjoint
is_disjoint = set1.isdisjoint(set2)
print("Apakah set1 dan set2 disjoint?", is_disjoint)

# Menggunakan metode update untuk menambahkan elemen-elemen set2 ke set1
set1.update(set2)
print("Set1 setelah update dengan set2:", set1)