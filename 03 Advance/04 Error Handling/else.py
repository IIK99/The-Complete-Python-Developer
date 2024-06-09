while True:
    print("\nElse")
    try:
        num_1 = int(input('Masukan angka pertama untuk di bagi: '))
        num_2 = int(input('Masukan angka kedua untuk di bagi: '))
        result = num_1 / num_2
    except ZeroDivisionError:
        print("Tidak bisa membagi dengan nol")
    else:
        print("Pembagian berhasil, hasilnya adalah", result)

        print(result)
        repeat = input("Would you like to repeat? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Program completed. Thanks You!")
            break