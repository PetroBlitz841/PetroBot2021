from robot import Robot
from pybricks.parameters import Stop, Button
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving
from util import conditions
from util import buttons
name = "run3"

def start():
    Robot.brick.screen.print("set your left arm")
    while buttons.button_pressed(Button.CENTER) == False:
        if buttons.button_pressed(Button.UP):
            Robot.arm_left.run(100)
        elif buttons.button_pressed(Button.DOWN):
            Robot.arm_left.run(-100)
        else:
            Robot.arm_left.brake()
    Robot.brick.screen.clear()
    Robot.reset_gyro()
    gyro.gyro_follow(0, 150, 475, 5)
    gyro.turn_to(20, 5)
    Robot.chassis.straight(20)
    Robot.arm_left.run_time(60, 500)
    Robot.arm_left.run_time(600, 650)
    gyro.turn_to(0, 5)
    Robot.chassis.drive(-500, 0)
    buttons.wait_for_any_press()
    Robot.chassis.stop()
