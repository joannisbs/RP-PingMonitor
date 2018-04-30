
from Var import *



def AtualizaCorBuilding(relogio,result):

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

def AtualizaCorLaser(relogio,result):
	if relogio == "academia":
	
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
		Telas.GUI_Tela1 .updateLaser()

	elif relogio == "instituto":


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

		Telas.GUI_Tela1 .updateLaser()

def AtualizaCorGravex(relogio,result):

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
			Info.Gravex.MiMarcos.RelogioCor = "red"
		elif result == 2:
			Info.Gravex.MiMarcos.ModuloCor  = "green"
			Info.Gravex.MiMarcos.RelogioCor = "red"
		elif result == 3:
			Info.Gravex.MiMarcos.ModuloCor  = "green"
			Info.Gravex.MiMarcos.RelogioCor = "green"
		elif result == 4:
			Info.Gravex.MiMarcos.ModuloCor  = "blue"
			Info.Gravex.MiMarcos.RelogioCor = "blue"
		else:
			Info.Gravex.MiMarcos.ModuloCor  = "pink"
			Info.Gravex.MiMarcos.RelogioCor = "pink"

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

def AtualizaCorCasaCristo(relogio,result):

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

def AtualizaCorBestInCLass(relogio,result):
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

def AtualizaCorIsoRadio(relogio,result):


	if relogio == "santana":

		if result == 1:
			Info.IsoRadio.Santana.ModuloCor  = "red"
			Info.IsoRadio.Santana.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Santana.ModuloCor  = "green"
			Info.IsoRadio.Santana.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.Santana.ModuloCor  = "green"
			Info.IsoRadio.Santana.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.Santana.ModuloCor  = "blue"
			Info.IsoRadio.Santana.RelogioCor = "blue"
		else:
			Info.IsoRadio.Santana.ModuloCor  = "pink"
			Info.IsoRadio.Santana.RelogioCor = "pink"



	elif relogio == "saomatheus":

		if result == 1:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "red"
			Info.IsoRadio.SaoMatheus.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "green"
			Info.IsoRadio.SaoMatheus.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "green"
			Info.IsoRadio.SaoMatheus.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "blue"
			Info.IsoRadio.SaoMatheus.RelogioCor = "blue"
		else:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "pink"
			Info.IsoRadio.SaoMatheus.RelogioCor = "pink"



	elif relogio == "vilamariana":

		if result == 1:
			Info.IsoRadio.VilaMariana.ModuloCor  = "red"
			Info.IsoRadio.VilaMariana.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.VilaMariana.ModuloCor  = "green"
			Info.IsoRadio.VilaMariana.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.VilaMariana.ModuloCor  = "green"
			Info.IsoRadio.VilaMariana.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.VilaMariana.ModuloCor  = "blue"
			Info.IsoRadio.VilaMariana.RelogioCor = "blue"
		else:
			Info.IsoRadio.VilaMariana.ModuloCor  = "pink"
			Info.IsoRadio.VilaMariana.RelogioCor = "pink"


	elif relogio == "lapa":


		if result == 1:
			Info.IsoRadio.Lapa.ModuloCor  = "red"
			Info.IsoRadio.Lapa.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Lapa.ModuloCor  = "green"
			Info.IsoRadio.Lapa.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.Lapa.ModuloCor  = "green"
			Info.IsoRadio.Lapa.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.Lapa.ModuloCor  = "blue"
			Info.IsoRadio.Lapa.RelogioCor = "blue"
		else:
			Info.IsoRadio.Lapa.ModuloCor  = "pink"
			Info.IsoRadio.Lapa.RelogioCor = "pink"


	elif relogio == "santoamaro":

		if result == 1:
			Info.IsoRadio.SAmaro.ModuloCor  = "red"
			Info.IsoRadio.SAmaro.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.SAmaro.ModuloCor  = "green"
			Info.IsoRadio.SAmaro.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.SAmaro.ModuloCor  = "green"
			Info.IsoRadio.SAmaro.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.SAmaro.ModuloCor  = "blue"
			Info.IsoRadio.SAmaro.RelogioCor = "blue"
		else:
			Info.IsoRadio.SAmaro.ModuloCor  = "pink"
			Info.IsoRadio.SAmaro.RelogioCor = "pink"


	elif relogio == "cidadedutra":

		if result == 1:
			Info.IsoRadio.CDutra.ModuloCor  = "red"
			Info.IsoRadio.CDutra.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.CDutra.ModuloCor  = "green"
			Info.IsoRadio.CDutra.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.CDutra.ModuloCor  = "green"
			Info.IsoRadio.CDutra.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.CDutra.ModuloCor  = "blue"
			Info.IsoRadio.CDutra.RelogioCor = "blue"
		else:
			Info.IsoRadio.CDutra.ModuloCor  = "pink"
			Info.IsoRadio.CDutra.RelogioCor = "pink"


	elif relogio == "tatuape":


		if result == 1:
			Info.IsoRadio.Tatuape.ModuloCor  = "red"
			Info.IsoRadio.Tatuape.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Tatuape.ModuloCor  = "green"
			Info.IsoRadio.Tatuape.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.Tatuape.ModuloCor  = "green"
			Info.IsoRadio.Tatuape.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.Tatuape.ModuloCor  = "blue"
			Info.IsoRadio.Tatuape.RelogioCor = "blue"
		else:
			Info.IsoRadio.Tatuape.ModuloCor  = "pink"
			Info.IsoRadio.Tatuape.RelogioCor = "pink"

	elif relogio == "campolimpo":


		if result == 1:
			Info.IsoRadio.CLimpo.ModuloCor  = "red"
			Info.IsoRadio.CLimpo.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.CLimpo.ModuloCor  = "green"
			Info.IsoRadio.CLimpo.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.CLimpo.ModuloCor  = "green"
			Info.IsoRadio.CLimpo.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.CLimpo.ModuloCor  = "blue"
			Info.IsoRadio.CLimpo.RelogioCor = "blue"
		else:
			Info.IsoRadio.CLimpo.ModuloCor  = "pink"
			Info.IsoRadio.CLimpo.RelogioCor = "pink"


	elif relogio == "ipiranga":


		if result == 1:
			Info.IsoRadio.Ipiranga.ModuloCor  = "red"
			Info.IsoRadio.Ipiranga.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.Ipiranga.ModuloCor  = "green"
			Info.IsoRadio.Ipiranga.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.Ipiranga.ModuloCor  = "green"
			Info.IsoRadio.Ipiranga.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.Ipiranga.ModuloCor  = "blue"
			Info.IsoRadio.Ipiranga.RelogioCor = "blue"
		else:
			Info.IsoRadio.Ipiranga.ModuloCor  = "pink"
			Info.IsoRadio.Ipiranga.RelogioCor = "pink"

	elif relogio == "anarosa":

		if result == 1:
			Info.IsoRadio.AnaRosa.ModuloCor  = "red"
			Info.IsoRadio.AnaRosa.RelogioCor = "red"
		elif result == 2:
			Info.IsoRadio.AnaRosa.ModuloCor  = "green"
			Info.IsoRadio.AnaRosa.RelogioCor = "red"
		elif result == 3:
			Info.IsoRadio.AnaRosa.ModuloCor  = "green"
			Info.IsoRadio.AnaRosa.RelogioCor = "green"
		elif result == 4:
			Info.IsoRadio.AnaRosa.ModuloCor  = "blue"
			Info.IsoRadio.AnaRosa.RelogioCor = "blue"
		else:
			Info.IsoRadio.AnaRosa.ModuloCor  = "pink"
			Info.IsoRadio.AnaRosa.RelogioCor = "pink"


	if result != 4:
		Info.IsoRadio.Status.Contage = 0

		if Info.IsoRadio.Santana.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.SaoMatheus.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.VilaMariana.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Lapa.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.SAmaro.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.CDutra.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Tatuape.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.CLimpo.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.Ipiranga.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

		if Info.IsoRadio.AnaRosa.ModuloCor == "green" :
			Info.IsoRadio.Status.Contage = Info.IsoRadio.Status.Contage + 1

def AtualizaCorGrupoNk(relogio,result):

	if relogio == "nelson":

		if result == 1:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "red"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "green"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "green"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "blue"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "blue"
		else:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "pink"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "pink"


	elif relogio == "furukawa":

		if result == 1:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "red"
			Info.GrupoNk.RDFurukawa.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "green"
			Info.GrupoNk.RDFurukawa.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "green"
			Info.GrupoNk.RDFurukawa.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "blue"
			Info.GrupoNk.RDFurukawa.RelogioCor = "blue"
		else:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "pink"
			Info.GrupoNk.RDFurukawa.RelogioCor = "pink"


	elif relogio == "kio1":

		if result == 1:
			Info.GrupoNk.Kio1.ModuloCor  = "red"
			Info.GrupoNk.Kio1.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Kio1.ModuloCor  = "green"
			Info.GrupoNk.Kio1.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.Kio1.ModuloCor  = "green"
			Info.GrupoNk.Kio1.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.Kio1.ModuloCor  = "blue"
			Info.GrupoNk.Kio1.RelogioCor = "blue"
		else:
			Info.GrupoNk.Kio1.ModuloCor  = "pink"
			Info.GrupoNk.Kio1.RelogioCor = "pink"



	elif relogio == "kio2":

		if result == 1:
			Info.GrupoNk.Kio2.ModuloCor  = "red"
			Info.GrupoNk.Kio2.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Kio2.ModuloCor  = "green"
			Info.GrupoNk.Kio2.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.Kio2.ModuloCor  = "green"
			Info.GrupoNk.Kio2.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.Kio2.ModuloCor  = "blue"
			Info.GrupoNk.Kio2.RelogioCor = "blue"
		else:
			Info.GrupoNk.Kio2.ModuloCor  = "pink"
			Info.GrupoNk.Kio2.RelogioCor = "pink"


	elif relogio == "granjaviana":

		if result == 1:
			Info.GrupoNk.GranjaViana.ModuloCor  = "red"
			Info.GrupoNk.GranjaViana.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.GranjaViana.ModuloCor  = "green"
			Info.GrupoNk.GranjaViana.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.GranjaViana.ModuloCor  = "green"
			Info.GrupoNk.GranjaViana.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.GranjaViana.ModuloCor  = "blue"
			Info.GrupoNk.GranjaViana.RelogioCor = "blue"
		else:
			Info.GrupoNk.GranjaViana.ModuloCor  = "pink"
			Info.GrupoNk.GranjaViana.RelogioCor = "pink"


	elif relogio == "santacecilia":

		if result == 1:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "red"
			Info.GrupoNk.SantaCecilia.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "green"
			Info.GrupoNk.SantaCecilia.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "green"
			Info.GrupoNk.SantaCecilia.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "blue"
			Info.GrupoNk.SantaCecilia.RelogioCor = "blue"
		else:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "pink"
			Info.GrupoNk.SantaCecilia.RelogioCor = "pink"


	elif relogio == "transfruit":

		if result == 1:
			Info.GrupoNk.Transfruit.ModuloCor  = "red"
			Info.GrupoNk.Transfruit.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Transfruit.ModuloCor  = "green"
			Info.GrupoNk.Transfruit.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.Transfruit.ModuloCor  = "green"
			Info.GrupoNk.Transfruit.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.Transfruit.ModuloCor  = "blue"
			Info.GrupoNk.Transfruit.RelogioCor = "blue"
		else:
			Info.GrupoNk.Transfruit.ModuloCor  = "pink"
			Info.GrupoNk.Transfruit.RelogioCor = "pink"

	elif relogio == "distrdefrutas":

		if result == 1:
			Info.GrupoNk.Distribuidora.ModuloCor  = "red"
			Info.GrupoNk.Distribuidora.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.Distribuidora.ModuloCor  = "green"
			Info.GrupoNk.Distribuidora.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.Distribuidora.ModuloCor  = "green"
			Info.GrupoNk.Distribuidora.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.Distribuidora.ModuloCor  = "blue"
			Info.GrupoNk.Distribuidora.RelogioCor = "blue"
		else:
			Info.GrupoNk.Distribuidora.ModuloCor  = "pink"
			Info.GrupoNk.Distribuidora.RelogioCor = "pink"


	elif relogio == "nkhortifruit":

		if result == 1:
			Info.GrupoNk.NKFilial.ModuloCor  = "red"
			Info.GrupoNk.NKFilial.RelogioCor = "red"
		elif result == 2:
			Info.GrupoNk.NKFilial.ModuloCor  = "green"
			Info.GrupoNk.NKFilial.RelogioCor = "red"
		elif result == 3:
			Info.GrupoNk.NKFilial.ModuloCor  = "green"
			Info.GrupoNk.NKFilial.RelogioCor = "green"
		elif result == 4:
			Info.GrupoNk.NKFilial.ModuloCor  = "blue"
			Info.GrupoNk.NKFilial.RelogioCor = "blue"
		else:
			Info.GrupoNk.NKFilial.ModuloCor  = "pink"
			Info.GrupoNk.NKFilial.RelogioCor = "pink"



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


