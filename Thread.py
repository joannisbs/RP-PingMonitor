
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


class ThreadloopSBCP(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopSBCP()


class ThreadloopPredman(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopPredman()

class ThreadloopOlimpark(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		loopOlimpark()




def loopOlimpark():
	print "Inicio do Servico da Olimpark"
	while(1):
		Info.Olimpark.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaOlimpark()
		if Controle.Stop : break 
	Flag.quit = True



def loopPredman():
	print "Inicio do Servico da Predman"
	while(1):
		TestaPredman()
		if Controle.Stop : break 
	Flag.quit = True



def loopSBCP():
	print "Inicio do Servico da SBCP"
	while(1):
		
		TestaSBCP()
		if Controle.Stop : break 
	Flag.quit = True




def loopElRio():
	print "Inicio do Servico da El Rio"
	while(1):
		Info.ElRio.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaElRio()
		if Controle.Stop : break 
	Flag.quit = True



def loopLotten():
	print "Inicio do Servico da Lotten"
	while(1):
		Info.Lotten.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaLotten()
		
		if Controle.Stop : break 
	Flag.quit = True





def loopGrupoNk():
	print "Inicio do Servico do Grupo Nk"
	while(1):
		Info.GrupoNk.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaGrupoNk()
		if Controle.Stop : break 
	Flag.quit = True


def loopGravex():
	print "Inicio do Servico da Gravex"
	while(1):
		Info.Gravex.Status.Horaultima = "Hora: " + GetTime().horaminuto()
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
		Info.BestInClass.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaBestInClass()
		if Controle.Stop : break 
	Flag.quit = True


def loopCasaCristo():
	print "Inicio do Servico da CasaCristo"
	while(1):
		Info.CasaCristo.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaCasCristo()
		#Info.CasaCristo.Status.Horaultima = "10:30"
		if Controle.Stop : break 
		time.sleep(60)
	Flag.quit = True


def loopIsoRadio():
	print "Inicio do Servico da Iso Radiologia"
	while(1):
		Info.IsoRadio.Status.Horaultima = "Hora: " + GetTime().horaminuto()
		TestaIsoRadio()
		if Controle.Stop : break 
	Flag.quit = True
