from tkinter import *
from PIL import ImageTk,Image
import os
win=Tk()
win.title('Banking App')

#function
def finish_reg():
    name=temp_name.get()
    age=temp_age.get()
    gender=temp_gender.get()
    password=temp_password.get()
    all_accounts=os.listdir()

    if name =="" or age=="" or gender=="" or password=="":
        notif.config(fg='Red',text='All Field is Required *')
        return
    for name_check in all_accounts:
        if name==name_check:
            notif.config(fg='red',text='Account Already Exists')
            return
        else:
            new_file= open(name,'w')
            new_file.write(name+'\n')
            new_file.write(age+'\n')
            new_file.write(gender+'\n')
            new_file.write(password+'\n')
            new_file.close()
            notif.config(fg='green',text='Account has been created')
def Register():
    #Vraiable
    global temp_name
    global temp_age
    global temp_gender
    global temp_password
    global notif
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()
    
    screen=Toplevel(win)
    screen.title('Register')

    Label(screen,text='Please Enter Your Details below Register',font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
    Label(screen,text='Name',font=('Calibri',12)).grid(row=1,sticky=W)
    Label(screen,text='Age',font=('Calibri',12)).grid(row=2,sticky=W)
    Label(screen,text='Gender',font=('Calibri',12)).grid(row=3,sticky=W)
    Label(screen,text='Password',font=('Calibri',12)).grid(row=4,sticky=W)
    notif=Label(screen,font=('Calibri',12))
    notif.grid(row=6,sticky=N,pady=10)
    
    #Entery
    Entry(screen,textvariable=temp_name).grid(row=1,column=1)
    Entry(screen,textvariable=temp_age).grid(row=2,column=1)
    Entry(screen,textvariable=temp_gender).grid(row=3,column=1)
    Entry(screen,textvariable=temp_password,show='*').grid(row=4,column=1)

    Button(screen,text='Register',command=finish_reg,font=('Calibri',12)).grid(row=5,sticky=N,pady=10)
def Login():
    pass

#Image Import
img=Image.open('bank.png')
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

#Lables
Label(win,text='Custom Banking Beta',font=('calibri',14)).grid(row=0,sticky=N,pady=10)
Label(win,text="The Most Secure Bank You've probably Used",font=('calibri',12)).grid(row=1,sticky=N)
Label(win,image=img).grid(row=2,sticky=N,pady=15)

#Button
Button(win,text="Register",font=('Calibri',12),width=20,command=Register).grid(row=3,sticky=N)
Button(win,text="Login",font=('Calibri',12),width=20,command=Login).grid(row=4,sticky=N)


win.mainloop()
