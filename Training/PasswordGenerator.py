import random
from tkinter import *

Alphabets = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
Digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
SpecSimb = ('!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ",", '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', "]", "_", "{", "}")

# Функция генерации пароля
def GeneratePassword():
    Password = ""
    PasswordSymbols = ()
    PassLength = PasswordLength.get()

    if not PassLength or int(PassLength) < 10:
        PasswordEntry.delete(0, END)
        return PasswordEntry.insert(0, 'Слишком мало символов')


    # Получаем статус кнопок  
    cb1Checked = cb1Var.get()
    cb2Checked = cb2Var.get()
    cb3Checked = cb3Var.get()
    ButtonStatus = [cb1Var.get(), cb2Var.get(), cb3Var.get()]

    # Если статус кнопок True (1), то добавляем наборы символов в кортеж
    # Если ни одна кнопка не выбрана, то добавляем сразу все наборы в кортеж
    if cb1Checked:
        PasswordSymbols = PasswordSymbols + Alphabets
    if cb2Checked:
        PasswordSymbols = PasswordSymbols + Digits
    if cb3Checked:
        PasswordSymbols = PasswordSymbols + SpecSimb
    if PasswordSymbols:
        for i in range(int(PassLength)):
            Password = Password + random.choice(PasswordSymbols)
        PasswordEntry.delete(0, END)
        PasswordEntry.insert(0, Password)
    else:
        for i in range(int(PassLength)):
            Password = Password + random.choice(Alphabets + Digits + SpecSimb)
        PasswordEntry.delete(0, END)
        PasswordEntry.insert(0, Password)
    return

root = Tk()
root.title('Password generator')
root.geometry('305x250')

PasswordLengthLabel = Label(root, text='Enter password length')
PasswordLength = Entry(width=10)

SelectSymbolsLabel = Label(root, text='Select symbols')
cb1Var = IntVar() # Переменная для хранения статуса кнопки, 0 не выбрана, 1 выбрана
cb1 = Checkbutton(text='Alphabets', variable=cb1Var)
cb2Var = IntVar() # Переменная для хранения статуса кнопки, 0 не выбрана, 1 выбрана
cb2 = Checkbutton(text='Digits', variable=cb2Var)
cb3Var = IntVar() # Переменная для хранения статуса кнопки, 0 не выбрана, 1 выбрана
cb3 = Checkbutton(text='Special symbols', variable=cb3Var)
bGen = Button(text='Generate password')
bGen.config(command=GeneratePassword)
PasswordLabel = Label(root, text='Password will be below')
PasswordEntry = Entry(width=50)

PasswordLengthLabel.grid(column=0, row=0, sticky = W)
PasswordLength.grid(column=0, row=1, sticky = W)
SelectSymbolsLabel.grid(column=0, row=2, sticky = W)
cb1.grid(column=0, row=3, sticky = W)
cb2.grid(column=0, row=4, sticky = W)
cb3.grid(column=0, row=5, sticky = W)
bGen.grid(column=0, row=6, sticky = W)
PasswordLabel.grid(column=0, row=7, sticky = W)
PasswordEntry.grid(column=0, row=8, sticky = W)

root.mainloop()