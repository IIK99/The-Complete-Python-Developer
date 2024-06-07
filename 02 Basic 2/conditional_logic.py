# yes or no
age = int(input("Input your age: "))
has_license = input("Do you have a license? (yes/no): ").strip().lower() == "yes"

# logic conditional with 'and'
if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You can't drive!")

# Logic conditional with 'or'
print("\n")
weather = input("is the weather good? (yes/no): ").strip().lower() == "yes"
vehicle_in_good_condition = (
    input("is the vehicle in good condition? (yes/no): ").strip().lower() == "yes"
)

if weather or vehicle_in_good_condition:
    print("you can drive!")
else:
    print("You are safe to drive!")


print("\nCara 1")
is_old = int(input("Please input your age: "))

if is_old >= 18:
    print("You are old enough to drive!")
else:
    print("You don't have enough age to drive!")

print("Thank you")

print("\nCara 2")
try:
    is_old = int(input("Please input your age: "))
    if is_old >= 18:
        print("You are old enough to drive!")
    else:
        print("You don't have enough age to drive!")
except ValueError:
    print("Invalid input! Please enter a valid number for your age")

print("Thank you")

print("\nOdd and even number")
number = int(input("Please input a numbers: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

print("\nDays work")
days = input(
    "Enter the day of the week (like: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday): "
).capitalize()

if days == "Monday":
    print("This day is first day to work on the weekday")
elif days == "Friday":
    print("This day is last day to work on the weekday")
elif days == "Saturday" or "Sunday":
    print("This day is weekend")
else:
    print(f"Today is {days}, day to work")

# truthy and falsy
print('\nTruthy and falsy')

if []:
    print("This won't print because an empty list is Falsy.")
else:
    print("This will print because an empty list is Falsy.")

if "hello":
    print("This will print because a non-empty string is Truthy.")

# Truthy has a value
# falsy does not have a value