#!/bin/python

import sys
import os
from time import time

def timer(msg='', ls = [0,'']):
	if ls[0]:
		print('TIME: {0:.4f} sec. ({1})'.format(time() - ls[0], ls[1]))
	else:
		print('START TIMER {0}'.format(ls[1]))
	ls[0] = time()
	ls[1] = msg
	
#----------------


runtimer = False

#print('len(sys.argv) = {0}'.format(len(sys.argv)))
#print('sys.argv = {0}'.format(sys.argv))

if len(sys.argv) > 2:
	if sys.argv[2] == '-t':
		runtimer = True

csfile = sys.argv[1]
base = csfile.split('.')[0]
exefile = base + '.exe'

cmd1 = 'mcs {0}'.format(csfile)
os.system(cmd1)

if runtimer: 
	timer('time of running')

cmd1 = './{0}'.format(exefile)
os.system(cmd1)

if runtimer: timer()
