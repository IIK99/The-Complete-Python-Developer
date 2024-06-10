# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


print("\n")
# A Python program to demonstrate use of
# generator object with next()


# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
    yield 4


# x is a generator object
x = simpleGeneratorFun()

# Iterating over the generator object using next

# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print("\nYield from")


def generator_1():
    yield from range(3)
    yield from [3, 4, 5]


for value in generator_1():
    print(value)


print("\nGenerator Function")
def generator_function(num):
    for i in range(num):
        yield i*2
        
# for value in generator_function(5):
#     print(value) # uncomment for see the results, and comment g = generator_function
    
g = generator_function(10)
next(g)
next(g)
print(next(g))