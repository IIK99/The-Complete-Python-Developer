# Jenis-jenis Error :
# Syntax Errors: Kesalahan dalam penulisan kode yang mencegah program untuk dijalankan.
#     Contoh: print("Hello world
# Exceptions: Kesalahan yang terjadi saat program dijalankan.
#     Contoh: ZeroDivisionError, TypeError, ValueError.

print("\nBlock Try-Except")
try:
    # Code yang mungkin menimbulkan exception
    result = 10 / 0
except ZeroDivisionError:
    # Penanganan untuk ZeroDivisionError
    print("Tidak bisa membagi dengan nol")


print("\nInput age, can't be negative and greater than 5")
while True:
    try:
        age = int(input("\nWhat's your age? "))
        if age < 0:
            raise ValueError("Age can't be negatif")
        elif 0 < age <= 5:
            raise ValueError("Age must be greater than 5 years old")
        result = 10 / age  # Contoh operasi untuk menghindari ZeroDivisionError
    except ValueError as e:
        print(f"Invalid input! {e}")
        continue
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        continue

    print(f"Your age is {age}. Thank you!")

    repeat = input("Would you like to repeat? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Program completed. Thanks You!")
        break
