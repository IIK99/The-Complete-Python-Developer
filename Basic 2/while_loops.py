# while loop
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("i is no longer less than or equal to 5")

# break, continue and pass
print("\nBreak")
i = 0
while i < 5:
    i += 1
    if i == 3:
        break  # break in 2
    print(i)

print("\nContinue")
for i in range(5):
    if i == 3:
        continue
    print(i)  # continue 3 skipped

print("\nPass")
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)   # Tidak melakukan apa-apa, hanya sebagai placeholder

print('\nAnother example pass and continue')
for i in range(5):
    if i == 2:
        pass  # Placeholder, tidak ada tindakan yang dilakukan
        print("Pass executed")
    elif i == 3:
        continue  # Lewati iterasi ini dan lanjutkan ke iterasi berikutnya
    print(i)

# exercise tree
print("\nExercise tree")
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\nExercise 2 check for duplicate in list")
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
            
print(duplicates)