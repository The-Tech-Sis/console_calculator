from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('265x370')
root.resizable(0,0)


text_input = StringVar()
operator = ""


def BtnClick(Numbers):
    global operator
    operator = operator + str(Numbers)
    text_input.set(operator)


def clear_display():
    global operator
    operator = ""
    text_input.set("")


def btn_equal():
    global operator
    sum_up = str(eval(operator))
    text_input.set(sum_up)
    operator = ""

Entry_Label = Entry(root, text=text_input, bd=20, font=('arial',15,'bold'), insertwidth=5,
 justify=RIGHT)
Entry_Label.grid(columnspan=4)


btn7 = Button(root, text='7', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(7))
btn7.grid(row=2,column=0)


btn8 = Button(root, text='8', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(8))
btn8.grid(row=2,column=1)


btn9 = Button(root, text='9', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(9))
btn9.grid(row=2,column=2)


btnDiv = Button(root, text='/', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick('/'))
btnDiv.grid(row=2,column=3)


btn4 = Button(root, text='4', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(4))
btn4.grid(row=3,column=0)


btn5 = Button(root, text='5', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(5))
btn5.grid(row=3,column=1)



btn6 = Button(root, text='6', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(6))
btn6.grid(row=3,column=2)


btnMul = Button(root, text='X', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick('*'))
btnMul.grid(row=3,column=3)



btn1 = Button(root, text='1', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(1))
btn1.grid(row=4,column=0)



btn2 = Button(root, text='2', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(2))
btn2.grid(row=4,column=1)



btn3 = Button(root, text='3', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(3))
btn3.grid(row=4,column=2)


btnSub = Button(root, text='-', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick('-'))
btnSub.grid(row=4,column=3)


btn0 = Button(root, text='0', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick(0))
btn0.grid(row=5,column=0)

btnEqual = Button(root, text='=', font=('arial',15,'bold'), bd=12, fg='black',
command=btn_equal)
btnEqual.grid(row=5,column=1)


btnCancel = Button(root, text='c', font=('arial',15,'bold'), bd=12, fg='black',
command = clear_display)
btnCancel.grid(row=5,column=2)

btnAdd = Button(root, text='+', font=('arial',15,'bold'), bd=12, fg='black',
command=lambda:BtnClick('+'))
btnAdd.grid(row=5,column=3)


root.mainloop()