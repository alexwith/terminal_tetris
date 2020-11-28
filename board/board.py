from objects.tetromino import Tetromino


class Board:

    def __init__(self):
        self.grid = [[0 for x in range(10)] for y in range(20)]

    def set_tetromino(self, type):
        self.tetromino = Tetromino(type)
