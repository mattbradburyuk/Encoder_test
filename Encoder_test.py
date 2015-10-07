""" test file for encoders

@ author Matthew Bradbury
@ date: 05/10/2015

add test change

"""

from __future__ import division
import sys
import time
import re
import socket
import threading
import numpy as np

import MBTimer as mbt

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.ADC as ADC

# Constants
LEFT = 0
RIGHT = 1
MIN = 0
MAX = 1
    

class Encoder_test():
    
	# === Class Properties ===
    # Parameters

    test_prop = 'hello world'

    # collection of test results
    results_ind = 0
    results = None

    # Pins
    ledPin = 'USR1'

    # Motor Pins -- (LEFT, RIGHT)
    dir1Pin = ('P8_14', 'P8_12')
    dir2Pin = ('P8_16', 'P8_10')
    pwmPin = ('P9_16', 'P9_14')

    # ADC Pins
    irPin = ('P9_38', 'P9_40', 'P9_36', 'P9_35', 'P9_33')
    encoderPin = ('P9_39', 'P9_37')



    # Constraints
    pwmLimits = [-100, 100]  # [min, max]

    # State PWM -- (LEFT, RIGHT)
    pwm = [0, 0]


    # === Class Methods ===
    # Constructor
    def __init__(self):
    	sys.stdout.write("initialising class\n\n")

    	# Initialize GPIO pins
        GPIO.setup(self.dir1Pin[LEFT], GPIO.OUT)
        GPIO.setup(self.dir2Pin[LEFT], GPIO.OUT)
        GPIO.setup(self.dir1Pin[RIGHT], GPIO.OUT)
        GPIO.setup(self.dir2Pin[RIGHT], GPIO.OUT)

        GPIO.setup(self.ledPin, GPIO.OUT)

        # Initialize PWM pins: PWM.start(channel, duty, freq=2000, polarity=0)
        PWM.start(self.pwmPin[LEFT], 0)
        PWM.start(self.pwmPin[RIGHT], 0)

        # Set motor speed to 0
        self.setPWM([0, 0])

        # Initialize ADC
        ADC.setup()

    
    def run_test(self):

        test_duration = 1
        sample_time = 0.005

        samples = test_duration/ sample_time

        print samples
        
        self.results = np.zeros((samples,4))

        # move robot forward

        self.setPWM([100,100])        

        # start ADC reading

        test_timer = mbt.MBTimer(sample_time,self.read_adc)
        
        print "Start timer"
        test_timer.start()



        # wait for 2 seconds
        time.sleep(test_duration)

        # stop robot

        self.setPWM([0,0])
        # stop ADC reading

        
        test_timer.isRunning = False
        print "Stop timer"

        # stop robot

        self.setPWM([0,0])


        # write out the results 


        
        
        for x in range(0,self.results_ind):
            r0 = self.results[x,0]
            r1 = self.results[x,1]
            r2 = self.results[x,2]
            r3 = self.results[x,3] 

            print '{0:4.0f} {1:2.5f} {2:4.0f} {3:4.0f} '.format(r0,r1,r2,r3)


    def read_adc(self):
        
        l_value = ADC.read_raw(self.encoderPin[LEFT])
        r_value = ADC.read_raw(self.encoderPin[RIGHT])

        self.results[self.results_ind,0] = self.results_ind
        self.results[self.results_ind,1] = time.time()
        self.results[self.results_ind,2] = l_value
        self.results[self.results_ind,3] = r_value

        self.results_ind = self.results_ind + 1

        # print 'hello world'
        # print 'left value: ', l_value, ' right value: ', r_value


    # def move(self):
    # 	sys.stdout.write("moving quickbot forwards")

    # 	setPWM([100,100])



    	    # Getters and Setters
    def setPWM(self, pwm):
        # [leftSpeed, rightSpeed]: 0 is off, caps at min and max values

        self.pwm[LEFT] = min(
            max(pwm[LEFT], self.pwmLimits[MIN]), self.pwmLimits[MAX])
        self.pwm[RIGHT] = min(
            max(pwm[RIGHT], self.pwmLimits[MIN]), self.pwmLimits[MAX])

        # Left motor
        if self.pwm[LEFT] > 0:
            GPIO.output(self.dir1Pin[LEFT], GPIO.LOW)
            GPIO.output(self.dir2Pin[LEFT], GPIO.HIGH)
            PWM.set_duty_cycle(self.pwmPin[LEFT], abs(self.pwm[LEFT]))
        elif self.pwm[LEFT] < 0:
            GPIO.output(self.dir1Pin[LEFT], GPIO.HIGH)
            GPIO.output(self.dir2Pin[LEFT], GPIO.LOW)
            PWM.set_duty_cycle(self.pwmPin[LEFT], abs(self.pwm[LEFT]))
        else:
            GPIO.output(self.dir1Pin[LEFT], GPIO.LOW)
            GPIO.output(self.dir2Pin[LEFT], GPIO.LOW)
            PWM.set_duty_cycle(self.pwmPin[LEFT], 0)

        # Right motor
        if self.pwm[RIGHT] > 0:
            GPIO.output(self.dir1Pin[RIGHT], GPIO.LOW)
            GPIO.output(self.dir2Pin[RIGHT], GPIO.HIGH)
            PWM.set_duty_cycle(self.pwmPin[RIGHT], abs(self.pwm[RIGHT]))
        elif self.pwm[RIGHT] < 0:
            GPIO.output(self.dir1Pin[RIGHT], GPIO.HIGH)
            GPIO.output(self.dir2Pin[RIGHT], GPIO.LOW)
            PWM.set_duty_cycle(self.pwmPin[RIGHT], abs(self.pwm[RIGHT]))
        else:
            GPIO.output(self.dir1Pin[RIGHT], GPIO.LOW)
            GPIO.output(self.dir2Pin[RIGHT], GPIO.LOW)
            PWM.set_duty_cycle(self.pwmPin[RIGHT], 0)





