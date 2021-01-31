# Calculador da data de nascimento
# Descrição
# dddddd
# 
#
#   Historico
#   v1.0 - Versão inicial - 20210130
#  
#  (c) 2021 Duarte André




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
    birthday = (input("Enter your birthday in dd/mm format: "))
    birthday_day, birthday_month = birthday.split("/")
    birthday_day = int(birthday_day)
    birthday_month = int(birthday_month)
    if birthday_day>31 or birthday_day<1 or birthday_month>12 or birthday_month<1:
        print("Invalid birthday, try again")  
    else:
        break 
 except ValueError:
     print("Invalid birthday, try again")







if birthday_month<today.month and birthday_day<today.day: 
    print("Hello ", name,"you are ", age, "years old. You were born in ", today.year - age,".")
elif birthday_month == today.month and birthday_day == today.day:
    print("Happy birthday",name, "you are", age, "years old. You were born in", today.year - age,".")
else:
    print ("Hello",name,"you are ", age, "years old. You were born in ", today.year - 1 - age)



