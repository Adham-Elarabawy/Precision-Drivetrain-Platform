import serial
from backend.interface import Interface


#setup serial connection
arduino = Interface()

#temp robot setup
max_speed = 40 #in/s

while True:
    in_left_speed = input("Enter left speed: ")
    in_right_speed = input("Enter right speed: ")
    print(' ')

    arduino.sendWheelSpeeds(in_left_speed, in_right_speed)    