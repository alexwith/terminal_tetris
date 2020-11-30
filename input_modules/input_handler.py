import queue
import threading

input_queue = queue.Queue()


def handle_input():
    while True:
        if (not input_queue.empty()):
            try:
                threading.Thread(target=input_queue.get()).start()
            except:
                pass
