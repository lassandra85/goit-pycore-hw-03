from datetime import datetime

def get_days_from_today(date: str) -> int:

    date_format = datetime.strptime(date, '%Y-%m-%d')
    dayToday = datetime.today()
    days_from_today = dayToday - date_format
    print(days_from_today)

get_days_from_today('2024-12-14')

