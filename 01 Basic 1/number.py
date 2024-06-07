# Fundamental data types
# int and float
print("Data types")
print(type(5))
print(type(5.0))
print(type(5 + 0))
print(type(5 + 0j))
print(type(5 / 2))
print(type(5 // 2))
print(type(5 % 2))
print(type(5**2))
print(type(-5))
print(type(5.0 + 0j))
print(type(5.0 / 2))
print(type(5.0 // 2))
print(type(5.0 % 2))
print(type(5.0**2))
print(type(-5.0))

# Integer
x = 5
y = 2

# Operasi aritmatika
sum_result = x + y  # Penjumlahan
diff_result = x - y  # Pengurangan
prod_result = x * y  # Perkalian
int_div_result = x // y  # Pembagian bulat
mod_result = x % y  # Modulo
exp_result = x**y  # Eksponensial

print("Integer Operations:")
print("Sum:", sum_result)  # Output: 7
print("Difference:", diff_result)  # Output: 3
print("Product:", prod_result)  # Output: 10
print("Integer Division:", int_div_result)  # Output: 2
print("Modulo:", mod_result)  # Output: 1
print("Exponent:", exp_result)  # Output: 25

# Float
a = 5.0
b = 2.0

# Operasi aritmatika
float_div_result = a / b  # Pembagian float

print("\nFloat Operations:")
print("Float Division:", float_div_result)  # Output: 2.5

# math functions
print("\nMath Functions:")
print(round(3.2))  # Output: 3
print(round(3.6))  # Output: 4
print(abs(-20))  # Output: 20

# Operator precedence
print("\nOperator precedence:")
print(20 - 3 * 4)  # Output: 8
print((20 - 3) + 2**2)  # Output: 21
print((5 + 4) * 10 / 2)  # Output: 45.0
print(((5 + 4) * 10) / 2)  # Output: 45.0
print((5 + 4) * (10 / 2))  # Output: 45.0
print(5 + (4 * 10) / 2)  # Output: 25.0
print(5 + 4 * 10 // 2)  # Output: 25

# ()
# **
# * /
# + -

# binary
print("\nBinary:")
print(0b1)  # Output: 1
print(0b10)  # Output: 2
print(0b11)  # Output: 3
print(0b100)  # Output: 4
print(0b101)  # Output: 5
print(int("0b1", 2))  # Output: 1
print(int("0b11", 2))  # Output: 3
