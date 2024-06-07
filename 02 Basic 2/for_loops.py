# for loops
print("\nFor 1")
for i in range(5):
    print(i)

print("\nFor 2")
for i in range(1, 5):
    print(i)

print("\nFor 3")
for i in "hallo":
    print(i)

print("\nFor 4")
for i in ["Apple", "Banana", "Mango"]:
    print(i)  # still applies to lists[], tuples() and dictionary{}.

print("\nFor 5")
student_scores = {"John": 85, "Jane": 90, "Tom": 78}
for student, score in student_scores.items():
    print(f"{student} scored {score}")

print("\nFor 6")
n = 5  # Jumlah baris yang diinginkan
for i in range(1, n + 1):
    print("*" * i)

n = 5  # Jumlah baris yang diinginkan
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

n = 5  # Jumlah baris yang diinginkan
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
