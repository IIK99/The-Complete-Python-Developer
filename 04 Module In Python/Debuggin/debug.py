# debugging
print("\nPrint statements")
x = 5
y = 10
print(f"x: {x}, y: {y}")
result = x + y
print(f"Result: {result}")

print("\nLogging")
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("\nExample")


def sum_elements(lst):
    total = 0
    for num in lst:
        total += num
        print(f"Added {num}, total now {total}")
    return total


my_list = [1, 2, 3, 4, 5]
print(sum_elements(my_list))


print("\nWith Logging")
import logging

logging.basicConfig(level=logging.DEBUG)


def sum_elements(lst):
    total = 0
    for num in lst:
        total += num
        logging.debug(f"Added {num}, total now {total}")
    return total


my_list = [1, 2, 3, 4, 5]
print(sum_elements(my_list))

print("\nPython debugger (PDB)")
import pdb

pdb.set_trace()

x = 5
y = 10
result = x + y
print(result)

print("\nWith PDB")
import pdb


def sum_elements(lst):
    total = 0
    pdb.set_trace()  # Mulai debugging
    for num in lst:
        total += num
    return total


my_list = [1, 2, 3, 4, 5]
print(sum_elements(my_list))
