from tkinter import *
import mysql.connector
class detail:
    def main():
        con=''
        try:
            ano=e1.get()
            if ano =='':
                msg.set("Entry Fields Not Be Empty")
            else:
                details.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                cur=details.con.cursor()
                cur.execute("select ACCNO from bankdb where ACCNO='"+ano+"'")
                address = cur.fetchone()
                if address is not None:
                    cur.execute("select ACCNO from bankdb where ACCNO='"+ano+"'")
                    info=cur.fetchone()
                    info=info[0]
                    cur.execute("select UNAME from bankdb where ACCNO='"+ano+"'")
                    info1=cur.fetchone()
                    msg.set(info)
                    msg1.set(info1)
                    cur.execute("select BALANCE from bankdbm where ACCNO='"+ano+"'")
                    info3=cur.fetchone()
                    info3=info3[0]
                    msg2.set(info3)
                    details.con.commit()
                else:
                    msg.set("Invalid ACCNO")
        except Exception as e:
            print("Exception",e)
            return
    def exitwindow():
        details.destroy()
        return
   
details=Tk()
msg=StringVar()
msg1=StringVar()
msg2=StringVar()
details.title("DETAILS")
details.geometry("1500x1000")
logo1=PhotoImage(file="signup.png")
img1=Label(details,image=logo1)
l1=Label(details,text='ACCOUNT NO',font='times 20')
l2=Label(details,text='USER NAME',font='times 20')
l3=Label(details,text='BALANCE',font='times 20')
l7=Label(details,text='ACCNO',font='times 20')
l4=Label(details,textvariable=msg,font='times 20',fg='red')
l5=Label(details,textvariable=msg1,font='times 20',fg='red')
l6=Label(details,textvariable=msg2,font='times 20',fg='red')
e1=Entry(details,font='times 20')
b1=Button(details,text='SUBMIT',bg='blue',fg='orange',font='calibre 20',command=detail.main)
b2=Button(details,text='EXIT',bg='blue',fg='white',font='calibre 20',command=detail.exitwindow)
l1.place(x=400,y=300)
e1.place(x=600,y=300)
l7.place(x=400,y=500)
l2.place(x=400,y=600)
l3.place(x=400,y=700)
l4.place(x=650,y=500)
l5.place(x=650,y=600)
l6.place(x=650,y=700)
b1.place(x=600,y=380)
b2.place(x=760,y=380)
img1.place(x=380,y=30)
details.mainloop()


