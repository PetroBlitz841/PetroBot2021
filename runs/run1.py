from robot import Robot
from pybricks.parameters import Stop, Button
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving
from util import conditions
from util import buttons
name = "run1"

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
    driving.drive_until_black(150, "left")
    lines.line_follower("right", "left", 500, 150)
    lines.line_follower("right", "left", 140, 30)

    Robot.settings(straight_speed=100)
    Robot.chassis.straight(-180)
    Robot.chassis.drive(200, -80)
    wait(1500)
    Robot.chassis.stop()
    # driving.drive_until_black(50, "right")
    lines.line_until("left", "right", 150, conditions.left_sensor_sees_white)
    gyro.gyro_straight(150, 300, 3) 
    Robot.chassis.stop()
    Robot.arm_left.run_angle(-180, 170)
    Robot.chassis.straight(-150)
    gyro.turn_by(-90, 150)
    gyro.gyro_straight(125, 200, 3)
    driving.drive_until_black(100, "right")
    Robot.chassis.drive(-150, 0)
    wait(250)
    Robot.chassis.stop()    
    Robot.wheel_left.run_time(250, 1500)
    lines.line_follower("right", "right", 100, 100)
    lines.line_until("right", "right", 70, conditions.left_sensor_sees_white, max_time=2.5)
    Robot.chassis.stop()
    Robot.arm_left.run_angle(70, 200)
    Robot.chassis.straight(-200)
    Robot.chassis.drive(0, -300)
    wait(410)
    Robot.chassis.stop()
    Robot.settings(straight_speed=250)
    Robot.chassis.drive(450, -5)
    buttons.wait_for_any_press()
    Robot.chassis.stop()
    #fin