from tkinter import *
import mysql.connector
class login:
    def main():
        con =' '
        accno=e1.get()
        pword=e2.get()
        if accno=='' or pword=='':
            msg.set("Entry fields can't be empty")
        else:
            try:
                login.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                cur=login.con.cursor()
                cur.execute("select ACCNO, PASSWORD from bankdb where ACCNO='"+accno+"'")
                address = cur.fetchone()
                if address is not None:
                    if accno == str(address[0]) and pword == address[1]:
                        log.destroy()
                        import home
                    else:
                        msg.set("INVALID LOGIN")
                else:
                    msg.set("INVALID LOGIN")
                return
            except Exception as e:
                print("exception",e)
    def exitwindow():
        log.destroy()
        return
log=Tk()
msg=StringVar()
log.title("LOGIN PAGE")
log.geometry("1500x1000")
logo=PhotoImage(file="logo.gif")
img=Label(log,image=logo)
l1=Label(log,text='ACCOUNT NO',font='times 20')
l2=Label(log,text='PASSWORD',font='times 20')
e1=Entry(log,font='times 20')
e2=Entry(log,font='times 20',show="*")
l3=Label(log,textvariable=msg,fg='red',font='times 18')
b1=Button(log,text='LOGIN',font='calibre 20',bg='blue',fg='orange',command=login.main)
b2=Button(log,text='EXIT',font='calibre 20',bg='blue',fg='white',command=login.exitwindow)
l1.place(x=650,y=350)
l2.place(x=650,y=450)
e1.place(x=850,y=350)
e2.place(x=850,y=450)
b1.place(x=860,y=550)
b2.place(x=990,y=550)
l3.place(x=650,y=300)
img.place(x=570,y=10)
l3.place(x=880,y=500)
log.mainloop()

