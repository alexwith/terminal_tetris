import time
import threading
import random
from objects.tetromino import Tetromino
from enums.tetromino_type import TetrominoType
from library.tetromino_library import get_shape, get_random


class Board:

    def __init__(self):
        self.grid = [[0 for x in range(10)] for y in range(20)]
        self.moving_grid = [[0 for x in range(10)] for y in range(20)]
        self.level = 0
        self.score = 0
        self.total_cleared = 0
        self.current = Tetromino(get_random())
        self.next = get_random()
        self.hold = None

    def redraw(self):
        self.give_points()
        self.advance_level()
        self.moving_grid = [[0 for x in range(10)] for y in range(20)]
        current_shape = get_shape(self.current.type, self.current.state)
        for y, row_value in enumerate(current_shape):
            for x, column_value in enumerate(row_value):
                if (current_shape[y][x] == 1):
                    if (self.current.y + y >= len(self.grid) - 1 or self.grid[self.current.y + y + 1][self.current.x + x] == 1):
                        self.current.set_complete(True)
                    self.moving_grid[self.current.y +
                                     y][self.current.x + x] = current_shape[y][x]
        if (not self.current.complete):
            self.current.y += 1
        else:
            for y, row_value in enumerate(current_shape):
                for x, column_value in enumerate(row_value):
                    if (current_shape[y][x] == 1):
                        self.grid[self.current.y + y][self.current.x + x] = 1
            self.current = Tetromino(self.next)
            self.next = get_random()
        for y, row_value in enumerate(self.grid):
            row_text = "#"
            for x, column_value in enumerate(row_value):
                if (column_value == 1 or self.moving_grid[y][x] == 1):
                    row_text += " #"
                elif (column_value == 0):
                    row_text += " ."
            print(row_text + " # " + self.get_side_display_line(y))

    def timeout(self):
        time.sleep(1/self.level)

    def give_points(self):
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
        if (self.total_cleared >= 10):
            self.total_cleared = 0
            self.level += 1

    def get_side_display_line(self, y):
        if (y == 15):
            return f"Level: {self.level}"
        elif (y == 16):
            return f"Score: {self.score}"
        elif (y == 18):
            return f"Next: {self.next.name}"
        elif (y == 19):
            return f"Hold: {self.hold}"
        return ""

    def move_left(self):
        if (self.is_blocked(lambda x, y: self.current.x + x - 1 < 0 or self.grid[self.current.y + y][self.current.x + x - 1] == 1)):
            return
        self.current.x -= 1

    def move_right(self):
        if (self.is_blocked(lambda x, y: self.current.x + x + 1 > 9 or self.grid[self.current.y + y][self.current.x + x + 1] == 1)):
            return
        self.current.x += 1

    def rotate_clockwise(self):
        if (self.is_blocked(lambda x, y: self.current.x + x > 9 or self.grid[self.current.y + y][self.current.x + x] == 1)):
            return
        state = self.current.state
        self.current.state = 0 if state == 3 else state + 1

    def rotate_counter_clockwise(self):
        if (self.is_blocked(lambda x, y: self.current.x + x > 9 or self.grid[self.current.y + y][self.current.x + x] == 1)):
            return
        state = self.current.state
        self.current.state = 0 if state == 3 else state - 1

    def soft_drop(self):
        pass

    def hard_drop(self):
        current_shape = get_shape(self.current.type, self.current.state)
        while (not self.current.complete):
            self.current.y += 1
            for y, row_value in enumerate(current_shape):
                for x, column_value in enumerate(row_value):
                    if (current_shape[y][x] == 1):
                        if (self.current.y + y >= len(self.grid) - 1 or self.grid[self.current.y + y + 1][self.current.x + x] == 1):
                            self.current.set_complete(True)

    def hold(self):
        pass

    def is_blocked(self, predicate):
        current_shape = get_shape(self.current.type, self.current.state)
        for y, row_value in enumerate(current_shape):
            for x, column_value in enumerate(row_value):
                if (current_shape[y][x] == 1):
                    if (predicate(x, y)):
                        return True
                        break
        return False
