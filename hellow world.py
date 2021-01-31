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
age = int(input("Enter your age: "))
birthday_day = int(input("Enter your birthday day: "))
birthday_month = int(input("Enter your birthday month (ex: 12 = december): "))


if birthday_month<today.month and birthday_day<today.day: 
    print("Hello ", name,"you are ", age, "years old. You were born in ", today.year - age,".")
elif birthday_month == today.month and birthday_day == today.day:
    print("Hello ", name, "you are ", age, "years old, and I want to wish you a Happy Birthday. You were born in ", today.year - age,".")
else:
    print ("Hello ", name,"you are ", age, "years old. You were born in ", today.year - 1 - age)

