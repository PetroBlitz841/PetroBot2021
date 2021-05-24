from robot import Robot
from util import buttons
import time

def light_calibration():
    Robot.brick.screen.print("left color on: BLACK")
    buttons.wait_for_any_press()
    BLACK = Robot.color_left.reflection()
    print(BLACK)
    Robot.brick.screen.clear()
    Robot.brick.screen.print("left color on: WHITE")
    buttons.wait_for_any_press()
    WHITE = Robot.color_left.reflection()
    print(WHITE)
    Robot.brick.screen.clear()


def line_follower(line_side, sensor_side, distance, p0):
    target = (Robot.WHITE + Robot.BLACK) / 2

    vision = Robot.color_right.reflection
    if sensor_side == "left":
        vision = Robot.color_left.reflection
    #choosing sensor

    Robot.chassis.reset()
    Robot.chassis.drive(p0, 0)
    #start moving forward
    while Robot.chassis.distance() < distance:
        #as long as you havn't made it to the end
        error = vision() - target
        if line_side == "right":
            Robot.chassis.drive(p0, -error * 4)
        elif line_side == "left":
            Robot.chassis.drive(p0, error * 4)

    Robot.brake()
    #STOP!

def line_until(line_side, sensor_side, p0, condition, max_time=0):
    target = (Robot.WHITE + Robot.BLACK) / 2
    start_time = time.time()
    vision = Robot.color_right.reflection
    if sensor_side == "left":
        vision = Robot.color_left.reflection
    #choosing sensor

    Robot.chassis.drive(p0, 0)
    #start moving forward
    while not condition() and (time.time() - start_time < max_time or max_time <= 0):
        #as long as you havn't made it to the condition
        error = vision() - target
        if line_side == "right":
            Robot.chassis.drive(p0, -error * 4)
        elif line_side == "left":
            Robot.chassis.drive(p0, error * 4)

    Robot.brake()
    #STOP!

