import random
import time

MONTHS: tuple = ("jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec")


def get_birthdays(number_of_birthdays: int) -> list:
    """Create a certain amount (number_of_birthdays) of random Birthdays."""
    birthdays: list = []

    while number_of_birthdays != 0:
        number_of_birthdays -= 1

        month: str = random.choice(MONTHS)
        if month in {"Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"}:
            day: str = str(random.randint(1, 31))
        elif month == "Feb":
            day: str = str(random.randint(1, 28))
        else:
            day: str = str(random.randint(1, 30))

        birthday: str = day + " " + month
        birthdays.append(birthday)

    return birthdays


def finding_duplicates(birthdays: list) -> list:
    seen: set = set()
    unique_birthdays: list = []
    duplicate_birthdays_set: set = set()

    for birthday in birthdays:
        if birthday not in seen:
            unique_birthdays.append(birthday)
            seen.add(birthday)
        else:
            duplicate_birthdays_set.add(birthday)

    duplicate_birthdays = list(duplicate_birthdays_set)

    return duplicate_birthdays


def get_total_number_of_duplicates(number_of_birthdays: int, total_simulations=100_000) -> int:
    """Determine the total Number of duplicates in 100000 Simulations."""

    number_of_simulation: int = 0
    total_count: int = 0
    milestones = {10_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 80_000, 90_000, 100_000}

    while number_of_simulation < total_simulations:
        number_of_simulation += 1

        birthdays: list = get_birthdays(number_of_birthdays)
        duplicate_birthdays: list = finding_duplicates(birthdays)

        if duplicate_birthdays:
            total_count += 1

        if number_of_simulation in milestones:
            print(f"{number_of_simulation} simulations run")

    return total_count


def main():
    while True:
        response: str = input("How many birthdays shall I generate? (Max 100) \n> ")
        if response.isdecimal() and (0 < int(response) <= 100):
            number_of_birthdays: int = int(response)
            break

    birthdays: list = get_birthdays(number_of_birthdays)
    time.sleep(1)

    print(f"\nHere are {number_of_birthdays} Birthdays:")
    print(", ".join(birthdays))

    duplicate_birthdays: list = finding_duplicates(birthdays)
    if len(duplicate_birthdays) == 0:
        print("In this Simulation no one has the same birthday.")
    else:
        duplicate_birthdays_formated = ", ".join(duplicate_birthdays)
        print(f"In this simulation, multiple people have a birthday on {duplicate_birthdays_formated}.")
    time.sleep(2)

    print(f"\nGenerating {number_of_birthdays} random birthdays 100,000 times ...")

    while True:
        start_process: str = input("Press Enter to begin ...")
        if start_process == "":
            break
        else:
            print("Wrong Key! Please press Enter.")

    matching_birthdays = get_total_number_of_duplicates(number_of_birthdays)
    probability = round(matching_birthdays / 100_000 * 100, 2)

    print(f"""\nOut of 100_000 simulations of {number_of_birthdays} people, there was a matching birthday in that group 
{matching_birthdays} times. This means that {number_of_birthdays} people have a {probability} % chance of
having a matching birthday in their group.
\nThat's probably more than you would think!""")


main()
