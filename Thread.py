
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

class ThreadloopGravex(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopGravex()

class ThreadloopGrupoNk(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopGrupoNk()


class ThreadloopLotten(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopLotten()





class ThreadloopElRio(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopElRio()




def loopElRio():
	print "Inicio do Servico da El Rio"
	while(1):
		TestaElRio()
		if Controle.Stop : break 
	Flag.quit = True





def loopLotten():
	print "Inicio do Servico da Lotten"
	while(1):
		TestaLotten()
		if Controle.Stop : break 
	Flag.quit = True





def loopGrupoNk():
	print "Inicio do Servico do Grupo Nk"
	while(1):
		TestaGrupoNk()
		if Controle.Stop : break 
	Flag.quit = True


def loopGravex():
	print "Inicio do Servico da Gravex"
	while(1):
		TestaGravex()
		if Controle.Stop : break 
		time.sleep(60)
	Flag.quit = True


def loopLaser():
	print "Inicio do Servico da Laser"
	while(1):
		TestaLaser()
		if Controle.Stop : break 
		time.sleep(100)
	Flag.quit = True


def loopBuilding():
	print "Inicio do Servico da Building"
	while(1):
		TestaBuilding()
		if Controle.Stop : break 
		time.sleep(100)
		#TestaCasCristo()
		#if Controle.Stop : break 
	Flag.quit = True


def loopBestInClass():
	print "Inicio do Servico da Best In Class"
	while(1):
		TestaBestInClass()
		if Controle.Stop : break 
	Flag.quit = True


def loopCasaCristo():
	print "Inicio do Servico da CasaCristo"
	while(1):
		TestaCasCristo()
		if Controle.Stop : break 
		time.sleep(60)
	Flag.quit = True


def loopIsoRadio():
	print "Inicio do Servico da Iso Radiologia"
	while(1):
		TestaIsoRadio()
		if Controle.Stop : break 
	Flag.quit = True
