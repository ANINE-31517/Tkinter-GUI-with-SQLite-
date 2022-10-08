import cgi
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("FORGET PASSWORD")
root.geometry("500x300+425+200")
root.resizable(False,False)
root.config(bg="black")
bg=ImageTk.PhotoImage(file='Images/A9.png')
bg_label=Label(root, bd=0, image=bg, relief=FLAT)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
import os
import sqlite3
import pyttsx3
import time
import webbrowser

#VARIABLES

v_EMAIL=StringVar()
v_NEW=StringVar()
v_CONFIRM=StringVar()            

#COMPANY NAME

HEAD=Label(root, text='>>> A9 STORE', font="ar 8 bold", bg="orange", fg="black", bd=0)
HEAD.place(x=4, y=4)

#HEADING

HEAD=Label(root,text="E-MAIL",font="ar 18 bold",bg="orange",fg="white", bd=0)
HEAD.place(x=211, y=18)

#HEADING2

HEAD2=Label(root,text="RESET PASSWORD",font="ar 18 bold",bg="orange",fg="white", bd=0)
HEAD2.place(x=141, y=118)

#E-MAIL

EMAIL=Label(root,text="E-MAIL :",font="ar 10 bold",bg="orange",fg="black", bd=0)
EMAIL.place(x=82, y=75)

EMAILentry=Entry(root, textvariable=v_EMAIL, width=35)
EMAILentry.place(x=173, y=73)

#NEW PASSWORD

def toggle_NEWentry():
    if NEWentry.cget('show') == '':
        NEWentry.config(show='*')
        toggle_btn.config(text='SHOW')
        
    else:
        NEWentry.config(show='')
        toggle_btn.config(text='HIDE')
        
NEW=Label(root,text="NEW PASSWORD :", font="ar 10 bold", bg="orange", fg="black", bd=0)
NEW.place(x=81, y=178)

NEWentry=Entry(root, show="*",  textvariable=v_NEW)
NEWentry.place(x=238, y=177)

toggle_btn=Button(root, text="SHOW", font='ar 6  bold', command=toggle_NEWentry, fg='black', bg='orange', cursor='hand2', bd=1)         
toggle_btn.place(x=363, y=178)

#CONFIRM PASSWORD

def toggle_CONFIRMentry():
    if CONFIRMentry.cget('show') == '':
        CONFIRMentry.config(show='*')
        toggle_bn.config(text='SHOW')
        
    else:
        CONFIRMentry.config(show='')
        toggle_bn.config(text='HIDE')
    

CONFIRM=Label(root,text="CONFIRM PASSWORD :", font="ar 10 bold", bg="orange", fg="black", bd=0)
CONFIRM.place(x=81, y=218)

CONFIRMentry=Entry(root, show="*",   textvariable=v_CONFIRM)
CONFIRMentry.place(x=268, y=216)

toggle_bn=Button(root, text="SHOW", font='ar 6  bold', command=toggle_CONFIRMentry, fg='black', bg='orange', cursor='hand2', bd=1)         
toggle_bn.place(x=393, y=217)

#FUNCTIONS

def callbackscreen():
    root.destroy()
    os.system('python p3.py')

def validate_Email():
    if v_EMAIL.get() == "":
        engine = pyttsx3.init()
        engine.say('ENTER YOUR EMAIL')
        engine.runAndWait()          
        messagebox.showerror('ERROR', 'ENTER YOUR E-MAIL')

    else:
        
        #RE-CHECKING

        try:
            
            email=v_EMAIL.get()
            new=v_NEW.get()
            
            conn=sqlite3.connect("DETAIL.db")
            with conn:
                cursor=conn.cursor()
                cursor.execute("SELECT * FROM DETAIL WHERE email = ?", (email, ))
                row=cursor.fetchone()
            
                if row == None:
                    engine = pyttsx3.init()
                    engine.say('EMAIL NOT FOUND')
                    engine.runAndWait()   
                    messagebox.showerror("ERROR", "E-MAIL NOT FOUND")
                    return False

                else:

                    if v_NEW.get() == "":
                        engine = pyttsx3.init()
                        engine.say("ENTER YOUR NEW PASSWORD")
                        engine.runAndWait()
                        messagebox.showerror("ERROR", "ENTER YOUR NEW PASSWORD")
                 
                    elif len(v_NEW.get()) < 10:
                        engine = pyttsx3.init()
                        engine.say("PASSWORD is TOO SHORT")
                        engine.say('ENTER A STRONG PASSWORD')
                        engine.runAndWait()           
                        messagebox.showerror('ERROR', 'ENTER A STRONG PASSWORD')

                    elif len(v_NEW.get()) > 15:
                        engine = pyttsx3.init()
                        engine.say('PASSWORD IS TOO LONG')
                        engine.runAndWait()         
                        messagebox.showwarning("ALERT", "PASSWORD IS TOO LONG")        

                    elif v_CONFIRM.get() == "":
                        engine = pyttsx3.init()
                        engine.say("ENTER YOUR CONFIRM PASSWORD")
                        engine.runAndWait()
                        messagebox.showerror("ERROR", "ENTER YOUR CONFIRM PASSWORD")

                    elif v_NEW.get() != v_CONFIRM.get() :
                        engine =  pyttsx3.init()
                        engine.say("PASSWORD MISMATCH")
                        engine.runAndWait()
                        messagebox.showwarning("ALERT", "PASSWORD MISMATCH")
                    
                    else:
                        cursor.execute("UPDATE DETAIL SET password = ? WHERE email = ?", (new, email, ))
                        conn.commit()
                     
                        engine = pyttsx3.init()
                        engine.say('PASSWORD CHANGED SUCCSSFULLY')
                        engine.runAndWait()                  
                        messagebox.showinfo("INFORMATION", "PASSWORD CHANGED SUCCSSFULLY")

                        EMAILentry.delete(0, END)
                        NEWentry.delete(0, END)
                        CONFIRMentry.delete(0, END)
                        root.destroy()
                     
                        time.sleep(0.5)
                        webbrowser.open_new_tab("HOME.html")
                 
        except Exception as es:
            engine = pyttsx3.init()
            engine.say("ERROR")
            engine.runAndWait()
            messagebox.showerror("ERROR", f"{str(es)}")
            conn.close()


#BUTTONS

Button(text="RESET NOW", font="ar 9 bold", fg='white', bg='orange', cursor='hand2', command=validate_Email).place(x=415, y=265)

Button(text="BACK", font="ar 9 bold", fg='white', bg='orange', cursor='hand2', command=callbackscreen).place(x=5, y=265)

root.mainloop()


