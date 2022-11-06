from datetime import date


users = [
    {"name": "Maryna", "birthday": date(1990,11,12)},
    {"name": "Olia", "birthday": date(1999,1,6)},
    {"name": "Katya", "birthday": date(2007,11,10)},
    {"name": "Tanya", "birthday": date(2000,11,10)},
    {"name": "Vanya", "birthday": date(2000,11,5)}
    ]

users_list = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
    }


def main():
  
    today = date.today()

    for item in users:
      
        b_day = item.get("birthday")
        b_day = b_day.replace(year=today.year)

        #Користувачів, у яких день народження був на вихідних, потрібно привітати у понеділок:
        if b_day.weekday() == 5:
            b_day = b_day.replace(day=b_day.day+2)
        if b_day.weekday() == 6:
            b_day = b_day.replace(day=b_day.day+1)

        if b_day < today:
            b_day = b_day.replace(year=today.year + 1)

        time_to_birthday = abs(b_day - today)

        if time_to_birthday.days < 8:
            b_day_weekday = b_day.strftime("%A")
            users_list.get(b_day_weekday).append(item.get("name"))

    print_users_list(users_list)


def print_users_list(users_list: dict):
    
    for key, value in users_list.items():
        if value:
            print(f"{key}: {', '.join(value)}")
   

if __name__ == "__main__":
    main()


