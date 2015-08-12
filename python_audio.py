#!/bin/python2

import os
import random
tone=random.randrange(50,17000)
print tone
play_synth = "play -n synth .5 sine %s fade h 0.1 1 0.1" % (tone)
os.system(play_synth)

