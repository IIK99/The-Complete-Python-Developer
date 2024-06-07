print("\n")
first_name = "Hello"
last_name = 'ik "how are you?"'
words = '\nI\'m "fine", what about you?'
print(first_name, last_name, words)

name = input("What's your name? ")
print(
    """
      WOW
      0 0
      ---
      HELLO
      """
    + name
)

# \n = new line
# \t = tab
# f = f-string which much be followed by {}

print("\nRectangle area")
width = float(input("Please input a width: "))
height = float(input("Please input a height: "))
area = f"\nThe area of the rectangle is {width * height} square meters."
print(area)

# [start:end:stepover]
apple = "I have a apple"
print(apple[0], apple[8:14])
print(apple[0:14:3])

print("\nHidden password")
name = input("Enter username: ")
password = input("Enter password: ")
password_length = len(password)
hidden_password = "*" * password_length
print(f"{name} your password {hidden_password}, is {password_length} letters long")
