from tkinter import *
from tkinter import ttk
import tkinter as tk

class Plc_visu:
    def __init__(self,parent,ip_1,ip_2,ip_3,ip_4,udp,tcp,n):
        self.ip_1=tk.StringVar()
        self.ip_1.set(ip_1)
        self.ip_2=tk.StringVar()
        self.ip_2.set(ip_2)
        self.ip_3=tk.StringVar()
        self.ip_3.set(ip_3)
        self.ip_4=tk.StringVar()
        self.ip_4.set(ip_4)
        self.udp=tk.StringVar()
        self.udp.set(udp)
        self.tcp=tk.StringVar()
        self.tcp.set(tcp)
        self.n=n
        self.parent=parent

    def show_visu(self):
        n=self.n*5

        ip_1_label=ttk.Label(self.parent,text="IP 1")
        ip_1_label.grid(column=n,row=1,padx=5) 
        ip_2_label=ttk.Label(self.parent,text="IP 2")
        ip_2_label.grid(column=n,row=2,padx=5)
        ip_3_label=ttk.Label(self.parent,text="IP 3")
        ip_3_label.grid(column=n,row=3,padx=5)
        ip_4_label=ttk.Label(self.parent,text="IP 4")
        ip_4_label.grid(column=n,row=4,padx=5)
        udp_label=ttk.Label(self.parent,text="UDP")
        udp_label.grid(column=n+2,row=1,padx=10)
        tcp_label=ttk.Label(self.parent,text="TCP")
        tcp_label.grid(column=n+2,row=2,padx=10)

        ip_1_entry=ttk.Entry(self.parent,textvariable=self.ip_1, width=14)
        ip_1_entry.grid(column=n+1,row=1,pady=15) 
        ip_2_entry=ttk.Entry(self.parent,textvariable=self.ip_2, width=14)
        ip_2_entry.grid(column=n+1,row=2,pady=15)
        ip_3_entry=ttk.Entry(self.parent,textvariable=self.ip_3, width=14)
        ip_3_entry.grid(column=n+1,row=3,pady=15)
        ip_4_entry=ttk.Entry(self.parent,textvariable=self.ip_4, width=14)
        ip_4_entry.grid(column=n+1,row=4,pady=15)
        udp_entry=ttk.Entry(self.parent,textvariable=self.udp, width=4)
        udp_entry.grid(column=n+3,row=1, padx=10)
        tcp_entry=ttk.Entry(self.parent,textvariable=self.tcp, width=4)
        tcp_entry.grid(column=n+3,row=2, padx=10)

        separator = ttk.Separator(self.parent, orient='vertical')
        separator.grid(column=n+4,row=1,rowspan=4,sticky='ns')