import time
import csv
class data_base():
    def __init__(self):
        self.state = False

    def guardar(self, data):
        if self.state == True:
            data.append(time.asctime())
            with open("melumat.csv", "a") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(data)

    def start(self):
        self.state = True
        print('Başlanğıc csv fayl saxlanılır')

    def stop(self):
        self.state = False
        print('Dayanma csv fayl saxlanılır')
