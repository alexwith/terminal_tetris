from pynput.keyboard import Key, KeyCode, Listener
from display.display import display
from exit_app import shutdown
from input_modules.input_handler import input_queue

def actions(board): return [
    [Key.left, board.move_left],
    [Key.right, board.move_right],
    [Key.up, KeyCode(char="x"), board.rotate_clockwise],
    [Key.ctrl, KeyCode(char="z"), board.rotate_counter_clockwise],
    [Key.space, board.hard_drop],
    [Key.shift, KeyCode(char="c"), board.hold],
    [Key.enter, display.start],
    [KeyCode(char="h"), display.controls],
    [KeyCode(char="e"), display.exit],
    [KeyCode(char="p"), display.pause],
    [KeyCode(char="r"), display.resume],
    [KeyCode(char="s"), display.leave_game_over],
    [KeyCode(char="l"), display.leave_game],
    [KeyCode(char="q"), shutdown]
]


def listen():
    
    def on_press(key):
        for entry in actions(display.board):
            successful = False
            for i in range(len(entry) - 1):
                if ((not successful) and key == entry[i]):
                    successful = True
            if (successful):
                input_queue.put(entry[len(entry) - 1])

    with Listener(on_press=on_press) as listener:
        listener.join()
