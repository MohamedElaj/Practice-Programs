import art
import datetime


month = ()

while True:
    response:str = input("Enter the year of the calender: \n> ")
    if response.isdecimal() and (0 < int(response) <= 9999):
        year = response
        break


while True:
    response: str = input("Enter the month of the calendar, 1-12: \n> ")
    if response.isdecimal() and (1 <= int(response) <= 12):
        month = int(response)
        # Hier vielleicht durch eine Dictionary, den richtigen Monat rauspicken durch die angegebene Zahl.
        break



