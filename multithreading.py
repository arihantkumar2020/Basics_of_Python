#thread = a small lightweight single process
#1 thread is always be there even if we dont create it explicitly, called main thread
from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(2):
            print('hello')
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(2):
            print('hi')
            sleep(1)


t1 = Hello()
t2 = Hi()


#here 3 threads exists, main t1 and t2
t1.start()
sleep(0.2)
t2.start()

#by using join, main thread only run after t1 and t2
t1.join()
t2.join()

print('bye')