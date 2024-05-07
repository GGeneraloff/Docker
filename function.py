import os



class Func:
    plc=[]
    port=[]
    def configread(self):
        file_path = os.path.realpath('config.txt')
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                message = file.readlines()

        i = 0
        while i < len(message) - 1:
            if message[i] == '# PLC1\n':
                i += 1
                while message[i] != '# PLC2\n':
                    self.folder.append(message[i])
                    i += 1
            elif message[i] == 'Папка, куда будут выложены прошивки:\n':
                i += 1
                while message[i] != 'Папка, куда будут перекладываться старые прошивки с сервера:\n':
                    self.folder.append(message[i])
                    i += 1
            
            elif message[i] == 'Шаблон текста для формирования отчетного сообщения:\n':
                i += 1
                self.txt.append(message[i])
            else:
                break

        # Удаление специальных символов типа \n из списков

        for x in range(len(self.folder)):
            self.folder[x] = self.folder[x].strip()
        for x in range(len(self.expansion)):
            self.expansion[x] = self.expansion[x].strip()
        for x in range(len(self.not_used_folder)):
            self.not_used_folder[x] = self.not_used_folder[x].strip()
        for x in range(len(self.shablon)):
            self.shablon[x] = self.shablon[x].strip()
        for x in range(len(self.shablon_joint)):
            self.shablon_joint[x] = self.shablon_joint[x].strip()

