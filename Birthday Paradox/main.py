import random
import time

months = ["jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]


def generieren_geburtstage(number_of_birthdays):
    birthdays = []

    while number_of_birthdays != 0:
        number_of_birthdays -= 1

        month = random.choice(months)
        if month == "jan" or "Mar" or "May" or "Jul" or "Sep" or "Nov":
            day = str(random.randint(1, 31))
        elif month == "Feb":
            day = str(random.randint(1, 28))
        else:
            day = str(random.randint(1, 30))

        birthday = day + " " + month
        birthdays.append(birthday)

    return birthdays
    # ", ".join(birthdays)


def finding_duplicates(birthdays):
    seen = set()
    unique_birthdays = []
    duplicate_birthdays = []

    for birthday in birthdays:
        if birthday not in seen:
            unique_birthdays.append(birthday)
            seen.add(birthday)
        else:
            duplicate_birthdays.append(birthday)

    return duplicate_birthdays


# def count_duplicates(duplicate_birthdays):
#     total_count = 0
#     count = 0
#     for i in duplicate_birthdays:
#         count += 1
#
#     total_count += count


def simulation(number_of_birthdays, total_simulations=10):

    number_of_simulation = 0
    total_count = 0

    while number_of_simulation <= total_simulations:
        number_of_simulation += 1

        geburtstage = generieren_geburtstage(number_of_birthdays)
        duplicate_birthdays = finding_duplicates(geburtstage)

        count = 0
        for i in duplicate_birthdays:
            print(f"Anzahl an Elementen {len(duplicate_birthdays)}")
            count += 1
        total_count += count
        print(total_count)

        if number_of_simulation in (10_000, 20_000, 30_000, 40_000, 50_000, 60_000, 70_000, 80_000, 90_000, 100_000):
            #time.sleep(2)
            print(f"{number_of_simulation} simulations run")

    return total_count


number_of_birthdays = input("How many birthdays shall I generate? (Max 100) \n> ")
birthdays = generieren_geburtstage(int(number_of_birthdays))

print(f"\nHere are {number_of_birthdays} Birthdays:")
print(", ".join(birthdays))

duplicate_birthdays = finding_duplicates(birthdays)
if len(duplicate_birthdays) == 0:
    print("In this Simulation no one has the same birthday.")
else:
    duplicate_birthdays_formated = ", ".join(duplicate_birthdays)
    print(f"In this simulation, multiple people have a birthday on {duplicate_birthdays_formated}.")


print(f"\nGenerating {number_of_birthdays} random birthdays 100,000 times ...")

check = True
while check:
    start_process = input("Press Enter to begin ...")
    if start_process == "":
        check = False
    else:
        print("Wrong Key! Please press Enter.")

matching_birthdays = simulation(int(number_of_birthdays))
print(matching_birthdays)

print(f"""\nOut of 100_000 simulations of {number_of_birthdays} people, there was a matching birthday in that group 
{matching_birthdays} times. This means that {number_of_birthdays} people have a {matching_birthdays:,} % chance of
having a matching birthday in their group.
\nThat's probably more than you would think!""")
