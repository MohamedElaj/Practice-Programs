import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_three_digits():
    hidden_three_digit = []
    for i in range(3):
        random_number = random.randint(0, 9)
        hidden_three_digit.append(str(random_number))
    return hidden_three_digit


def main():

    # print("""I am thinking of a 3-digit number. Try to guess what it is.
    # Here are some clues:
    # When I say:      That means:
    #  Pico           One digit is correct but in the wrong position.
    #  Fermi          One digit is correct and in the right position.
    #  Bagels         No digit is correct.
    # I have thought up a number.
    # You have 10 guesses to get it.""")

    for i in range(10):
        hidden_three_digits = generate_three_digits()
        i += 1
        guess = input(f"Guess #{i}:\n")
        guess_three_digits = [int(digit) for digit in guess]