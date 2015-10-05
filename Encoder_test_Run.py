
from Encoder_test import *
import time

print "Running Encoder_test"

ET = Encoder_test()

print "setPWM to [100,100]"

ET.setPWM([100,100])

t_end = time.time() + 2



while time.time() < t_end:

    pass

print "setPWM to [0,0]"

ET.setPWM([0,0])