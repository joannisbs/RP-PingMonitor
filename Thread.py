
import threading
from TestFuncions import *


class Threadloop0(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loop0()

class Threadloop1(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loop1()

