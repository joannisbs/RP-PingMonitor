from Var import *




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
