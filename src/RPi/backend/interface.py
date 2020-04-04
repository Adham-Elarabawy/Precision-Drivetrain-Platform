import serial

class Interface:

    def __init__(self, port="/dev/ttyUSB0", baud_rate=57600):
        self.port = port
        self.baud_rate = baud_rate
        self.ser = serial.Serial(port, baud_rate)
        self.ser.flushInput()


        #constants
        self.left = 'l'.encode()
        self.right = 'r'.encode()

    def serial_send(self, value_to_send):
        value_to_send = str(value_to_send) + "\n"
        self.ser.write(value_to_send.encode())

    def sendWheelSpeeds(self, left_speed, right_speed):
        self.ser.write(self.left)
        self.serial_send(left_speed)

        self.ser.write(self.right)
        self.serial_send(right_speed)