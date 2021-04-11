from robot import Robot
from util.functions import is_between

def turn_by(angle, speed, acceleration=-1):
    start_angle = Robot.gyro.angle()
    settings = Robot.chassis.settings()
    if acceleration <= 0:
        Robot.chassis.settings(settings[0], settings[1], settings[2], acceleration)

    if angle > 0:
        Robot.chassis.drive(0, speed)
        while not is_between(start_angle + angle, 2, Robot.gyro.angle()):
            print(Robot.gyro.angle())
    else:
        Robot.chassis.drive(0, -speed)
        while not is_between(start_angle + angle, 2, Robot.gyro.angle()):
            #if is_between(start_angle + angle, 2, Robot.gyro.angle()):
                #Robot.chassis.drive(0, speed / 2)
            pass
        
    Robot.brake()

    


    Robot.chassis.settings(settings[0], settings[1], settings[2], settings[3])
