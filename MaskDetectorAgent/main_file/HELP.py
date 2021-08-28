# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:19:55 2021

@author: AKASH
"""


def AI():
    import win32com.client as wincl
    import time
    speak = wincl.Dispatch("SAPI.SpVoice")
    text="Welcome in mask detector agent"
    speak.Speak(text)
    
    text="Follow these instruction to start mask detector agent"
    speak.Speak(text)
    
    text="First Instruction"
    speak.Speak(text)
    text="click on start detector buttton to start your detector agent"
    speak.Speak(text)
    text="Secound Instruction"
    speak.Speak(text)
    text="wait few secound and after you few secound a detector window open"
    speak.Speak(text)
    text="now you can see you detector agent start own working"
    speak.Speak(text)
   
    #speak.Speak("After sometime you will see your your covid 19 test report on corona test screen")
    speak.Speak("Thanks For Using ASSISTANT")
AI()