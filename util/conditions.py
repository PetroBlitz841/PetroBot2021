from robot import Robot

def left_sensor_sees_white():
    if Robot.color_left.reflection() >= Robot.WHITE - 5:
        return True
    else:
        return False