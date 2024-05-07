from tkinter import *
from tkinter import ttk

class Plc_visu:
    def __init__(self, ip_1,ip_2,ip_3,ip_4,port,n):
        self.ip_1=ip_1
        self.ip_2=ip_2
        self.ip_3=ip_3
        self.ip_4=ip_4
        self.port=port
        self.n=n

    def show_visu(self):
        n=self.n*4

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
        port_entry=ttk.Entry(textvariable=self.port, width=4)
        port_entry.grid(column=n+3,row=1)