__author__ = 'Avantha'
import threading

class AvanthaMessages(threading.Thread):
    def run(self):
        for _ in range(10):# thius ignores a variable but loop for 10 times
            print(threading.current_thread().getName())

x = AvanthaMessages(name='Send out messages')
y = AvanthaMessages(name='Receive messages')
x.start()
y.start()

