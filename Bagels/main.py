import random

print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:      That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")


def generate_three_digits():
    three_digit_number = []
    for i in range(3):
        random_number = random.randint(0, 9)
        three_digit_number.append(random_number)
    print(three_digit_number)


def get_clues(guess, secret_num):
    """Returns a string. On every guess we add a clue."""
    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi")
        elif guess[i] in secret_num:
            clues.append("Pico")

    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)