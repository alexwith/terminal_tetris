import threading
import display.display
from input_listener import listen
from library.tetromino_library import dictionary

input_thread = threading.Thread(target=listen)
input_thread.start()
