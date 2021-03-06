from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from time import sleep

name = "run4"

def start():
    Robot.gyro.reset_angle(0)
    gyro.gyro_follow(0, 360, 940, 10)
    gyro.turn_by(130, 180)
    for i in range(20):
        Robot.chassis.straight(-75)
        Robot.brick.speaker.beep(frequency=500, duration=50)
        Robot.chassis.straight(75)
        Robot.brick.speaker.beep(frequency=500, duration=50)
    #FINISHED