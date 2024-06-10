# module
import os

# Bersihkan terminal
os.system("cls" if os.name == "nt" else "clear")

# Kode lainnya
print(__name__)
print("Terminal sudah dibersihkan.")


def greet(name):
    return f"Hello, {name}!"


HEIGHT = 168
weight = 53
skin = "white"
hair = "black"

if __name__ == "__main__":
    print("File module_in_python.py dijalankan langsung")
else:
    print("File module_in_python.py diimpor sebagai module")
    
# Dengan begitu, if __name__ == "__main__":
# memungkinkan kode tertentu dijalankan hanya ketika file itu
# dijalankan secara langsung, bukan saat diimpor sebagai modul.
