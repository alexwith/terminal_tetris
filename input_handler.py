from pynput import keyboard  # pip3 install pynput
from pynput.keyboard import KeyCode


def on_press(key):
    if (key == KeyCode(char="a")):
        print("Pressed A")
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
