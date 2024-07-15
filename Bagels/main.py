import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def generate_secret_num():
    secret_num = ""
    """Generate a random three digit number split into one list."""
    for i in range(3):
        random_number = random.randint(0, 9)
        secret_num += str(random_number)
    return secret_num


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


def main():

    print("""I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:      That means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels         No digit is correct.""")

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

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}")

        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing")


<<<<<<< HEAD
main()
=======
main()
>>>>>>> main
