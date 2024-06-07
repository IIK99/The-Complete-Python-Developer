# ternary operator
a = 10
b = 20

min = a if a < b else b
print(min)

max = a if a > b else b
print(max)

is_raining = False
weather = "sunny" if is_raining else "cloudy"
print(weather)

# short circuit like math discrete logic
print("\nShort circuit logical")

print("and short circuit logical")
A = False
B = True

# Here, B will not be evaluated because A is False
result = A and B
print(result)  # Output: False

a = True
b = True
result = a and b
print(result)  # Output: True

a = False
b = False
result = a and b
print(result)  # Output: False

print("\nOr short circuit logical")
A = True
B = False

# Here, B will not be evaluated because A is True
result = A or B
print(result)  # Output: True

a = True
b = True
result = a or b
print(result)  # Output: True

a = False
b = False
result = a or b
print(result)  # Output: False

print("\nNot short circuit logical")
a = False
result = not a
print(result)  # Output: True

print("\nLogical operators")
print(2 > 1)  # Output: True
print(5 < 5)  # Output: False
print(5 <= 5)  # Output: True
print(20 >= 10)  # Output: True
print(10 == 8)  # Output: False
print(10 == 10)  # Output: True
print(7 != 7)  # Output: False
print(7 != 3)  # Output: True
print(not (1 == 1))  # Output: False
print(1 == 1 and True)  # Output: True
print(1 > 2 or False)  # Output: False

print("\nSimple mini game")
is_magician = input("You're magician? (Yes or no): ").strip().lower() == "yes"
is_expert = input("Are you an expert? (Yes or no): ").strip().lower() == "yes"

if is_magician and is_expert:
    print("You are a master magician")  # Output: True and True
elif is_magician and not is_expert:
    print("At least you are getting there")  # Output: True and False
elif not is_magician:
    print("You need magic power")  # Output False and False, False and True

# is vs ==

print("\nIs vs ==")
print("\n==")
print(1 == 1)  # Output: True
print(True == 1)  # Output: True
print(True == 2)  # Output: False
print("" == 1)  # Output: False
print("1" == 1)  # Output: False
print([] == [])  # Output: True
print([1, 2] == [])  # Output: False

print("\nIs")
print(1 is 1)  # Output: True
print(1 is not 1)  # Output: False
print(1 == 1.0)  # Output: True
print("1" is 1)  # Output: False
print([] is [])  # Output: False

print('\nComparison')
# Menggunakan ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True (nilai sama)

# Menggunakan is
print(a is b)  # Output: False (objek berbeda di memori)

# Menggunakan is dengan objek yang sama
c = a
print(a is c)  # Output: True (merujuk ke objek yang sama di memori)

