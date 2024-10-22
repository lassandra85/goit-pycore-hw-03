from datetime import datetime, timedelta

users = [
     {"name": "Іван", "birthday": "1985.10.27"},
    {"name": "Оксана", "birthday": "1990.10.12"},
    {"name": "Петро", "birthday": "1988.10.08"},
    {"name": "Анна", "birthday": "1995.10.11"},
    {"name": "Марія", "birthday": "1987.10.09"}
]



def get_upcoming_birthdays(users):

    today = datetime.now().date()
    
    congratulation  = []

    for user in users:
         
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < today:

            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        

        if 0 <= (birthday_this_year - today).days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  
                congratulation_date += timedelta(days=1)

            congratulation.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return congratulation

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)