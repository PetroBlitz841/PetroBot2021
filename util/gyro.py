from robot import Robot
from util.functions import is_between

def turn_by(angle, speed, acceleration=-1):
    start_angle = Robot.gyro.angle()
    settings = Robot.chassis.settings()
    if acceleration <= 0:
        Robot.settings(settings[0], settings[1], settings[2], acceleration)

    if angle > 0:
        Robot.chassis.drive(0, speed)
        while not is_between(start_angle + angle, 2, Robot.gyro.angle()):
            pass
    else:
        Robot.chassis.drive(0, -speed)
        while not is_between(start_angle + angle, 2, Robot.gyro.angle()):
            #if is_between(start_angle + angle, 2, Robot.gyro.angle()):
                #Robot.chassis.drive(0, speed / 2)
            pass
        
    Robot.brake()

    Robot.chassis.settings(settings[0], settings[1], settings[2], settings[3])

def turn_to(angle, kp=0.2 , acceleration=-1):
    settings = Robot.chassis.settings()
    if acceleration <= 0:
        Robot.settings(settings[0], settings[1], settings[2], acceleration)
    in_case = 0

    while Robot.gyro.angle() != angle and in_case != 1:
        error = angle - Robot.gyro.angle()
        Robot.chassis.drive(0, error*kp)
        if abs(error) <= 2:
            in_case = 1
            #if is_between(start_angle + angle, 2, Robot.gyro.angle()):
                #Robot.chassis.drive(0, speed / 2)
        
    Robot.brake()

    Robot.chassis.settings(settings[0], settings[1], settings[2], settings[3])

def gyro_follow(target, speed, distance, kp):
    error = 0
    Robot.chassis.reset()
    Robot.chassis.drive(speed, 0)
    while Robot.chassis.distance() < distance:
        error = target - Robot.gyro.angle()
        Robot.chassis.drive(speed, error * kp)

    Robot.brake()

def gyro_straight(speed, distance, kp):
    error = 0
    target = Robot.gyro.angle()
    Robot.chassis.reset()
    Robot.chassis.drive(speed, 0)
    while Robot.chassis.distance() < distance:
        error = target - Robot.gyro.angle()
        Robot.chassis.drive(speed, error * kp)

    Robot.brake()
