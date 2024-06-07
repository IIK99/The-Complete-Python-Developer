# dictionary
print("\nDictionary")

# Membuat dictionary
fruit_prices = {"apple": 10, "banana": 5, "cherry": 15}

# Mengakses nilai / key
print(fruit_prices["apple"])  # Output: 10

# Menambahkan pasangan kunci-nilai
fruit_prices["orange"] = 8

# Mengubah nilai
fruit_prices["banana"] = 6

# Menghapus pasangan kunci-nilai
del fruit_prices["cherry"]

# Metode dictionary
print(fruit_prices.keys())  # Output: dict_keys(['apple', 'banana', 'orange'])
print(fruit_prices.values())  # Output: dict_values([10, 6, 8])
print(
    fruit_prices.items()
)  # Output: dict_items([('apple', 10), ('banana', 6), ('orange', 8)])
print(fruit_prices.copy())
print(fruit_prices.pop('orange')) # Output: 8 remove orange
print(fruit_prices.popitem()) # Output: remove last item
print(fruit_prices.update({'apple': 15, 'banana': 10}))
print(fruit_prices)


print("\nDictionary")
dictionary = {"a": [1, 2, 3], "b": "hello", "c": True, "d": {"e": 1, "f": 2, "g": 3}}

print(dictionary["a"][1], dictionary["c"], dictionary["d"], dictionary["d"]["g"])
# output dictionary 2 True {'e': 1, 'f': 2, 'g': 3} 3

my_list_dictionary = [
    {
        "a": [1, 2, 3],
        "b": "hello",
        "c": True,
        "d": {"e": 1, "f": 2, "g": 3},
    },
    {
        "h": [
            4,
            5,
            6,
        ],
        "i": "world",
        "j": False,
        "k": {"l": 4, "n": 5, "o": 6},
    },
]

print(
    "\nMy list dictionary",
    my_list_dictionary[0]["a"][1],
    my_list_dictionary[0]["b"],
    my_list_dictionary[0]["d"],
)
print(
    "my list dictionary",
    my_list_dictionary[1]["h"],
    my_list_dictionary[1]["j"],
    my_list_dictionary[1]["k"]["n"],
)
# output my list dictionary 2 hello {'e': 1, 'f': 2, 'g': 3}
# output my list dictionary [4, 5, 6] False 5

print("\nDictionary user")
user = {
    "name": "Coa",
    "name": "Rin",  # reassign user name
    "age": 20,
    "address": "Jakarta",
    "hobby": ["coding", "traveling"],
    "is_married": True,
}
print(
    user["name"], user.get("age", 24), user.get("husband_name", "mal")
)  # age still 20 can't be reassigned and add key-value
print(user)  # output without husband name
print("address" in user, "child" in user)  # output address true, and child is false
print("name" in user.keys())  # output check the key, true have a name
print(24 in user.values())  # output check the value, false the value is 20


user2 = dict(husband_name="Mal")
print(user2)
