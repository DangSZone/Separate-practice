import tkinter as tk

def elem_():
    num1 = int(number1_.get())
    num2 = int(number2_.get())
    num3 = int(number3_.get()) * 30
    return num1, num2, num3

def delete(value):
    result_.delete(0,'end')
    result_.insert(0, value)

def resi():
    num1, num2, num3 = elem_()
    per = round(num1 + ((num1 * (num2/100) * num3) / 365))
    delete(per)




window = tk.Tk()
window.title('Сумма которую вы вернёте банку')
window.geometry('400x400')
window.resizable(False,False)

button_result = tk.Button(text= "Рассчитать", width=20, height=4, command=resi)
button_result.place(x=120, y=300)

number1_ = tk.Entry(window, width=15)
number1_.place(x=150, y=80)
number1_name = tk.Label(window, text='Сумма займа:')
number1_name.place(x=150, y=55)

number2_ = tk.Entry(window, width=15)
number2_.place(x=150, y=135)
number2_name = tk.Label(window, text='Процентная ставка:')
number2_name.place(x=150, y=110)

number3_ = tk.Entry(window, width=15)
number3_.place(x=150, y=190)
number3_name = tk.Label(window, text='Месяцы пользования:')
number3_name.place(x=150, y=165)

result_ = tk.Entry(window, width=15)
result_.place(x=150, y=250)
result_name = tk.Label(window, text='Сумма с процентом')
result_name.place(x=150, y=220)



window.mainloop()
