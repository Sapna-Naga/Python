# Multithreading:

class Hello:
              def run(self):
                             for i in range(5):
                                           print("Hello")

class Hi:
              def run(self):
                             for i in range(5):
                                           print("hi")
                                           
thread1=Hello()
thread2=Hi()

t1.run()
t2.run()
#this is not running simultaneously.


# to execute simultaneously & to run 2 thread:
from time import sleep
from threading import *

class Hello(Thread):
              def run(self):
                             for i in range(5):
                                           print("Hello")
                                           sleep(1)
                                           
class Hi(Thread):
              def run(self):
                             for in in range(5):
                                           print("Hi")
                                           sleep(1)

thread1=Hello()
thread2=Hi()

thread1.start()
sleep(0.2) #a time gap
thread2.start()

thread1.join()
thread2.join() 

print("End of execution")
