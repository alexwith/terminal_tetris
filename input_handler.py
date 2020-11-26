from pynput import keyboard  # pip3 install pynput
from pynput.keyboard import KeyCode
from pynput.keyboard import Key
from board import *


def on_press(key):
    if (key == Key.left):
        move_left()
    elif (key == Key.right):
        move_right()
    elif (key == Key.up or key == KeyCode(char="x")):
        rotate_clockwise()
    elif (key == Key.ctrl or key == KeyCode(char="z")):
        rotate_counter_clockwise()
    elif (key == Key.down):
        soft_drop()
    elif (key == Key.space):
        hard_drop()
    elif (key == Key.shift or key == KeyCode(char="c")):
        hold()
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
