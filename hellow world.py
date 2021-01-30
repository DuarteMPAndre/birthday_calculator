# Calculador da data de nascimento
# Descrição
# dddddd
# 
#
#   Historico
#   v1.0 - Versão inicial - 20210130
#  
#  (c) 2021 Duarte André



name = input("Enter your name: ")
age = int(input("Enter your age: "))
birthday_day = int(input("Enter your birthday day: "))
birthday_month = int(input("Enter your birthday month (ex: 12 = december): "))
current_day = int(input("Enter the current day: "))
current_month = int(input("Enter the current month: "))
current_year = int(input("Enter the current year: "))

if birthday_month<current_month and birthday_day<current_day: 
    print("Hello ", name,"you are ", age, "years old. You were born in ", current_year - age,".")
elif birthday_month == current_month and birthday_day == current_day:
    print("Hello ", name, "you are ", age, "years old, and I want to wish you a Happy Birthday. You were born in ", current_year - age,".")
else:
    print ("Hello ", name,"you are ", age, "years old. You were born in ", current_year - 1 - age)

