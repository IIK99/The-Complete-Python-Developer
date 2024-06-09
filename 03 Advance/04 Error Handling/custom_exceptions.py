print("\nCustom Exceptions")
# Anda bisa membuat exception sendiri dengan mendefinisikan class yang mewarisi dari Exception.


class CustomError(Exception):
    pass


try:
    raise CustomError("Ini adalah error custom")
except CustomError as e:
    print(e)
