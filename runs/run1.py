from robot import Robot
from pybricks.parameters import Stop
from util import gyro
from util import lines
from pybricks.tools import wait
from util import driving
from util import conditions
from util import buttons
name = "run1"

def start():
    Robot.reset_gyro()
    Robot.settings(straight_speed=150, straight_acceleration=125)
    # gyro.gyro_follow(-0, 150, 400, 2)
    Robot.chassis.straight(400)
    driving.drive_until_black(150, "left", brake=False)
    Robot.settings(straight_speed=30)
    Robot.chassis.straight(30)
    driving.drive_until_black(30, "left", brake=False, max_time = 7000)

    Robot.settings(straight_speed=100)
    Robot.chassis.straight(-330)
    Robot.chassis.drive(310, -65)
    wait(1500)
    Robot.chassis.stop()
    driving.drive_until_black(50, "right")
    lines.line_follower("left", "right", 100, 100)
    lines.line_until("left", "right", 150, conditions.left_sensor_sees_white)
    Robot.chassis.straight(300)
    # gyro.gyro_follow(-90, 150, 250, 2)
    Robot.arm_left.run_angle(225, 310)
    Robot.chassis.straight(-100)
    gyro.turn_by(-80, 150)
    # gyro.gyro_follow(-180, 125, 650, 2)
    driving.drive_until_black(100, "right")
    lines.line_follower("right", "right", 100, 100)
    # lines.line_until("right", "right", 50, conditions.left_sensor_sees_white, max_time=3000)
    Robot.chassis.stop()
    Robot.chassis.straight(-200)
    gyro.turn_by(-110, 150)
    Robot.settings(straight_speed=250)
    Robot.chassis.drive(250, 0)
    buttons.wait_for_any_press()
    Robot.chassis.stop()
    

