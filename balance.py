from tkinter import *
import mysql.connector
class bala:
    def main():
        con=''
        try:
            ano=e1.get()
            if ano =='':
                msg.set("ACCNO Not Be Empty")
            else:
                bala.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                cur=bala.con.cursor()
                cur.execute("select ACCNO from bankdb where ACCNO='"+ano+"'")
                address = cur.fetchone()
                if address is not None:
                    cur.execute("select BALANCE from bankdbm where ACCNO='"+ano+"'")
                    balance=cur.fetchone()
                    msg1.set(balance)
                else:
                    msg.set("Invalid ACCNO")
        except Exception as e:
            print("exception",e)
        finally:
            if con !='':
                balance.con.close()
    def exitwindow():
        balance.destroy()
        return
    def home():
        balance.destroy()
        import home
        return
balance=Tk()
balance.geometry("1500x1000")
msg=StringVar()
msg1=StringVar()
balance.title("BALANCE ENQUERY")
logo1=PhotoImage(file="signup.png")
img1=Label(balance,image=logo1)
l2=Label(balance,textvariable=msg,font='times 15',fg='red')
l1=Label(balance,text='AVAILABLE BALANCE',font='times 20',fg='red')
l4=Label(balance,textvariable=msg1,font='times 20')
l3=Label(balance,text='ACCNO',font='times 20')
e1=Entry(balance,font='times 20')
b1=Button(balance,text='SUBMIT',font='times 20',bg='blue',fg='orange',command=bala.main)
b2=Button(balance,text='EXIT',font='times 20',bg='blue',fg='white',command=bala.exitwindow)
l1.place(x=500,y=500)
l2.place(x=530,y=340)
l3.place(x=400,y=300)
l4.place(x=580,y=550)
e1.place(x=500,y=300)
b1.place(x=500,y=380)
b2.place(x=660,y=380)
img1.place(x=380,y=30)
balance.mainloop()
