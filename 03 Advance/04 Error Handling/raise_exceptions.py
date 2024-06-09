print("\nRaise Exceptions")
# Anda bisa secara eksplisit menimbulkan exception dengan menggunakan raise.


def check_value(x):
    if x < 0:
        raise ValueError("Nilai tidak boleh negatif")
    return x


try:
    check_value(-5)
except ValueError as e:
    print(e)
