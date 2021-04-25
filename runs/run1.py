from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait

name = "run1"

def start():
    Robot.reset_gyro()
    Robot.chassis.reset()
    