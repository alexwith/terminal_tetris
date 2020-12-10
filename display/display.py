import os
import sys
import time
import display
import threading
from enums.display_state import DisplayState
from math import log10
from board.board import Board
from high_score import high_score
from constants import REFRESH_INTERVAL


class Display:

    def __init__(self):
        self.display_state = DisplayState.START
        self.board = Board(self, 10, 20)

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
        elif (self.display_state == DisplayState.GAME_OVER):
            self.draw_game_over()

    def draw_start(self):
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■      TERMINAL TETRIS      ■")
        print("■                           ■")
        print("■    Press H for controls   ■")
        print("■    Press ENTER to start   ■")
        print("■                           ■")
        print(self.get_high_score_line())
        print("■                           ■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

    def draw_controls(self):
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■           TERMINAL TETRIS             ■")
        print("■                                       ■")
        print("■ ⇦          - move left                ■")
        print("■ ⇨          - move right               ■")
        print("■ ⇧ or X     - rotate clockwise         ■")
        print("■ ctrl or Z  - rotate counter clockwise ■")
        print("■ space      - hard drop                ■")
        print("■ shift or C - hold                     ■")
        print("■ P          - pause the game           ■")
        print("■ L          - leave the game           ■")
        print("■ E          - exit                     ■")
        print("■                                       ■")
        print("■ Q          - quit/shutdown            ■")
        print("■                                       ■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

    def draw_pause(self):
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■      TERMINAL TETRIS      ■")
        print("■                           ■")
        print("■           PAUSED          ■")
        print("■      Press R to resume    ■")
        print("■                           ■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

    def draw_game_over(self):
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
        print("■      TERMINAL TETRIS      ■")
        print("■                           ■")
        print("■        GAME OVER          ■")
        print("■   Press S to go to start  ■")
        print("■                           ■")
        print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

    def get_high_score_line(self):
        score = high_score.high_score
        line = f"■    High Score: {score}" + \
            (" " * (11 - (int(log10(score)) + 1))) + "■"
        return line

    def controls(self):
        if (self.display_state == DisplayState.START):
            self.display_state = DisplayState.CONTROLS
            self.update_display_timer()

    def start(self):
        if (self.display_state != DisplayState.RUN):
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

    def leave_game(self):
        self.display_state = DisplayState.START
        self.board = Board(self, 10, 20)
        self.update_display_timer()

    def exit(self):
        if (self.display_state == DisplayState.CONTROLS):
            self.display_state = DisplayState.START
            self.update_display_timer()

    def leave_game_over(self):
        if (self.display_state == DisplayState.GAME_OVER):
            self.display_state = DisplayState.START
            self.update_display_timer()

    def game_over(self):
        self.display_state = DisplayState.GAME_OVER
        self.board = Board(self, 10, 20)
        self.update_display_timer()

    def update_display_timer(self):
        if (self.display_state != DisplayState.RUN):
            self.draw_display()

        while self.display_state == DisplayState.RUN:
            self.draw_display()
            time.sleep(REFRESH_INTERVAL)


display = Display()
display.update_display_timer()
