import random

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print(f"You got it! The answer was {answer}")
            return True
        else:
            print(f"Sorry, you got it wrong. It was {answer}")
            return False

if __name__ == "__main__":
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue