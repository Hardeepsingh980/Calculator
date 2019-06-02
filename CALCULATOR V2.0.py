from tkinter import *


operator = ''

def button(no):
    global operator
    operator = str(operator)
    operator += str(no)
    inp.set(operator)

def equal():
    global operator
    total = eval(operator)
    inp.set(total)
    operator = total

def clear():
    global operator
    operator = ''
    inp.set('')

def about():
        more = Tk()
        more.configure(bg='powder blue')
        more.geometry('400x200+300+450')
        more.iconbitmap('ca.ico')
        

        Label(more, text='CALCULATOR',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='By: Hardeep Singh',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='This Calculator was created by Hardeep Singh\n  as a time pass project because he\nhe was feeling bored due to sunday :) \nAll the Right belong to Hardeep singh.',bg='powder blue',font=('Arial Black',10,'bold')).pack()

        Label(more, text='Contact us at:\n9803588671',bg='powder blue',font=('Arial Black',10,'bold')).pack(side=LEFT)


    
        



win = Tk()
win.geometry('313x315+379+128')
win.iconbitmap('ca.ico')

inp = StringVar()


Entry(win, font=('arial black',20),width=16,bd=10,justify='right',bg='light blue',textvariable=inp).place(x=0,y=3)

#----------------button line 1 ----------------------

Button(win, text='Clear',font=('arial black',10),bd=10,width=12,command=clear).place(x=0,y=65)
Button(win, text='A',font=('arial black',10),bd=10,width=2,command=about).place(x=130,y=65)
Button(win, text='-',font=('arial black',10),bd=10,width=2,command=lambda:button('-')).place(x=175,y=65)
Button(win, text='/',font=('arial black',10),bd=10,width=2,command=lambda:button('/')).place(x=220,y=65)
Button(win, text='*',font=('arial black',10),bd=10,width=2,command=lambda:button('*')).place(x=265,y=65)

#--------------Button line 2 ---------------------------
Button(win, text='7',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(7)).place(x=0,y=113)
Button(win, text='8',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(8)).place(x=70,y=113)
Button(win, text='9',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(9)).place(x=140,y=113)


#--------------Button line 3 ---------------------------
Button(win, text='4',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(4)).place(x=0,y=180)
Button(win, text='5',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(5)).place(x=70,y=180)
Button(win, text='6',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(6)).place(x=140,y=180)

#--------------Button line 4 ---------------------------
Button(win, text='1',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(1)).place(x=0,y=247)
Button(win, text='2',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(2)).place(x=70,y=247)
Button(win, text='3',font=('arial black',10),bd=10,width=5,height=2,command=lambda:button(3)).place(x=140,y=247)


Button(win, text='=', font=('arial black',10),bd=10,width=8,height=2,command=equal).place(x=210,y=247)
Button(win, text='0', font=('arial black',10),bd=7,width=3,height=6,command=lambda:button(0)).place(x=210,y=113)
Button(win, text='+', font=('arial black',10),bd=7,width=3,height=6,command=lambda:button('+')).place(x=260,y=113)







win.mainloop()

