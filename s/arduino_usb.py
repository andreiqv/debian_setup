#!/usr/bin/python
#coding=utf-8
# for python2
import os
usb0 = '/dev/ttyUSB0';
usb1 = '/dev/ttyUSB1';
if os.path.exists(usb0):
	print(usb0, end='');
else:
	print(usb1, end='');

