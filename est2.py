#!/usr/bin/python

from sys import stdout
import time
from threading import Timer


z = None
if z:
	print 'z'
z = 1
if not z:
	print 'z'