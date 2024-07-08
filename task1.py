from datetime import datetime

def get_days_from_today(date):
    try:
        difference = datetime.now().date() - datetime.strptime(date, "%Y-%m-%d").date()

        return (f"There are {difference.days} between current and set time")
    except ValueError:
        return "Date format is invalid. Please validate input"


print(get_days_from_today("2024-05-25"))
