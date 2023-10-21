from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()
    next_week_start = today + timedelta(days=(7 - today.weekday()))
    next_week_end = next_week_start + timedelta(days=7)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        birthday_weekday = (today.weekday() + delta_days) % 7
        if next_week_start <= birthday_this_year < next_week_end:
            if birthday_weekday == 5 or birthday_weekday == 6:
                birthday_weekday = 0
            day_of_week = get_day_of_week(birthday_weekday)
            birthday_dict[day_of_week].append(name)

    sorted_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    for day in sorted_days:
        names = birthday_dict[day]
        if names:
            print(f"{day}: {', '.join(names)}")


def get_day_of_week(weekday):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    return days[weekday]


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 18)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Dmitry Lupherov", "birthday": datetime(1980, 10, 23)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 10, 19)},
]


if __name__ == "__main__":
    print("Welcome to the birthdays funtion!")
    get_birthdays_per_week(users)
