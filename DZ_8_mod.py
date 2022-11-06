from datetime import date


users = [
{"name": "Maryna", "birthday": date(1990,11,12)},
{"name": "Olia", "birthday": date(1999,1,6)},
{"name": "Katya", "birthday": date(2007,11,10)},
{"name": "Tanya", "birthday": date(2000,11,10)},
{"name": "Vanya", "birthday": date(2000,11,5)}
]

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []


def main():
  
    today = date.today()

    for item in users:
      
        b_name = item.get("name")

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

            if b_day.weekday() == 0:
                monday.append(b_name)
            if b_day.weekday() == 1:
                tuesday.append(b_name)
            if b_day.weekday() == 2:
                wednesday.append(b_name)
            if b_day.weekday() == 3:
                thursday.append(b_name)
            if b_day.weekday() == 4:
                friday.append(b_name)
    
    if monday:
        monday_str = ", ".join(monday)
        print(f'Monday: {monday_str}')
    if tuesday:
        tuesday_str = ", ".join(tuesday)
        print(f'Tuesday: {tuesday_str}')
    if wednesday:
        wednesday_str = ", ".join(wednesday)
        print(f'Wednesday: {wednesday_str}')
    if thursday:
        thursday_str = ", ".join(thursday)
        print(f'Thursday: {thursday_str}')
    if friday:
        friday_str = ", ".join(friday)
        print(f'Friday: {friday_str}')
   

if __name__ == "__main__":
    main()


