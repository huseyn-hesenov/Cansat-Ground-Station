import random
import serial
import serial.tools.list_ports

class Communication:
    baudrate = ''
    portName = ''
    dummyPlug = False
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()

    def __init__(self):
        self.baudrate = 9600
        print("Uyğun portdadır; Oxuma problemi? -hansısa klavişi bas): ")
        for port in sorted(self.ports):
            # obtener la lista de puetos: https://stackoverflow.com/a/52809180
            print(("{}".format(port)))
        self.portName = input("Serial port adı (ex: /dev/ttyUSB0): ")
        try:
            self.ser = serial.Serial(self.portName, self.baudrate)
        except serial.serialutil.SerialException:
            print("açıla bilmir : ", self.portName)
            self.dummyPlug = True
    def close(self):
        if(self.ser.isOpen()):
            self.ser.close()
        else:
            print(self.portName, " port bağlıdır")

    def getData(self):
        if(self.dummyMode == False):
            value = self.ser.readline()  # read line (single value) from the serial port
            decoded_bytes = str(value[0:len(value) - 2].decode("utf-8"))
            print(decoded_bytes)
            value_chain = decoded_bytes.split(",")
        else:
            value_chain = [0] + random.sample(range(0, 300), 1) + \
                [random.getrandbits(1)] + random.sample(range(0, 20), 8)
        return value_chain

    def isOpen(self):
        return self.ser.isOpen()

    def dummyMode(self):
        return self.dummyPlug
