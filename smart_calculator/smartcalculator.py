#about @developer
"""
Developer : @akash
Associated with Moradabad Institute Of Technology(MIT)
"""


#---------------------------------
from tkinter import *
import tkinter as tk
import time 
#—-——--—--—-¼—--—------
wind = tk.Tk()
wind.geometry('400x240')
wind.configure(background="pink") 
wind.title("AKASH")
#-------------------------------------
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=125).place(x=15,y=1740)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=2,height=50).place(x=175,y=1280)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=2,height=50).place(x=355,y=1280)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=2,height=50).place(x=535,y=1280)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=2,height=50).place(x=715,y=1280)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=2,height=50).place(x=895,y=1280)
Label(wind, text="output", font=('Helvetica', 2, 'bold'),
      bg="SeaGreen2", relief="solid", 
      width=150).place(x=15,y=0)
Label(wind, text="output", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=160)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'), bg="violet", relief="solid", width=150).place(x=15,y=1280)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=1040)         
Label(wind, text="akash", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=1520)
Label(wind, text="akash", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=740) 
Label(wind, text="akash", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=490) 
Label(wind, text="akash", font=('Helvetica', 1, 'bold'),
      bg="violet", relief="solid", width=345).place(x=15,y=327)         
Label(wind, text="akash", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=150).place(x=15,y=1940)     
#Label(wind, text="", font=('Helvetica', 2, 'bold'),bg="SeaGreen1", relief="solid", width=1, height=139).place(x=0,y=0)
Label(wind, text="", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=2, height=15).place(x=730,y=1302)
Label(wind, text="", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=2, height=40).place(x=740,y=710)
Label(wind, text="", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=2, height=100).place(x=430,y=110) 
Label(wind, text="", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=1, height=139).place(x=1060,y=0) 
Label(wind, text="", font=('Helvetica', 2, 'bold'),
      bg="violet", relief="solid", width=1, height=139).place(x=0,y=0) 
Label(wind, text="Input 1", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=12,height=2).place(x=10, y=180)
Label(wind, text="Input 2", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=12,height=2).place(x=10, y=340)
wind.configure(background="violet")  
#-------------------------------------
a=StringVar()
#sc=StringVar()
b=StringVar()
#var = tk.StringVar()
var= tk.StringVar()
t=Entry(wind, width=38, bg="violet",bd=18)

t.place(x=10, y=20,height=150)
t1=Entry(wind,text=var, textvariable=a, width=22,bg="cyan",bd=12)
t1.place(x=445, y=180,height=150)
t2=Entry(wind, textvariable=b, width=22,bg="cyan",bd=12) 
t2.place(x=445, y=340,height=150)
#------------------++++--------------- 
def model():
    try:
     x = float(a.get())
     y = float(b.get())
     z = x + y
    except:
          z='Invalid Input'
    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)

Button(wind, text="+", font=('Helvetica', 8, 'bold'), bg='SeaGreen2',fg="blue", 
       width=11, height=3,bd=10, command=model).place(x=10, y=514)
#-------------------------------------
def model1():
    try:
     x = float(a.get())
     y = float(b.get())
     z = x - y
    except:
          z='Invalid Input'
    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=40)

Button(wind, text="-",  font=('Helvetica', 8, 'bold'),bg="SeaGreen2" ,fg="blue", 
       width=6,height=3,bd=10, command=model1).place(x=450, y=514)
def mod():
    try:
     x = int(a.get())
     y = int(b.get())
     z = x%y
    except:
          z='Invalid Input'
    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=40)

Button(wind, text="%",  font=('Helvetica', 8, 'bold'),bg="SeaGreen2" ,fg="blue", 
       width=6,height=3,bd=10, command=mod).place(x=760, y=514)
#-------------------------------------
def model2():
    try:
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     z = x * y
    except:
          z='Invalid Input'

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=40)
#------------------++++--------------- 
Button(wind, text="*",  font=('Helvetica', 8, 'bold'),bg='SeaGreen2',fg="blue",
       width=11,height=4,bd=10, command=model2).place(x=10, y=760) 
#-------------------------------------       
def model3():
    try:
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     if y == 0:
        try:
            z = x / y
        except:
            if x==0:
               z = "infinite"
            else:
                 z = "can't divide by zero" 
     else:
        z = x / y
    except:
          z='Invalid Input'

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125,y=40)
#------------------++++--------------- 
Button(wind, text="/",  font=('Helvetica', 8, 'bold'),bg='SeaGreen2',fg="blue",
       width=6,height=4,bd=10, command=model3).place(x=450, y=760)
#-------------------------------------

def Exit():
    exit(0)
#-------------------------------------
def fact():
    try:
      x = int(a.get())
      z=1
      for i in range(1,x+1):
        z=z*i
    except:
        z="Invalid Input"
    Label(wind, text=str(z), font=('Helvetica', 4, 'bold'),
          bg="violet",bd=0.00002,width=60,height=1).place(x=100, y=90) 
#------------------++++--------------- 
Button(wind, text="n!",  font=('Helvetica', 8, 'bold'),bg='SeaGreen2',fg="blue",
       width=6,height=3,bd=10, command=fact).place(x=450,y=1055) 
#-------------------------------------
def sq():
    try:
    # testing datacreate
     x = float(a.get())
     y = float(b.get())
     z = x**y
    except:
          z='Invalid Input'

    Label(wind, text=str(z), font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=40)
#------------------++++--------------- 
Button(wind, text="x^y",  font=('Helvetica', 8, 'bold'),bg='SeaGreen2',fg="blue",
       width=7,height=3,bd=10, command=sq).place(x=749,y=1055) 
#------------------++++--------------- 
Button(wind, text="OFF",  font=('Helvetica', 8, 'bold'),bg='red',fg="blue",
       width=7,height=3,bd=8, command=Exit).place(x=750,y=1297) 
#-------------------------------------
def clear():
    Label(wind, text=" "*30, font=('Helvetica', 14, 'bold'),
          bg="violet",bd=0.0003,width=24,height=1).place(x=35, y=40)
 #-------------------------------------
def clear1():
    for i in range(10):
      Label(wind, text=" ", font=('Helvetica', 10, 'bold'),
          bg="violet",bd=0.0003,width=24,height=1).place(x=35, y=40)     
#------------------++++---------------      
Button(wind, text="Ac", font=('Helvetica', 8, 'bold'), bg='SeaGreen2',fg="blue",width=11,height=3,bd=9,command=clear).place(x=10, y=1060)

label = Button(wind,width=10,height =3,font=("Courier", 8, 'bold'), bg="SeaGreen2", fg="blue", bd =12)
label.place(x=10, y=1295)
def digitalclock():
   text_input = time.strftime("%H:%M:%S %p")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()
#-------------------------------------   
"""
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

Fact=
Hello and welcome! 
Developer : Akash kumar\nInstitute : MIT\nArea.     : Computer Science\nWork as   : Software Engineer\ngithub    : www.github.com/Akash671\nemail.    : akashsainimit@gmail.com\nwebsite.  : www.medium.com/@akashsaininasa
 
T1 = Text(root, height =10, width = 35,bg="black", fg="magenta") 
# Create label 

l1= Label(root, text = "About Application", bg="black" ,fg="blue") 

l1.config(font =("Courier", 10)) 

  

Fact1= 
I'm Akash Kumar(Akash671),i am a competitive programmer and machine learning engineer as a student with strong background in mathematics, statistics, and problem solving.i am doing bachelor of technology(B.Tech) in computer science & engineering(cse) at Moradabad Institute Of Technology Moradabad, Uttar Pradesh India, with majors in technology and bachelor in science supported by A.P.J Abdul Kalam Technical University(AKTU) with majors in engineering and operational research.
Hi, this application is devloped by using python language which is a most powerful language and application is devloped on android platform and pydroid3 tool is use to development this application.

  
# Create button for next text. 

#b1 = Button(root, text = "Next", ) 

  
# Create an Exit button. 

b2 = Button(root, text = "Exit", bg="magenta", fg="blue", command = root.destroy)  

  
l.pack() 
T.pack() 
l1.pack()
T1.pack()

#b1.pack() 
b2.pack() 

  
# Insert The Fact. 
T.insert(tk.END, Fact) 
T1.insert(tk.END, Fact1) 

  
tk.mainloop() """  
def Devloper():
         import tkinter as tk
         n=tk.Tk()
         n.geometry("900x1000")
         n.configure(bg="magenta")
         n.title("information about developer")
         Button(n,text="@name", width=8,bd=10, height=2,bg="SeaGreen2").place(x=110,y=50)
         Button(n,text="Akash kumar", width=8,bd=10, height=2,bg="SeaGreen2").place(x=490,y=50)
         Button(n,text="@institute", width=8,bd=10, height=2,bg="SeaGreen2").place(x=110,y=250)
         Button(n,text="MIT", width=8,bd=10, height=2,bg="SeaGreen2").place(x=490,y=250)
         Button(n,text="@work as", width=8,bd=10, height=2,bg="SeaGreen2").place(x=110,y=450)
         Button(n,text="software engr.", width=8,bd=10, height=2,bg="SeaGreen2").place(x=490,y=450)
         Button(n,text="@github", width=8,bd=10, height=2,bg="SeaGreen2").place(x=110,y=650)
         def Akash671():
             import webbrowser as we
             url="https://github.com/Akash671"
             we.open(url)
         Button(n,text="Akash671", width=8,bd=10, height=2,bg="SeaGreen2",command=Akash671).place(x=490,y=650)
#-------------------------------------
         def destroy():
            n.destroy()
         Button(n, text="Exit", bg='red',
       width=9,bd=10,command=destroy).place(x=305, y=850)
         n.mainloop()
         
def akash():
    import Akash
#-------------------------------------
Button(wind, text="I am", font=('Helvetica', 5, 'bold'), bg='SeaGreen2',fg="blue",width=2, height=4,bd=9, command=akash).place(x=910, y=1540)

def z(event):
    button_arg = event.widget['text']
    var_entry.insert(0,'1')
Button(wind, text="0",textvariable=1,font=('Helvetica', 7, 'bold'), bg='violet',fg="blue",width=2,height=3,bd=8).place(x=10, y=1540)
#-------------------------------------
"""
#button0= tk.Button(win,text = '1')
B0=Button(wind, text="0", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8,command=z)
B0.bind("<Button-1>",z)
B0.place(x=10, y=1540)
"""
def handle_button0(event):
    button_arg = event.widget['text']
    t1.insert(0,'0')
    #tk.insert(0,'0')
button0 = tk.Button(wind, text="0", font=('Helvetica', 7, 'bold'), bg="SeaGreen2" ,fg="blue",width=2,height=3,bd=8)
button0.bind("<Button-1>", handle_button0)
button0.place(x=10,y=1540)

#-------------------------------------1 
def one(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'1')

B1=tk.Button(wind, text="1", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B1.bind("<Button-1>", one)
B1.place(x=10, y=1750)
#-------------------------------------

def two(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'2')
    
B2=tk.Button(wind, text="2", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B2.bind("<Button-1>",two)
B2.place(x=190, y=1540)
#-------------------------------------

def three(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'3')
    
    
B3=tk.Button(wind, text="3", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B3.bind("<Button-1>", three)
B3.place(x=190, y=1750)
#-------------------------------------

def four(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'4')
    
B4=tk.Button(wind, text="4", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B4.bind("<Button-1>",four)
B4.place(x=370, y=1540)
#-------------------------------------

def five(event1):
    button_arg = event1.widget['text']
    t1.insert(0,"5")
   
     
B5=tk.Button(wind, text="5", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B5.bind("<Button-1>",five)
B5.place(x=370, y=1750)
#-------------------------------------

def six(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'6')
    
B6=Button(wind, text="6", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B6.bind("<Button-1>",six)
B6.place(x=550, y=1540)
#-------------------------------------

def seven(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'7')
    
B7=Button(wind, text="7", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B7.bind("<Button-1>",seven)
B7.place(x=550, y=1750)
#-------------------------------------

def eight(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'8')
 #-----------   
B8=tk.Button(wind, text="8", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B8.bind("<Button-1>",eight)
B8.place(x=730, y=1540)
#-------------------------------------

def nine(event1):
    button_arg = event1.widget['text']
    t1.insert(0,'9')
B9=tk.Button(wind, text="9", font=('Helvetica', 7, 'bold'), bg='SeaGreen2',fg="blue",width=2,height=3,bd=8)
B9.bind("<Button-1>",nine)
B9.place(x=730, y=1750)
def point(event1):
    button_arg = event1.widget['text']
    t1.insert(0,".")
BP=Button(wind, text=".", font=('Helvetica', 5, 'bold'), bg='SeaGreen2',fg="blue",width=2, height=4,bd=8)
BP.bind("<Button-1>",point)
BP.place(x=910, y=1750) 

#------------------------
def Date():
  import tkinter as tk
  import sys
  import time
  import calendar
  import random
  import datetime as dt
  class Clock(tk.Label):
    def __init__(self, parent=None, seconds=True, colon=False):
        tk.Label.__init__(self, parent)
        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%I:%M:%S %p')
        else:
            self.time     = time.strftime('%I:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)
        if colon:
            self.blink_colon()
        self.after(200, self.tick)
    def tick(self):
        if self.display_seconds:
            new_time = time.strftime('%I:%M:%S %p')
        else:
            new_time = time.strftime('%I:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)
    def blink_colon(self):
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)
  class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
  root=tk.Tk() 
  root.configure(bg="orange")
  root.wm_attributes('-fullscreen','true')
  def ex():
      root.destroy()
  Button(root,text="back",bd=8,bg="red", command=ex).place(x=420,y=600)
  clock1 = Clock(root)
  clock1.place(x=295, y=280)
  clock1.configure(width=15, bg='red',fg='white',font=("helvetica",10))
  w = Label(root, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="white", bg="Deep pink", font=("helvetica", 10))
  w.place(x=300,y=400)
  root.mainloop()
Button(wind, text="date",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue", 
       width=6,height=3,bd=8, command=Date).place(x=450,y=1297)

label =Button(wind,width=10,height =3,font=("Courier", 8, 'bold'), bg="blue", fg="white", bd =12)
label.place(x=10, y=1295)
def digitalclock():
   text_input = time.strftime("%H:%M:%S %p")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()

#—-----—---------—-----—-----—
def scientific():
    import math
    import tkinter
    root1=Tk()
    root1.geometry('1020x1800')
    root1.configure(background="SeaGreen2") 
    root1.title("scientific calculator")
    Label(root1, text="Input", font=('Helvetica', 10, 'bold'),
      bg="Deep pink", relief="solid", width=12,height=2).place(x=10, y=180)
    sc=IntVar()
    var= tk.StringVar()
    tt=Entry(root1,width=36, bg="violet",bd=18)
    tt.place(x=10, y=20,height=150)
    tt1=Entry(root1, textvariable=sc, width=20,bg="cyan",bd=12)
    tt1.place(x=445, y=180,height=150)
   # sc=DoubleVar()
    import cmath
    def Sine():
        aa=float(sc.get())
        try:
         #  a=float(sc.get())
           z=math.sin(aa)
        except:
            z='invalid input!'
        Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="sinx",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=7,height=3,bd=7,command=Sine).place(x=10, y=350)
    def cose():
         try:
            aa=float(sc.get())
            z=math.cos(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="cosx",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=7,height=3,bd=7,command=cose).place(x=330, y=350)
    def tans():
         try:
            aa=float(sc.get())
            z=math.tan(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="tanx",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=9,height=3,bd=7,command=tans).place(x=650, y=350)
    def secs():
         try:
            aa=float(sc.get())
            z=1/math.cos(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="secx",  font=('Helvetica', 8, 'bold'),bg='orange', fg="blue",
       width=7,height=3,bd=7,command=secs).place(x=10, y=600)
    def cosecs():
         try:
            aa=float(sc.get())
            z=1/math.sin(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="cosecx",  font=('Helvetica', 8, 'bold'),bg='orange' ,fg="blue",
       width=7,height=3,bd=7,command=cosecs).place(x=330, y=600)
    def cots():
         try:
            aa=float(sc.get())
            z=1/math.tan(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="cotx",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=9,height=3,bd=7,command=cots).place(x=650, y=600)
    def loge():
         try:
            aa=float(sc.get())
            z=math.log2(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="log2x",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=7,height=3,bd=7,command=loge).place(x=10, y=850)
    def log10():
         try:
            aa=float(sc.get())
            z=math.log10(aa)
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="logx",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=7,height=3,bd=7,command=log10).place(x=330, y=850)
    def exps():
         try:
            aa=int(sc.get())
            b=aa
            z=(2.7182818284590455)**b
            #z=z**a
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="e^x",  font=('Helvetica', 8, 'bold'),bg='orange',fg="blue",
       width=9,height=3,bd=7,command=exps).place(x=650, y=850)
    def PI():
         try:
            #a=float(sc.get())
            z=math.pi
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="pi",  font=('Helvetica', 8, 'bold'),bg="blue" ,fg="gold",
       width=7,height=3,bd=7,command=PI).place(x=10, y=1100)
    def eval():
         try:
           # a=float(sc.get())
            z=math.e
         except:
            z='invalid input!'
         Label(root1,text=str(z), font=('Helvetica', 10, 'bold'),bg="violet",bd=0.00002,width=24,height=1).place(x=125, y=44)
    Button(root1, text="e",  font=('Helvetica', 8, 'bold'),bg='gold', fg="blue",
       width=7,height=3,bd=7,command=eval).place(x=330, y=1100)
     #------
    def ex():
        root1.destroy()
    Button(root1, text="OFF",  font=('Helvetica', 8, 'bold'),bg='red',fg="blue",
       width=9,height=3,bd=7,command=ex).place(x=650, y=1100)
    #-----------
    def ze(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'0')
    B0=Button(root1, text="0",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B0.bind("<Button-1>",ze)
    B0.place(x=20, y=1340)
    #---------
    def one(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'1')
    B1=Button(root1, text="1",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B1.bind("<Button-1>",one)
    B1.place(x=220, y=1340) 
    
    #----------------
    def two(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'2')
    B2=Button(root1, text="2",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B2.bind("<Button-1>", two)
    B2.place(x=430, y=1340) 
    #----------
    def three(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'3') 
    B3=Button(root1, text="3",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B3.bind("<Button-1>",three)
    B3.place(x=630, y=1340) 
    #----------
    def f4(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'4')
    B4=Button(root1, text="4",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B4.bind("<Button-1>",f4)
    B4.place(x=830, y=1340) 
    #------
    def f5(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'5')
    B5=Button(root1, text="5",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B5.bind("<Button-1>",f5)
    B5.place(x=20, y=1560) 
    #---------
    def s6(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'6')
    B6=Button(root1, text="6",textvariable=1,font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B6.bind("<Button-1>",s6)
    B6.place(x=220, y=1560) 
    #-------------
    def s7(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'7')
    B7=Button(root1, text="7",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B7.bind("<Button-1>",s7)
    B7.place(x=430, y=1560) 
    #------------
    def e8(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'8')
    B8=Button(root1, text="8",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B8.bind("<Button-1>",e8)
    B8.place(x=630, y=1560) 
    #-----—-----------
    def n9(event1):
       button_arg = event1.widget['text']
       tt1.insert(0,'9')
    B9=Button(root1, text="9",font=('Helvetica', 7, 'bold'), bg='magenta',fg="blue",width=2,height=3,bd=10)
    B9.bind("<Button-1>",n9)
    B9.place(x=830, y=1560) 
    #--------------
    root1.resizable(0,0)
    root1.mainloop()

Button(wind, text="scientific\ncalculator",  font=('Helvetica', 4, 'bold'),bg='SeaGreen2',fg="blue",
       width=12,height=8,bd=10,command=scientific).place(x=760, y=760) 
#-------------------------------------
wind.resizable(0, 0)
wind.mainloop()
#-------------------------------------
