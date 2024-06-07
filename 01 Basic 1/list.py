# syntax list
list_contoh = ["hello", 1, 2, 3, True]
print(list_contoh)

# new list range
print(list(range(10)))
print(list(range(5, 10)))

# access data list
print("\nThis is a access data list")
print(list_contoh[0])
print(list_contoh[1])
print(list_contoh[2])
print(list_contoh[3])
print(list_contoh[4])

# negative list syntax
print("\nThis is a negative list")
print(list_contoh[-1])
print(list_contoh[-2])
print(list_contoh[-3])
print(list_contoh[-4])
print(list_contoh[-5])

# range of indexes
print("\nThis is a list range of indexes")
print(list_contoh[1:3])
print(list_contoh[1:])
print(list_contoh[:3])
print(list_contoh[1:4:2])
print(list_contoh[:])
print(list_contoh[-4:-1])
print(list_contoh[-5:2])
print(list_contoh[0:-2])

# change data
print("\nchange data of a list")
list_contoh[0] = "hi"
list_contoh[-1] = False
print(list_contoh)

# add data
print("\nadd data of a list")
list_contoh.append("python")
list_contoh.insert(1, "mari belajar python")
print(list_contoh)

# delete data
print("\ndelete data of a list")
del list_contoh[0]
list_contoh.remove("mari belajar python")
list_contoh.pop()  # remove last element
# list_contoh.clear() # delete all elements
print(list_contoh)

# loop trough a list
print("\nloop through a list")
new_list_data_items = ["hello", 1, 2, 3, True]
for i in new_list_data_items:
    print(i)

# check if list contains
print("\ncheck if list contains")
new_data_list = ["hello", False]
if "hello" in new_data_list:
    print("hello is in list")
else:
    print("hello is not in list")

# length of list
print("\nlength of list")
length_list = [1, 2, 3, "mari belajar python", True]
print(len(length_list))

# copy list
print("\ncopy list")
list_copy = ["kita", "akan", "mencoba", "copy", "list", "ini"]
print(list_copy)

new_list = list_copy
new_list[1] = "test"

new_list1 = list_copy.copy()
new_list1[2] = "baru"

print(new_list)
print(new_list1)

# concat list
print("\nconcat list")
list_concat = ["sekarang", "kita", "akan", "menggabungkan", "suatu", "list"]
print(list_concat)

list1 = [1, 2, 3]
added_list = [True]

gabungkan_list = list1 + list_concat
print(gabungkan_list)

gabungkan_list.extend(added_list)  # extend adalah gabungkan list dari paling belakang
print(gabungkan_list)

# find index
print("\nfind index")
emot = "hallo "
new_name_list = emot.join(
    [" chika ", " adam ", " fajar ", " ibu rina ", " bapak ikmal "]
)
print(new_name_list)
name_list = ["chika", "adam", "fajar", "ibu rina", "bapak ikmal"]
findIndex = name_list.index("ibu rina")
print(findIndex)
print("ibu rina" in name_list)  # true
print("rin" in name_list)  # false


# findIndex1 = nameList.index('nisa')
# print(findIndex1) # error tidak menemukan yang namanya nisa

# sort list / masih menggunakan nameList
print("sort list")
name_list.sort()  # menyesuaikan dengan abjad ascending
print(name_list)
name_list.reverse()  # kebalikannya descending
print(name_list)

# 2d list
print("\n2d list")
list_two_dimension = [
    ["laptop", "mobile", "pc"],
    ["bersepeda", "jalan", "makan"],
    ["sepatu", "jaket", "kaca mata"],
]

print(list_two_dimension)
print(list_two_dimension[2])
print(list_two_dimension[2][0])

# list unpacking

print("\nlist unpacking")
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(d)
