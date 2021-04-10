from robot import Robot

def turn_by(angle, speed, acceleration=-1):
    start_angle = Robot.gyro.angle()
    settings = Robot.chassis.settings()
    if acceleration >= 0:
        Robot.chassis.settings(settings[0], settings[1], settings[2], acceleration)
    if angle > 0:
        pass
    else:
        pass
    


    Robot.chassis.settings(settings[0], settings[1], settings[2], settings[3])
