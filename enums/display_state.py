from enums.enum_value import EnumValue


class DisplayState:
    START = EnumValue(0, "start")
    CONTROLS = EnumValue(1, "controls")
    RUN = EnumValue(2, "run")
    PAUSE = EnumValue(3, "pause"),
    GAME_OVER = EnumValue(4, "game over")
