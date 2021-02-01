# Calculador da data de nascimento
# Descrição
# dddddd
# 
#
#   Historico
#   v1.0 - Versão inicial - 20210130
#  
#  (c) 2021 Duarte André


from tkinter import*
import datetime

today = datetime.date.today()

def run():
    name = name_storage.get()
    age = age_storage.get()
    birthday = birthday_storage.get()

    birthday_day, birthday_month = birthday.split("/")
    birthday_day    = int(birthday_day)
    birthday_month  = int(birthday_month)
    age             = int(age)
    if int(birthday_month) < today.month and int(birthday_day) < today.day: 
        result_1 = today.year - age
        sentence="Hello "+ name+"you are "+ str(age)+ "years old. You were born in "+ str(result_1) +"."
    elif birthday_month == today.month and birthday_day == today.day:
        result_2 = today.year - age
        sentence="Happy birthday"+name+ "you are"+ str(age)+ "years old. You were born in"+ str(result_2)+"."
    else: 
        result_3 = today.year - 1 - age
        sentence= "Hello " + name + " you are " + str(age) + " years old. You were born in " + str(result_3)

        sentence_label = Label(text = sentence, fg = "black", bg ="white" )
        sentence_label.pack()
    

    
screen = Tk()
screen.title("Birthday Calculator")
screen.geometry("500x500")

text = Label(text = "Enter your name, then your age, and then your birthday (dd/mm).", fg = "black", bg = "white")
text.pack()

click_when_done = Button(text = "Click when done", fg = "black", bg = "white", command = run)
click_when_done.place(x = 10, y = 20)

name_storage = StringVar()
name = Entry(textvariable = name_storage)
name.pack()
age_storage = StringVar()
age = Entry(textvariable = age_storage)
age.pack()
birthday_storage = StringVar()
birthday = Entry(textvariable = birthday_storage)
birthday.pack()


screen.mainloop()