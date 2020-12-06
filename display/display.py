import os
import time
import display
import threading
from enums.display_state import DisplayState
from board.board import Board


class Display:

    def __init__(self):
        self.display_state = DisplayState.START
        self.board = Board(10, 20)

    def draw_display(self):
        os.system("clear")
        if (self.display_state == DisplayState.START):
            self.draw_start()
        elif (self.display_state == DisplayState.CONTROLS):
            self.draw_controls()
        elif (self.display_state == DisplayState.RUN):
            self.board.redraw()
        elif (self.display_state == DisplayState.PAUSE):
            self.draw_pause()

    def draw_start(self):
        print("#############################")
        print("#      TERMINAL TETRIS      #")
        print("#                           #")
        print("#    Press H for controls   #")
        print("#    Press ENTER to start   #")
        print("#                           #")
        print("#############################")

    def draw_controls(self):
        print("#########################################")
        print("#           TERMINAL TETRIS             #")
        print("#                                       #")
        print("# ⇦          - move left                #")
        print("# ⇨          - move right               #")
        print("# ⇧ or X     - rotate clockwise         #")
        print("# ctrl or Z  - rotate counter clockwise #")
        print("# space      - hard drop                #")
        print("# ⇩          - soft drop                #")
        print("# shift or C - hold                     #")
        print("# P          - pause the game           #")
        print("# E          - exit                     #")
        print("#                                       #")
        print("#########################################")

    def draw_pause(self):
        print("#############################")
        print("#      TERMINAL TETRIS      #")
        print("#                           #")
        print("#           PAUSED          #")
        print("#      Press R to resume    #")
        print("#                           #")
        print("#############################")

    def controls(self):
        if (self.display_state == DisplayState.START):
            self.display_state = DisplayState.CONTROLS
            self.update_display_timer()

    def start(self):
        self.display_state = DisplayState.RUN
        self.update_display_timer()

    def pause(self):
        if (self.display_state == DisplayState.RUN):
            self.display_state = DisplayState.PAUSE
            self.update_display_timer()

    def resume(self):
        if (self.display_state == DisplayState.PAUSE):
            self.display_state = DisplayState.RUN
            self.update_display_timer()

    def exit(self):
        if (self.display_state == DisplayState.CONTROLS):
            self.display_state = DisplayState.START
            self.update_display_timer()

    def update_display_timer(self):
        if (self.display_state != DisplayState.RUN):
            self.draw_display()

        while self.display_state == DisplayState.RUN:
            self.draw_display()
            self.board.timeout()


display = Display()
display.update_display_timer()
