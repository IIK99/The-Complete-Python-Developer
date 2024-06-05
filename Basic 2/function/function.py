# function
def say():
    print("Hello World")


say()

print("\nFunction with parameters and arguments")


def say(name, emoji):  # parameter
    print(f"Hello {name}, {emoji}")


# arguments
say("Andrei", "😊")
say("Rin", "😍")
say("mal", "🤭")

# keyword arguments
say(name="Bibi", emoji="😅")


print("\nFunction 2")


def name(name="Dart Vader", emoji="😡"):
    print(f"Hello {name}, {emoji}")


# arguments
name("Andrei", "😊")
name("Rin", "😍")
name("mal", "🤭")

# keyword arguments
name(name="Bibi", emoji="😅")
name(name="Timmy")
name()