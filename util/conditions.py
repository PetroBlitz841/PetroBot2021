from robot import Robot

def left_sensor_sees_white():
    if Robot.color_left.reflection() >= Robot.WHITE - 5:
        return True
    else:
        return False

def left_sensor_sees_black():
    if Robot.color_left.reflection() >= Robot.BLACK + 5:
        return True
    else:
        return False

def right_sensor_sees_black():
    if Robot.color_right.reflection() >= Robot.BLACK + 2:
        return True
    else:
        return False