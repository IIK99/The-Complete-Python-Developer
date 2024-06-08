print("\nMap")
num1 = [1, 2, 3]
num2 = [4, 5, 6]
print("Sum: ", list(map(lambda x, y: x + y, num1, num2)))

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = [1, 1, 1]
print("Sum: ", list(map(lambda x, y, z: x + y - z, num1, num2, num3)))

print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))

print(list(map(lambda i: i.upper(), ["apple", "banana", "mango"])))

print("\nFilter")
print("Even numbers: ", list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5])))

print(
    "Filter ages: ", list(filter(lambda i: i <= 18, [7, 8, 12, 15, 17, 18, 19, 20, 21]))
)

fruits = ["strawberry", "banana", "cherry", "apple", "orange", "mango", "melon"]
fav_fruits = ["banana", "apple", "orange", "mango"]
print("Filter fruits: ", list(filter(lambda i: i in fav_fruits, fruits)))

print("\nReduce")
from functools import reduce

print("Lambda: ", reduce(lambda acc, i: acc + i, [1, 2, 3, 4, 5]))
