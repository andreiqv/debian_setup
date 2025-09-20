#!/usr/bin/python
#coding=utf-8

ram_dir = '/ram/tmp'

import sys
import os
from tkinter import *

cmd = ''
for k in range(1,len(sys.argv)): 
	cmd = cmd + sys.argv[k] + ' '
	
if len(os.listdir(ram_dir))==0:
	os.system(cmd)
	sys.exit()

# иначе:

def press_yes():
	#print('You have pressed YES')
	#print(str)
	os.system(cmd)
	sys.exit()

def press_no():
	#print('You have pressed NO')
	sys.exit()
	
root = Tk()
Label(root, text=ram_dir+' is not empty. Continue?').pack(side=TOP)
Button(root, text='YES', command=press_yes).pack(side=LEFT)
Button(root, text='NO', command=press_no).pack(side=RIGHT)
root.mainloop()


