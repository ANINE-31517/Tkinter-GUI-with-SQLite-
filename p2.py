import cgi
from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.title("STORE's REGISTRATION")
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
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

#VARIABLES
        
v_FIRST = StringVar()
v_LAST = StringVar()
v_GENDER = IntVar()
v_EMAIL = StringVar()
v_PASSWORD = StringVar()
v_PHONE = StringVar()
v_COUNTRY =StringVar()        
        
#COMPANY NAME

NAME=Label(root,text=">>> A9 STORE",font="ar 8 bold",bg='orange',  fg='black', bd=0)
NAME.place(x=1, y=1)

#HEADING

HEAD=Label(root, text="REGISTER HERE", font="ar 20 bold", bg="orange", fg="white", bd=0)
HEAD.place(x=140, y=5)

#FIRST NAME

def validate_FIRST(user_FIRST):
    if user_FIRST.isalpha():
        return True

    elif user_FIRST == "":
        return True

    else:
        engine = pyttsx3.init()
        engine.say("ONLY CHARACTERS ARE ALLOWED")
        engine.runAndWait()           
        messagebox.showwarning('ALERT', 'ONLY CHARACTERS ARE ALLOWED')
        return False

FIRST=Label(root, text="FIRST NAME:", font="ar 10 bold", bg="orange", fg="black", bd=0)
FIRST.place(x=5, y=60)

FIRSTentry=Entry(root, textvariable=v_FIRST)
FIRSTentry.place(x=120, y=58)

valid_FIRST=root.register(validate_FIRST)
FIRSTentry.config(validate="key", validatecommand=(valid_FIRST, '%P'))

#LAST NAME

def validate_LAST(user_LAST):
    if user_LAST.isalpha():
        return True

    elif user_LAST == "":
        return True

    else:
        engine = pyttsx3.init()
        engine.say("ONLY CHARACTERS ARE ALLOWED")
        engine.runAndWait()             
        messagebox.showwarning('ALERT', 'ONLY CHARACTERS ARE ALLOWED')
        return False

LAST=Label(root, text="LAST NAME:",font="ar 10 bold",bg="orange",fg="black", bd=0)
LAST.place(x=250, y=60)

LASTentry=Entry(root, textvariable=v_LAST)
LASTentry.place(x=360, y=58)

valid_LAST=root.register(validate_LAST)
LASTentry.config(validate="key", validatecommand=(valid_LAST, '%P'))

#GENDER

GENDER=Label(root, text="GENDER:", font="ar 10 bold", bg="orange", fg="black", bd=0)
GENDER.place(x=33, y=105)

R1 = Radiobutton(root, text="MALE", font="ar 9 bold", bg="orange", fg="black", variable=v_GENDER, value=1, cursor="hand2").place(x=150, y=97)
R2 = Radiobutton(root, text="FEMALE", font="ar 9 bold", bg="orange", fg="black", variable=v_GENDER, value=2, cursor="hand2").place(x=250, y=103)
R3 = Radiobutton(root, text="OTHERS", font="ar 9 bold", bg="orange", fg="black", variable=v_GENDER, value=3, cursor="hand2").place(x=360, y=107)

#E-MAIL

def validate_EMAIL(user_EMAIL):
         if re.match('^[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)$', user_EMAIL):
                 return True
                
         else:
                 engine = pyttsx3.init()
                 engine.say("INVALID E-MAIL ADDRESS")
                 engine.runAndWait()              
                 messagebox.showwarning("ALERT", "INVALID E-MAIL ADDRESS")
                 return False
  
EMAIL=Label(root, text="E-MAIL:", font="ar 10 bold", bg="orange", fg="black", bd=0)
EMAIL.place(x=40, y=150)

EMAILentry=Entry(root, textvariable=v_EMAIL, width=35)
EMAILentry.place(x=120, y=148)

#PASSWORD

def toggle_PASSWORD():
    if PASSWORDentry.cget('show') == '':
        PASSWORDentry.config(show='*')
        toggle_btn.config(text="SHOW")
        
    else:
        PASSWORDentry.config(show="")
        toggle_btn.config(text="HIDE")

PASSWORD=(Label(root, text="PASSWORD:", font="ar 10 bold", bg="orange", fg="black", bd=1))
PASSWORD.place(x=10, y=195)

PASSWORDentry=Entry(root, show="*", textvariable=v_PASSWORD)
PASSWORDentry.place(x=120, y=193)

toggle_btn=Button(root, text="SHOW", font="ar 6 bold", bg="orange", fg="black", command=toggle_PASSWORD, width=4, cursor='hand2', bd=1)
toggle_btn.place(x=246, y=195)

#PHONE

def validate_PHONE(user_PHONE):
         if re.match('^[+]91\d{3}\d{3}\d{4}$', user_PHONE):
                 return True
          
         else:
                 engine = pyttsx3.init()
                 engine.say("INVALID PHONE NUMBER")
                 engine.runAndWait()              
                 messagebox.showwarning("ALERT", "INVALID PHONE NUMBER")
                 return False

PHONE=Label(root, text="PHONE:", font="ar 10 bold", bg="orange", fg="black", bd=0)
PHONE.place(x=285, y=195)

PHONEentry=Entry(root, textvariable=v_PHONE)
PHONEentry.place(x=360, y=193)
    
##    if user_PHONE.isnumeric():
##        return True
##
##    elif user_PHONE == "":
##        return True 
##
##    else:
##        engine = pyttsx3.init()
##        engine.say("ONLY DIGITS ARE ALLOWED")
##        engine.runAndWait()              
##        messagebox.showwarning('ALERT', 'ONLY DIGITS ARE ALLOWED')
##        return False

##valid_PHONE=root.register(validate_PHONE)
##PHONEentry.config(validate="key", validatecommand=(valid_PHONE, '%P'))

#COUNTRY

COUNTRY=Label(root, text="COUNTRY:", font="ar 10 bold", bg="orange", fg="black", bd=0)
COUNTRY.place(x=25, y=240)
list_COUNTRY=['INDIA']

droplist=OptionMenu(root, v_COUNTRY, *list_COUNTRY)
droplist.config(width=25, bg="orange", fg="black", bd=0)
v_COUNTRY.set("SELECT YOUR COUNTRY")
droplist.place(x=120, y=236)

#FUNCTIONS

def validateallfields(): 
        if v_FIRST.get() == "":                
                engine = pyttsx3.init()
                engine.say('ENTER YOUR FIRST NAME')
                engine.runAndWait()
                messagebox.showerror('ERROR', 'ENTER YOUR FIRST NAME')
                
        elif v_LAST.get() == "":
                engine = pyttsx3.init()
                engine.say('ENTER YOUR LAST NAME')
                engine.runAndWait()            
                messagebox.showerror('ERROR', 'ENTER YOUR LAST NAME')
                
        elif v_GENDER.get() == 0:
                engine = pyttsx3.init()
                engine.say('SELECT YOUR GENDER')
                engine.runAndWait()            
                messagebox.showerror('ERROR', 'SELECT YOUR GENDER')
                
        elif v_EMAIL.get() == "":
                engine = pyttsx3.init()
                engine.say('ENTER YOUR EMAIL')
                engine.runAndWait()            
                messagebox.showerror('ERROR', 'ENTER YOUR E-MAIL')

        elif len(v_EMAIL.get()) < 10:
                engine = pyttsx3.init()
                engine.say('E-MAIL is TOO SHORT')
                engine.runAndWait()            
                messagebox.showwarning('ALERT', 'E-MAIL IS TOO SHORT')

        elif len(v_EMAIL.get()) > 50:
                engine = pyttsx3.init()
                engine.say('E-MAIL is TOO LONG')
                engine.runAndWait()                   
                messagebox.showwarning('ALERT', 'E-MAIL IS TOO LONG')                           
                
        elif v_PASSWORD.get() == "":
                engine = pyttsx3.init()
                engine.say('ENTER YOUR PASSWORD')
                engine.runAndWait()                   
                messagebox.showerror('ERROR', 'ENTER YOUR PASSWORD')
                
        elif len(v_PASSWORD.get()) < 10:
                engine = pyttsx3.init()
                engine.say("PASSWORD is TOO SHORT")
                engine.say("ENTER A STRONG PASSWORD")
                engine.runAndWait()              
                messagebox.showwarning("ALERT", "ENTER A STRONG PASSWORD")

        elif len(v_PASSWORD.get()) > 15:
                engine = pyttsx3.init()
                engine.say("PASSWORD is TOO LONG")
                engine.runAndWait()                   
                messagebox.showwarning("ALERT", "PASSWORD IS TOO LONG")                
                
        elif v_PHONE.get() == "":
                engine = pyttsx3.init()
                engine.say("ENTER YOUR PHONE NUMBER")
                engine.runAndWait()                
                messagebox.showerror('ERROR', 'ENTER YOUR PHONE NUMBER')
                
        elif len(v_PHONE.get()) != 13:
                engine = pyttsx3.init()
                engine.say("ENTER A VALID PHONE NUMBER WITH INDIAN COUNTRY CODE")
                engine.runAndWait()             
                messagebox.showwarning('ALERT', 'ENTER A VALID PHONE NUMBER WITH INDIAN COUNTRY CODE')
               
                
        elif v_COUNTRY.get() == "" or v_COUNTRY.get() == "SELECT YOUR COUNTRY":
                engine = pyttsx3.init()
                engine.say("SELECT YOUR COUNTRY")
                engine.runAndWait()                         
                messagebox.showerror('ERROR', 'SELECT YOUR COUNTRY')


        elif v_EMAIL.get() != "":
            Email=validate_EMAIL(v_EMAIL.get())
            
            if(Email==True):
                pass
            
                if(v_PHONE.get()) != "":
                    Phone=validate_PHONE(v_PHONE.get())
               
                    if(Phone==True):
                        pass
             
                        #DATABASE
                
                        try:
                    
                            first=v_FIRST.get()
                            last=v_LAST.get()
                            gender=v_GENDER.get()
                            email=v_EMAIL.get()
                            password=v_PASSWORD.get()
                            phone=v_PHONE.get()
                            country=v_COUNTRY.get()
                    
                            con=sqlite3.connect('DETAIL.db')
                            cur=con.cursor()    
                            cur.execute('CREATE TABLE IF NOT EXISTS DETAIL(FIRSTNAME text NOT NULL, LASTNAME text NOT NULL, GENDER integer NOT NULL, EMAIL text NOT NULL, PASSWORD text NOT NULL, PHONE integer NOT NULL UNIQUE, COUNTRY text NOT NULL)')
                            cur.execute('CREATE TABLE IF NOT EXISTS RESIDENCE(EMAIL text NOT NULL, ADDRESS text NOT NULL, LANDMARK text NOT NULL, PINCODE integer NOT NULL)')                            
                            cur.execute("SELECT * FROM DETAIL WHERE email=?", (email, ))
                            row=cur.fetchone()
                
                            if row!=None:
                                engine = pyttsx3.init()
                                engine.say("EMAIL  ALREADY EXISTS")
                                engine.runAndWait()                                         
                                messagebox.showwarning("ALERT", "E-MAIL  ALREADY EXISTS")
                                return False

                            else:
                                pass
                             
                            cur.execute("SELECT * FROM DETAIL WHERE phone=?", (phone, ))
                            row=cur.fetchone()

                            if row!=None:
                                engine = pyttsx3.init()
                                engine.say("PHONE NUMBER ALREADY EXISTS")
                                engine.runAndWait()                                         
                                messagebox.showwarning("ALERT", "PHONE NUMBER  ALREADY EXISTS")
                                return False
                                
                            else:                    
                                cur.execute('INSERT INTO DETAIL(FIRSTNAME, LASTNAME, GENDER, EMAIL, PASSWORD, PHONE, COUNTRY) VALUES(?, ?, ?, ?, ?, ?, ?)',(first, last, gender, email, password, phone, country))
                                con.commit()
                                con.close()
                                
                                engine = pyttsx3.init()
                                engine.say("SUCCESSFULLY REGISTERED")
                                engine.runAndWait()                   
                                messagebox.showinfo('INFORMATION', 'SUCCESSFULLY REGISTERED')
                                   
##                        EMAIL_info=v_EMAIL.get()
##                        PASSWORD_info= v_PASSWORD.get()
##
##                        file=open(EMAIL_info,  "w")
##                        file.write(EMAIL_info + "\n")
##                        file.write(PASSWORD_info)
##                        file.close()
                                number = phone


                                a = phonenumbers.parse(number, "CH")
                                print(geocoder.description_for_number(a, "en"))

                                b = phonenumbers.parse(number, "RO")
                                print(carrier.name_for_number(b, "en"))

                                c = phonenumbers.parse(number, None)
                                print(timezone.time_zones_for_number(c))

                                d =  phonenumbers.parse(number, None)
                                print(phonenumbers.is_valid_number(d))

                                e =  phonenumbers.parse(number, None)
                                print(phonenumbers.is_possible_number(e))
                                print(phone)

                                FIRSTentry.delete(0, END)
                                LASTentry.delete(0, END)
                                EMAILentry.delete(0, END)
                                PASSWORDentry.delete(0, END)                
                                PHONEentry.delete(0, END)
                                root.destroy()

##                                time.sleep(0.0)
##                                webbrowser.open_new_tab("HOME.html")            

                        except Exception as es:
                           engine = pyttsx3.init()
                           engine.say("ERROR")
                           engine.runAndWait()                    
                           messagebox.showerror("ERROR" ,f"{str(es)}")
               

   
#BUTTONS

btn_Register = Button(root, text="REGISTER NOW", fg="white", bg="orange", font="ar 9 bold", command = validateallfields, cursor="hand2").place(x=398, y=270)

def callbackscreen():
    root.destroy
    os.system("python p.py")

Button(text="BACK", fg="white", bg="orange", font="ar 9 bold", command = callbackscreen, cursor="hand2").place(x=5, y=270)

               


root.mainloop()





 
