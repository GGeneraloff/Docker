import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import subprocess #для выполнения скриплов 
import os
import stat
import re
from python.plc_visu import Plc_visu
from python.function import Func

class Visuality:    

    def workwindow(self):
        self.window = Tk()
        self.window.title("Настройка эмулятора")
        self.window.geometry("1050x300")
        f=Func()
        f.configread()
        btn_bar=tk.Frame(self.window)
        btn_bar.grid(column=0,row=0,sticky=W)
        self.plc_frame=tk.Frame(self.window)
        self.plc_frame.grid(column=0,row=2)

        # check = (self.window.register(self.is_valid), "%P")

        self.ip=f.ip
        self.port=f.port
        self.plc_list=[]

        # self.start_check()

        self.doc_text=tk.StringVar()
        self.doc_text.set('Start')

        btn_doc= Button(btn_bar,width=15, textvariable=self.doc_text, command=self.doc_fun)
        btn_doc.grid(column=0,row=0)

        if not self.start_check():
            self.btn_first_satrt= Button(btn_bar,width=15, text="Первый запуск", command=self.first_start)
            self.btn_first_satrt.grid(column=1,row=0)

        btn_test= Button(btn_bar,width=15, text="Считать",command=self.configread)
        btn_test.grid(column=2,row=0)

        for i in range (len(self.ip)):
            plc=Plc_visu(self.plc_frame,self.ip[i][0],self.ip[i][1],self.ip[i][2],self.ip[i][3],self.port[i],i)
            self.plc_list.append(plc)
        for i in range (len(self.ip)):
            self.plc_list[i].show_visu()
        
        # error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
        # error_label.grid(column=1,row=5)
        
        # проверка на наличие докера и тд, переход к определению ip

        self.window.mainloop()

    def first_start(self):
        first_start = os.path.expanduser('~/Docker/bash/first_start.sh')
        st = os.stat(first_start)
        os.chmod(first_start, st.st_mode | stat.S_IEXEC)# даем права
        subprocess.call([first_start])
        self.btn_first_satrt.destroy()
        messagebox.showinfo("Первый запуск","Первый запуск завершен")

    def doc_fun(self):
        start = os.path.expanduser( '~/Docker/bash/start.sh' )
        st_1 = os.stat(start)
        os.chmod(start, st_1.st_mode | stat.S_IEXEC)# даем права
        stop = os.path.expanduser( '~/Docker/bash/stop.sh' )
        st_2 = os.stat(stop)
        os.chmod(stop, st_2.st_mode | stat.S_IEXEC)# даем права
        try:
            print(self.plc_list[1].ip_1.get())
            
            if self.doc_text.get()=="Start":
                self.doc_text.set('Stop')
                subprocess.run([start,self.plc_list[0].ip_1.get(),self.plc_list[0].ip_2.get(),self.plc_list[0].ip_3.get(),self.plc_list[0].ip_4.get()])
            else:
                self.doc_text.set('Start')
                subprocess.run([stop])
        except:
            messagebox.showerror('')
        
            # messagebox.showinfo("Настройка окружения","Настройка выполнена")

    def start_check(self):
        work= os.path.expanduser( '~/work' )
        check=os.path.isdir(work)
        print(check)
        # subprocess.run( ["dpkg -s docker"])
        return check
        # st = os.stat(check)
        # os.chmod(check, st.st_mode | stat.S_IEXEC)# даем права
        # subprocess.call([check])

    def configread(self):
        f=Func()
        f.configread()
        self.ip=f.ip
        self.port=f.port
        for i in range (len(self.ip)):
            self.plc_list[i].ip_1.set(self.ip[i][0])
            self.plc_list[i].ip_2.set(self.ip[i][1])
            self.plc_list[i].ip_3.set(self.ip[i][2])
            self.plc_list[i].ip_4.set(self.ip[i][3])
            self.plc_list[i].port.set(self.port[i])
        

    
    # def is_valid(self,newval):
    #     result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    #     if not result and len(newval) <= 12:
    #         errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    #     else:
    #         errmsg.set("")
    #     return result