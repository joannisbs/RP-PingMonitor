import socket
import os
import shutil


from Var import *


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


def TestaFuncion(empresa2,relogio2,ip2,port2):

	testa = 4

	AtualizaCor(empresa2,relogio2,int(testa))
	Telas.Tela1 .update(empresa2,relogio2)

	testa = TestaPorta(ip2,port2) 
	AtualizaCor(empresa2,relogio2,int(testa))
	Telas.Tela1 .update(empresa2,relogio2)


def loop0():

	while(1):
		TestaBuilding()
		if Controle.Stop : break 
		TestaCasCristo()
		if Controle.Stop : break 

def loop1():
	while(1):
		TestaBestInClass()
		if Controle.Stop : break 



def leBanco():


	listaping = open("lista_relogio.csv","r")
	
	data = listaping.readlines()[1:]

	listaping.close()

	for line in data:

		word              = line.split(",")
		empresa_lido      = word[0] 
		relogio_lido      = word[1]
		ip_lido   	      = word[2]
		port_lido         = word[3]
		NumeroReP_Lido    = word[4]
		Responsavel_Lido  = word[5]
		Telefone_Lido     = word[6]


	######################################################### BUILDING #################################################

		if empresa_lido == "building":


			if relogio_lido == "allianz":
				
				Info.Building.Allianz.Empresa               = empresa_lido
				Info.Building.Allianz.Relogio               = relogio_lido
				Info.Building.Allianz.IP                    = ip_lido
				Info.Building.Allianz.Porta                 = port_lido
				Info.Building.Allianz.NumeroRep             = NumeroReP_Lido
				Info.Building.Allianz.Responsavel           = Responsavel_Lido
				Info.Building.Allianz.Telefone              = Telefone_Lido


			elif relogio_lido == "wtorre":

				Info.Building.WTorre.Empresa                = empresa_lido
				Info.Building.WTorre.Relogio                = relogio_lido
				Info.Building.WTorre.IP                     = ip_lido
				Info.Building.WTorre.Porta                  = port_lido
				Info.Building.WTorre.NumeroRep              = NumeroReP_Lido
				Info.Building.WTorre.Responsavel            = Responsavel_Lido
				Info.Building.WTorre.Telefone               = Telefone_Lido
				


			elif relogio_lido == "riojaneiro":


				Info.Building.RioJaneiro.Empresa            = empresa_lido
				Info.Building.RioJaneiro.Relogio            = relogio_lido
				Info.Building.RioJaneiro.IP                 = ip_lido
				Info.Building.RioJaneiro.Porta              = port_lido
				Info.Building.RioJaneiro.NumeroRep          = NumeroReP_Lido
				Info.Building.RioJaneiro.Responsavel        = Responsavel_Lido
				Info.Building.RioJaneiro.Telefone           = Telefone_Lido


	######################################################### GRAVEX ###################################################

		elif empresa_lido == "gravex":

			if relogio_lido == "adm":

			
				Info.Gravex.ADM.Empresa                    = empresa_lido
				Info.Gravex.ADM.Relogio                    = relogio_lido
				Info.Gravex.ADM.IP                         = ip_lido
				Info.Gravex.ADM.Porta                      = port_lido
				Info.Gravex.ADM.NumeroRep                  = NumeroReP_Lido
				Info.Gravex.ADM.Responsavel                = Responsavel_Lido
				Info.Gravex.ADM.Telefone                   = Telefone_Lido



			elif relogio_lido == "loja":


				Info.Gravex.Loja1.Empresa                   = empresa_lido
				Info.Gravex.Loja1.Relogio                   = relogio_lido
				Info.Gravex.Loja1.IP                        = ip_lido
				Info.Gravex.Loja1.Porta                     = port_lido
				Info.Gravex.Loja1.NumeroRep                 = NumeroReP_Lido
				Info.Gravex.Loja1.Responsavel               = Responsavel_Lido
				Info.Gravex.Loja1.Telefone                  = Telefone_Lido


			elif relogio_lido == "mimarcos":


				Info.Gravex.MiMarcos.Empresa                = empresa_lido
				Info.Gravex.MiMarcos.Relogio                = relogio_lido
				Info.Gravex.MiMarcos.IP                     = ip_lido
				Info.Gravex.MiMarcos.Porta                  = port_lido
				Info.Gravex.MiMarcos.NumeroRep              = NumeroReP_Lido
				Info.Gravex.MiMarcos.Responsavel            = Responsavel_Lido
				Info.Gravex.MiMarcos.Telefone               = Telefone_Lido


			elif relogio_lido == "dantchini":

				Info.Gravex.DantChini.Empresa               = empresa_lido
				Info.Gravex.DantChini.Relogio               = relogio_lido
				Info.Gravex.DantChini.IP                    = ip_lido
				Info.Gravex.DantChini.Porta                 = port_lido
				Info.Gravex.DantChini.NumeroRep             = NumeroReP_Lido
				Info.Gravex.DantChini.Responsavel           = Responsavel_Lido
				Info.Gravex.DantChini.Telefone              = Telefone_Lido


	########################################################## LASER ###################################################


		elif empresa_lido == "laser":
			if relogio_lido == "instituto":

				Info.Laser.Instituto.Empresa                = empresa_lido
				Info.Laser.Instituto.Relogio                = relogio_lido
				Info.Laser.Instituto.IP                     = ip_lido
				Info.Laser.Instituto.Porta                  = port_lido
				Info.Laser.Instituto.NumeroRep              = NumeroReP_Lido
				Info.Laser.Instituto.Responsavel            = Responsavel_Lido
				Info.Laser.Instituto.Telefone               = Telefone_Lido


			elif relogio_lido == "academia":

				Info.Laser.Academia.Empresa                = empresa_lido
				Info.Laser.Academia.Relogio                = relogio_lido
				Info.Laser.Academia.IP                     = ip_lido
				Info.Laser.Academia.Porta                  = port_lido
				Info.Laser.Academia.NumeroRep              = NumeroReP_Lido
				Info.Laser.Academia.Responsavel            = Responsavel_Lido
				Info.Laser.Academia.Telefone               = Telefone_Lido


	######################################################### CASA CRISTO ##############################################


		elif empresa_lido == "casacristo":

			if relogio_lido == "adm":

				Info.CasaCristo.ADM.Empresa                = empresa_lido
				Info.CasaCristo.ADM.Relogio                = relogio_lido
				Info.CasaCristo.ADM.IP                     = ip_lido
				Info.CasaCristo.ADM.Porta                  = port_lido
				Info.CasaCristo.ADM.NumeroRep              = NumeroReP_Lido
				Info.CasaCristo.ADM.Responsavel            = Responsavel_Lido
				Info.CasaCristo.ADM.Telefone               = Telefone_Lido

			elif relogio_lido == "cei1":

				Info.CasaCristo.CEI1.Empresa               = empresa_lido
				Info.CasaCristo.CEI1.Relogio               = relogio_lido
				Info.CasaCristo.CEI1.IP                    = ip_lido
				Info.CasaCristo.CEI1.Porta                 = port_lido
				Info.CasaCristo.CEI1.NumeroRep             = NumeroReP_Lido
				Info.CasaCristo.CEI1.Responsavel           = Responsavel_Lido
				Info.CasaCristo.CEI1.Telefone              = Telefone_Lido


			elif relogio_lido == "cei2":

				Info.CasaCristo.CEI2.Empresa               = empresa_lido
				Info.CasaCristo.CEI2.Relogio               = relogio_lido
				Info.CasaCristo.CEI2.IP                    = ip_lido
				Info.CasaCristo.CEI2.Porta                 = port_lido
				Info.CasaCristo.CEI2.NumeroRep             = NumeroReP_Lido
				Info.CasaCristo.CEI2.Responsavel           = Responsavel_Lido
				Info.CasaCristo.CEI2.Telefone              = Telefone_Lido


			elif relogio_lido == "cei3":

				Info.CasaCristo.CEI3.Empresa               = empresa_lido
				Info.CasaCristo.CEI3.Relogio               = relogio_lido
				Info.CasaCristo.CEI3.IP                    = ip_lido
				Info.CasaCristo.CEI3.Porta                 = port_lido
				Info.CasaCristo.CEI3.NumeroRep             = NumeroReP_Lido
				Info.CasaCristo.CEI3.Responsavel           = Responsavel_Lido
				Info.CasaCristo.CEI3.Telefone              = Telefone_Lido

			elif relogio_lido == "vovomatilde":

				Info.CasaCristo.VovoMatilde.Empresa        = empresa_lido
				Info.CasaCristo.VovoMatilde.Relogio        = relogio_lido
				Info.CasaCristo.VovoMatilde.IP             = ip_lido
				Info.CasaCristo.VovoMatilde.Porta          = port_lido
				Info.CasaCristo.VovoMatilde.NumeroRep      = NumeroReP_Lido
				Info.CasaCristo.VovoMatilde.Responsavel    = Responsavel_Lido
				Info.CasaCristo.VovoMatilde.Telefone       = Telefone_Lido


	######################################################### BEST IN CLASS ############################################


		elif empresa_lido == "bestinclass":
			if relogio_lido == "recife":

				Info.BestInClass.Recife.Empresa            = empresa_lido
				Info.BestInClass.Recife.Relogio            = relogio_lido
				Info.BestInClass.Recife.IP                 = ip_lido
				Info.BestInClass.Recife.Porta              = port_lido
				Info.BestInClass.Recife.NumeroRep          = NumeroReP_Lido
				Info.BestInClass.Recife.Responsavel        = Responsavel_Lido
				Info.BestInClass.Recife.Telefone           = Telefone_Lido


			elif relogio_lido == "itaquera":

				Info.BestInClass.Itaquera.Empresa           = empresa_lido
				Info.BestInClass.Itaquera.Relogio           = relogio_lido
				Info.BestInClass.Itaquera.IP                = ip_lido
				Info.BestInClass.Itaquera.Porta             = port_lido
				Info.BestInClass.Itaquera.NumeroRep         = NumeroReP_Lido
				Info.BestInClass.Itaquera.Responsavel       = Responsavel_Lido
				Info.BestInClass.Itaquera.Telefone          = Telefone_Lido

			elif relogio_lido == "itapevi":

				Info.BestInClass.Itapevi.Empresa            = empresa_lido
				Info.BestInClass.Itapevi.Relogio            = relogio_lido
				Info.BestInClass.Itapevi.IP                 = ip_lido
				Info.BestInClass.Itapevi.Porta              = port_lido
				Info.BestInClass.Itapevi.NumeroRep          = NumeroReP_Lido
				Info.BestInClass.Itapevi.Responsavel        = Responsavel_Lido
				Info.BestInClass.Itapevi.Telefone           = Telefone_Lido


			elif relogio_lido == "sorocaba":

				Info.BestInClass.Sorocaba.Empresa           = empresa_lido
				Info.BestInClass.Sorocaba.Relogio           = relogio_lido
				Info.BestInClass.Sorocaba.IP                = ip_lido
				Info.BestInClass.Sorocaba.Porta             = port_lido
				Info.BestInClass.Sorocaba.NumeroRep         = NumeroReP_Lido
				Info.BestInClass.Sorocaba.Responsavel       = Responsavel_Lido
				Info.BestInClass.Sorocaba.Telefone          = Telefone_Lido

			elif relogio_lido == "setelagoas":

				Info.BestInClass.SeteLagoas.Empresa         = empresa_lido
				Info.BestInClass.SeteLagoas.Relogio         = relogio_lido
				Info.BestInClass.SeteLagoas.IP              = ip_lido
				Info.BestInClass.SeteLagoas.Porta           = port_lido
				Info.BestInClass.SeteLagoas.NumeroRep       = NumeroReP_Lido
				Info.BestInClass.SeteLagoas.Responsavel     = Responsavel_Lido
				Info.BestInClass.SeteLagoas.Telefone        = Telefone_Lido


			elif relogio_lido == "curitiba":

				Info.BestInClass.Curitiba.Empresa           = empresa_lido
				Info.BestInClass.Curitiba.Relogio           = relogio_lido
				Info.BestInClass.Curitiba.IP                = ip_lido
				Info.BestInClass.Curitiba.Porta             = port_lido
				Info.BestInClass.Curitiba.NumeroRep         = NumeroReP_Lido
				Info.BestInClass.Curitiba.Responsavel       = Responsavel_Lido
				Info.BestInClass.Curitiba.Telefone          = Telefone_Lido

			elif relogio_lido == "fsant":

				Info.BestInClass.Fsantana.Empresa               = empresa_lido
				Info.BestInClass.Fsantana.Relogio               = relogio_lido
				Info.BestInClass.Fsantana.IP                    = ip_lido
				Info.BestInClass.Fsantana.Porta                 = port_lido
				Info.BestInClass.Fsantana.NumeroRep             = NumeroReP_Lido
				Info.BestInClass.Fsantana.Responsavel           = Responsavel_Lido
				Info.BestInClass.Fsantana.Telefone              = Telefone_Lido


			elif relogio_lido == "itu":

				Info.BestInClass.Itu.Empresa                = empresa_lido
				Info.BestInClass.Itu.Relogio                = relogio_lido
				Info.BestInClass.Itu.IP                     = ip_lido
				Info.BestInClass.Itu.Porta                  = port_lido
				Info.BestInClass.Itu.NumeroRep              = NumeroReP_Lido
				Info.BestInClass.Itu.Responsavel            = Responsavel_Lido
				Info.BestInClass.Itu.Telefone               = Telefone_Lido


			elif relogio_lido == "guarulhos":

				Info.BestInClass.Guarulhos.Empresa          = empresa_lido
				Info.BestInClass.Guarulhos.Relogio          = relogio_lido
				Info.BestInClass.Guarulhos.IP               = ip_lido
				Info.BestInClass.Guarulhos.Porta            = port_lido
				Info.BestInClass.Guarulhos.NumeroRep        = NumeroReP_Lido
				Info.BestInClass.Guarulhos.Responsavel      = Responsavel_Lido
				Info.BestInClass.Guarulhos.Telefone         = Telefone_Lido

			elif relogio_lido == "itaporanga":

				Info.BestInClass.Itaporanga.Empresa         = empresa_lido
				Info.BestInClass.Itaporanga.Relogio         = relogio_lido
				Info.BestInClass.Itaporanga.IP              = ip_lido
				Info.BestInClass.Itaporanga.Porta           = port_lido
				Info.BestInClass.Itaporanga.NumeroRep       = NumeroReP_Lido
				Info.BestInClass.Itaporanga.Responsavel     = Responsavel_Lido
				Info.BestInClass.Itaporanga.Telefone        = Telefone_Lido


			elif relogio_lido == "linhares":

				Info.BestInClass.Linhares.Empresa           = empresa_lido
				Info.BestInClass.Linhares.Relogio           = relogio_lido
				Info.BestInClass.Linhares.IP                = ip_lido
				Info.BestInClass.Linhares.Porta             = port_lido
				Info.BestInClass.Linhares.NumeroRep         = NumeroReP_Lido
				Info.BestInClass.Linhares.Responsavel       = Responsavel_Lido
				Info.BestInClass.Linhares.Telefone          = Telefone_Lido



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
def AtualizaCor(empresa,relogio,result):

	######################################################### BUILDING #################################################

	if empresa == "building":

		if relogio == "allianz":
			
			if result == 1:
				Info.Building.Allianz.ModuloCor  = "red"
				Info.Building.Allianz.RelogioCor = "red"
			elif result == 2:
				Info.Building.Allianz.ModuloCor  = "green"
				Info.Building.Allianz.RelogioCor = "red"
			elif result == 3:
				Info.Building.Allianz.ModuloCor  = "green"
				Info.Building.Allianz.RelogioCor = "green"
			elif result == 4:
				Info.Building.Allianz.ModuloCor  = "blue"
				Info.Building.Allianz.RelogioCor = "blue"
			else:
				Info.Building.Allianz.ModuloCor  = "pink"
				Info.Building.Allianz.RelogioCor = "pink"




		elif relogio == "wtorre":


			if result == 1:
				Info.Building.WTorre.ModuloCor  = "red"
				Info.Building.WTorre.RelogioCor = "red"
			elif result == 2:
				Info.Building.WTorre.ModuloCor  = "green"
				Info.Building.WTorre.RelogioCor = "red"
			elif result == 3:
				Info.Building.WTorre.ModuloCor  = "green"
				Info.Building.WTorre.RelogioCor = "green"
			elif result == 4:
				Info.Building.WTorre.ModuloCor  = "blue"
				Info.Building.WTorre.RelogioCor = "blue"
			else:
				Info.Building.WTorre.ModuloCor  = "pink"
				Info.Building.WTorre.RelogioCor = "pink"



		elif relogio == "riojaneiro":

			if result == 1:
				Info.Building.RioJaneiro.ModuloCor  = "red"
				Info.Building.RioJaneiro.RelogioCor = "red"
			elif result == 2:
				Info.Building.RioJaneiro.ModuloCor  = "green"
				Info.Building.RioJaneiro.RelogioCor = "red"
			elif result == 3:
				Info.Building.RioJaneiro.ModuloCor  = "green"
				Info.Building.RioJaneiro.RelogioCor = "green"
			elif result == 4:
				Info.Building.RioJaneiro.ModuloCor  = "blue"
				Info.Building.RioJaneiro.RelogioCor = "blue"
			else:
				Info.Building.RioJaneiro.ModuloCor  = "pink"
				Info.Building.RioJaneiro.RelogioCor = "pink"
		
		if result != 4:
			Info.Building.Status.Contage = 0
			if Info.Building.Allianz.RelogioCor == "green" : 
					Info.Building.Status.Contage = Info.Building.Status.Contage +1
			if Info.Building.WTorre.RelogioCor == "green" : 
					Info.Building.Status.Contage = Info.Building.Status.Contage +1
			if Info.Building.RioJaneiro.RelogioCor == "green" : 
					Info.Building.Status.Contage = Info.Building.Status.Contage +1
			


	######################################################### GRAVEX ###################################################

	elif empresa == "gravex":
		if relogio == "adm":

			if result == 1:
				Info.Gravex.ADM.ModuloCor  = "red"
				Info.Gravex.ADM.RelogioCor = "red"
			elif result == 2:
				Info.Gravex.ADM.ModuloCor  = "green"
				Info.Gravex.ADM.RelogioCor = "red"
			elif result == 3:
				Info.Gravex.ADM.ModuloCor  = "green"
				Info.Gravex.ADM.RelogioCor = "green"
			elif result == 4:
				Info.Gravex.ADM.ModuloCor  = "blue"
				Info.Gravex.ADM.RelogioCor = "blue"
			else:
				Info.Gravex.ADM.ModuloCor  = "pink"
				Info.Gravex.ADM.RelogioCor = "pink"

		elif relogio == "loja":

			if result == 1:
				Info.Gravex.Loja1.ModuloCor  = "red"
				Info.Gravex.Loja1.RelogioCor = "red"
			elif result == 2:
				Info.Gravex.Loja1.ModuloCor  = "green"
				Info.Gravex.Loja1.RelogioCor = "red"
			elif result == 3:
				Info.Gravex.Loja1.ModuloCor  = "green"
				Info.Gravex.Loja1.RelogioCor = "green"
			elif result == 4:
				Info.Gravex.Loja1.ModuloCor  = "blue"
				Info.Gravex.Loja1.RelogioCor = "blue"
			else:
				Info.Gravex.Loja1.ModuloCor  = "pink"
				Info.Gravex.Loja1.RelogioCor = "pink"

		elif relogio == "mimarcos":

			if result == 1:
				Info.Gravex.MiMarcos.ModuloCor  = "red"
				Info.Gravex.Mimarcos.RelogioCor = "red"
			elif result == 2:
				Info.Gravex.Mimarcos.ModuloCor  = "green"
				Info.Gravex.Mimarcos.RelogioCor = "red"
			elif result == 3:
				Info.Gravex.Mimarcos.ModuloCor  = "green"
				Info.Gravex.Mimarcos.RelogioCor = "green"
			elif result == 4:
				Info.Gravex.Mimarcos.ModuloCor  = "blue"
				Info.Gravex.Mimarcos.RelogioCor = "blue"
			else:
				Info.Gravex.Mimarcos.ModuloCor  = "pink"
				Info.Gravex.Mimarcos.RelogioCor = "pink"

		elif relogio == "dantchini":
			if result == 1:
				Info.Gravex.DantChini.ModuloCor  = "red"
				Info.Gravex.DantChini.RelogioCor = "red"
			elif result == 2:
				Info.Gravex.DantChini.ModuloCor  = "green"
				Info.Gravex.DantChini.RelogioCor = "red"
			elif result == 3:
				Info.Gravex.DantChini.ModuloCor  = "green"
				Info.Gravex.DantChini.RelogioCor = "green"
			elif result == 4:
				Info.Gravex.DantChini.ModuloCor  = "blue"
				Info.Gravex.DantChini.RelogioCor = "blue"
			else:
				Info.Gravex.DantChini.ModuloCor  = "pink"
				Info.Gravex.DantChini.RelogioCor = "pink"

	########################################################## LASER ###################################################

	elif empresa == "laser":
		if relogio == "instituto":
			if result == 1:
				Info.Laser.Instituto.ModuloCor  = "red"
				Info.Laser.Instituto.RelogioCor = "red"
			elif result == 2:
				Info.Laser.Instituto.ModuloCor  = "green"
				Info.Laser.Instituto.RelogioCor = "red"
			elif result == 3:
				Info.Laser.Instituto.ModuloCor  = "green"
				Info.Laser.Instituto.RelogioCor = "green"
			elif result == 4:
				Info.Laser.Instituto.ModuloCor  = "blue"
				Info.Laser.Instituto.RelogioCor = "blue"
			else:
				Info.Laser.Instituto.ModuloCor  = "pink"
				Info.Laser.Instituto.RelogioCor = "pink"

		elif relogio == "academia":
			if result == 1:
				Info.Laser.Academia.ModuloCor  = "red"
				Info.Laser.Academia.RelogioCor = "red"
			elif result == 2:
				Info.Laser.Academia.ModuloCor  = "green"
				Info.Laser.Academia.RelogioCor = "red"
			elif result == 3:
				Info.Laser.Academia.ModuloCor  = "green"
				Info.Laser.Academia.RelogioCor = "green"
			elif result == 4:
				Info.Laser.Academia.ModuloCor  = "blue"
				Info.Laser.Academia.RelogioCor = "blue"
			else:
				Info.Laser.Academia.ModuloCor  = "pink"
				Info.Laser.Academia.RelogioCor = "pink"

	######################################################### CASA CRISTO ##############################################

	elif empresa == "casacristo":
	
		if relogio == "adm":
	
			if result == 1:
				Info.CasaCristo.ADM.ModuloCor  = "red"
				Info.CasaCristo.ADM.RelogioCor = "red"
			elif result == 2:
				Info.CasaCristo.ADM.ModuloCor  = "green"
				Info.CasaCristo.ADM.RelogioCor = "red"
			elif result == 3:
				Info.CasaCristo.ADM.ModuloCor  = "green"
				Info.CasaCristo.ADM.RelogioCor = "green"
			elif result == 4:
				Info.CasaCristo.ADM.ModuloCor  = "blue"
				Info.CasaCristo.ADM.RelogioCor = "blue"
			else:
				Info.CasaCristo.ADM.ModuloCor  = "pink"
				Info.CasaCristo.ADM.RelogioCor = "pink"

		elif relogio == "cei1":
	
			if result == 1:
				Info.CasaCristo.CEI1.ModuloCor  = "red"
				Info.CasaCristo.CEI1.RelogioCor = "red"
			elif result == 2:
				Info.CasaCristo.CEI1.ModuloCor  = "green"
				Info.CasaCristo.CEI1.RelogioCor = "red"
			elif result == 3:
				Info.CasaCristo.CEI1.ModuloCor  = "green"
				Info.CasaCristo.CEI1.RelogioCor = "green"
			elif result == 4:
				Info.CasaCristo.CEI1.ModuloCor  = "blue"
				Info.CasaCristo.CEI1.RelogioCor = "blue"
			else:
				Info.CasaCristo.CEI1.ModuloCor  = "pink"
				Info.CasaCristo.CEI1.RelogioCor = "pink"

		elif relogio == "cei2":
	
			if result == 1:
				Info.CasaCristo.CEI2.ModuloCor  = "red"
				Info.CasaCristo.CEI2.RelogioCor = "red"
			elif result == 2:
				Info.CasaCristo.CEI2.ModuloCor  = "green"
				Info.CasaCristo.CEI2.RelogioCor = "red"
			elif result == 3:
				Info.CasaCristo.CEI2.ModuloCor  = "green"
				Info.CasaCristo.CEI2.RelogioCor = "green"
			elif result == 4:
				Info.CasaCristo.CEI2.ModuloCor  = "blue"
				Info.CasaCristo.CEI2.RelogioCor = "blue"
			else:
				Info.CasaCristo.CEI2.ModuloCor  = "pink"
				Info.CasaCristo.CEI2.RelogioCor = "pink"

		elif relogio == "cei3":
	
			if result == 1:
				Info.CasaCristo.CEI3.ModuloCor  = "red"
				Info.CasaCristo.CEI3.RelogioCor = "red"
			elif result == 2:
				Info.CasaCristo.CEI3.ModuloCor  = "green"
				Info.CasaCristo.CEI3.RelogioCor = "red"
			elif result == 3:
				Info.CasaCristo.CEI3.ModuloCor  = "green"
				Info.CasaCristo.CEI3.RelogioCor = "green"
			elif result == 4:
				Info.CasaCristo.CEI3.ModuloCor  = "blue"
				Info.CasaCristo.CEI3.RelogioCor = "blue"
			else:
				Info.CasaCristo.CEI3.ModuloCor  = "pink"
				Info.CasaCristo.CEI3.RelogioCor = "pink"

		elif relogio == "vovomatilde":
			if result == 1:
				Info.CasaCristo.VovoMatilde.ModuloCor  = "red"
				Info.CasaCristo.VovoMatilde.RelogioCor = "red"
			elif result == 2:
				Info.CasaCristo.VovoMatilde.ModuloCor  = "green"
				Info.CasaCristo.VovoMatilde.RelogioCor = "red"
			elif result == 3:
				Info.CasaCristo.VovoMatilde.ModuloCor  = "green"
				Info.CasaCristo.VovoMatilde.RelogioCor = "green"
			elif result == 4:
				Info.CasaCristo.VovoMatilde.ModuloCor  = "blue"
				Info.CasaCristo.VovoMatilde.RelogioCor = "blue"
			else:
				Info.CasaCristo.VovoMatilde.ModuloCor  = "pink"
				Info.CasaCristo.VovoMatilde.RelogioCor = "pink"

		if result != 4:
			Info.CasaCristo.Status.Contage = 0

			if Info.CasaCristo.ADM.RelogioCor == "green" : 
				Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1

			if Info.CasaCristo.CEI1.RelogioCor == "green" : 
				Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
			
			if Info.CasaCristo.CEI2.RelogioCor == "green" : 
				Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
			
			if Info.CasaCristo.CEI3.RelogioCor == "green" : 
				Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
			
			if Info.CasaCristo.VovoMatilde.RelogioCor == "green" : 
				Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1

	######################################################### BEST IN CLASS ############################################

	elif empresa == "bestinclass":

		if relogio == "recife":

			if result == 1:
				Info.BestInClass.Recife.ModuloCor  = "red"
				Info.BestInClass.Recife.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Recife.ModuloCor  = "green"
				Info.BestInClass.Recife.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Recife.ModuloCor  = "green"
				Info.BestInClass.Recife.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Recife.ModuloCor  = "blue"
				Info.BestInClass.Recife.RelogioCor = "blue"
			else:
				Info.BestInClass.Recife.ModuloCor  = "pink"
				Info.BestInClass.Recife.RelogioCor = "pink"


		elif relogio == "itaquera":

			if result == 1:
				Info.BestInClass.Itaquera.ModuloCor  = "red"
				Info.BestInClass.Itaquera.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Itaquera.ModuloCor  = "green"
				Info.BestInClass.Itaquera.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Itaquera.ModuloCor  = "green"
				Info.BestInClass.Itaquera.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Itaquera.ModuloCor  = "blue"
				Info.BestInClass.Itaquera.RelogioCor = "blue"
			else:
				Info.BestInClass.Itaquera.ModuloCor  = "pink"
				Info.BestInClass.Itaquera.RelogioCor = "pink"


		elif relogio == "itapevi":

			if result == 1:
				Info.BestInClass.Itapevi.ModuloCor  = "red"
				Info.BestInClass.Itapevi.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Itapevi.ModuloCor  = "green"
				Info.BestInClass.Itapevi.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Itapevi.ModuloCor  = "green"
				Info.BestInClass.Itapevi.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Itapevi.ModuloCor  = "blue"
				Info.BestInClass.Itapevi.RelogioCor = "blue"
			else:
				Info.BestInClass.Itapevi.ModuloCor  = "pink"
				Info.BestInClass.Itapevi.RelogioCor = "pink"



		elif relogio == "sorocaba":

			if result == 1:
				Info.BestInClass.Sorocaba.ModuloCor  = "red"
				Info.BestInClass.Sorocaba.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Sorocaba.ModuloCor  = "green"
				Info.BestInClass.Sorocaba.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Sorocaba.ModuloCor  = "green"
				Info.BestInClass.Sorocaba.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Sorocaba.ModuloCor  = "blue"
				Info.BestInClass.Sorocaba.RelogioCor = "blue"
			else:
				Info.BestInClass.Sorocaba.ModuloCor  = "pink"
				Info.BestInClass.Sorocaba.RelogioCor = "pink"

		elif relogio == "setelagoas":

			if result == 1:
				Info.BestInClass.SeteLagoas.ModuloCor  = "red"
				Info.BestInClass.SeteLagoas.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.SeteLagoas.ModuloCor  = "green"
				Info.BestInClass.SeteLagoas.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.SeteLagoas.ModuloCor  = "green"
				Info.BestInClass.SeteLagoas.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.SeteLagoas.ModuloCor  = "blue"
				Info.BestInClass.SeteLagoas.RelogioCor = "blue"
			else:
				Info.BestInClass.SeteLagoas.ModuloCor  = "pink"
				Info.BestInClass.SeteLagoas.RelogioCor = "pink"


		elif relogio == "curitiba":

			if result == 1:
				Info.BestInClass.Curitiba.ModuloCor  = "red"
				Info.BestInClass.Curitiba.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Curitiba.ModuloCor  = "green"
				Info.BestInClass.Curitiba.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Curitiba.ModuloCor  = "green"
				Info.BestInClass.Curitiba.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Curitiba.ModuloCor  = "blue"
				Info.BestInClass.Curitiba.RelogioCor = "blue"
			else:
				Info.BestInClass.Curitiba.ModuloCor  = "pink"
				Info.BestInClass.Curitiba.RelogioCor = "pink"

		elif relogio == "fsant":

			if result == 1:
				Info.BestInClass.Fsantana.ModuloCor  = "red"
				Info.BestInClass.Fsantana.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Fsantana.ModuloCor  = "green"
				Info.BestInClass.Fsantana.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Fsantana.ModuloCor  = "green"
				Info.BestInClass.Fsantana.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Fsantana.ModuloCor  = "blue"
				Info.BestInClass.Fsantana.RelogioCor = "blue"
			else:
				Info.BestInClass.Fsantana.ModuloCor  = "pink"
				Info.BestInClass.Fsantana.RelogioCor = "pink"					



		elif relogio == "itu":

			if result == 1:
				Info.BestInClass.Itu.ModuloCor  = "red"
				Info.BestInClass.Itu.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Itu.ModuloCor  = "green"
				Info.BestInClass.Itu.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Itu.ModuloCor  = "green"
				Info.BestInClass.Itu.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Itu.ModuloCor  = "blue"
				Info.BestInClass.Itu.RelogioCor = "blue"
			else:
				Info.BestInClass.Itu.ModuloCor  = "pink"
				Info.BestInClass.Itu.RelogioCor = "pink"


		elif relogio == "guarulhos":

			if result == 1:
				Info.BestInClass.Guarulhos.ModuloCor  = "red"
				Info.BestInClass.Guarulhos.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Guarulhos.ModuloCor  = "green"
				Info.BestInClass.Guarulhos.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Guarulhos.ModuloCor  = "green"
				Info.BestInClass.Guarulhos.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Guarulhos.ModuloCor  = "blue"
				Info.BestInClass.Guarulhos.RelogioCor = "blue"
			else:
				Info.BestInClass.Guarulhos.ModuloCor  = "pink"
				Info.BestInClass.Guarulhos.RelogioCor = "pink"


		elif relogio == "itaporanga":

			if result == 1:
				Info.BestInClass.Itaporanga.ModuloCor  = "red"
				Info.BestInClass.Itaporanga.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Itaporanga.ModuloCor  = "green"
				Info.BestInClass.Itaporanga.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Itaporanga.ModuloCor  = "green"
				Info.BestInClass.Itaporanga.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Itaporanga.ModuloCor  = "blue"
				Info.BestInClass.Itaporanga.RelogioCor = "blue"
			else:
				Info.BestInClass.Itaporanga.ModuloCor  = "pink"
				Info.BestInClass.Itaporanga.RelogioCor = "pink"


		elif relogio == "linhares":

			if result == 1:
				Info.BestInClass.Linhares.ModuloCor  = "red"
				Info.BestInClass.Linhares.RelogioCor = "red"
			elif result == 2:
				Info.BestInClass.Linhares.ModuloCor  = "green"
				Info.BestInClass.Linhares.RelogioCor = "red"
			elif result == 3:
				Info.BestInClass.Linhares.ModuloCor  = "green"
				Info.BestInClass.Linhares.RelogioCor = "green"
			elif result == 4:
				Info.BestInClass.Linhares.ModuloCor  = "blue"
				Info.BestInClass.Linhares.RelogioCor = "blue"
			else:
				Info.BestInClass.Linhares.ModuloCor  = "pink"
				Info.BestInClass.Linhares.RelogioCor = "pink"

	if result != 4:			
			Info.BestInClass.Status.Contage = 0

			if Info.BestInClass.Recife.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

			if Info.BestInClass.Itaquera.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.Itapevi.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.Sorocaba.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.SeteLagoas.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

			if Info.BestInClass.Curitiba.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

			if Info.BestInClass.Fsantana.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.Itu.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.Guarulhos.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
			
			if Info.BestInClass.Itaporanga.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

			if Info.BestInClass.Linhares.RelogioCor == "green" : 
				Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1


	if result != 4:
		Controle.TotalON = 0		
		Controle.TotalON = Controle.TotalON + Info.Building.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.CasaCristo.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.BestInClass.Status.Contage






def Contagem():

	Controle.TotalRelogios = 0


	Controle.TotalRelogios = Controle.TotalRelogios + Info.Building.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.CasaCristo.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.BestInClass.Status.TotalRelogios


