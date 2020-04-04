import serial
from backend import xbox
from backend.interface import Interface


#setup serial connection
arduino = Interface()

#xbox setup
joy = xbox.Joystick()

#temp robot setup
max_speed = 40 #in/s

def clamp(value, minimum, maximum):
    return min(max(value,minimum), maximum)

def arcade_drive():
    joyX = -joy.leftX()
    joyY = joy.leftY()

    if (abs(joyX) < 0.1):
        joyX = 0
    if (abs(joyY) < 0.1):
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

    arduino.sendWheelSpeeds(in_left_speed, in_right_speed)    