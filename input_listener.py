from pynput import keyboard  # pip3 install pynput
from pynput.keyboard import KeyCode
from pynput.keyboard import Key
from control.move_handler import *
from display.display import display

actions = [
    [Key.left, move_left],
    [Key.right, move_right],
    [Key.up, KeyCode(char="x"), rotate_clockwise],
    [Key.ctrl, KeyCode(char="z"), rotate_counter_clockwise],
    [Key.space, hard_drop],
    [Key.down, soft_drop],
    [Key.shift, KeyCode(char="c"), hold],
    [Key.enter, display.start],
    [KeyCode(char="h"), display.controls],
    [KeyCode(char="e"), display.exit]
]


def listen():
    def on_press(key):
        for entry in actions:
            successful = False
            for i in range(len(entry) - 1):
                if ((not successful) and key == entry[i]):
                    successful = True
            if (successful):
                entry[len(entry) - 1]()

    def on_release(key):
        pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
