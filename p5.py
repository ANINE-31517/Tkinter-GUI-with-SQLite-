import cgi
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("USER's RESIDENCE")
root.geometry("500x300+425+200")
root.config(bg="black")
root.resizable(False,False)
bg=ImageTk.PhotoImage(file='Images/A9.png')
bg_label=Label(root, bd=0, image=bg, relief=FLAT)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
import re
import os
import sqlite3
import pyttsx3
import webbrowser
import time

#VARIABLES

v_EMAIL = StringVar()
v_ADDRESS = StringVar()
v_LANDMARK=StringVar()
v_PINCODE=StringVar()

#COMPANY NAME

NAME=Label(root,text=">>> A9 STORE",font="ar 8 bold",bg='orange',  fg='black', bd=0)
NAME.place(x=5, y=5)

#HEADING1

HEAD=Label(root,text="E-MAIL",font="ar 18 bold",bg="orange",fg="white", bd=0)
HEAD.place(x=210, y=10)

#HEADING2

HEAD=Label(root, text="RESIDENCE", font="ar 20 bold", bg="orange", fg="white", bd=0)
HEAD.place(x=172, y=120)

#E-MAIL

EMAIL=Label(root,text="E-MAIL :",font="ar 10 bold",bg="orange",fg="black", bd=0)
EMAIL.place(x=82, y=75)

EMAILentry=Entry(root, textvariable=v_EMAIL, width=35)
EMAILentry.place(x=173, y=73)

#ADDRESS

ADDRESS=Label(root, text="ADDRESS:", font="ar 10 bold", fg="black", bg="orange", bd=0)
ADDRESS.place(x=25, y=170)

ADDRESSentry=Entry(root, textvariable=v_ADDRESS, width=60)
ADDRESSentry.place(x=120, y=169)

#LANDMARK

LANDMARK = Label(root, text="LANDMARK:", font="ar 10 bold", fg= "black", bg="orange", bd=0)
LANDMARK.place(x=15, y=205)

LANDMARKentry=Entry(root, textvariable=v_LANDMARK, width=60)
LANDMARKentry.place(x=120, y=204)

#PINCODE

PINCODE = Label(root, text="PINCODE:", font="ar 10 bold", fg="black", bg="orange", bd=0)
PINCODE.place(x=175, y=240)

PINCODEentry=Entry(root, textvariable=v_PINCODE, width=10)
PINCODEentry.place(x=265, y=239)

def validate_PINCODE(user_PINCODE):
    if user_PINCODE.isdigit():
        return True

    elif user_PINCODE == "":
        return True

    else:
        engine = pyttsx3.init()
        engine.say("ONLY DIGITS ARE ALLOWED")
        engine.runAndWait()              
        messagebox.showwarning('ALERT', 'ONLY DIGITS ARE ALLOWED')
        return False

valid_PINCODE=root.register(validate_PINCODE)
PINCODEentry.config(validate="key", validatecommand=(valid_PINCODE, '%P'))

#FUNCTIONS

def callbackscreen():
    root.destroy
    os.system("python p.py")

def validateallfields():
    if v_ADDRESS.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR ADDRESS')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'ENTER YOUR ADDRESS')
        
    elif v_ADDRESS.get() == "":
        engine = pyttsx3.init()
        engine.say(' ADDRESS')
        engine.runAndWait()
        messagebox.showerror('ERROR', ' ADDRESS')        

    elif len(v_ADDRESS.get()) < 20:
        engine = pyttsx3.init()
        engine.say('ADDRESS IS TOO SHORT')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'ADDRESS IS TOO SHORT')

    elif len(v_ADDRESS.get()) > 100:
        engine = pyttsx3.init()
        engine.say('ADDRESS IS TOO LONG')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'ADDRESS IS TOO LONG')    

    elif v_LANDMARK.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR LANDMARK')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'ENTER YOUR LANDMARK')

    elif len(v_LANDMARK.get()) < 20:
        engine = pyttsx3.init()
        engine.say('LANDMARK IS TOO SHORT')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'LANDMARK IS TOO SHORT')        

    elif len(v_LANDMARK.get()) > 100:
        engine = pyttsx3.init()
        engine.say('LANDMARK IS TOO LONG')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'LANDMARK IS TOO LONG')            

    elif v_PINCODE.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR PINCODE')
        engine.runAndWait()
        messagebox.showerror('ERROR', 'ENTER YOUR PINCODE')

    elif len(v_PINCODE.get()) != 6:
        engine = pyttsx3.init()
        engine.say('ENTER A VALID PINCODE')
        engine.runAndWait()
        messagebox.showwarning('ALERT', 'ENTER A VALID PINCODE')        

    else:
        try:
            email=v_EMAIL.get()
            address=v_ADDRESS.get() 
            landmark=v_LANDMARK.get()
            pincode=v_PINCODE.get()
                    
            con=sqlite3.connect('DETAIL.db')
            cur=con.cursor()
            cur.execute("SELECT * FROM DETAIL WHERE email= ?", (email, ))
            row=cur.fetchone()
                
            if row==None:
                engine = pyttsx3.init()
                engine.say("EMAIL  NOT FOUND")
                engine.runAndWait()                                         
                messagebox.showwarning("ALERT", "E-MAIL  NOT FOUND")
                return False        

            else:
##                cur.execute('UPDATE DETAIL SET address = ?, landmark = ?, pincode = ? WHERE email = ?', (address, landmark, pincode, email, ))
##                
                cur.execute('INSERT INTO RESIDENCE(EMAIL, ADDRESS, LANDMARK, PINCODE) VALUES(?, ?, ?, ?)', (email, address, landmark, pincode))
                con.commit()
                con.close()
                                
                engine = pyttsx3.init()
                engine.say("SUCCESSFULLY SUMITTED")
                engine.runAndWait()                   
                messagebox.showinfo('INFORMATION', 'SUCCESSFULLY SUMITTED')
                                
                ADDRESSentry.delete(0, END)
                LANDMARKentry.delete(0, END)
                PINCODEentry.delete(0, END)

                root.destroy()

##                time.sleep(0.0)
##                webbrowser.open_new_tab("HOME.html")            

        except Exception as es:
            engine = pyttsx3.init()
            engine.say("ERROR")
            engine.runAndWait()                    
            messagebox.showerror("ERROR" ,f"{str(es)}")
            

        
        
#BUTTONS

btn_Register = Button(root, text="SUBMIT", fg="white", bg="orange", font="ar 9 bold", command = validateallfields, cursor="hand2").place(x=442, y=270)    

Button(text="BACK", fg="white", bg="orange", font="ar 9 bold", command=callbackscreen, cursor="hand2").place(x=5, y=270)



root.mainloop()
