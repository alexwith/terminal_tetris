from objects.tetromino import Tetromino


class Board:

    def __init__(self):
        self.grid = [[0 for x in range(10)] for y in range(20)]
        self.score = 0
        self.next = "I"
        self.hold = None

    def set_tetromino(self, type):
        self.tetromino = Tetromino(type)

    def redraw(self):
        y = len(self.grid) + 1
        for row in self.grid:
            row_text = "#"
            y -= 1
            for column in row:
                row_text += " ."
            print(row_text + " # " + self.get_side_display_line(y))

    def get_side_display_line(self, y):
        if (y == 20):
            return f"Score: {self.score}"
        elif (y == 18):
            return f"Next: {self.next}"
        elif (y == 17):
            return f"Hold: {self.hold}"
        return ""

    def move_left(self):
        print("move left")
        pass

    def move_right(self):
        print("move right")
        pass

    def rotate_clockwise(self):
        print("rotate clockwise")
        pass

    def rotate_counter_clockwise(self):
        print("rotate counter clockwise")
        pass

    def soft_drop(self):
        print("soft drop")
        pass

    def hard_drop(self):
        print("hard drop")
        pass

    def hold(self):
        print("hold")
        self.score = 100
        pass
