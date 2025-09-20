"""
Python2
Main python script that start all others scripts.
"""
import os
import time
time.sleep(1)
#os.system('mkdir -p /ram/var')
#os.system('python2 /w/WORK/python/web/get_count.py&')
while(True):
	os.system('python2 /s/python_meteo/meteo.py')
	time.sleep(60)
