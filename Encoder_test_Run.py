
from Encoder_test import *
import time

print "Running Encoder_test"

ET = Encoder_test()

ET.setPWM([100,100])

t_end = time.time() + 60

while time.time() < t_end:

	a = a + 1

ET.setPWM([0,0])