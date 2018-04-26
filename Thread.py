
import threading
import time

from TestFuncions import *


class ThreadloopBuilding(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopBuilding()

class ThreadloopBestInClass(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopBestInClass()

class ThreadloopCasaCristo(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopCasaCristo()

class ThreadloopIsoRadio(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopIsoRadio()

class ThreadloopLaser(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopLaser()


def loopLaser():
	while(1):
		TestaLaser()
		if Controle.Stop : break 


def loopBuilding():

	while(1):
		TestaBuilding()
		if Controle.Stop : break 
		time.sleep(100)
		#TestaCasCristo()
		#if Controle.Stop : break 

def loopBestInClass():
	while(1):
		TestaBestInClass()
		if Controle.Stop : break 

def loopCasaCristo():

	while(1):
		
		TestaCasCristo()
		if Controle.Stop : break 
		time.sleep(60)

def loopIsoRadio():

	while(1):
		
		TestaIsoRadio()
		if Controle.Stop : break 
		
