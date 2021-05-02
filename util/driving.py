from robot import Robot
import time

def drive_until_black(speed, sensor, brake=True, max_time=0):
    start_time = time.time()
    Robot.chassis.drive(speed, 0)
    if sensor == "left":
        color = Robot.color_left.reflection
    elif sensor == "right":
        color = Robot.color_right.reflection
    else:
        raise AttributeError("Sensor must be left or right")
    while color() > Robot.BLACK and (time.time() - start_time < max_time or max_time <= 0):
        pass

    if brake:
        Robot.brake()
    else:
        Robot.chassis.stop()