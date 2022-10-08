import cgi
from tkinter import *
from PIL import ImageTk
from PIL import Image, ImageTk
root = Tk()
root.title("A9 STORE")
root.geometry("500x300+425+200")
root.config(bg="black")
root.resizable(False,False)
bg=ImageTk.PhotoImage(file='Images/A9.png')
bg_label=Label(root, image=bg, relief=FLAT)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
import os

#FUNCTIONS
def callnewscreen():
    root.destroy()
    os.system("python p2.py")

def callnewscreen2():
    root.destroy()
    os.system("python p3.py")


#HEADING

HEAD=Label(root,text="WELCOME TO A9 STORE", font="ar 20 bold", bg="orange", fg="white", bd=0)
HEAD.place(x=75, y=5)

#RUN BY

NAME=Label(root,text="POWERED BY A9", font="ar 10 bold", bg="orange", fg="black", bd=0)
NAME.place(x=360, y=250)

POST=Label(root,text="(DESIGNER)", font="ar 9 bold", bg="orange", fg="black", bd=0)
POST.place(x=385, y=270)

#ABOUT

VILLA=Label(root,text="AN ONLINE SHOPPING VILLA ",font="ar 9 bold",bg="orange",fg="black", bd=0)
VILLA.place(x=5, y=80)

#COMPARTMENTS

label5_4=Label(root,text=" || COMPRISES_OF ||", font="ar 9 bold", bg="orange", fg="black", bd=0)
label5_4.place(x=33, y=120)

SHOE=Label(root,text=">>> SHOES", font="ar 9 bold", bg="orange", fg="black", bd=0)
SHOE.place(x=58, y=158)

SANDAL=Label(root,text=">>> SANDALS", font="ar 9 bold", bg="orange", fg="black", bd=0)
SANDAL.place(x=81, y=180)

ACCESSORIES=Label(root,text=">>> ACCESSORIES", font="ar 9 bold", bg="orange", fg="black", bd=0)
ACCESSORIES.place(x=104, y=202)

#BUTTONS
B1 = Button(root, text="LOGIN", fg="white", bg="orange", font="ar 8 bold", command = callnewscreen2, cursor="hand2").place(x=375, y=115)
B2 = Button(root, text="REGISTER", fg="white", bg="orange", font="ar 8 bold", command=callnewscreen, cursor="hand2").place(x=400, y=145)


root.mainloop()

