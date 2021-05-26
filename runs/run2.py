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
    Robot.settings(turn_rate=88)
    driving.drive_until_black(100, "right")
    lines.line_follower("left", "right", 930, 150)
    Robot.chassis.drive(150, -5)
    wait(4000)
    Robot.chassis.stop()
    wait(300)
    Robot.hold()
    Robot.arm_right.run_time(1440, 4200, wait=False)
    wait(500)
    Robot.chassis.straight(5)
    wait(4200)
    Robot.arm_right.stop()

    Robot.arm_right.run_time(-600, 1500, wait=False)
    Robot.chassis.drive(-700, 0)
    wait(750) #This is what we are changing now
    Robot.chassis.stop()
    wait(250)
    Robot.chassis.turn(-102) 
    wait(250)
    Robot.chassis.drive(-300, 0)
    wait(520)
    Robot.chassis.stop()
    Robot.chassis.straight(300)
    wait(250)
    Robot.chassis.turn(108)
    wait(500)
    Robot.chassis.straight(125)
    wait(1000)
    Robot.chassis.drive(-100, 0)
    wait(100)
    Robot.settings(turn_rate=120)
    Robot.chassis.turn(-8)
    Robot.chassis.turn(8)
    Robot.settings(turn_rate=88)
    Robot.chassis.drive(-100, 0)
    wait(1780)
    Robot.chassis.turn(90)
    Robot.chassis.stop()
    driving.drive_until_black(100, "left")
    Robot.wheel_right.run_time(-300, 1400)
    Robot.chassis.drive(450, 0)
    buttons.wait_for_any_press()
    Robot.chassis.stop()
    


    # Robot.chassis.drive(-400, 15)
    # wait(1300)
    # Robot.chassis.stop()
    # Robot.chassis.drive(-700, -7)
    # buttons.wait_for_any_press()
    # Robot.brake()
    