from robot import Robot

def turn_by(angle, speed, acceleration=-1):
    start_angle = Robot.gyro.angle()
    if acceleration >= 0:
        settings = Robot.chassis.settings()
        Robot.chassis.settings(settings[0], settings[1], settings[2], acceleration)
    if angle > 0:
        Robot.chassis.drive(0, speed)
        while Robot.gyro.angle() < start_angle + angle:
            pass
        
    else:
        Robot.chassis.drive(0, -speed)
        while Robot.gyro.angle() > start_angle + angle:
            pass
        
    Robot.brake()
    
    


    Robot.chassis.settings(settings[0], settings[1], settings[2], settings[3])
