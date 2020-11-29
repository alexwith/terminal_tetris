from pynput import keyboard  # pip3 install pynput
from pynput.keyboard import KeyCode
from pynput.keyboard import Key
from display.display import display
from input_modules.input_handler import input_queue
import threading

board = display.board
actions = [
    [Key.left, board.move_left],
    [Key.right, board.move_right],
    [Key.up, KeyCode(char="x"), board.rotate_clockwise],
    [Key.ctrl, KeyCode(char="z"), board.rotate_counter_clockwise],
    [Key.space, board.hard_drop],
    [Key.down, board.soft_drop],
    [Key.shift, KeyCode(char="c"), board.hold],
    [Key.enter, display.start],
    [KeyCode(char="h"), display.controls],
    [KeyCode(char="e"), display.exit]
]


def listen():

    def on_press(key):
        print("pressed: " + threading.current_thread().name)
        for entry in actions:
            successful = False
            for i in range(len(entry) - 1):
                if ((not successful) and key == entry[i]):
                    successful = True
            if (successful):
                input_queue.put(entry[len(entry) - 1])

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
