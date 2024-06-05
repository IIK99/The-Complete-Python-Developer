# return def
def sum(a, b):
    print("hi")
    return a + b


print(sum(10, 5))

print("\nReturn 2")


def sum(a, b):
    return a + b


print(sum(10, sum(10, 5)))

total = sum(10, 5)
print(10 * total)

print("\nReturn 3")


def sum(a, b):
    def another_func(c, d):
        return c + d

    return another_func(a, b)


total = sum(10, 20)
print(total)


def fungsi_utama(x):
    def fungsi_bersarang(y):
        return y * y

    return fungsi_bersarang(x) + 1


hasil = fungsi_utama(5)
print(hasil)  # Output: 26
