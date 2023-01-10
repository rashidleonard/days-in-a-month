print("Days In A Month")

year = int(input("Enter the year: \n"))
month = int(input("Enter the month: \n"))
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]


def is_leap(year):
    # year = int(input("Enter the year "))

    if year % 4 == 0:
        if year % 100 == 0:
            return False
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


days = days_in_month(year, month)
s_month = months[month - 1]  # specific month
print(f"The number of days in {s_month} of the year {year} is: {days}")

# testing
