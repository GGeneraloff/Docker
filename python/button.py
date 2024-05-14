from tkinter import *


class Btn:
    def __init__(self,parent,text,command,state):
        self.parent=parent
        self.text=text
        self.command=command
        self.state=state
    
    def btn(self):
        button=Button(self.parent,text=self.text,command=self.command,state=self.state)
        button.grid(column=0,row=0)
        
       