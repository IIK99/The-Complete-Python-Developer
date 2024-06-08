# performance decorator.
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} seconds")
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000):
        i * 5


long_time()

print("\n")
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    "name": "Rin",
    "valid": True,  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    # code here
    def wrapper(*args, **kwargs):
        if args[0]["valid"]:
            return fn(*args, **kwargs)
        else:
            return print("invalid user")

    return wrapper


@authenticated
def message_friends(user):
    print("message has been sent")


message_friends(user1)
