# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:27:31 2021

@author: AKASH
"""


import tkinter as tk
from tkinter import*

dev=tk.Tk()
dev.geometry("400x420")
dev.configure(bg="violet")
dev.title("About Application")


T=Text(dev,bg='black',fg='blue',height=50,width=52)
Fact='''
+-------------------+
+ About application +
+-------------------+

+-----------------------------------------------+
.Hello and welcome in mask detector application .
.this application is a based on Machine Learning.
.and Artificial Inteligence and this application.
.is devloped by using Tensorflow framework which.
.is a Machine Learning library in python and it .
.is a advanced library based on Machine Learning.
.and devloped by Google and Tensorflow is free  .
.and open source software library and it is use .
.for both research and production at Google and .
.website of tensorflow is:"https://tensorflow.org".
.                                               .
+-----------------------------------------------+

+--------------------+
+  About devloper..  +
+--------------------+

+-----------------------------------------------+
.mask detector software application is devloped .
.by student of Moradabad Institute Of Technology.
.of computer science & engineering department.  .
.devloper team is :-                            .
.                                               .
.#1) Abhay Pratap Singh (Web Devloper)          .
.#2) Achal Gupta (Graphics Designer)            .
.#3) Akash Jauhari (Python Devloper)            .
.#4) Akash Kumar (ML Devloper)                  .
.                                               .
.this application is devloped by under guidance .
.of Anurag Malik                                .
.(assistant professor of research and software  .
.devlopement of  cse department in moradabad    .
.institute of technology).                      .
+-----------------------------------------------+
About source code...
+-----------------------------------------------+
.source code of mask detector application is at .
."https://github.com/Akash671/ML-Project"       .
+-----------------------------------------------+

+-------------+
+ About issue +
+-------------+

+-------------------------------+
+ for any issue you can male at:+
+ "1810107@mitmoradabad.edu.in" +
+-------------------------------+
Thank you.
'''


T.pack()
T.insert(tk.END,Fact)

dev.resizable(0,0)
dev.mainloop()