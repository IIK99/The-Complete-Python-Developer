print("\nContoh Lengkap")

while True:

    class CustomError(Exception):
        pass

    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Pembagi tidak boleh nol")
        return a / b

    try:
        x = int(input("\nMasukkan angka pertama: "))
        y = int(input("Masukkan angka kedua: "))
        result = divide(x, y)
    except ValueError:
        print("Input harus berupa angka")
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Hasil pembagian:", result)
    finally: # selalu dijalankan tidak peduli true/false, dan if, else
        print("Operasi pembagian selesai")
        repeat = input("Would you like to repeat? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Program completed. Thanks You!")
            break
