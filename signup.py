from tkinter import *
import mysql.connector
class create:
    con=' '
    def main():
        try:
            accno=e1.get()
            uname=e2.get()
            password=e3.get()
            cpassword=e4.get()
            balance=str(0)
            if accno =='' or uname =='' or password =='' or cpassword =='':
                msg.set("Entry Fields Not Be Empty")
            elif password !=cpassword:
                msg.set("password not correct")
            else:
                create.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                print("connected")
                cur=create.con.cursor()
                cur.execute("select ACCNO from bankdb where ACCNO='"+accno+"'")
                address = cur.fetchone()
                if address is None:  
                    cur.execute('insert into bankdb values(''"'+accno+'","'+uname+ '","' +password+ '","'+cpassword+'")')
                    cur.execute('update bankdbm set BALANCE=0 where ACCNO="'+accno+'"')
                    cur.execute('insert into bankdbm(ACCNO) select ACCNO from bankdb where ACCNO="'+accno+'"')
                    create.con.commit()
                    print("sign up completed")
                    msg.set("account created")
                    details.destroy()
                    import home
                else:
                    msg.set("INVALID ACCNO")
        except Exception as e:
             print("exception",e)
             return
        finally:
            if create.con !='':
                create.con.close()
                print("connection closed")
            return
    def login():
        details.destroy()
        import login
        return
details=Tk()
msg=StringVar()
msg1=StringVar()
msg2=StringVar()
msg1.set("OUR NEW SERVICES")
msg2.set("FOLLOW US ON TWITTER")
details.title("INDIAN BANK")
details.geometry("1500x1000")
logo=PhotoImage(file="signup.png")
img=Label(details,image=logo)
logo1=PhotoImage(file="Signup1.png")
img1=Label(details,image=logo1)
logo2=PhotoImage(file="signuP.png")
img2=Label(details,image=logo2)
l1=Label(details,text='ACCOUNT NO',font='times 20')
l2=Label(details,text='USER NAME',font='times 20')
l3=Label(details,text='PASSWORD',font='times 20')
l4=Label(details,text='CONFIRM PASSWORD',font='times 20')
l5=Label(details,textvariable=msg,font='times 15',fg='red')
l8=Label(details,textvariable=msg1,font='times 30',fg='blue')
l9=Label(details,textvariable=msg2,font='times 30',fg='blue')
e1=Entry(details,font='times 20')
e2=Entry(details,font='times 20')
e3=Entry(details,font='times 20',show="*")
e4=Entry(details,font='times 20',show="*")
b1=Button(details,text='SIGNUP',bg='blue',fg='orange',font='calibre 20',command=create.main)
b2=Button(details,text='LOGIN',bg='blue',fg='white',font='calibre 20',command=create.login)
l1.place(x=650,y=300)
l2.place(x=650,y=400)
l3.place(x=650,y=500)
l4.place(x=650,y=600)
e1.place(x=900,y=300)
e2.place(x=900,y=400)
e3.place(x=900,y=500)
e4.place(x=900,y=600)
b1.place(x=900,y=670)
b2.place(x=1040,y=670)
l5.place(x=935,y=635)
l8.place(x=0,y=430)
l9.place(x=10,y=20)
img.place(x=700,y=10)
img1.place(x=10,y=70)
img2.place(x=100,y=500)
details.mainloop
