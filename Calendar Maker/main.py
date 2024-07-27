import art
import datetime


def get_calendar_for_month(year: int, month: int) -> list:

    first_day_of_month = datetime.date(year, month, 1)

    if month == 12:
        first_day_of_next_month = datetime.date(year + 1, 1, 1)
    else:
        first_day_of_next_month = datetime.date(year, month + 1, 1)
    last_day_of_month = first_day_of_next_month - datetime.timedelta(days=1)

    # Specify the first and last Day in which we have to fill the calendar.
    start_date = first_day_of_month - datetime.timedelta(days=first_day_of_month.weekday() + 1)
    end_date = last_day_of_month + datetime.timedelta(days=(5 - last_day_of_month.weekday()))


    current_date = start_date
    monthly_calendar = []
    while current_date <= end_date:
        week = []
        for i in range(7):
            week.append(current_date.day)
            current_date += datetime.timedelta(days=1)
        monthly_calendar.append(week)

    print(monthly_calendar)
    return monthly_calendar


def main() -> None:

    while True:
        response: str = input("Enter the year of the calender: \n> ")
        if response.isdecimal() and (0 < int(response) <= 9999):
            year = int(response)
            break


    while True:
        response: str = input("Enter the month of the calendar, 1-12: \n> ")
        if response.isdecimal() and (1 <= int(response) <= 12):
            month = int(response)
            break

    get_calendar_for_month(year, month)


main()