# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:29:45 2021
+---------------------------------------------------------------------+
|     @author     :   AKASH KUMAR                                     |
|     @college    :   MIT Institute Moradabad                         |
|     @branch     :   Computer Science & Information Technology       |
|     @work       :   Software Devlope & Machine Learning             |
|     @github     :   https://github.com/Akash671                     |
+---------------------------------------------------------------------+
"""

#-------------------------------------------------------
from tkinter import*
import tkinter as tk
#-----------------------------------------------------

#-----------------------------------------------------
root=tk.Tk()
root.geometry("400x390")
root.configure(bg="magenta")
root.title("Face Mask Detector Login")

Label(root,text="username",font=('Helvetica',10,'bold'),bg='SeaGreen2',fg='blue',bd=1, relief="solid",width=20,height=2).place(x=20,y=40)
Label(root,text="password",font=('Helvetica',10,'bold'),bg='SeaGreen2',fg='blue',bd=1, relief="solid",width=20,height=2).place(x=20,y=100)

user_name = StringVar()  # User name variable
password = StringVar()  # Password variable
t1=Entry(root,textvariable=user_name,width=27, bg="cyan2",bd=2)
t1.place(x=210, y=40,height=35)
t2=Entry(root,textvariable=password,show='*',width=27, bg="cyan2",bd=2)
t2.place(x=210, y=100,height=35)

def login():
     username=user_name.get()
     Password=password.get()
     
     try:
       if username=="Akash671" and Password=="Akash@1996":
           import tkinter as tk
           wind=tk.Tk()
           wind.geometry("400x295")
           wind.configure(bg="purple")
           wind.title("Face Mask Dedector")
           
           def Detector():
               import detect_mask_video
           Button(wind,text="Start Detector",font=('Helvetica',9,'bold'),bg="gold",fg='blue',width=25,height=8,bd=5,command=Detector).place(x=6, y=5)
           
           def Help():
               import HELP
           Button(wind,text="Help",font=('Helvetica',9,'bold'),bg="cyan2",fg='blue',width=25,height=8,bd=5,command=Help).place(x=206, y=5)
           
           def ABOUT_APP():
               import Devloper
           Button(wind,text="About",font=('Helvetica',9,'bold'),bg="SeaGreen2",fg='blue',width=25,height=8,bd=5,command=ABOUT_APP).place(x=6, y=150)
           
           def EXIT():
               wind.destroy()
           Button(wind,text="Exit",font=('Helvetica',9,'bold'),bg="magenta",fg='blue',width=25,height=8,bd=5,command=EXIT).place(x=206, y=150)
           
           wind.resizable(0,0)
           wind.mainloop()
     except:
         print("rrr")
Button(root,text="Login",font=('Helvetica',9,'bold'),bg="SeaGreen2",fg='blue',width=15,height=2,bd=4,command=login).place(x=130,y=180)

root.resizable(0,0)
root.mainloop()


#---------------------Thank You----------------------------------------
#-------------------- Akash Kumar -------------------------------------
