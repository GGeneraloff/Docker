import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import subprocess #для выполнения скриплов 
import os
import stat
import re

class Visuality:
    

    def workwindow(self):
        self.window = Tk()
        self.window.title("Настройка эмулятора")
        self.window.geometry("430x300")
        # check = (self.window.register(self.is_valid), "%P")
        
        ip_1=tk.StringVar(value='192.168.1.0')
        ip_2=tk.StringVar(value='192.168.2.0')
        ip_3=tk.StringVar(value='192.168.3.0')
        ip_4=tk.StringVar(value='192.168.4.0')
        
        ip_1_label=ttk.Label(text="IP 1")
        ip_1_label.grid(column=0,row=1,padx=5) 
        ip_2_label=ttk.Label(text="IP 2")
        ip_2_label.grid(column=0,row=2,padx=5)
        ip_3_label=ttk.Label(text="IP 3")
        ip_3_label.grid(column=0,row=3,padx=5)
        ip_4_label=ttk.Label(text="IP 4")
        ip_4_label.grid(column=0,row=4,padx=5)
        
        ip_1_entry=ttk.Entry(textvariable=ip_1, width=10)
        ip_1_entry.grid(column=1,row=1,pady=15) 
        ip_2_entry=ttk.Entry(textvariable=ip_2, width=10)
        ip_2_entry.grid(column=1,row=2,pady=15)
        ip_3_entry=ttk.Entry(textvariable=ip_3, width=10)
        ip_3_entry.grid(column=1,row=3,pady=15)
        ip_4_entry=ttk.Entry(textvariable=ip_4, width=10)
        ip_4_entry.grid(column=1,row=4,pady=15)


        btn_first_satrt= Button(self.window,width=15, text="Первый запуск", command=self.first_start)
        btn_first_satrt.grid(column=3,row=0,sticky=tk.NS)
        # проверить скачан ли докер, создать дериктории(если их нет),загружаем докер контейнера, переход к определению ip

        btn_test= Button(self.window,width=15, text="Test",command=self.remove)
        btn_test.grid(column=3,row=2)

        btn_satrt= Button(self.window,width=15, text="Запуск", command=self.start)
        btn_satrt.grid(column=3,row=5)

        
 
        
        # error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
        # error_label.grid(column=1,row=5)

        
        # проверка на наличие докера и тд, переход к определению ip



        self.window.mainloop()

    def first_start(self):
        st = os.stat('/home/george/Docker/first_start.sh')
        os.chmod('/home/george/Docker/first_start.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/first_start.sh'])
        messagebox.showinfo("Первый запуск","Первый запуск завершен")

    def start(self,ip_1,ip_2,ip_3,ip_4):
        st = os.stat('/home/george/Docker/start.sh')
        os.chmod('/home/george/Docker/start.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/start.sh'])
        messagebox.showinfo("","")

    def remove(self):
        st = os.stat('/home/george/Docker/test.sh')
        os.chmod('/home/george/Docker/test.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/test.sh'])
    
    # def is_valid(self,newval):
    #     result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    #     if not result and len(newval) <= 12:
    #         errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    #     else:
    #         errmsg.set("")
    #     return result

