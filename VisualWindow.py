import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import subprocess #для выполнения скриплов 
import os
import stat
import re
from plc_visu import Plc_visu
from function import Func

class Visuality:
    

    def workwindow(self):
        self.window = Tk()
        self.window.title("Настройка эмулятора")
        self.window.geometry("500x300")

        f=Func()
        f.configread()
        print(f.ip)

        # check = (self.window.register(self.is_valid), "%P")
        
        self.ip_1=tk.StringVar()
        self.ip_2=tk.StringVar()
        self.ip_3=tk.StringVar()
        self.ip_4=tk.StringVar()

        self.port=tk.StringVar()

        self.ip=f.ip
        
        plc_list=[]
        num=1
        for i in range (len(self.ip)):
            self.ip_1.set(self.ip[i][0])
            self.ip_2.set(self.ip[i][1])
            self.ip_3.set(self.ip[i][2])
            self.ip_4.set(self.ip[i][3])
            plc=Plc_visu(self.ip_1,self.ip_2,self.ip_3,self.ip_4,self.port,i)
            plc_list.append(plc)
        for i in range (num):
            plc_list[i].show_visu()
        # plc_2=Plc_visu(self.ip_1,self.ip_2,self.ip_3,self.ip_4,self.port,1)
        # plc_2.show_visu()


        btn_first_satrt= Button(self.window,width=15, text="Первый запуск", command=self.first_start)
        btn_first_satrt.grid(column=1,row=0)
        # проверить скачан ли докер, создать дериктории(если их нет),загружаем докер контейнера, переход к определению ip

        btn_test= Button(self.window,width=15, text="Test",command=self.remove)
        btn_test.grid(column=2,row=0,columnspan=3)

        btn_start= Button(self.window,width=15, text="Запуск", command=self.start)
        btn_start.grid(column=5,row=0,columnspan=2)

        
 
        
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
    
    # def is_valid(self,newval):
    #     result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    #     if not result and len(newval) <= 12:
    #         errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    #     else:
    #         errmsg.set("")
    #     return result

