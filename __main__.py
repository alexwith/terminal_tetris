import threading
import display.display
from input_modules.input_listener import listen
from input_modules.input_handler import handle_input
from library.tetromino_library import dictionary

listener_thread = threading.Thread(target=listen)
listener_thread.start()

handle_input()
