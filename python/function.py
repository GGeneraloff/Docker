import os

class Func:
    ip=[]
    udp=[]
    tcp=[]

    def configread(self):
        self.ip=[]
        self.udp=[]
        self.tcp=[]
        file_path = os.path.realpath('Config.txt')

        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                message = file.readlines()

        i = 0
        while i < len(message) - 1:
            if '# PLC' in message[i]:
                plc=[]         
                for j in range (4):
                    i+=1 
                    plc.append(message[i])     
                self.ip.append(plc)
                i+=1
            else:
                break

        # Удаление специальных символов типа \n из списков
        for i in range (len(self.ip)):
            for j in range (len(self.ip[0])):
                self.ip[i][j]=self.ip[i][j].strip()
        
        for i in range (len(self.ip)):
            ip_port=self.ip[i][0].split(" ")
            self.ip[i][0]=ip_port[0]
            upd=ip_port[1].split(':')
            self.udp.append(upd[1])
            tcp=ip_port[2].split(':')
            self.tcp.append(tcp[1])
