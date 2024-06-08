# list, set, and dictionary

print('\nList')
my_list = []
for char in "hello":
    my_list.append(char)

print(my_list)

my_list2 = [char for char in "world"]
print(my_list2)

print(list(["hello", "world"]))
print(list(num for num in reversed(range(0, 11))))
print(list(num * 2 for num in range(0, 11)))
print(list(num * 2 for num in range(0, 11) if num >= 5))

print('\nTuple')
print(tuple(("hello")))

print('\nSet')
my_list = set()
for char in "hello":
    my_list.add(char)

print(my_list)

my_list2 = {char for char in "world"} # random string
print(my_list2)

print(set({"hello", "world"}))
print(set(num for num in range(0, 11)))
print(set(num * 2 for num in range(0, 11)))
print(set(num * 2 for num in range(0, 11) if num >= 5))

print('\nDictionary')
simple_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
print(dict({key:value**2 for key,value in simple_dict.items()}))
print(dict({key:value**2 for key,value in simple_dict.items() if value % 2 != 0}))
print(dict({num:num*2 for num in [4,5,6]}))
