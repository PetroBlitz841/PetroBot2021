#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from util import buttons
from robot import Robot
from runs import run1, run2,run3, run4, LightCal

button_codes = {Button.UP: 0, Button.RIGHT: 1, Button.DOWN: 2, Button.LEFT: 3, Button.CENTER: 4}
button_symbols = [" ^ ", " > ", " v ", " < ", "[] "]
runs = [run1, run2, run3, run4, LightCal]

def display_menu():
  Robot.brick.screen.clear()

  for i in range(len(runs)):
    Robot.brick.screen.print(button_symbols[i] + runs[i].name)

while True:
  display_menu()

  btn = buttons.wait_for_any_press()
  try:
    btn_index = button_codes[btn]
    Robot.brick.screen.clear()
    r = runs[btn_index]
    r.start()
  except Exception as e: print(e)
