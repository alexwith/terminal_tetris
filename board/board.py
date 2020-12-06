import time
import threading
import random
from objects.tetromino import Tetromino
from enums.tetromino_type import TetrominoType
from library.tetromino_library import get_shape, get_random


class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.generate_grid = lambda: [
            [0 for x in range(self.width)] for y in range(self.height)]

        self.level = 0
        self.score = 0
        self.total_cleared = 0
        self.grid = self.generate_grid()
        self.moving_grid = self.generate_grid()
        self.visualized_grid = self.generate_grid()
        self.current = Tetromino(get_random())
        self.next = get_random()
        self.hold = None
        self.current_shape = lambda: get_shape(
            self.current.type, self.current.state)
        self.timeout = lambda: time.sleep(1/(self.level + 1))

    def redraw(self):
        self.attempt_reward()
        self.advance_level()
        self.moving_grid = self.generate_grid()
        self.visualized_grid = self.generate_grid()
        self.visualize()
        self.apply_moving_grid()
        self.move_or_switch()
        self.draw_grids()

    def draw_grids(self):
        for y, row in enumerate(self.grid):
            row_text = "@"
            for x, x_value in enumerate(row):
                if (x_value == 1 or self.moving_grid[y][x] == 1):
                    row_text += " #"
                elif (self.visualized_grid[y][x] == 1):
                    row_text += " $"
                elif (x_value == 0):
                    row_text += " ."
            print(row_text + " @ " + self.get_side_bar(y))

    def get_side_bar(self, y):
        if (y == 15):
            return f"Level: {self.level}"
        elif (y == 16):
            return f"Score: {self.score}"
        elif (y == 18):
            return f"Next: {self.next.name}"
        elif (y == 19):
            return f"Hold: {self.hold}"
        return ""

    def attempt_reward(self):
        cleared = 0
        points = [40, 100, 300, 1200]
        for y, row in enumerate(self.grid):
            if (not 0 in row):
                self.grid[y] = [0 for x in range(10)]
                cleared += 1
                self.total_cleared += 1
        if (cleared > 0):
            self.score += points[cleared - 1]*(self.level + 1)

    def advance_level(self):
        if (self.total_cleared >= 1):
            self.total_cleared = 0
            self.level += 1

    def move_or_switch(self):
        if (not self.current.complete):
            self.current.y += 1
        else:
            self.apply_tetromino()
            self.current = Tetromino(self.next)
            self.next = get_random()

    def apply_tetromino(self):
        for y, row in enumerate(self.current_shape()):
            for x, x_value in enumerate(row):
                if (self.current_shape()[y][x] == 1):
                    self.grid[self.current.y + y][self.current.x + x] = 1

    def apply_moving_grid(self):
        for y, row in enumerate(self.current_shape()):
            for x, x_value in enumerate(row):
                if (self.current_shape()[y][x] == 1):
                    if (self.current.y + y >= len(self.grid) - 1 or self.grid[self.current.y + y + 1][self.current.x + x] == 1):
                        self.current.set_complete(True)
                    self.moving_grid[self.current.y +
                                     y][self.current.x + x] = self.current_shape()[y][x]

    def is_blocked(self, predicate):
        for y, row in enumerate(self.current_shape()):
            for x, x_value in enumerate(row):
                if (self.current_shape()[y][x] == 1):
                    if (predicate(x, y)):
                        return True
                        break
        return False

    def visualize(self):
        current_y = self.current.y
        complete = False
        while (not complete and not self.current.y >= 17):
            current_y += 1
            for y, row in enumerate(self.current_shape()):
                for x, x_value in enumerate(row):
                    if (self.current_shape()[y][x] == 1):
                        if (current_y + y >= len(self.grid) - 1 or self.grid[current_y + y + 1][self.current.x + x] == 1):
                            for y, row in enumerate(self.current_shape()):
                                for x, x_value in enumerate(row):
                                    if (self.current_shape()[y][x] == 1):
                                        self.visualized_grid[current_y +
                                                             y][self.current.x + x] = 1
                            complete = True

    def move_left(self):
        if (self.is_blocked(lambda x, y: self.current.x + x - 1 < 0 or self.grid[self.current.y + y][self.current.x + x - 1] == 1)):
            return
        self.current.x -= 1

    def move_right(self):
        if (self.is_blocked(lambda x, y: self.current.x + x + 1 >= self.width or self.grid[self.current.y + y][self.current.x + x + 1] == 1)):
            return
        self.current.x += 1

    def rotate_clockwise(self):
        if (self.is_blocked(lambda x, y: self.current.x + x >= self.width or self.grid[self.current.y + y][self.current.x + x] == 1)):
            return
        state = self.current.state
        self.current.state = 0 if state == 3 else state + 1

    def rotate_counter_clockwise(self):
        if (self.is_blocked(lambda x, y: self.current.x + x >= self.width or self.grid[self.current.y + y][self.current.x + x] == 1)):
            return
        state = self.current.state
        self.current.state = 0 if state == 3 else state - 1

    def soft_drop(self):
        pass

    def hard_drop(self):
        while (not self.current.complete):
            self.current.y += 1
            for y, row in enumerate(self.current_shape()):
                for x, x_value in enumerate(row):
                    if (self.current_shape()[y][x] == 1 and (self.current.y + y >= len(self.grid) - 1 or self.grid[self.current.y + y + 1][self.current.x + x] == 1)):
                        self.current.set_complete(True)

    def hold(self):
        pass
