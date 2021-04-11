from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, ColorSensor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

class Robot():

  #robot hardware
  brick = EV3Brick()

  wheel_left = Motor(Port.C)
  wheel_right = Motor(Port.B)

  arm_left = Motor(Port.D)
  arm_right = Motor(Port.A)

  gyro = GyroSensor(Port.S4, Direction.COUNTERCLOCKWISE)
  color_left = ColorSensor(Port.S2)
  color_right = ColorSensor(Port.S3)

  chassis = DriveBase(wheel_left, wheel_right, wheel_diameter=62.4, axle_track=130)

  @classmethod
  def brake(cls):
    cls.chassis.stop()
    cls.wheel_left.brake()
    cls.wheel_right.brake()

  @classmethod
  def reset_gyro(cls):
    cls.gyro.reset_angle(0)

    cls.gyro.angle()
    cls.gyro.speed()
    cls.gyro.angle()
    
    wait(10)

