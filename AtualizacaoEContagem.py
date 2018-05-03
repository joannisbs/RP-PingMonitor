
from Var import *



def AtualizaCorBuilding(relogio,result):

	if relogio == "allianz":
			
		if result == 1:
			Info.Building.Allianz.ModuloCor  = "firebrick1"
			Info.Building.Allianz.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Building.Allianz.ModuloCor  = "green3"
			Info.Building.Allianz.RelogioCor = "red4"
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
			Info.Building.WTorre.ModuloCor  = "firebrick1"
			Info.Building.WTorre.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Building.WTorre.ModuloCor  = "green3"
			Info.Building.WTorre.RelogioCor = "red4"
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
			Info.Building.RioJaneiro.ModuloCor  = "firebrick1"
			Info.Building.RioJaneiro.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Building.RioJaneiro.ModuloCor  = "green3"
			Info.Building.RioJaneiro.RelogioCor = "red4"
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
			Info.Laser.Academia.ModuloCor  = "firebrick1"
			Info.Laser.Academia.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Laser.Academia.ModuloCor  = "green3"
			Info.Laser.Academia.RelogioCor = "red4"
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
			Info.Laser.Instituto.ModuloCor  = "firebrick1"
			Info.Laser.Instituto.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Laser.Instituto.ModuloCor  = "green3"
			Info.Laser.Instituto.RelogioCor = "red4"
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

	if result !=4:
		Info.Laser.Status.Contage = 0
		if Info.Laser.Academia.RelogioCor == "green3" : 
				Info.Laser.Status.Contage = Info.Laser.Status.Contage +1
		if Info.Laser.Instituto.RelogioCor == "green3" : 
				Info.Laser.Status.Contage = Info.Laser.Status.Contage +1


def AtualizaCorGravex(relogio,result):

	if relogio == "adm":

		if result == 1:
			Info.Gravex.ADM.ModuloCor  = "firebrick1"
			Info.Gravex.ADM.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Gravex.ADM.ModuloCor  = "green3"
			Info.Gravex.ADM.RelogioCor = "red4"
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
			Info.Gravex.Loja1.ModuloCor  = "firebrick1"
			Info.Gravex.Loja1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Gravex.Loja1.ModuloCor  = "green3"
			Info.Gravex.Loja1.RelogioCor = "red4"
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
			Info.Gravex.MiMarcos.ModuloCor  = "firebrick1"
			Info.Gravex.MiMarcos.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Gravex.MiMarcos.ModuloCor  = "green3"
			Info.Gravex.MiMarcos.RelogioCor = "red4"
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
			Info.Gravex.DantChini.ModuloCor  = "firebrick1"
			Info.Gravex.DantChini.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Gravex.DantChini.ModuloCor  = "green3"
			Info.Gravex.DantChini.RelogioCor = "red4"
		elif result == 3:
			Info.Gravex.DantChini.ModuloCor  = "green3"
			Info.Gravex.DantChini.RelogioCor = "green3"
		elif result == 4:
			Info.Gravex.DantChini.ModuloCor  = "cyan"
			#Info.Gravex.DantChini.RelogioCor = "cyan"
		else:
			Info.Gravex.DantChini.ModuloCor  = "pink"
			Info.Gravex.DantChini.RelogioCor = "pink"

	if result != 4:
		Info.Gravex.Status.Contage = 0

		if Info.Gravex.ADM.RelogioCor == "green3" : 
			Info.Gravex.Status.Contage = Info.Gravex.Status.Contage +1

		if Info.Gravex.Loja1.RelogioCor == "green3" : 
			Info.Gravex.Status.Contage = Info.Gravex.Status.Contage +1

		if Info.Gravex.MiMarcos.RelogioCor == "green3" : 
			Info.Gravex.Status.Contage = Info.Gravex.Status.Contage +1

		if Info.Gravex.DantChini.RelogioCor == "green3" : 
			Info.Gravex.Status.Contage = Info.Gravex.Status.Contage +1


def AtualizaCorCasaCristo(relogio,result):

	if relogio == "adm":

		if result == 1:
			Info.CasaCristo.ADM.ModuloCor  = "firebrick1"
			Info.CasaCristo.ADM.RelogioCor = "firebrick1"
		elif result == 2:
			Info.CasaCristo.ADM.ModuloCor  = "green3"
			Info.CasaCristo.ADM.RelogioCor = "red4"
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
			Info.CasaCristo.CEI1.ModuloCor  = "firebrick1"
			Info.CasaCristo.CEI1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.CasaCristo.CEI1.ModuloCor  = "green3"
			Info.CasaCristo.CEI1.RelogioCor = "red4"
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
			Info.CasaCristo.CEI2.ModuloCor  = "firebrick1"
			Info.CasaCristo.CEI2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.CasaCristo.CEI2.ModuloCor  = "green3"
			Info.CasaCristo.CEI2.RelogioCor = "red4"
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
			Info.CasaCristo.CEI3.ModuloCor  = "firebrick1"
			Info.CasaCristo.CEI3.RelogioCor = "firebrick1"
		elif result == 2:
			Info.CasaCristo.CEI3.ModuloCor  = "green3"
			Info.CasaCristo.CEI3.RelogioCor = "red4"
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
			Info.CasaCristo.VovoMatilde.ModuloCor  = "firebrick1"
			Info.CasaCristo.VovoMatilde.RelogioCor = "firebrick1"
		elif result == 2:
			Info.CasaCristo.VovoMatilde.ModuloCor  = "green3"
			Info.CasaCristo.VovoMatilde.RelogioCor = "red4"
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
			Info.BestInClass.Recife.ModuloCor  = "firebrick1"
			Info.BestInClass.Recife.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Recife.ModuloCor  = "green3"
			Info.BestInClass.Recife.RelogioCor = "red4"
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
			Info.BestInClass.Itaquera.ModuloCor  = "firebrick1"
			Info.BestInClass.Itaquera.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Itaquera.ModuloCor  = "green3"
			Info.BestInClass.Itaquera.RelogioCor = "red4"
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
			Info.BestInClass.Itapevi.ModuloCor  = "firebrick1"
			Info.BestInClass.Itapevi.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Itapevi.ModuloCor  = "green3"
			Info.BestInClass.Itapevi.RelogioCor = "red4"
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
			Info.BestInClass.Sorocaba.ModuloCor  = "firebrick1"
			Info.BestInClass.Sorocaba.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Sorocaba.ModuloCor  = "green3"
			Info.BestInClass.Sorocaba.RelogioCor = "red4"
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
			Info.BestInClass.SeteLagoas.ModuloCor  = "firebrick1"
			Info.BestInClass.SeteLagoas.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.SeteLagoas.ModuloCor  = "green3"
			Info.BestInClass.SeteLagoas.RelogioCor = "red4"
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
			Info.BestInClass.Curitiba.ModuloCor  = "firebrick1"
			Info.BestInClass.Curitiba.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Curitiba.ModuloCor  = "green3"
			Info.BestInClass.Curitiba.RelogioCor = "red4"
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
			Info.BestInClass.Fsantana.ModuloCor  = "firebrick1"
			Info.BestInClass.Fsantana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Fsantana.ModuloCor  = "green3"
			Info.BestInClass.Fsantana.RelogioCor = "red4"
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
			Info.BestInClass.Itu.ModuloCor  = "firebrick1"
			Info.BestInClass.Itu.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Itu.ModuloCor  = "green3"
			Info.BestInClass.Itu.RelogioCor = "red4"
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
			Info.BestInClass.Guarulhos.ModuloCor  = "firebrick1"
			Info.BestInClass.Guarulhos.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Guarulhos.ModuloCor  = "green3"
			Info.BestInClass.Guarulhos.RelogioCor = "red4"
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
			Info.BestInClass.Itaporanga.ModuloCor  = "firebrick1"
			Info.BestInClass.Itaporanga.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Itaporanga.ModuloCor  = "green3"
			Info.BestInClass.Itaporanga.RelogioCor = "red4"
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
			Info.BestInClass.Linhares.ModuloCor  = "firebrick1"
			Info.BestInClass.Linhares.RelogioCor = "firebrick1"
		elif result == 2:
			Info.BestInClass.Linhares.ModuloCor  = "green3"
			Info.BestInClass.Linhares.RelogioCor = "red4"
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
			Info.IsoRadio.Santana.ModuloCor  = "firebrick1"
			Info.IsoRadio.Santana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.Santana.ModuloCor  = "green3"
			Info.IsoRadio.Santana.RelogioCor = "red4"
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
			Info.IsoRadio.SaoMatheus.ModuloCor  = "firebrick1"
			Info.IsoRadio.SaoMatheus.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.SaoMatheus.ModuloCor  = "green3"
			Info.IsoRadio.SaoMatheus.RelogioCor = "red4"
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
			Info.IsoRadio.VilaMariana.ModuloCor  = "firebrick1"
			Info.IsoRadio.VilaMariana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.VilaMariana.ModuloCor  = "green3"
			Info.IsoRadio.VilaMariana.RelogioCor = "red4"
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
			Info.IsoRadio.Lapa.ModuloCor  = "firebrick1"
			Info.IsoRadio.Lapa.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.Lapa.ModuloCor  = "green3"
			Info.IsoRadio.Lapa.RelogioCor = "red4"
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
			Info.IsoRadio.SAmaro.ModuloCor  = "firebrick1"
			Info.IsoRadio.SAmaro.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.SAmaro.ModuloCor  = "green3"
			Info.IsoRadio.SAmaro.RelogioCor = "red4"
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
			Info.IsoRadio.CDutra.ModuloCor  = "firebrick1"
			Info.IsoRadio.CDutra.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.CDutra.ModuloCor  = "green3"
			Info.IsoRadio.CDutra.RelogioCor = "red4"
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
			Info.IsoRadio.Tatuape.ModuloCor  = "firebrick1"
			Info.IsoRadio.Tatuape.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.Tatuape.ModuloCor  = "green3"
			Info.IsoRadio.Tatuape.RelogioCor = "red4"
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
			Info.IsoRadio.CLimpo.ModuloCor  = "firebrick1"
			Info.IsoRadio.CLimpo.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.CLimpo.ModuloCor  = "green3"
			Info.IsoRadio.CLimpo.RelogioCor = "red4"
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
			Info.IsoRadio.Ipiranga.ModuloCor  = "firebrick1"
			Info.IsoRadio.Ipiranga.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.Ipiranga.ModuloCor  = "green3"
			Info.IsoRadio.Ipiranga.RelogioCor = "red4"
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
			Info.IsoRadio.AnaRosa.ModuloCor  = "firebrick1"
			Info.IsoRadio.AnaRosa.RelogioCor = "firebrick1"
		elif result == 2:
			Info.IsoRadio.AnaRosa.ModuloCor  = "green3"
			Info.IsoRadio.AnaRosa.RelogioCor = "red4"
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
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "firebrick1"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.NelsonKioshi.ModuloCor  = "green3"
			Info.GrupoNk.NelsonKioshi.RelogioCor = "red4"
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
			Info.GrupoNk.RDFurukawa.ModuloCor  = "firebrick1"
			Info.GrupoNk.RDFurukawa.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.RDFurukawa.ModuloCor  = "green3"
			Info.GrupoNk.RDFurukawa.RelogioCor = "red4"
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
			Info.GrupoNk.Kio1.ModuloCor  = "firebrick1"
			Info.GrupoNk.Kio1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.Kio1.ModuloCor  = "green3"
			Info.GrupoNk.Kio1.RelogioCor = "red4"
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
			Info.GrupoNk.Kio2.ModuloCor  = "firebrick1"
			Info.GrupoNk.Kio2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.Kio2.ModuloCor  = "green3"
			Info.GrupoNk.Kio2.RelogioCor = "red4"
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
			Info.GrupoNk.GranjaViana.ModuloCor  = "firebrick1"
			Info.GrupoNk.GranjaViana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.GranjaViana.ModuloCor  = "green3"
			Info.GrupoNk.GranjaViana.RelogioCor = "red4"
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
			Info.GrupoNk.SantaCecilia.ModuloCor  = "firebrick1"
			Info.GrupoNk.SantaCecilia.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.SantaCecilia.ModuloCor  = "green3"
			Info.GrupoNk.SantaCecilia.RelogioCor = "red4"
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
			Info.GrupoNk.Transfruit.ModuloCor  = "firebrick1"
			Info.GrupoNk.Transfruit.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.Transfruit.ModuloCor  = "green3"
			Info.GrupoNk.Transfruit.RelogioCor = "red4"
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
			Info.GrupoNk.Distribuidora.ModuloCor  = "firebrick1"
			Info.GrupoNk.Distribuidora.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.Distribuidora.ModuloCor  = "green3"
			Info.GrupoNk.Distribuidora.RelogioCor = "red4"
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
			Info.GrupoNk.NKFilial.ModuloCor  = "firebrick1"
			Info.GrupoNk.NKFilial.RelogioCor = "firebrick1"
		elif result == 2:
			Info.GrupoNk.NKFilial.ModuloCor  = "green3"
			Info.GrupoNk.NKFilial.RelogioCor = "red4"
		elif result == 3:
			Info.GrupoNk.NKFilial.ModuloCor  = "green3"
			Info.GrupoNk.NKFilial.RelogioCor = "green3"
		elif result == 4:
			Info.GrupoNk.NKFilial.ModuloCor  = "cyan"
			#Info.GrupoNk.NKFilial.RelogioCor = "cyan"
		else:
			Info.GrupoNk.NKFilial.ModuloCor  = "pink"
			Info.GrupoNk.NKFilial.RelogioCor = "pink"

	if result != 4:
		Info.GrupoNk.Status.Contage = 0
		if Info.GrupoNk.NelsonKioshi.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.RDFurukawa.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.Kio1.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.Kio2.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.GranjaViana.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.SantaCecilia.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.Transfruit.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.Distribuidora.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1
		if Info.GrupoNk.NKFilial.RelogioCor == "green3" : 
				Info.GrupoNk.Status.Contage = Info.GrupoNk.Status.Contage +1


def AtualizaLotten(relogio,result):

	if relogio == "sfjardins":

		if result == 1:
			Info.Lotten.Jardins.ModuloCor  = "firebrick1"
			Info.Lotten.Jardins.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Jardins.ModuloCor  = "green3"
			Info.Lotten.Jardins.RelogioCor = "red4"
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
			Info.Lotten.Alphaville.ModuloCor  = "firebrick1"
			Info.Lotten.Alphaville.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Alphaville.ModuloCor  = "green3"
			Info.Lotten.Alphaville.RelogioCor = "red4"
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
			Info.Lotten.Osasco.ModuloCor  = "firebrick1"
			Info.Lotten.Osasco.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Osasco.ModuloCor  = "green3"
			Info.Lotten.Osasco.RelogioCor = "red4"
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
			Info.Lotten.Santana.ModuloCor  = "firebrick1"
			Info.Lotten.Santana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Santana.ModuloCor  = "green3"
			Info.Lotten.Santana.RelogioCor = "red4"
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
			Info.Lotten.Tatuape.ModuloCor  = "firebrick1"
			Info.Lotten.Tatuape.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Tatuape.ModuloCor  = "green3"
			Info.Lotten.Tatuape.RelogioCor = "red4"
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
			Info.Lotten.Moema.ModuloCor  = "firebrick1"
			Info.Lotten.Moema.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Moema.ModuloCor  = "green3"
			Info.Lotten.Moema.RelogioCor = "red4"
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
			Info.Lotten.JardimSul.ModuloCor  = "firebrick1"
			Info.Lotten.JardimSul.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.JardimSul.ModuloCor  = "green3"
			Info.Lotten.JardimSul.RelogioCor = "red4"
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
			Info.Lotten.Conceicao.ModuloCor  = "firebrick1"
			Info.Lotten.Conceicao.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Conceicao.ModuloCor  = "green3"
			Info.Lotten.Conceicao.RelogioCor = "red4"
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
			Info.Lotten.Lapa.ModuloCor  = "firebrick1"
			Info.Lotten.Lapa.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Lapa.ModuloCor  = "green3"
			Info.Lotten.Lapa.RelogioCor = "red4"
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
			Info.Lotten.Perdizes.ModuloCor  = "firebrick1"
			Info.Lotten.Perdizes.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Perdizes.ModuloCor  = "green3"
			Info.Lotten.Perdizes.RelogioCor = "red4"
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
			Info.Lotten.SaoCaetano.ModuloCor  = "firebrick1"
			Info.Lotten.SaoCaetano.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.SaoCaetano.ModuloCor  = "green3"
			Info.Lotten.SaoCaetano.RelogioCor = "red4"
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
			Info.Lotten.Pinheiros.ModuloCor  = "firebrick1"
			Info.Lotten.Pinheiros.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Pinheiros.ModuloCor  = "green3"
			Info.Lotten.Pinheiros.RelogioCor = "red4"
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
			Info.Lotten.Morumbi.ModuloCor  = "firebrick1"
			Info.Lotten.Morumbi.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Morumbi.ModuloCor  = "green3"
			Info.Lotten.Morumbi.RelogioCor = "red4"
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
			Info.Lotten.Berrini.ModuloCor  = "firebrick1"
			Info.Lotten.Berrini.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Berrini.ModuloCor  = "green3"
			Info.Lotten.Berrini.RelogioCor = "red4"
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
			Info.Lotten.VilaMariana.ModuloCor  = "firebrick1"
			Info.Lotten.VilaMariana.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.VilaMariana.ModuloCor  = "green3"
			Info.Lotten.VilaMariana.RelogioCor = "red4"
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
			Info.Lotten.VilaOlimpia.ModuloCor  = "firebrick1"
			Info.Lotten.VilaOlimpia.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.VilaOlimpia.ModuloCor  = "green3"
			Info.Lotten.VilaOlimpia.RelogioCor = "red4"
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
			Info.Lotten.Itaim.ModuloCor  = "firebrick1"
			Info.Lotten.Itaim.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Itaim.ModuloCor  = "green3"
			Info.Lotten.Itaim.RelogioCor = "red4"
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
			Info.Lotten.Guarulhos.ModuloCor  = "firebrick1"
			Info.Lotten.Guarulhos.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Lotten.Guarulhos.ModuloCor  = "green3"
			Info.Lotten.Guarulhos.RelogioCor = "red4"
		elif result == 3:
			Info.Lotten.Guarulhos.ModuloCor  = "green3"
			Info.Lotten.Guarulhos.RelogioCor = "green3"
		elif result == 4:
			Info.Lotten.Guarulhos.ModuloCor  = "cyan"
			#Info.Lotten.Guarulhos.RelogioCor = "cyan"
		else:
			Info.Lotten.Guarulhos.ModuloCor  = "pink"
			Info.Lotten.Guarulhos.RelogioCor = "pink"

	if result != 4:
		Info.Lotten.Status.Contage = 0
		if Info.Lotten.Jardins.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Alphaville.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Osasco.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Santana.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Tatuape.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Moema.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.JardimSul.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Conceicao.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Perdizes.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Lapa.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.SaoCaetano.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Pinheiros.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Morumbi.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Berrini.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.VilaMariana.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.VilaOlimpia.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Itaim.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1
		if Info.Lotten.Guarulhos.RelogioCor == "green3" : 
				Info.Lotten.Status.Contage = Info.Lotten.Status.Contage +1


def AtualizaElRio(relogio, result):



	if relogio == "botafogomuniz":

		if result == 1:
			Info.ElRio.BotafogoMuniz.ModuloCor  = "firebrick1"
			Info.ElRio.BotafogoMuniz.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.BotafogoMuniz.ModuloCor  = "green3"
			Info.ElRio.BotafogoMuniz.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.BotafogoMuniz.ModuloCor  = "green3"
			Info.ElRio.BotafogoMuniz.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.BotafogoMuniz.ModuloCor  = "cyan"
			#Info.ElRio.BotafogoMuniz.RelogioCor = "cyan"
		else:
			Info.ElRio.BotafogoMuniz.ModuloCor  = "pink"
			Info.ElRio.BotafogoMuniz.RelogioCor = "pink"

	elif relogio == "botafogopraia":

		if result == 1:
			Info.ElRio.BotafogoPraia.ModuloCor  = "firebrick1"
			Info.ElRio.BotafogoPraia.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.BotafogoPraia.ModuloCor  = "green3"
			Info.ElRio.BotafogoPraia.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.BotafogoPraia.ModuloCor  = "green3"
			Info.ElRio.BotafogoPraia.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.BotafogoPraia.ModuloCor  = "cyan"
			#Info.ElRio.BotafogoPraia.RelogioCor = "cyan"
		else:
			Info.ElRio.BotafogoPraia.ModuloCor  = "pink"
			Info.ElRio.BotafogoPraia.RelogioCor = "pink"


	elif relogio == "boulevard":

		if result == 1:
			Info.ElRio.Boulevard.ModuloCor  = "firebrick1"
			Info.ElRio.Boulevard.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Boulevard.ModuloCor  = "green3"
			Info.ElRio.Boulevard.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Boulevard.ModuloCor  = "green3"
			Info.ElRio.Boulevard.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Boulevard.ModuloCor  = "cyan"
			#Info.ElRio.Boulevard.RelogioCor = "cyan"
		else:
			Info.ElRio.Boulevard.ModuloCor  = "pink"
			Info.ElRio.Boulevard.RelogioCor = "pink"

	elif relogio == "carioca":

		if result == 1:
			Info.ElRio.Carioca.ModuloCor  = "firebrick1"
			Info.ElRio.Carioca.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Carioca.ModuloCor  = "green3"
			Info.ElRio.Carioca.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Carioca.ModuloCor  = "green3"
			Info.ElRio.Carioca.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Carioca.ModuloCor  = "cyan"
			#Info.ElRio.Carioca.RelogioCor = "cyan"
		else:
			Info.ElRio.Carioca.ModuloCor  = "pink"
			Info.ElRio.Carioca.RelogioCor = "pink"

	
	elif relogio == "centro1":

		if result == 1:
			Info.ElRio.Centro1.ModuloCor  = "firebrick1"
			Info.ElRio.Centro1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Centro1.ModuloCor  = "green3"
			Info.ElRio.Centro1.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Centro1.ModuloCor  = "green3"
			Info.ElRio.Centro1.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Centro1.ModuloCor  = "cyan"
			#Info.ElRio.Centro1.RelogioCor = "cyan"
		else:
			Info.ElRio.Centro1.ModuloCor  = "pink"
			Info.ElRio.Centro1.RelogioCor = "pink"

	elif relogio == "centro2":
	
		if result == 1:
			Info.ElRio.Centro2.ModuloCor  = "firebrick1"
			Info.ElRio.Centro2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Centro2.ModuloCor  = "green3"
			Info.ElRio.Centro2.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Centro2.ModuloCor  = "green3"
			Info.ElRio.Centro2.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Centro2.ModuloCor  = "cyan"
			#Info.ElRio.Centro2.RelogioCor = "cyan"
		else:
			Info.ElRio.Centro2.ModuloCor  = "pink"
			Info.ElRio.Centro2.RelogioCor = "pink"

	elif relogio == "centro3":

		if result == 1:
			Info.ElRio.Centro3.ModuloCor  = "firebrick1"
			Info.ElRio.Centro3.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Centro3.ModuloCor  = "green3"
			Info.ElRio.Centro3.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Centro3.ModuloCor  = "green3"
			Info.ElRio.Centro3.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Centro3.ModuloCor  = "cyan"
			#Info.ElRio.Centro3.RelogioCor = "cyan"
		else:
			Info.ElRio.Centro3.ModuloCor  = "pink"
			Info.ElRio.Centro3.RelogioCor = "pink"



	elif relogio == "fashion":

		if result == 1:
			Info.ElRio.Fashion.ModuloCor  = "firebrick1"
			Info.ElRio.Fashion.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Fashion.ModuloCor  = "green3"
			Info.ElRio.Fashion.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Fashion.ModuloCor  = "green3"
			Info.ElRio.Fashion.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Fashion.ModuloCor  = "cyan"
			#Info.ElRio.Fashion.RelogioCor = "cyan"
		else:
			Info.ElRio.Fashion.ModuloCor  = "pink"
			Info.ElRio.Fashion.RelogioCor = "pink"


	elif relogio == "flamengo":

		if result == 1:
			Info.ElRio.Flamengo.ModuloCor  = "firebrick1"
			Info.ElRio.Flamengo.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Flamengo.ModuloCor  = "green3"
			Info.ElRio.Flamengo.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Flamengo.ModuloCor  = "green3"
			Info.ElRio.Flamengo.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Flamengo.ModuloCor  = "cyan"
			#Info.ElRio.Flamengo.RelogioCor = "cyan"
		else:
			Info.ElRio.Flamengo.ModuloCor  = "pink"
			Info.ElRio.Flamengo.RelogioCor = "pink"

	

	elif relogio == "leblon":

		if result == 1:
			Info.ElRio.Leblon.ModuloCor  = "firebrick1"
			Info.ElRio.Leblon.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Leblon.ModuloCor  = "green3"
			Info.ElRio.Leblon.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Leblon.ModuloCor  = "green3"
			Info.ElRio.Leblon.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Leblon.ModuloCor  = "cyan"
			#Info.ElRio.Leblon.RelogioCor = "cyan"
		else:
			Info.ElRio.Leblon.ModuloCor  = "pink"
			Info.ElRio.Leblon.RelogioCor = "pink"

	

	elif relogio == "novaamerica":

		if result == 1:
			Info.ElRio.NovaAmerica.ModuloCor  = "firebrick1"
			Info.ElRio.NovaAmerica.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.NovaAmerica.ModuloCor  = "green3"
			Info.ElRio.NovaAmerica.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.NovaAmerica.ModuloCor  = "green3"
			Info.ElRio.NovaAmerica.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.NovaAmerica.ModuloCor  = "cyan"
			#Info.ElRio.NovaAmerica.RelogioCor = "cyan"
		else:
			Info.ElRio.NovaAmerica.ModuloCor  = "pink"
			Info.ElRio.NovaAmerica.RelogioCor = "pink"

	

	elif relogio == "shopgrande":

		if result == 1:
			Info.ElRio.ShopGrande.ModuloCor  = "firebrick1"
			Info.ElRio.ShopGrande.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.ShopGrande.ModuloCor  = "green3"
			Info.ElRio.ShopGrande.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.ShopGrande.ModuloCor  = "green3"
			Info.ElRio.ShopGrande.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.ShopGrande.ModuloCor  = "cyan"
			#Info.ElRio.ShopGrande.RelogioCor = "cyan"
		else:
			Info.ElRio.ShopGrande.ModuloCor  = "pink"
			Info.ElRio.ShopGrande.RelogioCor = "pink"

	

	elif relogio == "shopmacae":

		if result == 1:
			Info.ElRio.ShopMacae.ModuloCor  = "firebrick1"
			Info.ElRio.ShopMacae.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.ShopMacae.ModuloCor  = "green3"
			Info.ElRio.ShopMacae.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.ShopMacae.ModuloCor  = "green3"
			Info.ElRio.ShopMacae.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.ShopMacae.ModuloCor  = "cyan"
			#Info.ElRio.ShopMacae.RelogioCor = "cyan"
		else:
			Info.ElRio.ShopMacae.ModuloCor  = "pink"
			Info.ElRio.ShopMacae.RelogioCor = "pink"

	

	elif relogio == "shopnorte":

		if result == 1:
			Info.ElRio.ShopNorte.ModuloCor  = "firebrick1"
			Info.ElRio.ShopNorte.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.ShopNorte.ModuloCor  = "green3"
			Info.ElRio.ShopNorte.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.ShopNorte.ModuloCor  = "green3"
			Info.ElRio.ShopNorte.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.ShopNorte.ModuloCor  = "cyan"
			#Info.ElRio.ShopNorte.RelogioCor = "cyan"
		else:
			Info.ElRio.ShopNorte.ModuloCor  = "pink"
			Info.ElRio.ShopNorte.RelogioCor = "pink"

	

	elif relogio == "backup1":

		if result == 1:
			Info.ElRio.Backup1.ModuloCor  = "firebrick1"
			Info.ElRio.Backup1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Backup1.ModuloCor  = "green3"
			Info.ElRio.Backup1.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Backup1.ModuloCor  = "green3"
			Info.ElRio.Backup1.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Backup1.ModuloCor  = "cyan"
			#Info.ElRio.Backup1.RelogioCor = "cyan"
		else:
			Info.ElRio.Backup1.ModuloCor  = "pink"
			Info.ElRio.Backup1.RelogioCor = "pink"

	

	elif relogio == "backup2":

		if result == 1:
			Info.ElRio.Backup2.ModuloCor  = "firebrick1"
			Info.ElRio.Backup2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.ElRio.Backup2.ModuloCor  = "green3"
			Info.ElRio.Backup2.RelogioCor = "red4"
		elif result == 3:
			Info.ElRio.Backup2.ModuloCor  = "green3"
			Info.ElRio.Backup2.RelogioCor = "green3"
		elif result == 4:
			Info.ElRio.Backup2.ModuloCor  = "cyan"
			#Info.ElRio.Backup2.RelogioCor = "cyan"
		else:
			Info.ElRio.Backup2.ModuloCor  = "pink"
			Info.ElRio.Backup2.RelogioCor = "pink"


	if result != 4:
		Info.ElRio.Status.Contage = 0
		if Info.ElRio.BotafogoMuniz.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.BotafogoPraia.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Boulevard.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Carioca.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Centro3.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Centro2.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Centro1.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Fashion.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Flamengo.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Leblon.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.NovaAmerica.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.ShopNorte.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.ShopGrande.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.ShopMacae.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Backup1.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1

		if Info.ElRio.Backup2.RelogioCor == "green3" : 
				Info.ElRio.Status.Contage = Info.ElRio.Status.Contage +1
	

def AtualizaSBCP(relogio, result):

	if relogio == "nacional":

		if result == 1:
			Info.SBCP.Nacional.ModuloCor  = "firebrick1"
			Info.SBCP.Nacional.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.Nacional.ModuloCor  = "green3"
			Info.SBCP.Nacional.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.Nacional.ModuloCor  = "green3"
			Info.SBCP.Nacional.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.Nacional.ModuloCor  = "cyan"
			#Info.SBCP.Nacional.RelogioCor = "cyan"
		else:
			Info.SBCP.Nacional.ModuloCor  = "pink"
			Info.SBCP.Nacional.RelogioCor = "pink"







	elif relogio == "es":

		if result == 1:
			Info.SBCP.ES.ModuloCor  = "firebrick1"
			Info.SBCP.ES.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.ES.ModuloCor  = "green3"
			Info.SBCP.ES.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.ES.ModuloCor  = "green3"
			Info.SBCP.ES.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.ES.ModuloCor  = "cyan"
			#Info.SBCP.ES.RelogioCor = "cyan"
		else:
			Info.SBCP.ES.ModuloCor  = "pink"
			Info.SBCP.ES.RelogioCor = "pink"







	elif relogio == "df":

		if result == 1:
			Info.SBCP.DF.ModuloCor  = "firebrick1"
			Info.SBCP.DF.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.DF.ModuloCor  = "green3"
			Info.SBCP.DF.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.DF.ModuloCor  = "green3"
			Info.SBCP.DF.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.DF.ModuloCor  = "cyan"
			#Info.SBCP.DF.RelogioCor = "cyan"
		else:
			Info.SBCP.DF.ModuloCor  = "pink"
			Info.SBCP.DF.RelogioCor = "pink"







	elif relogio == "ce":

		if result == 1:
			Info.SBCP.CE.ModuloCor  = "firebrick1"
			Info.SBCP.CE.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.CE.ModuloCor  = "green3"
			Info.SBCP.CE.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.CE.ModuloCor  = "green3"
			Info.SBCP.CE.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.CE.ModuloCor  = "cyan"
			#Info.SBCP.CE.RelogioCor = "cyan"
		else:
			Info.SBCP.CE.ModuloCor  = "pink"
			Info.SBCP.CE.RelogioCor = "pink"







	elif relogio == "ba":

		if result == 1:
			Info.SBCP.BA.ModuloCor  = "firebrick1"
			Info.SBCP.BA.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.BA.ModuloCor  = "green3"
			Info.SBCP.BA.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.BA.ModuloCor  = "green3"
			Info.SBCP.BA.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.BA.ModuloCor  = "cyan"
			#Info.SBCP.BA.RelogioCor = "cyan"
		else:
			Info.SBCP.BA.ModuloCor  = "pink"
			Info.SBCP.BA.RelogioCor = "pink"







	elif relogio == "sp":

		if result == 1:
			Info.SBCP.SP.ModuloCor  = "firebrick1"
			Info.SBCP.SP.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.SP.ModuloCor  = "green3"
			Info.SBCP.SP.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.SP.ModuloCor  = "green3"
			Info.SBCP.SP.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.SP.ModuloCor  = "cyan"
			#Info.SBCP.SP.RelogioCor = "cyan"
		else:
			Info.SBCP.SP.ModuloCor  = "pink"
			Info.SBCP.SP.RelogioCor = "pink"







	elif relogio == "sc":

		if result == 1:
			Info.SBCP.SC.ModuloCor  = "firebrick1"
			Info.SBCP.SC.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.SC.ModuloCor  = "green3"
			Info.SBCP.SC.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.SC.ModuloCor  = "green3"
			Info.SBCP.SC.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.SC.ModuloCor  = "cyan"
			#Info.SBCP.SC.RelogioCor = "cyan"
		else:
			Info.SBCP.SC.ModuloCor  = "pink"
			Info.SBCP.SC.RelogioCor = "pink"







	elif relogio == "rs":

		if result == 1:
			Info.SBCP.RS.ModuloCor  = "firebrick1"
			Info.SBCP.RS.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.RS.ModuloCor  = "green3"
			Info.SBCP.RS.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.RS.ModuloCor  = "green3"
			Info.SBCP.RS.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.RS.ModuloCor  = "cyan"
			#Info.SBCP.RS.RelogioCor = "cyan"
		else:
			Info.SBCP.RS.ModuloCor  = "pink"
			Info.SBCP.RS.RelogioCor = "pink"







	elif relogio == "rj":

		if result == 1:
			Info.SBCP.RJ.ModuloCor  = "firebrick1"
			Info.SBCP.RJ.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.RJ.ModuloCor  = "green3"
			Info.SBCP.RJ.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.RJ.ModuloCor  = "green3"
			Info.SBCP.RJ.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.RJ.ModuloCor  = "cyan"
			#Info.SBCP.RJ.RelogioCor = "cyan"
		else:
			Info.SBCP.RJ.ModuloCor  = "pink"
			Info.SBCP.RJ.RelogioCor = "pink"







	elif relogio == "pr":

		if result == 1:
			Info.SBCP.PR.ModuloCor  = "firebrick1"
			Info.SBCP.PR.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.PR.ModuloCor  = "green3"
			Info.SBCP.PR.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.PR.ModuloCor  = "green3"
			Info.SBCP.PR.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.PR.ModuloCor  = "cyan"
			#Info.SBCP.PR.RelogioCor = "cyan"
		else:
			Info.SBCP.PR.ModuloCor  = "pink"
			Info.SBCP.PR.RelogioCor = "pink"







	elif relogio == "pe":

		if result == 1:
			Info.SBCP.PE.ModuloCor  = "firebrick1"
			Info.SBCP.PE.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.PE.ModuloCor  = "green3"
			Info.SBCP.PE.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.PE.ModuloCor  = "green3"
			Info.SBCP.PE.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.PE.ModuloCor  = "cyan"
			#Info.SBCP.PE.RelogioCor = "cyan"
		else:
			Info.SBCP.PE.ModuloCor  = "pink"
			Info.SBCP.PE.RelogioCor = "pink"







	elif relogio == "mg":

		if result == 1:
			Info.SBCP.MG.ModuloCor  = "firebrick1"
			Info.SBCP.MG.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.MG.ModuloCor  = "green3"
			Info.SBCP.MG.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.MG.ModuloCor  = "green3"
			Info.SBCP.MG.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.MG.ModuloCor  = "cyan"
			#Info.SBCP.MG.RelogioCor = "cyan"
		else:
			Info.SBCP.MG.ModuloCor  = "pink"
			Info.SBCP.MG.RelogioCor = "pink"







	elif relogio == "go":

		if result == 1:
			Info.SBCP.GO.ModuloCor  = "firebrick1"
			Info.SBCP.GO.RelogioCor = "firebrick1"
		elif result == 2:
			Info.SBCP.GO.ModuloCor  = "green3"
			Info.SBCP.GO.RelogioCor = "red4"
		elif result == 3:
			Info.SBCP.GO.ModuloCor  = "green3"
			Info.SBCP.GO.RelogioCor = "green3"
		elif result == 4:
			Info.SBCP.GO.ModuloCor  = "cyan"
			#Info.SBCP.GO.RelogioCor = "cyan"
		else:
			Info.SBCP.GO.ModuloCor  = "pink"
			Info.SBCP.GO.RelogioCor = "pink"

	if result != 4:
		Info.SBCP.Status.Contage = 0
		if Info.SBCP.Nacional.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.ES.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.DF.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.CE.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.BA.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.SP.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.SC.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.RS.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.RJ.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.PR.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.PE.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.MG.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1

		if Info.SBCP.GO.RelogioCor == "green3" : 
				Info.SBCP.Status.Contage = Info.SBCP.Status.Contage +1


def AtualizaPredman(relogio, result):



	if relogio == "bunge":

		if result == 1:
			Info.Predman.Bunge.ModuloCor  = "firebrick1"
			Info.Predman.Bunge.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Bunge.ModuloCor  = "green3"
			Info.Predman.Bunge.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Bunge.ModuloCor  = "green3"
			Info.Predman.Bunge.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Bunge.ModuloCor  = "cyan"
			#Info.Predman.Bunge.RelogioCor = "cyan"
		else:
			Info.Predman.Bunge.ModuloCor  = "pink"
			Info.Predman.Bunge.RelogioCor = "pink"







	elif relogio == "cabot":

		if result == 1:
			Info.Predman.Cabot.ModuloCor  = "firebrick1"
			Info.Predman.Cabot.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Cabot.ModuloCor  = "green3"
			Info.Predman.Cabot.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Cabot.ModuloCor  = "green3"
			Info.Predman.Cabot.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Cabot.ModuloCor  = "cyan"
			#Info.Predman.Cabot.RelogioCor = "cyan"
		else:
			Info.Predman.Cabot.ModuloCor  = "pink"
			Info.Predman.Cabot.RelogioCor = "pink"








	elif relogio == "kelloggs":

		if result == 1:
			Info.Predman.Kelloggs.ModuloCor  = "firebrick1"
			Info.Predman.Kelloggs.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Kelloggs.ModuloCor  = "green3"
			Info.Predman.Kelloggs.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Kelloggs.ModuloCor  = "green3"
			Info.Predman.Kelloggs.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Kelloggs.ModuloCor  = "cyan"
			#Info.Predman.Kelloggs.RelogioCor = "cyan"
		else:
			Info.Predman.Kelloggs.ModuloCor  = "pink"
			Info.Predman.Kelloggs.RelogioCor = "pink"








	elif relogio == "magazine":

		if result == 1:
			Info.Predman.Magazine.ModuloCor  = "firebrick1"
			Info.Predman.Magazine.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Magazine.ModuloCor  = "green3"
			Info.Predman.Magazine.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Magazine.ModuloCor  = "green3"
			Info.Predman.Magazine.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Magazine.ModuloCor  = "cyan"
			#Info.Predman.Magazine.RelogioCor = "cyan"
		else:
			Info.Predman.Magazine.ModuloCor  = "pink"
			Info.Predman.Magazine.RelogioCor = "pink"








	elif relogio == "oxiteno1":

		if result == 1:
			Info.Predman.Oxiteno1.ModuloCor  = "firebrick1"
			Info.Predman.Oxiteno1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Oxiteno1.ModuloCor  = "green3"
			Info.Predman.Oxiteno1.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Oxiteno1.ModuloCor  = "green3"
			Info.Predman.Oxiteno1.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Oxiteno1.ModuloCor  = "cyan"
			#Info.Predman.Oxiteno1.RelogioCor = "cyan"
		else:
			Info.Predman.Oxiteno1.ModuloCor  = "pink"
			Info.Predman.Oxiteno1.RelogioCor = "pink"








	elif relogio == "oxiteno2":

		if result == 1:
			Info.Predman.Oxiteno2.ModuloCor  = "firebrick1"
			Info.Predman.Oxiteno2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Oxiteno2.ModuloCor  = "green3"
			Info.Predman.Oxiteno2.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Oxiteno2.ModuloCor  = "green3"
			Info.Predman.Oxiteno2.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Oxiteno2.ModuloCor  = "cyan"
			#Info.Predman.Oxiteno2.RelogioCor = "cyan"
		else:
			Info.Predman.Oxiteno2.ModuloCor  = "pink"
			Info.Predman.Oxiteno2.RelogioCor = "pink"








	elif relogio == "santoandre":

		if result == 1:
			Info.Predman.SantoAndre.ModuloCor  = "firebrick1"
			Info.Predman.SantoAndre.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.SantoAndre.ModuloCor  = "green3"
			Info.Predman.SantoAndre.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.SantoAndre.ModuloCor  = "green3"
			Info.Predman.SantoAndre.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.SantoAndre.ModuloCor  = "cyan"
			#Info.Predman.SantoAndre.RelogioCor = "cyan"
		else:
			Info.Predman.SantoAndre.ModuloCor  = "pink"
			Info.Predman.SantoAndre.RelogioCor = "pink"








	elif relogio == "pysmianes":

		if result == 1:
			Info.Predman.PrysmianES.ModuloCor  = "firebrick1"
			Info.Predman.PrysmianES.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.PrysmianES.ModuloCor  = "green3"
			Info.Predman.PrysmianES.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.PrysmianES.ModuloCor  = "green3"
			Info.Predman.PrysmianES.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.PrysmianES.ModuloCor  = "cyan"
			#Info.Predman.PrysmianES.RelogioCor = "cyan"
		else:
			Info.Predman.PrysmianES.ModuloCor  = "pink"
			Info.Predman.PrysmianES.RelogioCor = "pink"








	elif relogio == "tradegar":

		if result == 1:
			Info.Predman.Tradegar.ModuloCor  = "firebrick1"
			Info.Predman.Tradegar.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Tradegar.ModuloCor  = "green3"
			Info.Predman.Tradegar.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Tradegar.ModuloCor  = "green3"
			Info.Predman.Tradegar.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Tradegar.ModuloCor  = "cyan"
			#Info.Predman.Tradegar.RelogioCor = "cyan"
		else:
			Info.Predman.Tradegar.ModuloCor  = "pink"
			Info.Predman.Tradegar.RelogioCor = "pink"








	elif relogio == "portao1":

		if result == 1:
			Info.Predman.Portao1.ModuloCor  = "firebrick1"
			Info.Predman.Portao1.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Portao1.ModuloCor  = "green3"
			Info.Predman.Portao1.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Portao1.ModuloCor  = "green3"
			Info.Predman.Portao1.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Portao1.ModuloCor  = "cyan"
			#Info.Predman.Portao1.RelogioCor = "cyan"
		else:
			Info.Predman.Portao1.ModuloCor  = "pink"
			Info.Predman.Portao1.RelogioCor = "pink"








	elif relogio == "portao2":

		if result == 1:
			Info.Predman.Portao2.ModuloCor  = "firebrick1"
			Info.Predman.Portao2.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Portao2.ModuloCor  = "green3"
			Info.Predman.Portao2.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Portao2.ModuloCor  = "green3"
			Info.Predman.Portao2.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Portao2.ModuloCor  = "cyan"
			#Info.Predman.Portao2.RelogioCor = "cyan"
		else:
			Info.Predman.Portao2.ModuloCor  = "pink"
			Info.Predman.Portao2.RelogioCor = "pink"








	elif relogio == "sabic":

		if result == 1:
			Info.Predman.Sabic.ModuloCor  = "firebrick1"
			Info.Predman.Sabic.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Sabic.ModuloCor  = "green3"
			Info.Predman.Sabic.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Sabic.ModuloCor  = "green3"
			Info.Predman.Sabic.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Sabic.ModuloCor  = "cyan"
			#Info.Predman.Sabic.RelogioCor = "cyan"
		else:
			Info.Predman.Sabic.ModuloCor  = "pink"
			Info.Predman.Sabic.RelogioCor = "pink"








	elif relogio == "santhebrag":

		if result == 1:
			Info.Predman.SBraganca.ModuloCor  = "firebrick1"
			Info.Predman.SBraganca.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.SBraganca.ModuloCor  = "green3"
			Info.Predman.SBraganca.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.SBraganca.ModuloCor  = "green3"
			Info.Predman.SBraganca.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.SBraganca.ModuloCor  = "cyan"
			#Info.Predman.SBraganca.RelogioCor = "cyan"
		else:
			Info.Predman.SBraganca.ModuloCor  = "pink"
			Info.Predman.SBraganca.RelogioCor = "pink"








	elif relogio == "santhepenha":

		if result == 1:
			Info.Predman.SPenha.ModuloCor  = "firebrick1"
			Info.Predman.SPenha.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.SPenha.ModuloCor  = "green3"
			Info.Predman.SPenha.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.SPenha.ModuloCor  = "green3"
			Info.Predman.SPenha.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.SPenha.ModuloCor  = "cyan"
			#Info.Predman.SPenha.RelogioCor = "cyan"
		else:
			Info.Predman.SPenha.ModuloCor  = "pink"
			Info.Predman.SPenha.RelogioCor = "pink"








	elif relogio == "vilavelha":

		if result == 1:
			Info.Predman.VilaVelha.ModuloCor  = "firebrick1"
			Info.Predman.VilaVelha.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.VilaVelha.ModuloCor  = "green3"
			Info.Predman.VilaVelha.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.VilaVelha.ModuloCor  = "green3"
			Info.Predman.VilaVelha.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.VilaVelha.ModuloCor  = "cyan"
			#Info.Predman.VilaVelha.RelogioCor = "cyan"
		else:
			Info.Predman.VilaVelha.ModuloCor  = "pink"
			Info.Predman.VilaVelha.RelogioCor = "pink"








	elif relogio == "faurencia":

		if result == 1:
			Info.Predman.Faurencia.ModuloCor  = "firebrick1"
			Info.Predman.Faurencia.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.Faurencia.ModuloCor  = "green3"
			Info.Predman.Faurencia.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.Faurencia.ModuloCor  = "green3"
			Info.Predman.Faurencia.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.Faurencia.ModuloCor  = "cyan"
			#Info.Predman.Faurencia.RelogioCor = "cyan"
		else:
			Info.Predman.Faurencia.ModuloCor  = "pink"
			Info.Predman.Faurencia.RelogioCor = "pink"








	elif relogio == "admrondo":

		if result == 1:
			Info.Predman.AdmRondonopolis.ModuloCor  = "firebrick1"
			Info.Predman.AdmRondonopolis.RelogioCor = "firebrick1"
		elif result == 2:
			Info.Predman.AdmRondonopolis.ModuloCor  = "green3"
			Info.Predman.AdmRondonopolis.RelogioCor = "red4"
		elif result == 3:
			Info.Predman.AdmRondonopolis.ModuloCor  = "green3"
			Info.Predman.AdmRondonopolis.RelogioCor = "green3"
		elif result == 4:
			Info.Predman.AdmRondonopolis.ModuloCor  = "cyan"
			#Info.Predman.AdmRondonopolis.RelogioCor = "cyan"
		else:
			Info.Predman.AdmRondonopolis.ModuloCor  = "pink"
			Info.Predman.AdmRondonopolis.RelogioCor = "pink"


	if result != 4:
		Info.Predman.Status.Contage = 0

		if Info.Predman.Bunge.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Cabot.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Kelloggs.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Magazine.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Oxiteno1.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Oxiteno2.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.SantoAndre.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.PrysmianES.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Tradegar.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Portao1.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Portao2.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Sabic.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.SBraganca.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.SPenha.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.Faurencia.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.AdmRondonopolis.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

		if Info.Predman.VilaVelha.RelogioCor == "green3" : 
			Info.Predman.Status.Contage = Info.Predman.Status.Contage +1

	
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


	elif empresa == "elrio":
		AtualizaElRio(relogio, result)


	elif empresa == "sbcp":
		AtualizaSBCP(relogio, result)


	elif empresa == "predman":
		AtualizaPredman(relogio, result)





	if result != 4:
		Controle.TotalON = 0	

		Controle.TotalON =  Info.Building.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.CasaCristo.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.BestInClass.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.IsoRadio.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.Laser.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.Lotten.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.GrupoNk.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.ElRio.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.SBCP.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.Gravex.Status.Contage
		Controle.TotalON = Controle.TotalON + Info.Predman.Status.Contage



def Contagem():

	Controle.TotalRelogios = 0


	Controle.TotalRelogios = Info.Building.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.CasaCristo.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.BestInClass.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.Laser.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.Lotten.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.GrupoNk.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.IsoRadio.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.ElRio.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.SBCP.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.Gravex.Status.TotalRelogios
	Controle.TotalRelogios = Controle.TotalRelogios + Info.Predman.Status.TotalRelogios