import datetime



today = datetime.date.today()
name = input("Enter your name: ")
while True:
 try:
    age = int(input("Enter your age: "))
    break
 except ValueError:
    print("Invalid age, try again")
while True:
 try:
    birthday_day = str(input("Enter your birthday(dd/mm): "))
    break
 except ValueError:
     print("Invalid birthday, try again")

birthday_day_datetime = datetime.datetime.strptime(birthday_day, "%d/%m")

birth_day = (birthday_day_datetime.index("%d", 42))

if birth_month<today.month and birth_day<today.day: 
    print("Hello ", name,"you are ", age, "years old. You were born in ", today.year - age,".")
elif birth_month == today.month and birth_day == today.day:
    print("Happy birthday",name, "you are", age, "years old. You were born in", today.year - age,".")
else:
    print ("Hello",name,"you are ", age, "years old. You were born in ", today.year - 1 - age)



