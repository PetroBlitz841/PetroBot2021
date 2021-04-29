from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving

name = "run1"

def start():
    Robot.reset_gyro()
    Robot.settings(straight_speed=150)
    gyro.gyro_follow(0, 100, 550, 5)
    driving.drive_until_black(150, "left", brake=False)
    Robot.settings(straight_speed=30)
    Robot.chassis.straight(30)
    driving.drive_until_black(30, "left")

    Robot.settings(straight_speed=100)
    Robot.chassis.straight(-350)
    Robot.chassis.drive(300, -70)
    wait(1500)
    Robot.chassis.stop()
    driving.drive_until_black(50, "right")
    lines.line_follower("left", "right", 100, 100)

