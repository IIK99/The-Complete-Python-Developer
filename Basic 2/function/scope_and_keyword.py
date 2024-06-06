x = 5  # variabel global


def outer():
    x = 10  # variabel di enclosing scope

    def inner():
        nonlocal x  # mengakses variabel di enclosing scope, jika di komen outer tetap 10
        x = 20
        print(f"inner: {x}")  # output: 20 mengubah variabel di enclosing scope

    inner()
    print(f"outer: {x}")  # output: 20


outer()
print(f"global: {x}")  # output: 5


def global_test():
    global x
    x = 30
    print(f"global_test: {x}")  # output: 30 mengubah variabel global x = 5


global_test()
print(f"global after global_test: {x}")  # output: 30

