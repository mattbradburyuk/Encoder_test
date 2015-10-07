"""
Timer class to schedule a function every n seconds


"""
import time
import threading

class MBTimer(threading.Thread):

    # === Class Properties ===
    # Parameters

    interval = 0
    func = null = 0
    isRunning = True


    # === Class Methods ===
    # Constructor
    def __init__(self,interval, func):
        
        # Initialize thread
        threading.Thread.__init__(self)

        self.interval = interval
        self.func = func


        print self.interval
        print self.func



    # def start(self):
    #     print "starting timer"
    #     self.isRunning = True
    #     self.timer_loop()


    # def stop(self):
    #     print "stopping timer"
    #     self.isRunning = False

    def run(self):



        t_start = time.time()
        next_step = t_start + self.interval

        while self.isRunning is True:
            while time.time() < next_step:
                pass

            next_step = next_step + self.interval
            self.func()


    

