import serial
port = "/dev/ttyUSB0"

ser = serial.Serial(port,9600)
ser.flushInput()

#constants
left = 'l'.encode()
right = 'r'.encode()

def serial_send(value_to_send):
    value_to_send = str(value_to_send) + "\n"
    ser.write(value_to_send.encode())

def sendWheelSpeeds(left_speed, right_speed):
    ser.write(left)
    serial_send(left_speed)

    serial_send(right)
    serial_send(right_speed)
    print("Successfully sent desired wheel speeds. \n")

while True:
    in_left_speed = input("Enter left speed: ")
    in_right_speed = input("Enter right speed: ")
    print("Sending wheel speeds to arduino microcontroller...")

    sendWheelSpeeds(in_left_speed, in_right_speed)    