#!/bin/python2

import os
import random
tone=random.randrange(50,8000)
print tone
play_synth = "play -n synth .5 sine %s fade h 0.1 1 0.1" % (tone)
os.system(play_synth)

guess_tone = int(raw_input("guess the tone:"))

if guess_tone == tone:
	print "correct"
	print "%sHz" % (tone)
else:
	print "no"
	print "%sHz" % (tone)
