import socket
import os
import shutil


from Var import *
from AtualizacaoEContagem import *

def TestaBuilding():
	if Controle.Stop : return
	TestaFuncion(Info.Building.Allianz.Empresa,
				Info.Building.Allianz.Relogio,
				Info.Building.Allianz.IP,
				Info.Building.Allianz.Porta)

	if Controle.Stop : return
	TestaFuncion(Info.Building.WTorre.Empresa,
				Info.Building.WTorre.Relogio,
				Info.Building.WTorre.IP,
				Info.Building.WTorre.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.Building.RioJaneiro.Empresa,
				Info.Building.RioJaneiro.Relogio,
				Info.Building.RioJaneiro.IP,
				Info.Building.RioJaneiro.Porta)

def TestaCasCristo():

	TestaFuncion(Info.CasaCristo.ADM.Empresa,
				Info.CasaCristo.ADM.Relogio,
				Info.CasaCristo.ADM.IP,
				Info.CasaCristo.ADM.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.CasaCristo.CEI1.Empresa,
				Info.CasaCristo.CEI1.Relogio,
				Info.CasaCristo.CEI1.IP,
				Info.CasaCristo.CEI1.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.CasaCristo.CEI2.Empresa,
				Info.CasaCristo.CEI2.Relogio,
				Info.CasaCristo.CEI2.IP,
				Info.CasaCristo.CEI2.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.CasaCristo.CEI3.Empresa,
				Info.CasaCristo.CEI3.Relogio,
				Info.CasaCristo.CEI3.IP,
				Info.CasaCristo.CEI3.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.CasaCristo.VovoMatilde.Empresa,
				Info.CasaCristo.VovoMatilde.Relogio,
				Info.CasaCristo.VovoMatilde.IP,
				Info.CasaCristo.VovoMatilde.Porta)
	if Controle.Stop : return

def TestaBestInClass():

	TestaFuncion(Info.BestInClass.Recife.Empresa,
				Info.BestInClass.Recife.Relogio,
				Info.BestInClass.Recife.IP,
				Info.BestInClass.Recife.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Itaquera.Empresa,
				Info.BestInClass.Itaquera.Relogio,
				Info.BestInClass.Itaquera.IP,
				Info.BestInClass.Itaquera.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Itapevi.Empresa,
				Info.BestInClass.Itapevi.Relogio,
				Info.BestInClass.Itapevi.IP,
				Info.BestInClass.Itapevi.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Sorocaba.Empresa,
				Info.BestInClass.Sorocaba.Relogio,
				Info.BestInClass.Sorocaba.IP,
				Info.BestInClass.Sorocaba.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.SeteLagoas.Empresa,
				Info.BestInClass.SeteLagoas.Relogio,
				Info.BestInClass.SeteLagoas.IP,
				Info.BestInClass.SeteLagoas.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Curitiba.Empresa,
				Info.BestInClass.Curitiba.Relogio,
				Info.BestInClass.Curitiba.IP,
				Info.BestInClass.Curitiba.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Fsantana.Empresa,
				Info.BestInClass.Fsantana.Relogio,
				Info.BestInClass.Fsantana.IP,
				Info.BestInClass.Fsantana.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Itu.Empresa,
				Info.BestInClass.Itu.Relogio,
				Info.BestInClass.Itu.IP,
				Info.BestInClass.Itu.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Guarulhos.Empresa,
				Info.BestInClass.Guarulhos.Relogio,
				Info.BestInClass.Guarulhos.IP,
				Info.BestInClass.Guarulhos.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Itaporanga.Empresa,
				Info.BestInClass.Itaporanga.Relogio,
				Info.BestInClass.Itaporanga.IP,
				Info.BestInClass.Itaporanga.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.BestInClass.Linhares.Empresa,
				Info.BestInClass.Linhares.Relogio,
				Info.BestInClass.Linhares.IP,
				Info.BestInClass.Linhares.Porta)
	if Controle.Stop : return


def TestaIsoRadio():



	TestaFuncion(Info.IsoRadio.Santana.Empresa,
				Info.IsoRadio.Santana.Relogio,
				Info.IsoRadio.Santana.IP,
				Info.IsoRadio.Santana.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.SaoMatheus.Empresa,
				Info.IsoRadio.SaoMatheus.Relogio,
				Info.IsoRadio.SaoMatheus.IP,
				Info.IsoRadio.SaoMatheus.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.VilaMariana.Empresa,
				Info.IsoRadio.VilaMariana.Relogio,
				Info.IsoRadio.VilaMariana.IP,
				Info.IsoRadio.VilaMariana.Porta)
	if Controle.Stop : return


	TestaFuncion(Info.IsoRadio.Lapa.Empresa,
				Info.IsoRadio.Lapa.Relogio,
				Info.IsoRadio.Lapa.IP,
				Info.IsoRadio.Lapa.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.SAmaro.Empresa,
				Info.IsoRadio.SAmaro.Relogio,
				Info.IsoRadio.SAmaro.IP,
				Info.IsoRadio.SAmaro.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.CDutra.Empresa,
				Info.IsoRadio.CDutra.Relogio,
				Info.IsoRadio.CDutra.IP,
				Info.IsoRadio.CDutra.Porta)
	if Controle.Stop : return


	TestaFuncion(Info.IsoRadio.Tatuape.Empresa,
				Info.IsoRadio.Tatuape.Relogio,
				Info.IsoRadio.Tatuape.IP,
				Info.IsoRadio.Tatuape.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.CLimpo.Empresa,
				Info.IsoRadio.CLimpo.Relogio,
				Info.IsoRadio.CLimpo.IP,
				Info.IsoRadio.CLimpo.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.Ipiranga.Empresa,
				Info.IsoRadio.Ipiranga.Relogio,
				Info.IsoRadio.Ipiranga.IP,
				Info.IsoRadio.Ipiranga.Porta)
	if Controle.Stop : return

	TestaFuncion(Info.IsoRadio.AnaRosa.Empresa,
				Info.IsoRadio.AnaRosa.Relogio,
				Info.IsoRadio.AnaRosa.IP,
				Info.IsoRadio.AnaRosa.Porta)
	if Controle.Stop : return

	



def TestaFuncion(empresa2,relogio2,ip2,port2):

	testa = 4

	AtualizaCor(empresa2,relogio2,int(testa))
	Telas.GUI_Tela1 .update(empresa2,relogio2)
	
	Telas.GUI_Monitor.update()


	testa = TestaPorta(ip2,port2) 
	AtualizaCor(empresa2,relogio2,int(testa))
	Telas.GUI_Tela1 .update(empresa2,relogio2)
	

	Telas.GUI_Monitor.update()




def TestaPorta(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#print ip + " porta = " + port
	#print "Test Ping"

	if TestaPing(ip):

		try:
			s.connect((ip,int(port)))		
			s.close()
			return 3

		except:
			return 2

	else:
		return 1

def TestaPing(ip):
	resposta = os.system("ping " + ip + " -c 4")

	if resposta == 0 :
		#print "ping ok"
		return True
	else:
		#print "Falha ping"
		return False


#Atualiza a cor das variaveis. 
