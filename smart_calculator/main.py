import tkinter as tk
from tkinter import*
root = tk.Tk() 

  
# specify size of window. 

root.geometry("1000x1400") 
root.configure(bg="black")
  
# Create text widget and specify size. 

T = Text(root, height = 10, width = 35,bg="black", fg="magenta") 
l = Label(root, text = "About Devloper", bg="black" ,fg="blue") 
l.config(font =("Courier", 10)) 

Fact='''
Hello and welcome! 
Developer : Akash kumar\nInstitute : MIT\nArea.     : Computer Science\nWork as   : Software Engineer\ngithub    : www.github.com/Akash671\nemail.    : akashsainimit@gmail.com\nwebsite.  : www.medium.com/@akashsaininasa
 '''
T1 = Text(root, height =10, width = 35,bg="black", fg="magenta") 
# Create label 

l1= Label(root, text = "About Application", bg="black" ,fg="blue") 

l1.config(font =("Courier", 10)) 

  

Fact1= """
Hi! i'm Akash Kumar(Akash671),i am a competitive programmer and machine learning engineer as a student with strong background in mathematics, statistics, and problem solving.i am doing bachelor of technology(B.Tech) in computer science & engineering(cse) at Moradabad Institute Of Technology Moradabad, Uttar Pradesh India, with majors in technology and bachelor in science supported by A.P.J Abdul Kalam Technical University(AKTU) with majors in engineering and operational research.
Hi, this application is devloped by using python language which is a most powerful language and application is devloped on android platform and pydroid3 tool is use to development this application."""

  
# Create button for next text. 

#b1 = Button(root, text = "Next", ) 

  
# Create an Exit button. 

b2 = Button(root, text = "Exit", bg="magenta",fg="blue",bd=8,command = root.destroy)  

  
l.pack() 
T.pack() 
l1.pack()
T1.pack()

#b1.pack() 
b2.place(x=430,y=1230)

  
# Insert The Fact. 
T.insert(tk.END, Fact) 
T1.insert(tk.END, Fact1) 

  
tk.mainloop() 
