print("\n")
# Decorators adalah fungsi yang memodifikasi atau meningkatkan fungsi atau metode lainnya.
# Mereka sering digunakan untuk menambahkan fungsionalitas seperti logging, akses kontrol,
# pengukuran waktu eksekusi, dan lainnya tanpa mengubah kode asli dari fungsi yang dihiasi.


def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dipanggil")
        func()
        print("Setelah fungsi dipanggil")

    return wrapper


@my_decorator  # decorator selalu di ikuti dengan @... sesuai dengan def yang di atas
def say_hello():
    print("Hello!")


say_hello()

print("\n")


# Higher-Order Functions (HOC) adalah fungsi yang menerima fungsi lain sebagai
# argumen atau mengembalikan fungsi sebagai hasilnya. HOC sering digunakan
# untuk membangun abstraksi dan komposisi fungsi.
def greet(func):
    def wrapper(name):
        return func(name)

    return wrapper


@greet  # sesuai sama def yang di atas
def hello(name):
    return f"Hello, {name}!"


print(hello("Alice"))
