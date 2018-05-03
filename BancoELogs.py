from Var import *


def BancoAtribui(EstRelogio, word):
	#word              		= line.split(",")
	EstRelogio.Empresa      = word[0] 
	EstRelogio.Relogio      = word[1]
	EstRelogio.IP   	    = word[2]
	EstRelogio.Porta        = word[3]
	EstRelogio.NumeroRep    = word[4]
	EstRelogio.Responsavel  = word[5]
	EstRelogio.Telefone     = word[6]


def LeBancoBuilding(relogio_lido,word):


	if relogio_lido == "allianz":
		
		EstRelogio = Info.Building.Allianz
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "wtorre":


		EstRelogio = Info.Building.WTorre
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "riojaneiro":

		EstRelogio = Info.Building.RioJaneiro
		BancoAtribui(EstRelogio, word)


def LeBancoPredman(relogio_lido,word):

	if relogio_lido == "bunge" :

		EstRelogio = Info.Predman.Bunge
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "cabot":


		EstRelogio = Info.Predman.Cabot
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "kellogs":


		EstRelogio = Info.Predman.Kellogs
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "magazine":


		EstRelogio = Info.Predman.Magazine
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "oxiteno1":


		EstRelogio = Info.Predman.Oxiteno1
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "oxiteno2":


		EstRelogio = Info.Predman.Oxiteno2
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "santoandre":


		EstRelogio = Info.Predman.SantoAndre
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "pysmianes":


		EstRelogio = Info.Predman.PrysmianES
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "tradegar":


		EstRelogio = Info.Predman.Tradegar
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "portao1":


		EstRelogio = Info.Predman.Portao1
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "portao2":


		EstRelogio = Info.Predman.Portao2
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "sabic":


		EstRelogio = Info.Predman.Sabic
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "santhebrag":


		EstRelogio = Info.Predman.SBraganca
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "santhepenha":


		EstRelogio = Info.Predman.SPenha
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "faurencia":


		EstRelogio = Info.Predman.Faurencia
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "admrondo":


		EstRelogio = Info.Predman.AdmRondonopolis
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "vilavelha":


		EstRelogio = Info.Predman.VilaVelha
		BancoAtribui(EstRelogio, word)


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

			LeBancoBuilding(relogio_lido,word)
			
		elif empresa_lido == "predman":

			LeBancoPredman(relogio_lido,word)

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

				Info.BestInClass.Recife.Empresa            	= empresa_lido
				Info.BestInClass.Recife.Relogio            	= relogio_lido
				Info.BestInClass.Recife.IP                 	= ip_lido
				Info.BestInClass.Recife.Porta              	= port_lido
				Info.BestInClass.Recife.NumeroRep          	= NumeroReP_Lido
				Info.BestInClass.Recife.Responsavel        	= Responsavel_Lido
				Info.BestInClass.Recife.Telefone           	= Telefone_Lido


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

				Info.BestInClass.Fsantana.Empresa          	= empresa_lido
				Info.BestInClass.Fsantana.Relogio           	    = relogio_lido
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



		elif empresa_lido == "isoradiologia":

			if relogio_lido == "santana":

				Info.IsoRadio.Santana.Empresa            = empresa_lido
				Info.IsoRadio.Santana.Relogio            = relogio_lido
				Info.IsoRadio.Santana.IP                 = ip_lido
				Info.IsoRadio.Santana.Porta              = port_lido
				Info.IsoRadio.Santana.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.Santana.Responsavel        = Responsavel_Lido
				Info.IsoRadio.Santana.Telefone           = Telefone_Lido

			elif relogio_lido == "saomatheus":

				Info.IsoRadio.SaoMatheus.Empresa            = empresa_lido
				Info.IsoRadio.SaoMatheus.Relogio            = relogio_lido
				Info.IsoRadio.SaoMatheus.IP                 = ip_lido
				Info.IsoRadio.SaoMatheus.Porta              = port_lido
				Info.IsoRadio.SaoMatheus.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.SaoMatheus.Responsavel        = Responsavel_Lido
				Info.IsoRadio.SaoMatheus.Telefone           = Telefone_Lido

			elif relogio_lido == "vilamariana":

				Info.IsoRadio.VilaMariana.Empresa            = empresa_lido
				Info.IsoRadio.VilaMariana.Relogio            = relogio_lido
				Info.IsoRadio.VilaMariana.IP                 = ip_lido
				Info.IsoRadio.VilaMariana.Porta              = port_lido
				Info.IsoRadio.VilaMariana.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.VilaMariana.Responsavel        = Responsavel_Lido
				Info.IsoRadio.VilaMariana.Telefone           = Telefone_Lido

			elif relogio_lido == "lapa":

				Info.IsoRadio.Lapa.Empresa            = empresa_lido
				Info.IsoRadio.Lapa.Relogio            = relogio_lido
				Info.IsoRadio.Lapa.IP                 = ip_lido
				Info.IsoRadio.Lapa.Porta              = port_lido
				Info.IsoRadio.Lapa.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.Lapa.Responsavel        = Responsavel_Lido
				Info.IsoRadio.Lapa.Telefone           = Telefone_Lido

			elif relogio_lido == "santoamaro":

				Info.IsoRadio.SAmaro.Empresa            = empresa_lido
				Info.IsoRadio.SAmaro.Relogio            = relogio_lido
				Info.IsoRadio.SAmaro.IP                 = ip_lido
				Info.IsoRadio.SAmaro.Porta              = port_lido
				Info.IsoRadio.SAmaro.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.SAmaro.Responsavel        = Responsavel_Lido
				Info.IsoRadio.SAmaro.Telefone           = Telefone_Lido


			elif relogio_lido == "cidadedutra":

				Info.IsoRadio.CDutra.Empresa            = empresa_lido
				Info.IsoRadio.CDutra.Relogio            = relogio_lido
				Info.IsoRadio.CDutra.IP                 = ip_lido
				Info.IsoRadio.CDutra.Porta              = port_lido
				Info.IsoRadio.CDutra.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.CDutra.Responsavel        = Responsavel_Lido
				Info.IsoRadio.CDutra.Telefone           = Telefone_Lido

			elif relogio_lido == "tatuape":

				Info.IsoRadio.Tatuape.Empresa            = empresa_lido
				Info.IsoRadio.Tatuape.Relogio            = relogio_lido
				Info.IsoRadio.Tatuape.IP                 = ip_lido
				Info.IsoRadio.Tatuape.Porta              = port_lido
				Info.IsoRadio.Tatuape.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.Tatuape.Responsavel        = Responsavel_Lido
				Info.IsoRadio.Tatuape.Telefone           = Telefone_Lido

			elif relogio_lido == "campolimpo":

				Info.IsoRadio.CLimpo.Empresa            = empresa_lido
				Info.IsoRadio.CLimpo.Relogio            = relogio_lido
				Info.IsoRadio.CLimpo.IP                 = ip_lido
				Info.IsoRadio.CLimpo.Porta              = port_lido
				Info.IsoRadio.CLimpo.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.CLimpo.Responsavel        = Responsavel_Lido
				Info.IsoRadio.CLimpo.Telefone           = Telefone_Lido

			elif relogio_lido == "ipiranga":

				Info.IsoRadio.Ipiranga.Empresa            = empresa_lido
				Info.IsoRadio.Ipiranga.Relogio            = relogio_lido
				Info.IsoRadio.Ipiranga.IP                 = ip_lido
				Info.IsoRadio.Ipiranga.Porta              = port_lido
				Info.IsoRadio.Ipiranga.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.Ipiranga.Responsavel        = Responsavel_Lido
				Info.IsoRadio.Ipiranga.Telefone           = Telefone_Lido



			elif relogio_lido == "anarosa":

				Info.IsoRadio.AnaRosa.Empresa            = empresa_lido
				Info.IsoRadio.AnaRosa.Relogio            = relogio_lido
				Info.IsoRadio.AnaRosa.IP                 = ip_lido
				Info.IsoRadio.AnaRosa.Porta              = port_lido
				Info.IsoRadio.AnaRosa.NumeroRep          = NumeroReP_Lido
				Info.IsoRadio.AnaRosa.Responsavel        = Responsavel_Lido
				Info.IsoRadio.AnaRosa.Telefone           = Telefone_Lido



		elif empresa_lido == "gruponk":


			if relogio_lido == "nelson":
				
				Info.GrupoNk.NelsonKioshi.Empresa               = empresa_lido
				Info.GrupoNk.NelsonKioshi.Relogio               = relogio_lido
				Info.GrupoNk.NelsonKioshi.IP                    = ip_lido
				Info.GrupoNk.NelsonKioshi.Porta                 = port_lido
				Info.GrupoNk.NelsonKioshi.NumeroRep             = NumeroReP_Lido
				Info.GrupoNk.NelsonKioshi.Responsavel           = Responsavel_Lido
				Info.GrupoNk.NelsonKioshi.Telefone              = Telefone_Lido


			elif relogio_lido == "furukawa":

				Info.GrupoNk.RDFurukawa.Empresa                	= empresa_lido
				Info.GrupoNk.RDFurukawa.Relogio                	= relogio_lido
				Info.GrupoNk.RDFurukawa.IP                     	= ip_lido
				Info.GrupoNk.RDFurukawa.Porta                  	= port_lido
				Info.GrupoNk.RDFurukawa.NumeroRep              	= NumeroReP_Lido
				Info.GrupoNk.RDFurukawa.Responsavel            	= Responsavel_Lido
				Info.GrupoNk.RDFurukawa.Telefone               	= Telefone_Lido
				


			elif relogio_lido == "kio1":


				Info.GrupoNk.Kio1.Empresa            			= empresa_lido
				Info.GrupoNk.Kio1.Relogio           			= relogio_lido
				Info.GrupoNk.Kio1.IP                		 	= ip_lido
				Info.GrupoNk.Kio1.Porta              			= port_lido
				Info.GrupoNk.Kio1.NumeroRep          			= NumeroReP_Lido
				Info.GrupoNk.Kio1.Responsavel        			= Responsavel_Lido
				Info.GrupoNk.Kio1.Telefone           			= Telefone_Lido


			if relogio_lido == "kio2":
				
				Info.GrupoNk.Kio2.Empresa               = empresa_lido
				Info.GrupoNk.Kio2.Relogio               = relogio_lido
				Info.GrupoNk.Kio2.IP                    = ip_lido
				Info.GrupoNk.Kio2.Porta                 = port_lido
				Info.GrupoNk.Kio2.NumeroRep             = NumeroReP_Lido
				Info.GrupoNk.Kio2.Responsavel           = Responsavel_Lido
				Info.GrupoNk.Kio2.Telefone              = Telefone_Lido


			elif relogio_lido == "granjaviana":

				Info.GrupoNk.GranjaViana.Empresa                = empresa_lido
				Info.GrupoNk.GranjaViana.Relogio                = relogio_lido
				Info.GrupoNk.GranjaViana.IP                     = ip_lido
				Info.GrupoNk.GranjaViana.Porta                  = port_lido
				Info.GrupoNk.GranjaViana.NumeroRep              = NumeroReP_Lido
				Info.GrupoNk.GranjaViana.Responsavel            = Responsavel_Lido
				Info.GrupoNk.GranjaViana.Telefone               = Telefone_Lido
				


			elif relogio_lido == "santacecilia":


				Info.GrupoNk.SantaCecilia.Empresa            = empresa_lido
				Info.GrupoNk.SantaCecilia.Relogio            = relogio_lido
				Info.GrupoNk.SantaCecilia.IP                 = ip_lido
				Info.GrupoNk.SantaCecilia.Porta              = port_lido
				Info.GrupoNk.SantaCecilia.NumeroRep          = NumeroReP_Lido
				Info.GrupoNk.SantaCecilia.Responsavel        = Responsavel_Lido
				Info.GrupoNk.SantaCecilia.Telefone           = Telefone_Lido



			if relogio_lido == "transfruit":
				
				Info.GrupoNk.Transfruit.Empresa               = empresa_lido
				Info.GrupoNk.Transfruit.Relogio               = relogio_lido
				Info.GrupoNk.Transfruit.IP                    = ip_lido
				Info.GrupoNk.Transfruit.Porta                 = port_lido
				Info.GrupoNk.Transfruit.NumeroRep             = NumeroReP_Lido
				Info.GrupoNk.Transfruit.Responsavel           = Responsavel_Lido
				Info.GrupoNk.Transfruit.Telefone              = Telefone_Lido


			elif relogio_lido == "distrdefrutas":

				Info.GrupoNk.Distribuidora.Empresa                = empresa_lido
				Info.GrupoNk.Distribuidora.Relogio                = relogio_lido
				Info.GrupoNk.Distribuidora.IP                     = ip_lido
				Info.GrupoNk.Distribuidora.Porta                  = port_lido
				Info.GrupoNk.Distribuidora.NumeroRep              = NumeroReP_Lido
				Info.GrupoNk.Distribuidora.Responsavel            = Responsavel_Lido
				Info.GrupoNk.Distribuidora.Telefone               = Telefone_Lido
				


			elif relogio_lido == "nkhortifruit":


				Info.GrupoNk.NKFilial.Empresa            = empresa_lido
				Info.GrupoNk.NKFilial.Relogio            = relogio_lido
				Info.GrupoNk.NKFilial.IP                 = ip_lido
				Info.GrupoNk.NKFilial.Porta              = port_lido
				Info.GrupoNk.NKFilial.NumeroRep          = NumeroReP_Lido
				Info.GrupoNk.NKFilial.Responsavel        = Responsavel_Lido
				Info.GrupoNk.NKFilial.Telefone           = Telefone_Lido


		elif empresa_lido == "lotten":


			if relogio_lido == "sfjardins":
				
				Info.Lotten.Jardins.Empresa               = empresa_lido
				Info.Lotten.Jardins.Relogio               = relogio_lido
				Info.Lotten.Jardins.IP                    = ip_lido
				Info.Lotten.Jardins.Porta                 = port_lido
				Info.Lotten.Jardins.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Jardins.Responsavel           = Responsavel_Lido
				Info.Lotten.Jardins.Telefone              = Telefone_Lido

			if relogio_lido == "alphaville":
				
				Info.Lotten.Alphaville.Empresa               = empresa_lido
				Info.Lotten.Alphaville.Relogio               = relogio_lido
				Info.Lotten.Alphaville.IP                    = ip_lido
				Info.Lotten.Alphaville.Porta                 = port_lido
				Info.Lotten.Alphaville.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Alphaville.Responsavel           = Responsavel_Lido
				Info.Lotten.Alphaville.Telefone              = Telefone_Lido

			if relogio_lido == "osasco":
				
				Info.Lotten.Osasco.Empresa               = empresa_lido
				Info.Lotten.Osasco.Relogio               = relogio_lido
				Info.Lotten.Osasco.IP                    = ip_lido
				Info.Lotten.Osasco.Porta                 = port_lido
				Info.Lotten.Osasco.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Osasco.Responsavel           = Responsavel_Lido
				Info.Lotten.Osasco.Telefone              = Telefone_Lido

			if relogio_lido == "santana":
				
				Info.Lotten.Santana.Empresa               = empresa_lido
				Info.Lotten.Santana.Relogio               = relogio_lido
				Info.Lotten.Santana.IP                    = ip_lido
				Info.Lotten.Santana.Porta                 = port_lido
				Info.Lotten.Santana.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Santana.Responsavel           = Responsavel_Lido
				Info.Lotten.Santana.Telefone              = Telefone_Lido

			if relogio_lido == "tatuape":
				
				Info.Lotten.Tatuape.Empresa               = empresa_lido
				Info.Lotten.Tatuape.Relogio               = relogio_lido
				Info.Lotten.Tatuape.IP                    = ip_lido
				Info.Lotten.Tatuape.Porta                 = port_lido
				Info.Lotten.Tatuape.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Tatuape.Responsavel           = Responsavel_Lido
				Info.Lotten.Tatuape.Telefone              = Telefone_Lido

			if relogio_lido == "moema":
				
				Info.Lotten.Moema.Empresa               = empresa_lido
				Info.Lotten.Moema.Relogio               = relogio_lido
				Info.Lotten.Moema.IP                    = ip_lido
				Info.Lotten.Moema.Porta                 = port_lido
				Info.Lotten.Moema.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Moema.Responsavel           = Responsavel_Lido
				Info.Lotten.Moema.Telefone              = Telefone_Lido

			if relogio_lido == "jardimsul":
				
				Info.Lotten.JardimSul.Empresa               = empresa_lido
				Info.Lotten.JardimSul.Relogio               = relogio_lido
				Info.Lotten.JardimSul.IP                    = ip_lido
				Info.Lotten.JardimSul.Porta                 = port_lido
				Info.Lotten.JardimSul.NumeroRep             = NumeroReP_Lido
				Info.Lotten.JardimSul.Responsavel           = Responsavel_Lido
				Info.Lotten.JardimSul.Telefone              = Telefone_Lido

			if relogio_lido == "conceicao":
				
				Info.Lotten.Conceicao.Empresa               = empresa_lido
				Info.Lotten.Conceicao.Relogio               = relogio_lido
				Info.Lotten.Conceicao.IP                    = ip_lido
				Info.Lotten.Conceicao.Porta                 = port_lido
				Info.Lotten.Conceicao.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Conceicao.Responsavel           = Responsavel_Lido
				Info.Lotten.Conceicao.Telefone              = Telefone_Lido

			if relogio_lido == "lapa":
				
				Info.Lotten.Lapa.Empresa               = empresa_lido
				Info.Lotten.Lapa.Relogio               = relogio_lido
				Info.Lotten.Lapa.IP                    = ip_lido
				Info.Lotten.Lapa.Porta                 = port_lido
				Info.Lotten.Lapa.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Lapa.Responsavel           = Responsavel_Lido
				Info.Lotten.Lapa.Telefone              = Telefone_Lido

			if relogio_lido == "perdizes":
				
				Info.Lotten.Perdizes.Empresa               = empresa_lido
				Info.Lotten.Perdizes.Relogio               = relogio_lido
				Info.Lotten.Perdizes.IP                    = ip_lido
				Info.Lotten.Perdizes.Porta                 = port_lido
				Info.Lotten.Perdizes.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Perdizes.Responsavel           = Responsavel_Lido
				Info.Lotten.Perdizes.Telefone              = Telefone_Lido

			if relogio_lido == "saocaetano":
				
				Info.Lotten.SaoCaetano.Empresa               = empresa_lido
				Info.Lotten.SaoCaetano.Relogio               = relogio_lido
				Info.Lotten.SaoCaetano.IP                    = ip_lido
				Info.Lotten.SaoCaetano.Porta                 = port_lido
				Info.Lotten.SaoCaetano.NumeroRep             = NumeroReP_Lido
				Info.Lotten.SaoCaetano.Responsavel           = Responsavel_Lido
				Info.Lotten.SaoCaetano.Telefone              = Telefone_Lido

			if relogio_lido == "pinheiros":
				
				Info.Lotten.Pinheiros.Empresa               = empresa_lido
				Info.Lotten.Pinheiros.Relogio               = relogio_lido
				Info.Lotten.Pinheiros.IP                    = ip_lido
				Info.Lotten.Pinheiros.Porta                 = port_lido
				Info.Lotten.Pinheiros.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Pinheiros.Responsavel           = Responsavel_Lido
				Info.Lotten.Pinheiros.Telefone              = Telefone_Lido

			if relogio_lido == "morumbi":
				
				Info.Lotten.Morumbi.Empresa               = empresa_lido
				Info.Lotten.Morumbi.Relogio               = relogio_lido
				Info.Lotten.Morumbi.IP                    = ip_lido
				Info.Lotten.Morumbi.Porta                 = port_lido
				Info.Lotten.Morumbi.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Morumbi.Responsavel           = Responsavel_Lido
				Info.Lotten.Morumbi.Telefone              = Telefone_Lido

			if relogio_lido == "berrini":
				
				Info.Lotten.Berrini.Empresa               = empresa_lido
				Info.Lotten.Berrini.Relogio               = relogio_lido
				Info.Lotten.Berrini.IP                    = ip_lido
				Info.Lotten.Berrini.Porta                 = port_lido
				Info.Lotten.Berrini.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Berrini.Responsavel           = Responsavel_Lido
				Info.Lotten.Berrini.Telefone              = Telefone_Lido

			if relogio_lido == "vilamariana":
				
				Info.Lotten.VilaMariana.Empresa               = empresa_lido
				Info.Lotten.VilaMariana.Relogio               = relogio_lido
				Info.Lotten.VilaMariana.IP                    = ip_lido
				Info.Lotten.VilaMariana.Porta                 = port_lido
				Info.Lotten.VilaMariana.NumeroRep             = NumeroReP_Lido
				Info.Lotten.VilaMariana.Responsavel           = Responsavel_Lido
				Info.Lotten.VilaMariana.Telefone              = Telefone_Lido

			if relogio_lido == "vilaolimpia":
				
				Info.Lotten.VilaOlimpia.Empresa               = empresa_lido
				Info.Lotten.VilaOlimpia.Relogio               = relogio_lido
				Info.Lotten.VilaOlimpia.IP                    = ip_lido
				Info.Lotten.VilaOlimpia.Porta                 = port_lido
				Info.Lotten.VilaOlimpia.NumeroRep             = NumeroReP_Lido
				Info.Lotten.VilaOlimpia.Responsavel           = Responsavel_Lido
				Info.Lotten.VilaOlimpia.Telefone              = Telefone_Lido
				
			if relogio_lido == "itaim":
				
				Info.Lotten.Itaim.Empresa               = empresa_lido
				Info.Lotten.Itaim.Relogio               = relogio_lido
				Info.Lotten.Itaim.IP                    = ip_lido
				Info.Lotten.Itaim.Porta                 = port_lido
				Info.Lotten.Itaim.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Itaim.Responsavel           = Responsavel_Lido
				Info.Lotten.Itaim.Telefone              = Telefone_Lido

			if relogio_lido == "garulhos":
				
				Info.Lotten.Guarulhos.Empresa               = empresa_lido
				Info.Lotten.Guarulhos.Relogio               = relogio_lido
				Info.Lotten.Guarulhos.IP                    = ip_lido
				Info.Lotten.Guarulhos.Porta                 = port_lido
				Info.Lotten.Guarulhos.NumeroRep             = NumeroReP_Lido
				Info.Lotten.Guarulhos.Responsavel           = Responsavel_Lido
				Info.Lotten.Guarulhos.Telefone              = Telefone_Lido



		elif empresa_lido == "elrio":


			if relogio_lido == "botafogomuniz":
				
				Info.ElRio.BotafogoMuniz.Empresa               = empresa_lido
				Info.ElRio.BotafogoMuniz.Relogio               = relogio_lido
				Info.ElRio.BotafogoMuniz.IP                    = ip_lido
				Info.ElRio.BotafogoMuniz.Porta                 = port_lido
				Info.ElRio.BotafogoMuniz.NumeroRep             = NumeroReP_Lido
				Info.ElRio.BotafogoMuniz.Responsavel           = Responsavel_Lido
				Info.ElRio.BotafogoMuniz.Telefone              = Telefone_Lido




			elif relogio_lido == "botafogopraia":
				
				Info.ElRio.BotafogoPraia.Empresa               = empresa_lido
				Info.ElRio.BotafogoPraia.Relogio               = relogio_lido
				Info.ElRio.BotafogoPraia.IP                    = ip_lido
				Info.ElRio.BotafogoPraia.Porta                 = port_lido
				Info.ElRio.BotafogoPraia.NumeroRep             = NumeroReP_Lido
				Info.ElRio.BotafogoPraia.Responsavel           = Responsavel_Lido
				Info.ElRio.BotafogoPraia.Telefone              = Telefone_Lido




			elif relogio_lido == "boulevard":
				
				Info.ElRio.Boulevard.Empresa               		= empresa_lido
				Info.ElRio.Boulevard.Relogio               		= relogio_lido
				Info.ElRio.Boulevard.IP                    		= ip_lido
				Info.ElRio.Boulevard.Porta                 		= port_lido
				Info.ElRio.Boulevard.NumeroRep             		= NumeroReP_Lido
				Info.ElRio.Boulevard.Responsavel           		= Responsavel_Lido
				Info.ElRio.Boulevard.Telefone              		= Telefone_Lido




			elif relogio_lido == "carioca":
				
				Info.ElRio.Carioca.Empresa               = empresa_lido
				Info.ElRio.Carioca.Relogio               = relogio_lido
				Info.ElRio.Carioca.IP                    = ip_lido
				Info.ElRio.Carioca.Porta                 = port_lido
				Info.ElRio.Carioca.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Carioca.Responsavel           = Responsavel_Lido
				Info.ElRio.Carioca.Telefone              = Telefone_Lido




			elif relogio_lido == "centro1":
				
				Info.ElRio.Centro1.Empresa               = empresa_lido
				Info.ElRio.Centro1.Relogio               = relogio_lido
				Info.ElRio.Centro1.IP                    = ip_lido
				Info.ElRio.Centro1.Porta                 = port_lido
				Info.ElRio.Centro1.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Centro1.Responsavel           = Responsavel_Lido
				Info.ElRio.Centro1.Telefone              = Telefone_Lido




			elif relogio_lido == "centro2":
				
				Info.ElRio.Centro2.Empresa               = empresa_lido
				Info.ElRio.Centro2.Relogio               = relogio_lido
				Info.ElRio.Centro2.IP                    = ip_lido
				Info.ElRio.Centro2.Porta                 = port_lido
				Info.ElRio.Centro2.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Centro2.Responsavel           = Responsavel_Lido
				Info.ElRio.Centro2.Telefone              = Telefone_Lido




			elif relogio_lido == "centro3":
				
				Info.ElRio.Centro3.Empresa               = empresa_lido
				Info.ElRio.Centro3.Relogio               = relogio_lido
				Info.ElRio.Centro3.IP                    = ip_lido
				Info.ElRio.Centro3.Porta                 = port_lido
				Info.ElRio.Centro3.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Centro3.Responsavel           = Responsavel_Lido
				Info.ElRio.Centro3.Telefone              = Telefone_Lido




			elif relogio_lido == "fashion":
				
				Info.ElRio.Fashion.Empresa               = empresa_lido
				Info.ElRio.Fashion.Relogio               = relogio_lido
				Info.ElRio.Fashion.IP                    = ip_lido
				Info.ElRio.Fashion.Porta                 = port_lido
				Info.ElRio.Fashion.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Fashion.Responsavel           = Responsavel_Lido
				Info.ElRio.Fashion.Telefone              = Telefone_Lido




			elif relogio_lido == "flamengo":
				
				Info.ElRio.Flamengo.Empresa               = empresa_lido
				Info.ElRio.Flamengo.Relogio               = relogio_lido
				Info.ElRio.Flamengo.IP                    = ip_lido
				Info.ElRio.Flamengo.Porta                 = port_lido
				Info.ElRio.Flamengo.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Flamengo.Responsavel           = Responsavel_Lido
				Info.ElRio.Flamengo.Telefone              = Telefone_Lido




			elif relogio_lido == "leblon":
				
				Info.ElRio.Leblon.Empresa               = empresa_lido
				Info.ElRio.Leblon.Relogio               = relogio_lido
				Info.ElRio.Leblon.IP                    = ip_lido
				Info.ElRio.Leblon.Porta                 = port_lido
				Info.ElRio.Leblon.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Leblon.Responsavel           = Responsavel_Lido
				Info.ElRio.Leblon.Telefone              = Telefone_Lido




			elif relogio_lido == "novaamerica":
				
				Info.ElRio.NovaAmerica.Empresa               = empresa_lido
				Info.ElRio.NovaAmerica.Relogio               = relogio_lido
				Info.ElRio.NovaAmerica.IP                    = ip_lido
				Info.ElRio.NovaAmerica.Porta                 = port_lido
				Info.ElRio.NovaAmerica.NumeroRep             = NumeroReP_Lido
				Info.ElRio.NovaAmerica.Responsavel           = Responsavel_Lido
				Info.ElRio.NovaAmerica.Telefone              = Telefone_Lido




			elif relogio_lido == "botafogomuniz":
				
				Info.ElRio.BotafogoMuniz.Empresa               = empresa_lido
				Info.ElRio.BotafogoMuniz.Relogio               = relogio_lido
				Info.ElRio.BotafogoMuniz.IP                    = ip_lido
				Info.ElRio.BotafogoMuniz.Porta                 = port_lido
				Info.ElRio.BotafogoMuniz.NumeroRep             = NumeroReP_Lido
				Info.ElRio.BotafogoMuniz.Responsavel           = Responsavel_Lido
				Info.ElRio.BotafogoMuniz.Telefone              = Telefone_Lido




			elif relogio_lido == "shopgrande":
				
				Info.ElRio.ShopGrande.Empresa               = empresa_lido
				Info.ElRio.ShopGrande.Relogio               = relogio_lido
				Info.ElRio.ShopGrande.IP                    = ip_lido
				Info.ElRio.ShopGrande.Porta                 = port_lido
				Info.ElRio.ShopGrande.NumeroRep             = NumeroReP_Lido
				Info.ElRio.ShopGrande.Responsavel           = Responsavel_Lido
				Info.ElRio.ShopGrande.Telefone              = Telefone_Lido




			elif relogio_lido == "shopmacae":
				
				Info.ElRio.ShopMacae.Empresa               = empresa_lido
				Info.ElRio.ShopMacae.Relogio               = relogio_lido
				Info.ElRio.ShopMacae.IP                    = ip_lido
				Info.ElRio.ShopMacae.Porta                 = port_lido
				Info.ElRio.ShopMacae.NumeroRep             = NumeroReP_Lido
				Info.ElRio.ShopMacae.Responsavel           = Responsavel_Lido
				Info.ElRio.ShopMacae.Telefone              = Telefone_Lido




			elif relogio_lido == "shopnorte":
				
				Info.ElRio.ShopNorte.Empresa               = empresa_lido
				Info.ElRio.ShopNorte.Relogio               = relogio_lido
				Info.ElRio.ShopNorte.IP                    = ip_lido
				Info.ElRio.ShopNorte.Porta                 = port_lido
				Info.ElRio.ShopNorte.NumeroRep             = NumeroReP_Lido
				Info.ElRio.ShopNorte.Responsavel           = Responsavel_Lido
				Info.ElRio.ShopNorte.Telefone              = Telefone_Lido




			elif relogio_lido == "backup1":
				
				Info.ElRio.Backup1.Empresa               = empresa_lido
				Info.ElRio.Backup1.Relogio               = relogio_lido
				Info.ElRio.Backup1.IP                    = ip_lido
				Info.ElRio.Backup1.Porta                 = port_lido
				Info.ElRio.Backup1.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Backup1.Responsavel           = Responsavel_Lido
				Info.ElRio.Backup1.Telefone              = Telefone_Lido




			elif relogio_lido == "backup2":
				
				Info.ElRio.Backup2.Empresa               = empresa_lido
				Info.ElRio.Backup2.Relogio               = relogio_lido
				Info.ElRio.Backup2.IP                    = ip_lido
				Info.ElRio.Backup2.Porta                 = port_lido
				Info.ElRio.Backup2.NumeroRep             = NumeroReP_Lido
				Info.ElRio.Backup2.Responsavel           = Responsavel_Lido
				Info.ElRio.Backup2.Telefone              = Telefone_Lido



		elif empresa_lido == "sbcp":



			if relogio_lido == "nacional":
				
				Info.SBCP.Nacional.Empresa               = empresa_lido
				Info.SBCP.Nacional.Relogio               = relogio_lido
				Info.SBCP.Nacional.IP                    = ip_lido
				Info.SBCP.Nacional.Porta                 = port_lido
				Info.SBCP.Nacional.NumeroRep             = NumeroReP_Lido
				Info.SBCP.Nacional.Responsavel           = Responsavel_Lido
				Info.SBCP.Nacional.Telefone              = Telefone_Lido







			elif relogio_lido == "es":
				
				Info.SBCP.ES.Empresa               = empresa_lido
				Info.SBCP.ES.Relogio               = relogio_lido
				Info.SBCP.ES.IP                    = ip_lido
				Info.SBCP.ES.Porta                 = port_lido
				Info.SBCP.ES.NumeroRep             = NumeroReP_Lido
				Info.SBCP.ES.Responsavel           = Responsavel_Lido
				Info.SBCP.ES.Telefone              = Telefone_Lido







			elif relogio_lido == "df":
				
				Info.SBCP.DF.Empresa               = empresa_lido
				Info.SBCP.DF.Relogio               = relogio_lido
				Info.SBCP.DF.IP                    = ip_lido
				Info.SBCP.DF.Porta                 = port_lido
				Info.SBCP.DF.NumeroRep             = NumeroReP_Lido
				Info.SBCP.DF.Responsavel           = Responsavel_Lido
				Info.SBCP.DF.Telefone              = Telefone_Lido







			elif relogio_lido == "ce":
				
				Info.SBCP.CE.Empresa               = empresa_lido
				Info.SBCP.CE.Relogio               = relogio_lido
				Info.SBCP.CE.IP                    = ip_lido
				Info.SBCP.CE.Porta                 = port_lido
				Info.SBCP.CE.NumeroRep             = NumeroReP_Lido
				Info.SBCP.CE.Responsavel           = Responsavel_Lido
				Info.SBCP.CE.Telefone              = Telefone_Lido







			elif relogio_lido == "ba":
				
				Info.SBCP.BA.Empresa               = empresa_lido
				Info.SBCP.BA.Relogio               = relogio_lido
				Info.SBCP.BA.IP                    = ip_lido
				Info.SBCP.BA.Porta                 = port_lido
				Info.SBCP.BA.NumeroRep             = NumeroReP_Lido
				Info.SBCP.BA.Responsavel           = Responsavel_Lido
				Info.SBCP.BA.Telefone              = Telefone_Lido







			elif relogio_lido == "sp":
				
				Info.SBCP.SP.Empresa               = empresa_lido
				Info.SBCP.SP.Relogio               = relogio_lido
				Info.SBCP.SP.IP                    = ip_lido
				Info.SBCP.SP.Porta                 = port_lido
				Info.SBCP.SP.NumeroRep             = NumeroReP_Lido
				Info.SBCP.SP.Responsavel           = Responsavel_Lido
				Info.SBCP.SP.Telefone              = Telefone_Lido







			elif relogio_lido == "sc":
				
				Info.SBCP.SC.Empresa               = empresa_lido
				Info.SBCP.SC.Relogio               = relogio_lido
				Info.SBCP.SC.IP                    = ip_lido
				Info.SBCP.SC.Porta                 = port_lido
				Info.SBCP.SC.NumeroRep             = NumeroReP_Lido
				Info.SBCP.SC.Responsavel           = Responsavel_Lido
				Info.SBCP.SC.Telefone              = Telefone_Lido







			elif relogio_lido == "rs":
				
				Info.SBCP.RS.Empresa               = empresa_lido
				Info.SBCP.RS.Relogio               = relogio_lido
				Info.SBCP.RS.IP                    = ip_lido
				Info.SBCP.RS.Porta                 = port_lido
				Info.SBCP.RS.NumeroRep             = NumeroReP_Lido
				Info.SBCP.RS.Responsavel           = Responsavel_Lido
				Info.SBCP.RS.Telefone              = Telefone_Lido







			elif relogio_lido == "rj":
				
				Info.SBCP.RJ.Empresa               = empresa_lido
				Info.SBCP.RJ.Relogio               = relogio_lido
				Info.SBCP.RJ.IP                    = ip_lido
				Info.SBCP.RJ.Porta                 = port_lido
				Info.SBCP.RJ.NumeroRep             = NumeroReP_Lido
				Info.SBCP.RJ.Responsavel           = Responsavel_Lido
				Info.SBCP.RJ.Telefone              = Telefone_Lido







			elif relogio_lido == "pr":
				
				Info.SBCP.PR.Empresa               = empresa_lido
				Info.SBCP.PR.Relogio               = relogio_lido
				Info.SBCP.PR.IP                    = ip_lido
				Info.SBCP.PR.Porta                 = port_lido
				Info.SBCP.PR.NumeroRep             = NumeroReP_Lido
				Info.SBCP.PR.Responsavel           = Responsavel_Lido
				Info.SBCP.PR.Telefone              = Telefone_Lido







			elif relogio_lido == "pe":
				
				Info.SBCP.PE.Empresa               = empresa_lido
				Info.SBCP.PE.Relogio               = relogio_lido
				Info.SBCP.PE.IP                    = ip_lido
				Info.SBCP.PE.Porta                 = port_lido
				Info.SBCP.PE.NumeroRep             = NumeroReP_Lido
				Info.SBCP.PE.Responsavel           = Responsavel_Lido
				Info.SBCP.PE.Telefone              = Telefone_Lido







			elif relogio_lido == "mg":
				
				Info.SBCP.MG.Empresa               = empresa_lido
				Info.SBCP.MG.Relogio               = relogio_lido
				Info.SBCP.MG.IP                    = ip_lido
				Info.SBCP.MG.Porta                 = port_lido
				Info.SBCP.MG.NumeroRep             = NumeroReP_Lido
				Info.SBCP.MG.Responsavel           = Responsavel_Lido
				Info.SBCP.MG.Telefone              = Telefone_Lido







			elif relogio_lido == "go":
				
				Info.SBCP.GO.Empresa               = empresa_lido
				Info.SBCP.GO.Relogio               = relogio_lido
				Info.SBCP.GO.IP                    = ip_lido
				Info.SBCP.GO.Porta                 = port_lido
				Info.SBCP.GO.NumeroRep             = NumeroReP_Lido
				Info.SBCP.GO.Responsavel           = Responsavel_Lido
				Info.SBCP.GO.Telefone              = Telefone_Lido
