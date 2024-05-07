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
        self.window.geometry("500x300")
        # check = (self.window.register(self.is_valid), "%P")
        num=1
        self.plc_visu(num)


        btn_first_satrt= Button(self.window,width=15, text="Первый запуск", command=self.first_start)
        btn_first_satrt.grid(column=1,row=0,sticky=tk.NS)
        # проверить скачан ли докер, создать дериктории(если их нет),загружаем докер контейнера, переход к определению ip

        btn_test= Button(self.window,width=15, text="Test",command=self.remove)
        btn_test.grid(column=2,row=0)

        btn_start= Button(self.window,width=15, text="Запуск", command=self.start)
        btn_start.grid(column=3,row=0)

        
 
        
        # error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
        # error_label.grid(column=1,row=5)

        
        # проверка на наличие докера и тд, переход к определению ip



        self.window.mainloop()

    def first_start(self):
        first_start = os.path.expanduser('~/Docker/first_start.sh')
        st = os.stat(first_start)
        os.chmod(first_start, st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call([first_start])
        messagebox.showinfo("Первый запуск","Первый запуск завершен")

    def start(self):
        start = os.path.expanduser( '~/Docker/start.sh' )
        st = os.stat(start)
        os.chmod(start, st.st_mode | stat.S_IEXEC)# даем права
        subprocess.run([start,self.ip_1.get(),self.ip_2.get(),self.ip_3.get(),self.ip_4.get()])
        # messagebox.showinfo("Настройка окружения","Настройка выполнена")

    def remove(self):
        st = os.stat('/home/george/Docker/test.sh')
        os.chmod('/home/george/Docker/test.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/test.sh'])

    def plc_visu(self,num):
        for i in range(num):
            n=i
            self.ip_1=tk.StringVar(value='')
            self.ip_2=tk.StringVar(value='')
            self.ip_3=tk.StringVar(value='')
            self.ip_4=tk.StringVar(value='')

            self.port=tk.StringVar(value='0000')
        
            ip_1_label=ttk.Label(text="IP 1")
            ip_1_label.grid(column=n,row=1,padx=5) 
            ip_2_label=ttk.Label(text="IP 2")
            ip_2_label.grid(column=n,row=2,padx=5)
            ip_3_label=ttk.Label(text="IP 3")
            ip_3_label.grid(column=n,row=3,padx=5)
            ip_4_label=ttk.Label(text="IP 4")
            ip_4_label.grid(column=n,row=4,padx=5)
            port_label=ttk.Label(text="Port")
            port_label.grid(column=n+2,row=1)
            
            ip_1_entry=ttk.Entry(textvariable=self.ip_1, width=14)
            ip_1_entry.grid(column=n+1,row=1,pady=15) 
            ip_2_entry=ttk.Entry(textvariable=self.ip_2, width=14)
            ip_2_entry.grid(column=n+1,row=2,pady=15)
            ip_3_entry=ttk.Entry(textvariable=self.ip_3, width=14)
            ip_3_entry.grid(column=n+1,row=3,pady=15)
            ip_4_entry=ttk.Entry(textvariable=self.ip_4, width=14)
            ip_4_entry.grid(column=n+1,row=4,pady=15)
    
    # def is_valid(self,newval):
    #     result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    #     if not result and len(newval) <= 12:
    #         errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    #     else:
    #         errmsg.set("")
    #     return result

