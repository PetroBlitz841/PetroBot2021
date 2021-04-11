from robot import Robot
from pybricks.parameters import Stop
from util import gyro

name = "run1"

def start():
    #Robot.chassis.straight(350)
    #Robot.arm_left.run_angle(400, 180, then=Stop.HOLD, wait=True)
    #Robot.chassis.turn(-180)
    #Robot.chassis.turn(250)

    #TEST
     Robot.gyro.reset_angle(0)
     Robot.chassis.straight(300)
     gyro.turn_by(90, 90, 30)
     gyro.turn_by(-90, 90, 30)

    # while True:
    #     print(Robot.gyro.angle())


    
