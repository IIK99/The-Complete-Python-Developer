# iterable - list, dictionary, tuple, set, string
# iterable => one by one check each item in the collection

user = {
    "name": "David",
    "age": 24,
    "hobby": ["coding", "traveling"],
    "is_married": True,
    "address": {
        "city": "Jakarta",
    },
}

print("\nItems")
for item in user.items():
    print(item)

print("\nKeys")
for item in user.keys():
    print(item)

print("\nValues")
for item in user.values():
    print(item)

print("\nCombine")
for key, value in user.items():
    print(key, value)

print("\nReverse loops")
for i in range(5, 0, -1):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(2):
    print(list(range(10)))
    print(list(range(1, 5)))

# enumerate
print("\nEnumerate")
for index, item in enumerate(user.items()):
    print(index, item)

for index, item in enumerate(user.keys()):
    print(index, item)

for index, char in enumerate(list(range(100))):
    # print(index, char) # Output : 0-99
    if char == 50:
        print(f"Index of 50 is: {index}")
