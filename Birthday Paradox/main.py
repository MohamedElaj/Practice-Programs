import random


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

    return ", ".join(birthdays)


def finding_duplicates(geburtstage):
    



number_of_birthdays = input("How many birthdays shall I generate? (Max 100) \n> ")
geburtstage = generieren_geburtstage(int(number_of_birthdays))


print(f"\nHere are {number_of_birthdays} Birthdays:")
print(geburtstage)


#print("In this simulation, multiple people have a birthday on ...")