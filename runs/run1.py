from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving
from util import conditions
name = "run1"

def start():
    Robot.reset_gyro()
    Robot.settings(straight_speed=150, straight_acceleration=125)
    Robot.chassis.straight(400)
    driving.drive_until_black(150, "left", brake=False, max_time = 7000)
    Robot.settings(straight_speed=30)
    Robot.chassis.straight(30)
    driving.drive_until_black(30, "left")

    Robot.settings(straight_speed=100)
    Robot.chassis.straight(-350)
    Robot.chassis.drive(300, -65)
    wait(1500)
    Robot.chassis.stop()
    driving.drive_until_black(50, "right")
    lines.line_follower("left", "right", 100, 100)
    lines.line_until("left", "right", 150, conditions.left_sensor_sees_white)
    Robot.chassis.straight(300)
    # gyro.gyro_follow(-90, 150, 250, 2)
    Robot.arm_left.run_angle(225, 310)
    Robot.chassis.straight(-100)
    gyro.turn_by(-45, 90)
    Robot.chassis.straight(400)

