from robot import Robot
from pybricks.parameters import Stop

name = "run1"

def start():
    Robot.chassis.straight(350)
    Robot.arm_left.run_angle(400, 180, then=Stop.HOLD, wait=True)
    Robot.chassis.turn(-180)
    Robot.chassis.turn(250)
    Robot.chassis.straight(300)

    
