from customtkinter import *

set_appearance_mode("System")
set_default_color_theme("blue")

root = CTk()
root.title	  (	"Калькулятор")
root.geometry (	"400x400")
root.resizable(False, False)
for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(4): root.rowconfigure(index=r, weight=1)


num = IntVar()
num_entry =	CTkEntry(master=root, textvariable = num, font=("Calibri", 28))
num_entry.configure(state= DISABLED)
num_entry.grid(row=0, column=0, columnspan=4, ipadx= 150)
actions = []
values  = []



last_answer = 0
def add_number(x):
    global last_answer
    if int(last_answer) == int(num.get()): 
        num.set(0)
        last_answer = 0
        
    if num.get() != 0:
        num.set(int(str(num.get())+ str(x)))
    else:
        num.set(x)
        
    print(x)
    
def add_command(some_command):
    actions.append(some_command)
    values.append(num.get())
    num.set(0)
    
def result():
    global actions
    global values
    global last_answer
    values.append(num.get())
    print(values)
    print(actions)
    
    answer = values[0]
    for i in zip(values[1:], actions):
        if i[1] == "plus":
            answer = answer + i[0]
        if i[1] == "minus":
            answer = answer - i[0]
        if i[1] == "mult":
            answer = answer * i[0]
        if i[1] == "dev":
            answer = answer / i[0]
    num.set(answer)
    actions = []
    values = []
    last_answer = answer
    
num7 = CTkButton(master=root, text="7", command = lambda: add_number(7))
num7.grid(row=1, column=0, ipadx=10, ipady=10, padx=10, pady=10)
 
num8 = CTkButton(master=root, text="8", command = lambda: add_number(8))
num8.grid(row=1, column=1, ipadx=10, ipady=10, padx=10, pady=10)

num9 = CTkButton(master=root, text="9", command = lambda: add_number(9))
num9.grid(row=1, column=2, ipadx=10, ipady=10, padx=10, pady=10)

btn_plus = CTkButton(master=root, text="+", command = lambda: add_command("plus"))
btn_plus.grid(row=1, column=3, ipadx=10, ipady=10, padx=10, pady=10)

num4 = CTkButton(master=root, text="4", command = lambda: add_number(4))
num4.grid(row=2, column=0, ipadx=10, ipady=10, padx=10, pady=10)
 
num5 = CTkButton(master=root, text="5", command = lambda: add_number(5))
num5.grid(row=2, column=1, ipadx=10, ipady=10, padx=10, pady=10)

num6 = CTkButton(master=root, text="6", command = lambda: add_number(6))
num6.grid(row=2, column=2, ipadx=10, ipady=10, padx=10, pady=10)

btn_minus = CTkButton(master=root, text="-", command = lambda: add_command("minus"))
btn_minus.grid(row=2, column=3, ipadx=10, ipady=10, padx=10, pady=10)

num1 = CTkButton(master=root, text="1", command	= lambda: add_number(1))
num1.grid(row=3, column=0, ipadx=10, ipady=10, padx=10, pady=10)

num2 = CTkButton(master=root, text="2", command = lambda: add_number(2))
num2.grid(row=3, column=1, ipadx=10, ipady=10, padx=10, pady=10)

num3 = CTkButton(master=root, text="3", command = lambda: add_number(3))
num3.grid(row=3, column=2, ipadx=10, ipady=10, padx=10, pady=10)

btn_mult = CTkButton(master=root, text="*", command = lambda: add_command("mult"))
btn_mult.grid(row=3, column=3, ipadx=10, ipady=10, padx=10, pady=10)

num0 = CTkButton(master=root, text="0", command = lambda: add_number(0))
num0.grid(row=4, column=0, ipadx=10, ipady=10, padx=10, pady=10)
 
btn_answ = CTkButton(master=root, text="=", command = result)
btn_answ.grid(row=4, column=1, columnspan=2, ipadx=70, ipady=10, padx=5, pady=5)



btn_dev = CTkButton(master=root, text="/", command = lambda: add_command("dev"))
btn_dev.grid(row=4, column=3, ipadx=10, ipady=10, padx=10, pady=10)



root.mainloop()