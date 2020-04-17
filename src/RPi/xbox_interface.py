import serial
from backend import xbox
from backend.interface import Interface
from backend.gen_suite import Pose, Path, Trajectory, Robot
import time


#setup serial connection
arduino = Interface()

#xbox setup
joy = xbox.Joystick()


print('Computing trajectory...')
waypoints = [Pose(0,0,0), Pose(80, 30, 90), Pose(50, 50, 180)]
path = Path(waypoints)
robot = Robot(190 * 0.03937, 8, 5)
trajectory = Trajectory(robot, path)

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

    # if spdL==0 or spdR == 0:
    #     print('', end='\r')
    # print(pwrL, pwrR, end='\r')
    return spdL, spdR

def do_trajectory():
    print('Finished computing trajectory, starting trajectory...')

    traj_time = time.time()
    total_traj_time = trajectory.trajectory[-1].time

    while (time.time() - traj_time) <= total_traj_time:
        if(joy.B()):
            break
        t = time.time() - traj_time
        state = trajectory.sample(t)
        left_speed, right_speed = robot.get_wheel_speeds_from_state(state)
        arduino.sendWheelSpeeds(left_speed, right_speed)
    print('Finished trajectory, returning to joystick control.')


while not joy.Back():


    if(joy.Y()):
        do_trajectory()
    
    in_left_speed, in_right_speed = arcade_drive()

    arduino.sendWheelSpeeds(in_left_speed, in_right_speed)    