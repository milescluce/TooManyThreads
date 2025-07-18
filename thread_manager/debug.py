import time

from thread_manager import ThreadedServer

app = ThreadedServer()

app.thread.start()
time.sleep(100)