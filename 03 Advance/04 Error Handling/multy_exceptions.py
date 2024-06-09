while True:
    print("\nMultiple Exceptions")
    try:
        value = int(input("Masukkan angka: "))
        result = 10 / value
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        result = None  # optional
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol. Silakan coba lagi.")
        result = None  # optional

    if result is not None:
        print(f"Hasil pembagian adalah {result}")
        repeat = input("Would you like to repeat? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Program completed. Thanks You!")
            break
