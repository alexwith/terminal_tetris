from library.tetromino_library import get_shape


class Tetromino:

    def __init__(self, type):
        self.type = type
        self.state = 0
        self.x = 3
        self.y = 0
        self.complete = False

    def get_shape(self):
        return get_shape(self.type, self.state)

    def get_type(self):
        return self.type

    def set_state(self, state):
        self.state = state

    def set_complete(self, complete):
        self.complete = complete
