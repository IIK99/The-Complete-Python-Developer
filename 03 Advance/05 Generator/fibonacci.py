# A simple generator for Fibonacci Numbers
def fib(limit):

    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("\nAnother Fibonacci")


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()

for _ in range(10):
    print(next(fib_gen))


# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)

print("\n")
import random


def lottery():
    # memunculkan iterasi sebanyak 6 dengan range random 1-40
    for i in range(6):
        yield random.randint(1, 40)
    # menambahkan item ke tujuh dengan range random 1-15
    yield random.randint(1, 15)


for random_number in lottery():
    print("Nomor yang akan keluar adalah ... %d!" % (random_number))
