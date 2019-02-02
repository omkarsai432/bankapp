from tkinter import *
class home1:
    def insert():
        homepage.destroy()
        import insertrecord
        return
    def balance():
        homepage.destroy()
        import balance
        return
    def update():
        homepage.destroy()
        import update
        return
    def details():
        homepage.destroy()
        import details
        return
    def exitwindow():
        homepage.destroy()
        return
homepage=Tk()
homepage.geometry("1500x1000")
homepage.title("INDIAN BANK HOME PAGE")
logo=PhotoImage(file="bank.gif")
img=Label(homepage,image=logo)
b1=Button(homepage,text='INSERT',width=20,font='times 30',bg='blue',fg='white',command=home1.insert)
b2=Button(homepage,text='BALANCE ENQUERY',width=20,font='times 30',bg='blue',fg='white',command=home1.balance)
b3=Button(homepage,text='UPDATE',width=20,font='times 30',bg='blue',fg='orange',command=home1.update)
b4=Button(homepage,text='DETAILS',width=20,font='times 30',bg='blue',fg='white',command=home1.details)
b5=Button(homepage,text='EXIT',width=20,font='times 30',bg='blue',fg='white',command=home1.exitwindow)
b1.place(x=700,y=150)
b2.place(x=700,y=250)
b3.place(x=700,y=350)
b4.place(x=700,y=450)
b5.place(x=700,y=550)
img.place(x=100,y=240)
homepage.mainloop()
