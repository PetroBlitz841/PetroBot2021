from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving
from util import conditions
from util import buttons
name = "run2"

def start():
    Robot.reset_gyro()
    driving.drive_until_black(100, "right")
    lines.line_follower("left", "right", 930, 150)
    Robot.chassis.drive(150, -5)
    wait(4000)
    Robot.chassis.stop()
    wait(300)
    Robot.hold()
    Robot.arm_right.run_time(1000, 8000)
    Robot.arm_right.stop()
    Robot.arm_right.run_time(-600, 1500, wait=False)
    Robot.chassis.drive(-700, 0)
    wait(500)
    Robot.chassis.stop()
    Robot.chassis.drive(-400, 0)
    wait(500)
    Robot.chassis.stop()
    # gyro.gyro_follow(0, -500, 250, 10)
    # Robot.chassis.drive(-400, 3)
    # wait(1500)
    # Robot.chassis.stop()
    # Robot.chassis.drive(-400, 20)
    # wait(2000)
    # Robot.chassis.stop()




    # gyro.gyro_follow(0, 100, 250, 3)

    # gyro.turn_by(-110, 100)
    # gyro.gyro_straight(150, 300, 5)
    # driving.drive_until_black(100, "right")
    # gyro.turn_by(30, 100)
    # gyro.gyro_straight(100, 150, 3)

    # Robot.arm_left.run_time(360, 2000)
