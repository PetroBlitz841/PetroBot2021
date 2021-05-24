from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving

name = "LightCal"

def start():
    lines.light_calibration()
