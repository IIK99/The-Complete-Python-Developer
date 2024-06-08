# MRO (Method Resolution Order)

# MRO menentukan urutan di mana metode dicari dalam kasus pewarisan ganda.
# Python menggunakan algoritma C3 linearization untuk menentukan MRO.
# Anda dapat melihat MRO dari kelas dengan menggunakan atribut __mro__ atau fungsi mro().


class A:
    num = 0


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print("\n")
print(D.num)  # Output: 1 (because class C have num)
print("\n")
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

print("\n")


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.__mro__)
