my_list = [1, "hello", 3.14]
print(my_list, "Can store elements of different types (integers, strings, etc.)")


import array

my_array = array.array("i", [1, 2, 3, 4])
# print(my_array, "Store elements of the same type")
print(my_array)


import numpy as np

# pip install numpy
my_array = np.array([1, 2, 3, 4])
print(my_array, "Array with numpy")
