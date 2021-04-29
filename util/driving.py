from robot import Robot

def drive_until_black(speed, sensor, brake=True):
    Robot.chassis.drive(speed, 0)
    if sensor == "left":
        color = Robot.color_left.reflection
    elif sensor == "right":
        color = Robot.color_right.reflection
    else:
        raise AttributeError("Sensor must be left or right")
    while color() > Robot.BLACK:
        pass

    if brake:
        Robot.brake()
    else:
        Robot.chassis.stop()