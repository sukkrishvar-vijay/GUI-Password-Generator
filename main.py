from tkinter import *
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

window = Tk()

window.title('Password Generator')
window.config(padx=20,pady=20)

def password():
    nr_letters= int(l_input.get())
    nr_symbols = int(s_input.get())
    nr_numbers = int(n_input.get())
    password_list = []
    
    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))
    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)
    
    random.shuffle(password_list)
    passwd = ""
    for char in password_list:
        passwd += char
    
    ps_label.insert(0,passwd)

def save():
    pyperclip.copy(ps_label.get())

l_label=Label(text='Letters')
l_label.grid(column=0,row=0)

l_input=Entry(width=15)
l_input.grid(column=1,row=0)
l_input.focus()

n_label=Label(text='Numbers')
n_label.grid(column=0,row=1)

n_input=Entry(width=15)
n_input.grid(column=1,row=1)

s_label=Label(text='Symbols')
s_label.grid(column=0,row=2)

s_input=Entry(width=15)
s_input.grid(column=1,row=2)

p_label=Label(text='Password')
p_label.grid(column=0,row=3)

ps_label=Entry(width=15)
ps_label.grid(column=1,row=3)

gen=Button(text='Generate',command=password)
gen.grid(column=1,row=4)

cop=Button(text='Copy',command=save)
cop.grid(column=2,row=3)

window.mainloop()
