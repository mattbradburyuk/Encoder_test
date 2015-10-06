
import MBTimer as mbt
import time

def myfunc1():
	print "Timer tick 1"

def myfunc2():
    print "Timer tick 2"



t1 = mbt.MBTimer(1,myfunc1)
t2 = mbt.MBTimer(3,myfunc2)

t1.start()
t2.start()

time.sleep(10)

t1.isRunning = False
t2.isRunning = False
