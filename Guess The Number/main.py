import random


number = random.randint(1, 100)
print(number)
attempts = 10

print("I am thinking of a number between 1 and 100.")

prozess = True
while prozess:
    guess = ""
    while not (guess.isdecimal() and 1 <= int(guess) <= 100):
        print(f"You have {attempts} guesses left. Take a guess.")
        guess = input("> ")

    
    attempts -= 1
    if int(guess) < number:
        print("Your guess is too low.")
    elif int(guess) > number:
        print("Your guess is too high.")
    else:
        print("Yay! You guessed my number!")


    if attempts == 0:
        print("You lost the Game!!!")
        prozess = False
        # Hier geht nicht richtig aus dem Spiel raus, wenn die Zahl richtig erraten wird.