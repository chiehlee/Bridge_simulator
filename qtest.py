#!/usr/bin/python

import threading
from threading import Timer
import time

def printit(n):
	t = Timer(0.5, printit, [k])
	t.start()
	c = 0
	while c < 10:
		print 'counting...', c
		c += 1
	if k == 10:
		t.cancel()
	print n


def printit2():
	threading.Timer(3.0, printit, [k]).start()
	print "Hello World!2"

k = 1

printit(k)


while True:
	print 'true'
	k = k + 1
	time.sleep(2)
	if k == 5:
		printit(3)
	if k == 20:
		printit(3)





