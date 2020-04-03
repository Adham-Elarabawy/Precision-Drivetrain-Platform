import serial
import xbox

#setup serial connection
port = "/dev/ttyUSB0"

ser = serial.Serial(port,57600) #9600
ser.flushInput()

#xbox setup
joy = xbox.Joystick()

#temp robot setup
max_speed = 40 #in/s


#constants
left = 'l'.encode()
right = 'r'.encode()

def serial_send(value_to_send):
    value_to_send = str(value_to_send) + "\n"
    ser.write(value_to_send.encode())

def sendWheelSpeeds(left_speed, right_speed):
    ser.write(left)
    serial_send(left_speed)

    ser.write(right)
    serial_send(right_speed)

def clamp(value, minimum, maximum):
    return min(max(value,minimum), maximum)

def arcade_drive():
    joyX = -joy.leftX()
    joyY = joy.leftY()

    if (abs(joyX) < 0.2):
        joyX = 0
    if (abs(joyY) < 0.2):
        joyY = 0
    
    pwrL = clamp(joyY-joyX, -1, 1)
    pwrR = clamp(joyY+joyX, -1, 1)

    spdL = pwrL * max_speed
    spdR = pwrR * max_speed

    if spdL==0 or spdR == 0:
        print('', end='\r')
    print(pwrL, pwrR, end='\r')
    return spdL, spdR


while not joy.Back():

    in_left_speed, in_right_speed = arcade_drive()

    sendWheelSpeeds(in_left_speed, in_right_speed)    