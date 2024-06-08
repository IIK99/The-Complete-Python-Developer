def multiply_by2(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


print(multiply_by2([1, 2, 3, 4, 5]))


print("\nMap")


def multiply_map(i):
    return i * 2


print(list(map(multiply_map, [1, 2, 3, 4, 5])))


fruits = ["apple", "banana", "mango"]


def map_fruits(i):
    return i.upper()


print(list(map(map_fruits, fruits)))


print("\nFilter")


def only_odd(i):
    return i % 2 != 0


print(list(filter(only_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


ages = [7, 8, 12, 15, 17, 18, 19, 20, 21]


def filter_ages(i):
    if i <= 18:
        return False
    else:
        return True


adults = filter(filter_ages, ages)
for x in adults:
    print(x)
print("One line", list(filter(filter_ages, [7, 8, 12, 15, 17, 18, 19, 20, 21])))


def filter_fruits(i):
    fav_fruits = ["banana", "apple", "orange", "mango"]
    if i in fav_fruits:
        return True
    else:
        return False


fruits = ["strawberry", "banana", "cherry", "apple", "orange", "mango", "melon"]
filtered_fruits = filter(filter_fruits, fruits)

print(
    "The filtered list of fruit names: ",
    list(
        filter(
            filter_fruits,
            ["strawberry", "banana", "cherry", "apple", "orange", "mango", "melon"],
        )
    ),
)
print("The filtered list of fruit names: ")
for fruit in filtered_fruits:
    print(fruit)

print("\nZip")
# use 2 lists or more lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
print(list(zip(list_1, list_2, list_3)))
print(
    list(zip(["aku", "saling", "selama"], ["kamu", "mencintai", "lamanya"]))
)  # cringe T_T

print("\nReduce")
from functools import reduce

list = [1, 2, 3, 4, 5]


def accumulator(acc, i):
    print(acc, i)
    return acc + i


print(list)
print(reduce(accumulator, list, 0))
print('_'*10)
print(reduce(accumulator, list, 10))

