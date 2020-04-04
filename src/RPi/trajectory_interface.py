import serial
from backend.interface import Interface
from backend.gen_suite import Pose, Path, Trajectory, Robot
import time

arduino = Interface()

waypoints = [Pose(0,0,0), Pose(20,20,90)]
path = Path(waypoints)
robot = Robot(5, 40, 5)
trajectory = Trajectory(robot, path)

traj_time = time.time()
total_traj_time = trajectory.trajectory[-1].time

while (time.time() - traj_time) <= total_traj_time:
    t = time.time() - traj_time
    state = trajectory.sample(t)
    print(state.curvature)
    left_speed, right_speed = robot.get_wheel_speeds_from_state(state)
    arduino.sendWheelSpeeds(left_speed, right_speed)
print('FINISHED')