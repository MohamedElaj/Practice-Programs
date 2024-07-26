import art
import datetime

weekdays = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}


def get_days_in_month(year: int, month: int) -> dict:

    start_date = datetime.date(year, month, 1)

    if month == 12:
        end_date = datetime.date(year + 1, 1, 1)
    else:
        end_date = datetime.date(year, month + 1, 1)

    weekdays_of_month = {}
    current_date = start_date
    while current_date < end_date:
        weekdays_of_month[current_date.day] = weekdays[current_date.isoweekday()]
        current_date += datetime.timedelta(days=1)

    return weekdays_of_month


def main() -> None:
    month = ()

    while True:
        response:str = input("Enter the year of the calender: \n> ")
        if response.isdecimal() and (0 < int(response) <= 9999):
            year = int(response)
            break


    while True:
        response: str = input("Enter the month of the calendar, 1-12: \n> ")
        if response.isdecimal() and (1 <= int(response) <= 12):
            month = int(response)
            # Hier vielleicht durch eine Dictionary, den richtigen Monat rauspicken durch die angegebene Zahl.
            break

    weekdays_of_month = get_days_in_month(year, month)
    print(weekdays_of_month)


main()






