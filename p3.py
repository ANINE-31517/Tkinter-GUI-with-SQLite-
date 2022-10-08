import cgi
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("STORE's LOGIN")
root.geometry("500x300+425+200")
root.resizable(False,False)
root.config(bg="black")
bg=ImageTk.PhotoImage(file='Images/A9.png')
bg_label=Label(root, bd=0, image=bg, relief=FLAT)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
import os
import sqlite3
import pyttsx3
import webbrowser
import time

#VARIABLES

v_EMAIL=StringVar()
v_PASSWORD=StringVar()        
        
#COMPANY NAME
        
NAME=Label(root,text=">>> A9 STORE",font="ar 8 bold", bg='orange', fg="black", bd=0)
NAME.place(x=6, y=6)

#HEADING

HEAD=Label(root,text="LOGIN HERE",font="ar 20 bold",bg="orange",fg="white", bd=0)
HEAD.place(x=160, y=30)

#E-MAIL

EMAIL=Label(root,text="E-MAIL :",font="ar 10 bold",bg="orange",fg="black", bd=0)
EMAIL.place(x=90, y=100)

EMAILentry=Entry(root, textvariable=v_EMAIL, width=35)
EMAILentry.place(x=200, y=98)

#PASSWORD

def toggle_PASSWORD():
    if PASSWORDentry.cget('show') == '':
        PASSWORDentry.config(show='*')
        toggle_btn.config(text="SHOW")
        
    else:
        PASSWORDentry.config(show="")
        toggle_btn.config(text="HIDE")

PASSWORD=Label(root,text="PASSWORD :",font="ar 10 bold",bg="orange",fg="black", bd=0)
PASSWORD.place(x=88, y=136)

PASSWORDentry=Entry(root, show="*", textvariable=v_PASSWORD)
PASSWORDentry.place(x=200, y=134)

toggle_btn=Button(root, text='SHOW', font='ar 6 bold', bg='orange', fg='black', cursor='hand2', bd=1, command=toggle_PASSWORD, width=4)    
toggle_btn.place(x=326, y=136)

#FUNCTIONS

def callnewscreen():
    root.destroy()
    os.system('python p4.py')

def callbackscreen():
    root.destroy()
    os.system('python p.py')

def getvals():   
    if v_EMAIL.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR EMAIL')
        engine.runAndWait()          
        messagebox.showerror('ERROR', 'ENTER YOUR E-MAIL')
        
    elif v_PASSWORD.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR PASSWORD')
        engine.runAndWait()         
        messagebox.showerror('ERROR', 'ENTER YOUR PASSWORD')
        
    else:
    
        #RE-CHECKING

        try:

            email=v_EMAIL.get()
            password=v_PASSWORD.get()
            
            con=sqlite3.connect("DETAIL.db")     
            cur=con.cursor()
            cur.execute("SELECT * FROM DETAIL WHERE email=?", (email, ))
            row=cur.fetchone()
                
            if row==None:
                engine = pyttsx3.init()
                engine.say("EMAIL NOT FOUND")
                engine.runAndWait()
                messagebox.showerror("ERROR", "E-MAIL NOT FOUND")
                return False

            else:
                pass
                
            cur.execute("SELECT * FROM DETAIL WHERE  password=?", (password, ))
            column=cur.fetchone()

            if column==None:
                engine = pyttsx3.init()
                engine.say("INCORRECT PASSWORD")
                engine.runAndWait()
                messagebox.showerror("ERROR", "INCORRECT PASSWORD")
                return False

            else:         
                engine = pyttsx3.init()
                engine.say("SUCCESSFULLY  LOGGED IN")
                engine.runAndWait()
                messagebox.showinfo("INFORMATION", "SUCCESSFULLY  LOGGED IN")

                con.commit()
                con.close()
                    
                EMAILentry.delete(0,END)
                PASSWORDentry.delete(0,END)
                root.destroy()
                    
                time.sleep(0.5)
                webbrowser.open_new_tab("HOME.html")
                
            
##        EMAIL1=v_EMAIL.get()
##        PASSWORD1=v_PASSWORD.get()
##                             
##        list_of_files=os.listdir()
##        if  EMAIL1 in  list_of_files:
##            file1=open(EMAIL1, "r")
##            verify=file1.read().splitlines()
##        
##            if  PASSWORD1 in verify:
##                engine = pyttsx3.init()
##                engine.say('SUCCESSFULLY  LOGGED IN')
##                engine.runAndWait()              
##                messagebox.showinfo("INFORMATION", "SUCCESSFULLY  LOGED IN")
##                root.destroy()
##            
##            else:
##                 engine = pyttsx3.init()
##                 engine.say('PASSWORD NOT RECOGNISED')
##                 engine.runAndWait()              
##                 messagebox.showerror("ERROR",  "PASSWORD NOT RECOGNISED")
##
##        else:
##            engine = pyttsx3.init()
##            engine.say('EMAIL NOT FOUND')
##            engine.runAndWait()         
##            messagebox.showerror("ERROR",  "E-MAIL NOT FOUND")

        except Exception as es:
            engine = pyttsx3.init()
            engine.say("ERROR")
            engine.runAndWait()            
            messagebox.showerror("ERROR", f"{str(es)}")                

#BUTTONS

btn_forgetpassword = Button(root, text="FORGET PASSWORD ? ",font="ar 9 bold",bg="orange",fg="white", cursor="hand2", command=callnewscreen, bd=1).place(x=196, y=170)

btn_login = Button(root, text="LOGIN NOW", fg="white", bg="orange", font="ar 8 bold", cursor="hand2", command=getvals).place(x=405, y=250)

Button(text="BACK", fg="white", bg="orange", font="ar 8 bold", cursor="hand2", command=callbackscreen).place(x=20, y=250)

root.mainloop()


