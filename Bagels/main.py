import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_num():
    hidden_three_digit = []
    for i in range(3):
        random_number = random.randint(0, 9)
<<<<<<< HEAD
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
=======
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

    while True:
        secret_num = generate_secret_num()
        print("I have thought up a Number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            #Checking the Input, before saving it.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess {num_guesses}")
                guess = input("> ")


if __name__ == '__main__':
    main()
>>>>>>> feature1
