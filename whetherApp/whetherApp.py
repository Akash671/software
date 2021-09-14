#---------------------------------
from tkinter import *
import tkinter as tk
import time 
#—-——--—--—-¼—--—------

#—-——--—--—-¼—--—------
wind = tk.Tk()
wind.geometry('400x240')
#wind.configure(background="pink") 
wind.title("AKASH")
#-----------------------
Label(wind, text="City", font=('Helvetica', 10, 'bold'),
      bg="magenta", fg="black",relief="solid", width=12,height=2).place(x=10, y=10)
Label(wind, text="Country", font=('Helvetica', 10, 'bold'),
      bg="magenta", fg="black",relief="solid", width=12,height=2).place(x=10, y=170)
wind.configure(background="white")  

a=StringVar()
#sc=StringVar()
b=StringVar()
#var = tk.StringVar()
var= tk.StringVar()
t1=Entry(wind,text=var, textvariable=a, width=22,bg="cyan",bd=12)
t1.place(x=445, y=10,height=150)
t2=Entry(wind, textvariable=b, width=22,bg="cyan",bd=12) 
t2.place(x=445, y=170,height=150)




Label(wind, text="Clouds", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=580)
Label(wind, text="Min Temp", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=740)
      
      
Label(wind, text="Max Temp", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=900)
Label(wind, text="Pressure", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=1060)
      
      
      
Label(wind, text="Humidity", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=1220)
Label(wind, text="Wind Speed", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=1380)
      
      
Label(wind, text="Sunrise", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=1540)
Label(wind, text="Sunset", font=('Helvetica', 10, 'bold'),
      bg="pink", fg="blue",relief="solid", width=12,height=2).place(x=10, y=1700)
    
      
Label(wind, text="app version 0.0.1", font=('Helvetica', 6,'bold'),
      bg="black", fg="cyan",relief="solid", width=50, height=2).place(x=10, y=1860)



#-------------
Label(wind, text="", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=17,height=2).place(x=460, y=580)  

        
Label(wind, text="", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=17,height=2).place(x=460, y=740)  
                         

Label(wind, text="", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=17,height=2).place(x=460, y=900)  

        
Label(wind, text="", font=('Helvetica', 10, 'bold'),
      bg="orange", fg="blue",relief="solid", width=17,height=2).place(x=460, y=1060)  
                              
Label(wind, text="",font=('Helvetica', 10, 'bold'),bg="orange", fg="blue", relief="solid", width=17,height=2).place(x=460, y=1220)

Label(wind, text="",font=('Helvetica', 10, 'bold'),bg="orange", fg="blue", relief="solid", width=17,height=2).place(x=460, y=1380)

Label(wind, text="",font=('Helvetica', 10, 'bold'),bg="orange", fg="blue", relief="solid", width=17,height=2).place(x=460, y=1540)

Label(wind, text="",font=('Helvetica', 10, 'bold'),bg="orange" , fg="blue", relief="solid", width=17,height=2).place(x=460, y=1700)

#Function api



import requests
#import time
 
def getWeather():
    #city = textField.get()
    city=str(a.get())
    try:
      api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    
      json_data = requests.get(api).json()
      condition = json_data['weather'][0]['main']
      temp = int(json_data['main']['temp'] - 273.15)
      min_temp = int(json_data['main']['temp_min'] - 273.15)
      max_temp = int(json_data['main']['temp_max'] - 273.15)
      pressure = json_data['main']['pressure']
      humidity = json_data['main']['humidity']
      wind = json_data['wind']['speed']
      sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
      sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
      ans=[]
      ans.append(condition)
      ans.append(str(temp)+" °C")
      ans.append(str(min_temp) + " °C")
      ans.append(str(max_temp) + " °C")
      ans.append(str(pressure)+" B.C")
      ans.append(str(humidity)+" %")
      ans.append(str(wind)+" km/h")
      ans.append(str(sunrise)+" AM")
      ans.append(str(sunset)+" PM")
      return ans
    except:
        ans=[]
        for i in range(9):
            ans.append("city not found")
        return ans

#-------------ans
def whether():
  #x = float(a.get())
  ans=getWeather()
  Label(wind, text=ans[1], font=('Helvetica', 10, 'bold'),
      bg="SeaGreen", fg="cyan",relief="solid", width=17,height=2).place(x=460, y=580)  

        
  Label(wind, text=ans[2],font=('Helvetica', 10, 'bold'),
      bg="magenta", fg="cyan",relief="solid", width=17,height=2).place(x=460, y=740)  
                         

  Label(wind, text=ans[3], font=('Helvetica', 10, 'bold'),
      bg="green", fg="cyan",relief="solid", width=17,height=2).place(x=460, y=900)  

        
  Label(wind, text=ans[4], font=('Helvetica', 10, 'bold'),
      bg="magenta", fg="cyan",relief="solid", width=17,height=2).place(x=460, y=1060)  
                              
  Label(wind, text=ans[5],font=('Helvetica', 10, 'bold'),bg="purple", fg="cyan", relief="solid", width=17,height=2).place(x=460, y=1220)

  Label(wind, text=ans[6],font=('Helvetica', 10, 'bold'),bg="magenta" , fg="cyan", relief="solid", width=17,height=2).place(x=460, y=1380)

  Label(wind, text=ans[7],font=('Helvetica', 10, 'bold'),bg="blue", fg="cyan", relief="solid", width=17,height=2).place(x=460, y=1540)

  Label(wind, text=ans[8],font=('Helvetica', 10, 'bold'),bg="magenta", fg="cyan", relief="solid", width=17,height=2).place(x=460, y=1700)


#buton
Button(wind, text="Whether", font=('Helvetica', 8, 'bold'), bg='blue',fg="yellow", 
       width=9, height=3,bd=10,command=whether).place(x=10, y=335)
       

label =Button(wind, font=('Helvetica', 8, 'bold'),bg="violet" ,fg="blue", 
       width=8,height=3,bd=10)
label.place(x=400, y=335)
def digitalclock():
   text_input = time.strftime("%H:%M:%S %p")
   label.config(text=text_input)
   label.after(200, digitalclock)
digitalclock()              

       
def quit():
    wind.destroy()
Button(wind, text="Exit",  font=('Helvetica', 8, 'bold'),bg="red" ,fg="blue", 
       width=7,height=3,bd=10,command=quit).place(x=760, y=335)
 

 
#-------------------------------------
wind.resizable(0, 0)
wind.mainloop()
#----------------------