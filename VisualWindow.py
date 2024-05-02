import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import subprocess #для выполнения скриплов 
import os
import stat


# from function import Func


class Visuality:

    def workwindow(self):
        self.window = Tk()
        self.window.title("Настройка эмулятора")
        self.window.geometry("430x300")

        btn_first_satrt= Button(self.window,width=15, text="Первый запуск", command=self.first_start)
        btn_first_satrt.grid(column=3,row=0)
        # проверить скачан ли докер, создать дериктории(если их нет),загружаем докер контейнера, переход к определению ip

        btn_test= Button(self.window,width=15, text="Test",command=self.remove)
        btn_test.grid(column=3,row=2)

        btn_satrt= Button(self.window,width=15, text="Запуск")
        btn_satrt.grid(column=3,row=5)
        
        ip_1=tk.StringVar()
        ip_2=tk.StringVar()
        ip_3=tk.StringVar()
        ip_4=tk.StringVar()
        
        ip_1_label=ttk.Label(text="IP 1")
        ip_1_label.grid(column=0,row=1,padx=5) 
        ip_2_label=ttk.Label(text="IP 2")
        ip_2_label.grid(column=0,row=2,padx=5)
        ip_3_label=ttk.Label(text="IP 3")
        ip_3_label.grid(column=0,row=3,padx=5)
        ip_4_label=ttk.Label(text="IP 4")
        ip_4_label.grid(column=0,row=4,padx=5)
        
        ip_1_entry=ttk.Entry(textvariable=ip_1, width=30)
        ip_1_entry.grid(column=1,row=1,pady=15) 
        ip_2_entry=ttk.Entry(textvariable=ip_2, width=30)
        ip_2_entry.grid(column=1,row=2,pady=15)
        ip_3_entry=ttk.Entry(textvariable=ip_3, width=30)
        ip_3_entry.grid(column=1,row=3,pady=15)
        ip_4_entry=ttk.Entry(textvariable=ip_4, width=30)
        ip_4_entry.grid(column=1,row=4,pady=15)

        
        # проверка на наличие докера и тд, переход к определению ip



        self.window.mainloop()

    def first_start(self):
        st = os.stat('/home/george/Docker/first_start.sh')
        os.chmod('/home/george/Docker/first_start.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/first_start.sh'])
        messagebox.showinfo("Первый запуск","Первый запуск завершен")



    def remove(self):
        st = os.stat('/home/george/Docker/test.sh')
        os.chmod('/home/george/Docker/test.sh', st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call(['/home/george/Docker/test.sh'])
  

