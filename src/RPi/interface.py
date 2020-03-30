import serial
port = "/dev/ttyUSB0"

ser = serial.Serial(port,9600)
ser.flushInput()

#constants
left = "l"
right = "r"


def sendWheelSpeeds(left_speed, right_speed):
    print(left_speed)
    print(right_speed)
    leftSpeed_encode = b'%f' %left_speed
    rightSpeed_encode = b'%f' %right_speed

    ser.write(left.encode())
    ser.write(leftSpeed_encode)

    ser.write(right.encode())
    ser.write(rightSpeed_encode)

while True:
    in_left_speed = input("Enter left speed: ")
    in_right_speed = input("Enter right speed: ")

    sendWheelSpeeds(in_left_speed, in_right_speed)







    