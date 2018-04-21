
import threading
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
