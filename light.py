def reset_light(cls):
    cls.brick.screen.clear()

    cls.brick.screen.draw_text(0, 0, "reset black")
    buttons.wait_for_press(Button.CENTER)
    cls.black = cls.color_left.reflection()

    cls.brick.screen.draw_text(120, 0, str(cls.black))
    cls.brick.screen.draw_text(0, 20, "reset white")
    buttons.wait_for_press(Button.CENTER)
    cls.white = cls.color_left.reflection()

    cls.brick.screen.draw_text(120, 20, str(cls.white))
    buttons.wait_for_press(Button.CENTER)

def get_light(cls):
    return (cls.color_left.reflection(), cls.color_right.reflection())