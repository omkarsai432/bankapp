from tkinter import *
import mysql.connector
class updated:
    def main():
        con=''
        try:
            accno=e1.get()
            uname=e2.get()
            password=e3.get()
            cpassword=e4.get()
            if accno =='' or uname =='' or password =='' or cpassword =='':
                msg.set("Entry Fields Not Be Empty")
            elif password !=cpassword:
                msg.set("password not correct")
            else:
                update.con=mysql.connector.connect(user='root',password='omkarsai432',host='127.0.0.1',database='omkar')
                print("connected")
                cur=update.con.cursor()
                cur.execute("select ACCNO from bankdb where ACCNO='"+accno+"'")
                address = cur.fetchone()
                if address is not None:
                    cur.execute("update bankdb set UNAME='"+uname+"',""PASSWORD='"+password+"',""CPASSWORD='"+cpassword+"'""where ACCNO='"+accno+"'")
                    update.con.commit()
                    msg.set("UPDATED")
                    update.destroy()
                    import home
                else:
                    msg.set("Invalid ACCNO")
        except Exception as e:
            print("Exception",e)
            return
        finally:
            if con !='':
                update.con.close()
            return
    def exitwindow():
        update.destroy()
        return
update=Tk()
msg=StringVar()
update.title("UPDATE")
update.geometry("1500x1000")
logo=PhotoImage(file="signup.png")
img=Label(update,image=logo)
l1=Label(update,text='ACCOUNT NO',font='times 20')
l2=Label(update,text='USER NAME',font='times 20')
l3=Label(update,text='PASSWORD',font='times 20')
l4=Label(update,text='CONFIRM PASSWORD',font='times 20')
l5=Label(update,textvariable=msg,font='times 15',fg='red')
e1=Entry(update,font='times 20')
e2=Entry(update,font='times 20')
e3=Entry(update,font='times 20',show="*")
e4=Entry(update,font='times 20',show="*")
b1=Button(update,text='SUBMIT',bg='blue',fg='orange',font='calibre 20',command=updated.main)
b2=Button(update,text='EXIT',bg='blue',fg='white',font='calibre 20',command=updated.exitwindow)
l1.place(x=650,y=300)
l2.place(x=650,y=400)
l3.place(x=650,y=500)
l4.place(x=650,y=600)
e1.place(x=900,y=300)
e2.place(x=900,y=400)
e3.place(x=900,y=500)
e4.place(x=900,y=600)
b1.place(x=910,y=670)
b2.place(x=1060,y=670)
l5.place(x=935,y=635)
img.place(x=700,y=10)
update.mainloop
