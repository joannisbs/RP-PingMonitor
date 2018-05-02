
from Var import *



def AtualizaCorBuilding(relogio,result):

	if relogio == "allianz":
			
		if result == 1:
			Info.Building.Allianz.ModuloCor  = "red"
			Info.Building.Allianz.RelogioCor = "red"
		elif result == 2:
			Info.Building.Allianz.ModuloCor  = "green3"
			Info.Building.Allianz.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Building.Allianz.ModuloCor  = "green3"
			Info.Building.Allianz.RelogioCor = "green3"
		elif result == 4:
			Info.Building.Allianz.ModuloCor  = "cyan"
			#Info.Building.Allianz.RelogioCor = "cyan"
		else:
			Info.Building.Allianz.ModuloCor  = "pink"
			Info.Building.Allianz.RelogioCor = "pink"




	elif relogio == "wtorre":


		if result == 1:
			Info.Building.WTorre.ModuloCor  = "red"
			Info.Building.WTorre.RelogioCor = "red"
		elif result == 2:
			Info.Building.WTorre.ModuloCor  = "green3"
			Info.Building.WTorre.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Building.WTorre.ModuloCor  = "green3"
			Info.Building.WTorre.RelogioCor = "green3"
		elif result == 4:
			Info.Building.WTorre.ModuloCor  = "cyan"
			#Info.Building.WTorre.RelogioCor = "cyan"
		else:
			Info.Building.WTorre.ModuloCor  = "pink"
			Info.Building.WTorre.RelogioCor = "pink"



	elif relogio == "riojaneiro":

		if result == 1:
			Info.Building.RioJaneiro.ModuloCor  = "red"
			Info.Building.RioJaneiro.RelogioCor = "red"
		elif result == 2:
			Info.Building.RioJaneiro.ModuloCor  = "green3"
			Info.Building.RioJaneiro.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Building.RioJaneiro.ModuloCor  = "green3"
			Info.Building.RioJaneiro.RelogioCor = "green3"
		elif result == 4:
			Info.Building.RioJaneiro.ModuloCor  = "cyan"
			#Info.Building.RioJaneiro.RelogioCor = "cyan"
		else:
			Info.Building.RioJaneiro.ModuloCor  = "pink"
			Info.Building.RioJaneiro.RelogioCor = "pink"
	
	if result != 4:
		Info.Building.Status.Contage = 0
		if Info.Building.Allianz.RelogioCor == "green3" : 
				Info.Building.Status.Contage = Info.Building.Status.Contage +1
		if Info.Building.WTorre.RelogioCor == "green3" : 
				Info.Building.Status.Contage = Info.Building.Status.Contage +1
		if Info.Building.RioJaneiro.RelogioCor == "green3" : 
				Info.Building.Status.Contage = Info.Building.Status.Contage +1

def AtualizaCorLaser(relogio,result):
	if relogio == "academia":
	
		if result == 1:
			Info.Laser.Academia.ModuloCor  = "red"
			Info.Laser.Academia.RelogioCor = "red"
		elif result == 2:
			Info.Laser.Academia.ModuloCor  = "green3"
			Info.Laser.Academia.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Laser.Academia.ModuloCor  = "green3"
			Info.Laser.Academia.RelogioCor = "green3"

		elif result == 4:
			Info.Laser.Academia.ModuloCor  = "cyan"
			#Info.Laser.Academia.RelogioCor = "cyan"

		else:
			Info.Laser.Academia.ModuloCor  = "pink"
			Info.Laser.Academia.RelogioCor = "pink"
		Telas.GUI_Tela1 .updateLaser()

	elif relogio == "instituto":


		if result == 1:
			Info.Laser.Instituto.ModuloCor  = "red"
			Info.Laser.Instituto.RelogioCor = "red"
		elif result == 2:
			Info.Laser.Instituto.ModuloCor  = "green3"
			Info.Laser.Instituto.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Laser.Instituto.ModuloCor  = "green3"
			Info.Laser.Instituto.RelogioCor = "green3"
		elif result == 4:
			Info.Laser.Instituto.ModuloCor  = "cyan"
			#Info.Laser.Instituto.RelogioCor = "cyan"

		else:
			Info.Laser.Instituto.ModuloCor  = "pink"
			Info.Laser.Instituto.RelogioCor = "pink"

		Telas.GUI_Tela1 .updateLaser()

def AtualizaCorGravex(relogio,result):

	if relogio == "adm":

		if result == 1:
			Info.Gravex.ADM.ModuloCor  = "red"
			Info.Gravex.ADM.RelogioCor = "red"
		elif result == 2:
			Info.Gravex.ADM.ModuloCor  = "green3"
			Info.Gravex.ADM.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Gravex.ADM.ModuloCor  = "green3"
			Info.Gravex.ADM.RelogioCor = "green3"
		elif result == 4:
			Info.Gravex.ADM.ModuloCor  = "cyan"
			#Info.Gravex.ADM.RelogioCor = "cyan"
		else:
			Info.Gravex.ADM.ModuloCor  = "pink"
			Info.Gravex.ADM.RelogioCor = "pink"

	elif relogio == "loja":

		if result == 1:
			Info.Gravex.Loja1.ModuloCor  = "red"
			Info.Gravex.Loja1.RelogioCor = "red"
		elif result == 2:
			Info.Gravex.Loja1.ModuloCor  = "green3"
			Info.Gravex.Loja1.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Gravex.Loja1.ModuloCor  = "green3"
			Info.Gravex.Loja1.RelogioCor = "green3"
		elif result == 4:
			Info.Gravex.Loja1.ModuloCor  = "cyan"
			#Info.Gravex.Loja1.RelogioCor = "cyan"
		else:
			Info.Gravex.Loja1.ModuloCor  = "pink"
			Info.Gravex.Loja1.RelogioCor = "pink"

	elif relogio == "mimarcos":

		if result == 1:
			Info.Gravex.MiMarcos.ModuloCor  = "red"
			Info.Gravex.MiMarcos.RelogioCor = "red"
		elif result == 2:
			Info.Gravex.MiMarcos.ModuloCor  = "green3"
			Info.Gravex.MiMarcos.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Gravex.MiMarcos.ModuloCor  = "green3"
			Info.Gravex.MiMarcos.RelogioCor = "green3"
		elif result == 4:
			Info.Gravex.MiMarcos.ModuloCor  = "cyan"
			#Info.Gravex.MiMarcos.RelogioCor = "cyan"
		else:
			Info.Gravex.MiMarcos.ModuloCor  = "pink"
			Info.Gravex.MiMarcos.RelogioCor = "pink"

	elif relogio == "dantchini":
		if result == 1:
			Info.Gravex.DantChini.ModuloCor  = "red"
			Info.Gravex.DantChini.RelogioCor = "red"
		elif result == 2:
			Info.Gravex.DantChini.ModuloCor  = "green3"
			Info.Gravex.DantChini.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Gravex.DantChini.ModuloCor  = "green3"
			Info.Gravex.DantChini.RelogioCor = "green3"
		elif result == 4:
			Info.Gravex.DantChini.ModuloCor  = "cyan"
			#Info.Gravex.DantChini.RelogioCor = "cyan"
		else:
			Info.Gravex.DantChini.ModuloCor  = "pink"
			Info.Gravex.DantChini.RelogioCor = "pink"

def AtualizaCorCasaCristo(relogio,result):

	if relogio == "adm":

		if result == 1:
			Info.CasaCristo.ADM.ModuloCor  = "red"
			Info.CasaCristo.ADM.RelogioCor = "red"
		elif result == 2:
			Info.CasaCristo.ADM.ModuloCor  = "green3"
			Info.CasaCristo.ADM.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.CasaCristo.ADM.ModuloCor  = "green3"
			Info.CasaCristo.ADM.RelogioCor = "green3"
		elif result == 4:
			Info.CasaCristo.ADM.ModuloCor  = "cyan"
			#Info.CasaCristo.ADM.RelogioCor = "cyan"
		else:
			Info.CasaCristo.ADM.ModuloCor  = "pink"
			Info.CasaCristo.ADM.RelogioCor = "pink"

	elif relogio == "cei1":

		if result == 1:
			Info.CasaCristo.CEI1.ModuloCor  = "red"
			Info.CasaCristo.CEI1.RelogioCor = "red"
		elif result == 2:
			Info.CasaCristo.CEI1.ModuloCor  = "green3"
			Info.CasaCristo.CEI1.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.CasaCristo.CEI1.ModuloCor  = "green3"
			Info.CasaCristo.CEI1.RelogioCor = "green3"
		elif result == 4:
			Info.CasaCristo.CEI1.ModuloCor  = "cyan"
			#Info.CasaCristo.CEI1.RelogioCor = "cyan"
		else:
			Info.CasaCristo.CEI1.ModuloCor  = "pink"
			Info.CasaCristo.CEI1.RelogioCor = "pink"

	elif relogio == "cei2":

		if result == 1:
			Info.CasaCristo.CEI2.ModuloCor  = "red"
			Info.CasaCristo.CEI2.RelogioCor = "red"
		elif result == 2:
			Info.CasaCristo.CEI2.ModuloCor  = "green3"
			Info.CasaCristo.CEI2.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.CasaCristo.CEI2.ModuloCor  = "green3"
			Info.CasaCristo.CEI2.RelogioCor = "green3"
		elif result == 4:
			Info.CasaCristo.CEI2.ModuloCor  = "cyan"
			#Info.CasaCristo.CEI2.RelogioCor = "cyan"
		else:
			Info.CasaCristo.CEI2.ModuloCor  = "pink"
			Info.CasaCristo.CEI2.RelogioCor = "pink"

	elif relogio == "cei3":

		if result == 1:
			Info.CasaCristo.CEI3.ModuloCor  = "red"
			Info.CasaCristo.CEI3.RelogioCor = "red"
		elif result == 2:
			Info.CasaCristo.CEI3.ModuloCor  = "green3"
			Info.CasaCristo.CEI3.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.CasaCristo.CEI3.ModuloCor  = "green3"
			Info.CasaCristo.CEI3.RelogioCor = "green3"
		elif result == 4:
			Info.CasaCristo.CEI3.ModuloCor  = "cyan"
			#Info.CasaCristo.CEI3.RelogioCor = "cyan"
		else:
			Info.CasaCristo.CEI3.ModuloCor  = "pink"
			Info.CasaCristo.CEI3.RelogioCor = "pink"

	elif relogio == "vovomatilde":
		if result == 1:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "red"
			Info.CasaCristo.VovoMatilde.RelogioCor = "red"
		elif result == 2:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "green3"
			Info.CasaCristo.VovoMatilde.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "green3"
			Info.CasaCristo.VovoMatilde.RelogioCor = "green3"
		elif result == 4:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "cyan"
			#Info.CasaCristo.VovoMatilde.RelogioCor = "cyan"
		else:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "pink"
			Info.CasaCristo.VovoMatilde.RelogioCor = "pink"

	if result != 4:
		Info.CasaCristo.Status.Contage = 0

		if Info.CasaCristo.ADM.RelogioCor == "green3" : 
			Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1

		if Info.CasaCristo.CEI1.RelogioCor == "green3" : 
			Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
		
		if Info.CasaCristo.CEI2.RelogioCor == "green3" : 
			Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
		
		if Info.CasaCristo.CEI3.RelogioCor == "green3" : 
			Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1
		
		if Info.CasaCristo.VovoMatilde.RelogioCor == "green3" : 
			Info.CasaCristo.Status.Contage = Info.CasaCristo.Status.Contage +1

def AtualizaCorBestInCLass(relogio,result):
	if relogio == "recife":

		if result == 1:
			Info.BestInClass.Recife.ModuloCor  = "red"
			Info.BestInClass.Recife.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Recife.ModuloCor  = "green3"
			Info.BestInClass.Recife.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Recife.ModuloCor  = "green3"
			Info.BestInClass.Recife.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Recife.ModuloCor  = "cyan"
			#Info.BestInClass.Recife.RelogioCor = "cyan"
		else:
			Info.BestInClass.Recife.ModuloCor  = "pink"
			Info.BestInClass.Recife.RelogioCor = "pink"


	elif relogio == "itaquera":

		if result == 1:
			Info.BestInClass.Itaquera.ModuloCor  = "red"
			Info.BestInClass.Itaquera.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Itaquera.ModuloCor  = "green3"
			Info.BestInClass.Itaquera.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Itaquera.ModuloCor  = "green3"
			Info.BestInClass.Itaquera.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Itaquera.ModuloCor  = "cyan"
			#Info.BestInClass.Itaquera.RelogioCor = "cyan"
		else:
			Info.BestInClass.Itaquera.ModuloCor  = "pink"
			Info.BestInClass.Itaquera.RelogioCor = "pink"


	elif relogio == "itapevi":

		if result == 1:
			Info.BestInClass.Itapevi.ModuloCor  = "red"
			Info.BestInClass.Itapevi.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Itapevi.ModuloCor  = "green3"
			Info.BestInClass.Itapevi.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Itapevi.ModuloCor  = "green3"
			Info.BestInClass.Itapevi.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Itapevi.ModuloCor  = "cyan"
			#Info.BestInClass.Itapevi.RelogioCor = "cyan"
		else:
			Info.BestInClass.Itapevi.ModuloCor  = "pink"
			Info.BestInClass.Itapevi.RelogioCor = "pink"



	elif relogio == "sorocaba":

		if result == 1:
			Info.BestInClass.Sorocaba.ModuloCor  = "red"
			Info.BestInClass.Sorocaba.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Sorocaba.ModuloCor  = "green3"
			Info.BestInClass.Sorocaba.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Sorocaba.ModuloCor  = "green3"
			Info.BestInClass.Sorocaba.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Sorocaba.ModuloCor  = "cyan"
			#Info.BestInClass.Sorocaba.RelogioCor = "cyan"
		else:
			Info.BestInClass.Sorocaba.ModuloCor  = "pink"
			Info.BestInClass.Sorocaba.RelogioCor = "pink"

	elif relogio == "setelagoas":

		if result == 1:
			Info.BestInClass.SeteLagoas.ModuloCor  = "red"
			Info.BestInClass.SeteLagoas.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.SeteLagoas.ModuloCor  = "green3"
			Info.BestInClass.SeteLagoas.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.SeteLagoas.ModuloCor  = "green3"
			Info.BestInClass.SeteLagoas.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.SeteLagoas.ModuloCor  = "cyan"
			#Info.BestInClass.SeteLagoas.RelogioCor = "cyan"
		else:
			Info.BestInClass.SeteLagoas.ModuloCor  = "pink"
			Info.BestInClass.SeteLagoas.RelogioCor = "pink"


	elif relogio == "curitiba":

		if result == 1:
			Info.BestInClass.Curitiba.ModuloCor  = "red"
			Info.BestInClass.Curitiba.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Curitiba.ModuloCor  = "green3"
			Info.BestInClass.Curitiba.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Curitiba.ModuloCor  = "green3"
			Info.BestInClass.Curitiba.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Curitiba.ModuloCor  = "cyan"
			#Info.BestInClass.Curitiba.RelogioCor = "cyan"
		else:
			Info.BestInClass.Curitiba.ModuloCor  = "pink"
			Info.BestInClass.Curitiba.RelogioCor = "pink"

	elif relogio == "fsant":

		if result == 1:
			Info.BestInClass.Fsantana.ModuloCor  = "red"
			Info.BestInClass.Fsantana.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Fsantana.ModuloCor  = "green3"
			Info.BestInClass.Fsantana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Fsantana.ModuloCor  = "green3"
			Info.BestInClass.Fsantana.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Fsantana.ModuloCor  = "cyan"
			#Info.BestInClass.Fsantana.RelogioCor = "cyan"
		else:
			Info.BestInClass.Fsantana.ModuloCor  = "pink"
			Info.BestInClass.Fsantana.RelogioCor = "pink"					



	elif relogio == "itu":

		if result == 1:
			Info.BestInClass.Itu.ModuloCor  = "red"
			Info.BestInClass.Itu.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Itu.ModuloCor  = "green3"
			Info.BestInClass.Itu.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Itu.ModuloCor  = "green3"
			Info.BestInClass.Itu.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Itu.ModuloCor  = "cyan"
			#Info.BestInClass.Itu.RelogioCor = "cyan"
		else:
			Info.BestInClass.Itu.ModuloCor  = "pink"
			Info.BestInClass.Itu.RelogioCor = "pink"


	elif relogio == "guarulhos":

		if result == 1:
			Info.BestInClass.Guarulhos.ModuloCor  = "red"
			Info.BestInClass.Guarulhos.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Guarulhos.ModuloCor  = "green3"
			Info.BestInClass.Guarulhos.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Guarulhos.ModuloCor  = "green3"
			Info.BestInClass.Guarulhos.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Guarulhos.ModuloCor  = "cyan"
			#Info.BestInClass.Guarulhos.RelogioCor = "cyan"
		else:
			Info.BestInClass.Guarulhos.ModuloCor  = "pink"
			Info.BestInClass.Guarulhos.RelogioCor = "pink"


	elif relogio == "itaporanga":

		if result == 1:
			Info.BestInClass.Itaporanga.ModuloCor  = "red"
			Info.BestInClass.Itaporanga.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Itaporanga.ModuloCor  = "green3"
			Info.BestInClass.Itaporanga.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Itaporanga.ModuloCor  = "green3"
			Info.BestInClass.Itaporanga.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Itaporanga.ModuloCor  = "cyan"
			#Info.BestInClass.Itaporanga.RelogioCor = "cyan"
		else:
			Info.BestInClass.Itaporanga.ModuloCor  = "pink"
			Info.BestInClass.Itaporanga.RelogioCor = "pink"


	elif relogio == "linhares":

		if result == 1:
			Info.BestInClass.Linhares.ModuloCor  = "red"
			Info.BestInClass.Linhares.RelogioCor = "red"
		elif result == 2:
			Info.BestInClass.Linhares.ModuloCor  = "green3"
			Info.BestInClass.Linhares.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.BestInClass.Linhares.ModuloCor  = "green3"
			Info.BestInClass.Linhares.RelogioCor = "green3"
		elif result == 4:
			Info.BestInClass.Linhares.ModuloCor  = "cyan"
			#Info.BestInClass.Linhares.RelogioCor = "cyan"
		else:
			Info.BestInClass.Linhares.ModuloCor  = "pink"
			Info.BestInClass.Linhares.RelogioCor = "pink"

	if result != 4:			
		Info.BestInClass.Status.Contage = 0

		if Info.BestInClass.Recife.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

		if Info.BestInClass.Itaquera.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.Itapevi.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.Sorocaba.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.SeteLagoas.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

		if Info.BestInClass.Curitiba.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

		if Info.BestInClass.Fsantana.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.Itu.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.Guarulhos.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1
		
		if Info.BestInClass.Itaporanga.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

		if Info.BestInClass.Linhares.RelogioCor == "green3" : 
			Info.BestInClass.Status.Contage = Info.BestInClass.Status.Contage +1

def AtualizaCorIsoRadio(relogio,result):


	if relogio == "santana":

		if result == 1:
			Info.IsoRadio.Santana.ModuloCor  = "red"
			Info.IsoRadio.Santana.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Santana.ModuloCor  = "green3"
			Info.IsoRadio.Santana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.Santana.ModuloCor  = "green3"
			Info.IsoRadio.Santana.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.Santana.ModuloCor  = "cyan"
			##Info.IsoRadio.Santana.RelogioCor = "cyan"
		else:
			Info.IsoRadio.Santana.ModuloCor  = "pink"
			Info.IsoRadio.Santana.RelogioCor = "pink"



	elif relogio == "saomatheus":

		if result == 1:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "red"
			Info.IsoRadio.SaoMatheus.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "green3"
			Info.IsoRadio.SaoMatheus.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "green3"
			Info.IsoRadio.SaoMatheus.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "cyan"
			#Info.IsoRadio.SaoMatheus.RelogioCor = "cyan"
		else:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "pink"
			Info.IsoRadio.SaoMatheus.RelogioCor = "pink"



	elif relogio == "vilamariana":

		if result == 1:
			Info.IsoRadio.VilaMariana.ModuloCor  = "red"
			Info.IsoRadio.VilaMariana.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.VilaMariana.ModuloCor  = "green3"
			Info.IsoRadio.VilaMariana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.VilaMariana.ModuloCor  = "green3"
			Info.IsoRadio.VilaMariana.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.VilaMariana.ModuloCor  = "cyan"
			#Info.IsoRadio.VilaMariana.RelogioCor = "cyan"
		else:
			Info.IsoRadio.VilaMariana.ModuloCor  = "pink"
			Info.IsoRadio.VilaMariana.RelogioCor = "pink"


	elif relogio == "lapa":


		if result == 1:
			Info.IsoRadio.Lapa.ModuloCor  = "red"
			Info.IsoRadio.Lapa.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Lapa.ModuloCor  = "green3"
			Info.IsoRadio.Lapa.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.Lapa.ModuloCor  = "green3"
			Info.IsoRadio.Lapa.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.Lapa.ModuloCor  = "cyan"
			#Info.IsoRadio.Lapa.RelogioCor = "cyan"
		else:
			Info.IsoRadio.Lapa.ModuloCor  = "pink"
			Info.IsoRadio.Lapa.RelogioCor = "pink"


	elif relogio == "santoamaro":

		if result == 1:
			Info.IsoRadio.SAmaro.ModuloCor  = "red"
			Info.IsoRadio.SAmaro.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.SAmaro.ModuloCor  = "green3"
			Info.IsoRadio.SAmaro.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.SAmaro.ModuloCor  = "green3"
			Info.IsoRadio.SAmaro.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.SAmaro.ModuloCor  = "cyan"
			#Info.IsoRadio.SAmaro.RelogioCor = "cyan"
		else:
			Info.IsoRadio.SAmaro.ModuloCor  = "pink"
			Info.IsoRadio.SAmaro.RelogioCor = "pink"


	elif relogio == "cidadedutra":

		if result == 1:
			Info.IsoRadio.CDutra.ModuloCor  = "red"
			Info.IsoRadio.CDutra.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.CDutra.ModuloCor  = "green3"
			Info.IsoRadio.CDutra.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.CDutra.ModuloCor  = "green3"
			Info.IsoRadio.CDutra.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.CDutra.ModuloCor  = "cyan"
			#Info.IsoRadio.CDutra.RelogioCor = "cyan"
		else:
			Info.IsoRadio.CDutra.ModuloCor  = "pink"
			Info.IsoRadio.CDutra.RelogioCor = "pink"


	elif relogio == "tatuape":


		if result == 1:
			Info.IsoRadio.Tatuape.ModuloCor  = "red"
			Info.IsoRadio.Tatuape.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Tatuape.ModuloCor  = "green3"
			Info.IsoRadio.Tatuape.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.Tatuape.ModuloCor  = "green3"
			Info.IsoRadio.Tatuape.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.Tatuape.ModuloCor  = "cyan"
			#Info.IsoRadio.Tatuape.RelogioCor = "cyan"
		else:
			Info.IsoRadio.Tatuape.ModuloCor  = "pink"
			Info.IsoRadio.Tatuape.RelogioCor = "pink"

	elif relogio == "campolimpo":


		if result == 1:
			Info.IsoRadio.CLimpo.ModuloCor  = "red"
			Info.IsoRadio.CLimpo.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.CLimpo.ModuloCor  = "green3"
			Info.IsoRadio.CLimpo.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.CLimpo.ModuloCor  = "green3"
			Info.IsoRadio.CLimpo.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.CLimpo.ModuloCor  = "cyan"
			#Info.IsoRadio.CLimpo.RelogioCor = "cyan"
		else:
			Info.IsoRadio.CLimpo.ModuloCor  = "pink"
			Info.IsoRadio.CLimpo.RelogioCor = "pink"


	elif relogio == "ipiranga":


		if result == 1:
			Info.IsoRadio.Ipiranga.ModuloCor  = "red"
			Info.IsoRadio.Ipiranga.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Ipiranga.ModuloCor  = "green3"
			Info.IsoRadio.Ipiranga.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.Ipiranga.ModuloCor  = "green3"
			Info.IsoRadio.Ipiranga.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.Ipiranga.ModuloCor  = "cyan"
			#Info.IsoRadio.Ipiranga.RelogioCor = "cyan"
		else:
			Info.IsoRadio.Ipiranga.ModuloCor  = "pink"
			Info.IsoRadio.Ipiranga.RelogioCor = "pink"

	elif relogio == "anarosa":

		if result == 1:
			Info.IsoRadio.AnaRosa.ModuloCor  = "red"
			Info.IsoRadio.AnaRosa.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.AnaRosa.ModuloCor  = "green3"
			Info.IsoRadio.AnaRosa.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.IsoRadio.AnaRosa.ModuloCor  = "green3"
			Info.IsoRadio.AnaRosa.RelogioCor = "green3"
		elif result == 4:
			Info.IsoRadio.AnaRosa.ModuloCor  = "cyan"
			#Info.IsoRadio.AnaRosa.RelogioCor = "cyan"
		else:
			Info.IsoRadio.AnaRosa.ModuloCor  = "pink"
			Info.IsoRadio.AnaRosa.RelogioCor = "pink"


	if result != 4:
		Info.IsoRadio.Status.Contage = 0

		if Info.IsoRadio.Santana.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.SaoMatheus.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.VilaMariana.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Lapa.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.SAmaro.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.CDutra.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Tatuape.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.CLimpo.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Ipiranga.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.AnaRosa.ModuloCor == "green3" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

def AtualizaCorGrupoNk(relogio,result):

	if relogio == "nelson":

		if result == 1:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "red"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "green3"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "green3"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "cyan"
			#Info.GrupoNk.NelsonKioshi.RelogioCor = "cyan"
		else:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "pink"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "pink"


	elif relogio == "furukawa":

		if result == 1:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "red"
			Info.GrupoNk.RDFurukawa.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "green3"
			Info.GrupoNk.RDFurukawa.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "green3"
			Info.GrupoNk.RDFurukawa.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "cyan"
			#Info.GrupoNk.RDFurukawa.RelogioCor = "cyan"
		else:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "pink"
			Info.GrupoNk.RDFurukawa.RelogioCor = "pink"


	elif relogio == "kio1":

		if result == 1:
			Info.GrupoNk.Kio1.ModuloCor  = "red"
			Info.GrupoNk.Kio1.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Kio1.ModuloCor  = "green3"
			Info.GrupoNk.Kio1.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.Kio1.ModuloCor  = "green3"
			Info.GrupoNk.Kio1.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.Kio1.ModuloCor  = "cyan"
			#Info.GrupoNk.Kio1.RelogioCor = "cyan"
		else:
			Info.GrupoNk.Kio1.ModuloCor  = "pink"
			Info.GrupoNk.Kio1.RelogioCor = "pink"



	elif relogio == "kio2":

		if result == 1:
			Info.GrupoNk.Kio2.ModuloCor  = "red"
			Info.GrupoNk.Kio2.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Kio2.ModuloCor  = "green3"
			Info.GrupoNk.Kio2.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.Kio2.ModuloCor  = "green3"
			Info.GrupoNk.Kio2.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.Kio2.ModuloCor  = "cyan"
			#Info.GrupoNk.Kio2.RelogioCor = "cyan"
		else:
			Info.GrupoNk.Kio2.ModuloCor  = "pink"
			Info.GrupoNk.Kio2.RelogioCor = "pink"


	elif relogio == "granjaviana":

		if result == 1:
			Info.GrupoNk.GranjaViana.ModuloCor  = "red"
			Info.GrupoNk.GranjaViana.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.GranjaViana.ModuloCor  = "green3"
			Info.GrupoNk.GranjaViana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.GranjaViana.ModuloCor  = "green3"
			Info.GrupoNk.GranjaViana.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.GranjaViana.ModuloCor  = "cyan"
			#Info.GrupoNk.GranjaViana.RelogioCor = "cyan"
		else:
			Info.GrupoNk.GranjaViana.ModuloCor  = "pink"
			Info.GrupoNk.GranjaViana.RelogioCor = "pink"


	elif relogio == "santacecilia":

		if result == 1:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "red"
			Info.GrupoNk.SantaCecilia.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "green3"
			Info.GrupoNk.SantaCecilia.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "green3"
			Info.GrupoNk.SantaCecilia.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "cyan"
			#Info.GrupoNk.SantaCecilia.RelogioCor = "cyan"
		else:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "pink"
			Info.GrupoNk.SantaCecilia.RelogioCor = "pink"


	elif relogio == "transfruit":

		if result == 1:
			Info.GrupoNk.Transfruit.ModuloCor  = "red"
			Info.GrupoNk.Transfruit.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Transfruit.ModuloCor  = "green3"
			Info.GrupoNk.Transfruit.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.Transfruit.ModuloCor  = "green3"
			Info.GrupoNk.Transfruit.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.Transfruit.ModuloCor  = "cyan"
			#Info.GrupoNk.Transfruit.RelogioCor = "cyan"
		else:
			Info.GrupoNk.Transfruit.ModuloCor  = "pink"
			Info.GrupoNk.Transfruit.RelogioCor = "pink"

	elif relogio == "distrdefrutas":

		if result == 1:
			Info.GrupoNk.Distribuidora.ModuloCor  = "red"
			Info.GrupoNk.Distribuidora.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Distribuidora.ModuloCor  = "green3"
			Info.GrupoNk.Distribuidora.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.Distribuidora.ModuloCor  = "green3"
			Info.GrupoNk.Distribuidora.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.Distribuidora.ModuloCor  = "cyan"
			#Info.GrupoNk.Distribuidora.RelogioCor = "cyan"
		else:
			Info.GrupoNk.Distribuidora.ModuloCor  = "pink"
			Info.GrupoNk.Distribuidora.RelogioCor = "pink"


	elif relogio == "nkhortifruit":

		if result == 1:
			Info.GrupoNk.NKFilial.ModuloCor  = "red"
			Info.GrupoNk.NKFilial.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.NKFilial.ModuloCor  = "green3"
			Info.GrupoNk.NKFilial.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.GrupoNk.NKFilial.ModuloCor  = "green3"
			Info.GrupoNk.NKFilial.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.NKFilial.ModuloCor  = "cyan"
			#Info.GrupoNk.NKFilial.RelogioCor = "cyan"
		else:
			Info.GrupoNk.NKFilial.ModuloCor  = "pink"
			Info.GrupoNk.NKFilial.RelogioCor = "pink"

def AtualizaLotten(relogio,result):

	if relogio == "sfjardins":

		if result == 1:
			Info.Lotten.Jardins.ModuloCor  = "red"
			Info.Lotten.Jardins.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Jardins.ModuloCor  = "green3"
			Info.Lotten.Jardins.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Jardins.ModuloCor  = "green3"
			Info.Lotten.Jardins.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Jardins.ModuloCor  = "cyan"
			#Info.Lotten.Jardins.RelogioCor = "cyan"
		else:
			Info.Lotten.Jardins.ModuloCor  = "pink"
			Info.Lotten.Jardins.RelogioCor = "pink"

	if relogio == "alphaville":

		if result == 1:
			Info.Lotten.Alphaville.ModuloCor  = "red"
			Info.Lotten.Alphaville.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Alphaville.ModuloCor  = "green3"
			Info.Lotten.Alphaville.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Alphaville.ModuloCor  = "green3"
			Info.Lotten.Alphaville.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Alphaville.ModuloCor  = "cyan"
			#Info.Lotten.Alphaville.RelogioCor = "cyan"
		else:
			Info.Lotten.Alphaville.ModuloCor  = "pink"
			Info.Lotten.Alphaville.RelogioCor = "pink"

	if relogio == "osasco":

		if result == 1:
			Info.Lotten.Osasco.ModuloCor  = "red"
			Info.Lotten.Osasco.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Osasco.ModuloCor  = "green3"
			Info.Lotten.Osasco.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Osasco.ModuloCor  = "green3"
			Info.Lotten.Osasco.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Osasco.ModuloCor  = "cyan"
			#Info.Lotten.Osasco.RelogioCor = "cyan"
		else:
			Info.Lotten.Osasco.ModuloCor  = "pink"
			Info.Lotten.Osasco.RelogioCor = "pink"

	if relogio == "santana":

		if result == 1:
			Info.Lotten.Santana.ModuloCor  = "red"
			Info.Lotten.Santana.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Santana.ModuloCor  = "green3"
			Info.Lotten.Santana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Santana.ModuloCor  = "green3"
			Info.Lotten.Santana.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Santana.ModuloCor  = "cyan"
			#Info.Lotten.Santana.RelogioCor = "cyan"
		else:
			Info.Lotten.Santana.ModuloCor  = "pink"
			Info.Lotten.Santana.RelogioCor = "pink"

	if relogio == "tatuape":

		if result == 1:
			Info.Lotten.Tatuape.ModuloCor  = "red"
			Info.Lotten.Tatuape.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Tatuape.ModuloCor  = "green3"
			Info.Lotten.Tatuape.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Tatuape.ModuloCor  = "green3"
			Info.Lotten.Tatuape.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Tatuape.ModuloCor  = "cyan"
			#Info.Lotten.Tatuape.RelogioCor = "cyan"
		else:
			Info.Lotten.Tatuape.ModuloCor  = "pink"
			Info.Lotten.Tatuape.RelogioCor = "pink"

	if relogio == "moema":

		if result == 1:
			Info.Lotten.Moema.ModuloCor  = "red"
			Info.Lotten.Moema.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Moema.ModuloCor  = "green3"
			Info.Lotten.Moema.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Moema.ModuloCor  = "green3"
			Info.Lotten.Moema.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Moema.ModuloCor  = "cyan"
			#Info.Lotten.Moema.RelogioCor = "cyan"
		else:
			Info.Lotten.Moema.ModuloCor  = "pink"
			Info.Lotten.Moema.RelogioCor = "pink"

	if relogio == "jardimsul":

		if result == 1:
			Info.Lotten.JardimSul.ModuloCor  = "red"
			Info.Lotten.JardimSul.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.JardimSul.ModuloCor  = "green3"
			Info.Lotten.JardimSul.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.JardimSul.ModuloCor  = "green3"
			Info.Lotten.JardimSul.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.JardimSul.ModuloCor  = "cyan"
			#Info.Lotten.JardimSul.RelogioCor = "cyan"
		else:
			Info.Lotten.JardimSul.ModuloCor  = "pink"
			Info.Lotten.JardimSul.RelogioCor = "pink"

	if relogio == "conceicao":

		if result == 1:
			Info.Lotten.Conceicao.ModuloCor  = "red"
			Info.Lotten.Conceicao.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Conceicao.ModuloCor  = "green3"
			Info.Lotten.Conceicao.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Conceicao.ModuloCor  = "green3"
			Info.Lotten.Conceicao.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Conceicao.ModuloCor  = "cyan"
			#Info.Lotten.Conceicao.RelogioCor = "cyan"
		else:
			Info.Lotten.Conceicao.ModuloCor  = "pink"
			Info.Lotten.Conceicao.RelogioCor = "pink"

	if relogio == "lapa":

		if result == 1:
			Info.Lotten.Lapa.ModuloCor  = "red"
			Info.Lotten.Lapa.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Lapa.ModuloCor  = "green3"
			Info.Lotten.Lapa.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Lapa.ModuloCor  = "green3"
			Info.Lotten.Lapa.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Lapa.ModuloCor  = "cyan"
			#Info.Lotten.Lapa.RelogioCor = "cyan"
		else:
			Info.Lotten.Lapa.ModuloCor  = "pink"
			Info.Lotten.Lapa.RelogioCor = "pink"

	if relogio == "perdizes":

		if result == 1:
			Info.Lotten.Perdizes.ModuloCor  = "red"
			Info.Lotten.Perdizes.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Perdizes.ModuloCor  = "green3"
			Info.Lotten.Perdizes.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Perdizes.ModuloCor  = "green3"
			Info.Lotten.Perdizes.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Perdizes.ModuloCor  = "cyan"
			#Info.Lotten.Perdizes.RelogioCor = "cyan"
		else:
			Info.Lotten.Perdizes.ModuloCor  = "pink"
			Info.Lotten.Perdizes.RelogioCor = "pink"

	if relogio == "saocaetano":

		if result == 1:
			Info.Lotten.SaoCaetano.ModuloCor  = "red"
			Info.Lotten.SaoCaetano.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.SaoCaetano.ModuloCor  = "green3"
			Info.Lotten.SaoCaetano.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.SaoCaetano.ModuloCor  = "green3"
			Info.Lotten.SaoCaetano.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.SaoCaetano.ModuloCor  = "cyan"
			#Info.Lotten.SaoCaetano.RelogioCor = "cyan"
		else:
			Info.Lotten.SaoCaetano.ModuloCor  = "pink"
			Info.Lotten.SaoCaetano.RelogioCor = "pink"

	if relogio == "pinheiros":

		if result == 1:
			Info.Lotten.Pinheiros.ModuloCor  = "red"
			Info.Lotten.Pinheiros.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Pinheiros.ModuloCor  = "green3"
			Info.Lotten.Pinheiros.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Pinheiros.ModuloCor  = "green3"
			Info.Lotten.Pinheiros.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Pinheiros.ModuloCor  = "cyan"
			#Info.Lotten.Pinheiros.RelogioCor = "cyan"
		else:
			Info.Lotten.Pinheiros.ModuloCor  = "pink"
			Info.Lotten.Pinheiros.RelogioCor = "pink"


	if relogio == "morumbi":

		if result == 1:
			Info.Lotten.Morumbi.ModuloCor  = "red"
			Info.Lotten.Morumbi.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Morumbi.ModuloCor  = "green3"
			Info.Lotten.Morumbi.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Morumbi.ModuloCor  = "green3"
			Info.Lotten.Morumbi.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Morumbi.ModuloCor  = "cyan"
			#Info.Lotten.Morumbi.RelogioCor = "cyan"
		else:
			Info.Lotten.Morumbi.ModuloCor  = "pink"
			Info.Lotten.Morumbi.RelogioCor = "pink"

	if relogio == "berrini":

		if result == 1:
			Info.Lotten.Berrini.ModuloCor  = "red"
			Info.Lotten.Berrini.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Berrini.ModuloCor  = "green3"
			Info.Lotten.Berrini.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Berrini.ModuloCor  = "green3"
			Info.Lotten.Berrini.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Berrini.ModuloCor  = "cyan"
			#Info.Lotten.Berrini.RelogioCor = "cyan"
		else:
			Info.Lotten.Berrini.ModuloCor  = "pink"
			Info.Lotten.Berrini.RelogioCor = "pink"


	if relogio == "vilamariana":

		if result == 1:
			Info.Lotten.VilaMariana.ModuloCor  = "red"
			Info.Lotten.VilaMariana.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.VilaMariana.ModuloCor  = "green3"
			Info.Lotten.VilaMariana.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.VilaMariana.ModuloCor  = "green3"
			Info.Lotten.VilaMariana.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.VilaMariana.ModuloCor  = "cyan"
			#Info.Lotten.VilaMariana.RelogioCor = "cyan"
		else:
			Info.Lotten.VilaMariana.ModuloCor  = "pink"
			Info.Lotten.VilaMariana.RelogioCor = "pink"


	if relogio == "vilaolimpia":

		if result == 1:
			Info.Lotten.VilaOlimpia.ModuloCor  = "red"
			Info.Lotten.VilaOlimpia.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.VilaOlimpia.ModuloCor  = "green3"
			Info.Lotten.VilaOlimpia.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.VilaOlimpia.ModuloCor  = "green3"
			Info.Lotten.VilaOlimpia.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.VilaOlimpia.ModuloCor  = "cyan"
			#Info.Lotten.VilaOlimpia.RelogioCor = "cyan"
		else:
			Info.Lotten.VilaOlimpia.ModuloCor  = "pink"
			Info.Lotten.VilaOlimpia.RelogioCor = "pink"


	if relogio == "itaim":

		if result == 1:
			Info.Lotten.Itaim.ModuloCor  = "red"
			Info.Lotten.Itaim.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Itaim.ModuloCor  = "green3"
			Info.Lotten.Itaim.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Itaim.ModuloCor  = "green3"
			Info.Lotten.Itaim.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Itaim.ModuloCor  = "cyan"
			#Info.Lotten.Itaim.RelogioCor = "cyan"
		else:
			Info.Lotten.Itaim.ModuloCor  = "pink"
			Info.Lotten.Itaim.RelogioCor = "pink"


	if relogio == "garulhos":

		if result == 1:
			Info.Lotten.Guarulhos.ModuloCor  = "red"
			Info.Lotten.Guarulhos.RelogioCor = "red"
		elif result == 2:
			Info.Lotten.Guarulhos.ModuloCor  = "green3"
			Info.Lotten.Guarulhos.RelogioCor = "DarkOrange1"
		elif result == 3:
			Info.Lotten.Guarulhos.ModuloCor  = "green3"
			Info.Lotten.Guarulhos.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Guarulhos.ModuloCor  = "cyan"
			#Info.Lotten.Guarulhos.RelogioCor = "cyan"
		else:
			Info.Lotten.Guarulhos.ModuloCor  = "pink"
			Info.Lotten.Guarulhos.RelogioCor = "pink"









def AtualizaCor(empresa,relogio,result):


	if empresa == "building":
		AtualizaCorBuilding(relogio,result)
	

	elif empresa == "laser":
		AtualizaCorLaser(relogio,result)		


	elif empresa == "gravex":
		AtualizaCorGravex(relogio,result)


	elif empresa == "casacristo":
		AtualizaCorCasaCristo(relogio,result)	


	elif empresa == "bestinclass":
		AtualizaCorBestInCLass(relogio,result)


	elif empresa == "isoradiologia":
		AtualizaCorIsoRadio(relogio,result)


	elif empresa == "gruponk":
		AtualizaCorGrupoNk(relogio,result)


	elif empresa == "lotten":
		AtualizaLotten(relogio,result)



	if result != 4:
		Controle.TotalON = 0	

		Controle.TotalON =  Info.Building.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.CasaCristo.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.BestInClass.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.IsoRadio.Status.Contage





def Contagem():

	Controle.TotalRelogios = 0


	Controle.TotalRelogios = Controle.TotalRelogios + Info.Building.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.CasaCristo.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.BestInClass.Status.TotalRelogios


