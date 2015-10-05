
from Encoder_test import *
import time

print "Running Encoder_test"

ET = Encoder_test()

print "setPWM to [100,100]"

ET.setPWM([100,100])

t_end = time.time() + 2

a = 0

while time.time() < t_end:

    a = a + 1

print "setPWM to [0,0]"

ET.setPWM([0,0])