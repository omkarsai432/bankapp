from tkinter import *
from PIL import *
import mysql.connector
class insert:
    con=' '
    def main():
            ano=e1.get()
            amount=e3.get()
            if ano =='' or  amount =='':
                msg.set("Entry Fields Not Be Empty")
            else:
                insert.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                print("connected")
                cur=insert.con.cursor()
                cur.execute("select ACCNO from bankdb where ACCNO='"+ano+"'")
                address = cur.fetchone()
                if address is not None:
                    cur.execute("select BALANCE from bankdbm where ACCNo='"+ano+"'")
                    bal=cur.fetchone()
                    bal=bal[0]
                    if bal is None:
                        cur.execute("update bankdbm set BALANCE='"+amount+"'""where ACCNO='"+ano+"'")
                        msg1.set("Record Inserted")
                        insert.con.commit()
                    else:
                        bal=str(bal)
                        bal=int(bal)
                        amount=int(amount)
                        amount=amount+bal
                        cur.execute("update bankdbm set BALANCE='"+str(amount)+"'""where ACCNO='"+ano+"'")
                        msg1.set("Record Updated")
                        insert.con.commit()
                else:
                    msg1.set("Invalid ACCNO")
    def exitwindow():
        details.destroy()
        return
details=Tk()
msg=StringVar()
msg1=StringVar()
details.title("RECORD INSERTION")
details.geometry("1500x1000")
logo=PhotoImage(file="insert1.png")
img=Label(details,image=logo)
logo1=PhotoImage(file="signup.png")
img1=Label(details,image=logo1)
l1=Label(details,text='ACC NO',font='times 20')
l3=Label(details,text='AMOUNT',font='times 20')
l4=Label(details,textvariable=msg,font='times 15',fg='red')
l5=Label(details,textvariable=msg1,font='times 15',fg='red')
e1=Entry(details,font='times 20')
e3=Entry(details,font='times 20')
b=Button(details,text='RECORD',bg='blue',fg='orange',font='times 20',command=insert.main)
b1=Button(details,text='EXIT',bg='blue',fg='white',font='times 20',command=insert.exitwindow)
l1.place(x=700,y=350)
e1.place(x=850,y=350)
l3.place(x=700,y=450)
e3.place(x=850,y=450)
l4.place(x=880,y=490)
l5.place(x=880,y=500)
b.place(x=850,y=530)
b1.place(x=1000,y=530)
img.place(x=80,y=50)
img1.place(x=700,y=50)
details.mainloop
