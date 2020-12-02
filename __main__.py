import threading
from input_modules.input_listener import listen
from input_modules.input_handler import handle_input

listener_thread = threading.Thread(target=listen)
listener_thread.start()

input_thread = threading.Thread(target=handle_input)
input_thread.start()
