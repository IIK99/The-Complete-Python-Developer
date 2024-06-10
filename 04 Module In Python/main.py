# this is the main file/center
# import module
from datetime import datetime

import module_in_python

now = datetime.now()
print(now)

print(module_in_python.greet("Rin"))
print(module_in_python.HEIGHT)

from module_in_python import greet, hair  # impor hanya bagian tertentu dari module

print(greet("Mal"))
print(hair)

from my_package import module_1, module_2

print(module_1.func1())
print(module_2.func2())

from my_package.deep_package import deep_func

print(deep_func.deep_func())
