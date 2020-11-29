import queue

input_queue = queue.Queue()


def handle_input():
    while True:
        if (not input_queue.empty()):
            try:
                input_queue.get()()
            except:
                pass
