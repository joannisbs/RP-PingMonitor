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


	elif relogio_lido == "kelloggs":


		EstRelogio = Info.Predman.Kelloggs
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


def LeBancoOlimpark(relogio_lido,word):

	if relogio_lido == "jdpaulista" :

		EstRelogio = Info.Olimpark.JdPaulista
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "santacecilia":


		EstRelogio = Info.Olimpark.SantaCecilia
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "vilaolimpia":


		EstRelogio = Info.Olimpark.VilaOlimpia
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "previdencia":


		EstRelogio = Info.Olimpark.Previdencia
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "belenzinho":


		EstRelogio = Info.Olimpark.Belezinho
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "santana":


		EstRelogio = Info.Olimpark.Santana
		BancoAtribui(EstRelogio, word)


def LeBancoGravex(relogio_lido,word):

	
	if relogio_lido == "adm":
			
		EstRelogio = Info.Gravex.ADM
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "loja":
	
		EstRelogio = Info.Gravex.Loja1
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "mimarcos":
	
		EstRelogio = Info.Gravex.MiMarcos
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "dantchini":
	
		EstRelogio = Info.Gravex.DantChini
		BancoAtribui(EstRelogio, word)


def LeBancoLaser(relogio_lido,word):

	if relogio_lido == "instituto":
		
		EstRelogio = Info.Laser.Instituto
		BancoAtribui(EstRelogio, word)

		
	elif relogio_lido == "academia":
		
		EstRelogio = Info.Laser.Academia
		BancoAtribui(EstRelogio, word)


def LeBancoCasaCristo(relogio_lido,word):

	if relogio_lido == "adm":

		EstRelogio = Info.CasaCristo.ADM
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "cei1":

		EstRelogio = Info.CasaCristo.CEI1
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "cei2":

		EstRelogio = Info.CasaCristo.CEI2
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "cei3":

		EstRelogio = Info.CasaCristo.CEI3
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "vovomatilde":

		EstRelogio = Info.CasaCristo.VovoMatilde
		BancoAtribui(EstRelogio, word)


def LeBancoBestInCLass(relogio_lido,word):

	if relogio_lido == "recife":

		EstRelogio = Info.BestInClass.Recife
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "itaquera":

		EstRelogio = Info.BestInClass.Itaquera
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "itapevi":

		EstRelogio = Info.BestInClass.Itapevi
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "sorocaba":

		EstRelogio = Info.BestInClass.Sorocaba
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "setelagoas":

		EstRelogio = Info.BestInClass.SeteLagoas
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "curitiba":

		EstRelogio = Info.BestInClass.Curitiba
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "fsant":

		EstRelogio = Info.BestInClass.Fsantana
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "itu":

		EstRelogio = Info.BestInClass.Itu
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "guarulhos":

		EstRelogio = Info.BestInClass.Guarulhos
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "itaporanga":

		EstRelogio = Info.BestInClass.Itaporanga
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "linhares":

		EstRelogio = Info.BestInClass.Linhares
		BancoAtribui(EstRelogio, word)


def LeBancoIsoRadiologia(relogio_lido,word):

	if relogio_lido == "santana":
		EstRelogio = Info.IsoRadio.Santana
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "saomatheus":
		EstRelogio = Info.IsoRadio.SaoMatheus
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "vilamariana":
		EstRelogio = Info.IsoRadio.VilaMariana
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "lapa":
		EstRelogio = Info.IsoRadio.Lapa
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "santoamaro":
		EstRelogio = Info.IsoRadio.SAmaro
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "cidadedutra":
		EstRelogio = Info.IsoRadio.CDutra
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "tatuape":
		EstRelogio = Info.IsoRadio.Tatuape
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "campolimpo":
		EstRelogio = Info.IsoRadio.CLimpo
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "ipiranga":
		EstRelogio = Info.IsoRadio.Ipiranga
		BancoAtribui(EstRelogio, word)




	elif relogio_lido == "anarosa":
		EstRelogio = Info.IsoRadio.AnaRosa
		BancoAtribui(EstRelogio, word)


def LeBancoGrupoNk(relogio_lido,word):

	if relogio_lido == "nelson":
		EstRelogio = Info.GrupoNk.NelsonKioshi
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "furukawa":
		EstRelogio = Info.GrupoNk.RDFurukawa
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "kio1":
		EstRelogio = Info.GrupoNk.Kio1
		BancoAtribui(EstRelogio, word)



	if relogio_lido == "kio2":
		EstRelogio = Info.GrupoNk.Kio2
		BancoAtribui(EstRelogio, word)

	

	elif relogio_lido == "granjaviana":
		EstRelogio = Info.GrupoNk.GranjaViana
		BancoAtribui(EstRelogio, word)

		


	elif relogio_lido == "santacecilia":
		EstRelogio = Info.GrupoNk.SantaCecilia
		BancoAtribui(EstRelogio, word)




	if relogio_lido == "transfruit":
		EstRelogio = Info.GrupoNk.Transfruit
		BancoAtribui(EstRelogio, word)



	elif relogio_lido == "distrdefrutas":
		EstRelogio = Info.GrupoNk.Distribuidora
		BancoAtribui(EstRelogio, word)

		


	elif relogio_lido == "nkhortifruit":
		EstRelogio = Info.GrupoNk.NKFilial
		BancoAtribui(EstRelogio, word)


def LeBancoLotten(relogio_lido,word):
	if relogio_lido == "sfjardins":
		EstRelogio = Info.Lotten.Jardins
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "alphaville":
		EstRelogio = Info.Lotten.Alphaville
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "osasco":
		EstRelogio = Info.Lotten.Osasco
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "santana":
		EstRelogio = Info.Lotten.Santana
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "tatuape":
		EstRelogio = Info.Lotten.Tatuape
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "moema":
		EstRelogio = Info.Lotten.Moema
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "jardimsul":
		EstRelogio = Info.Lotten.JardimSul
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "conceicao":
		EstRelogio = Info.Lotten.Conceicao
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "lapa":
		EstRelogio = Info.Lotten.Lapa
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "perdizes":
		EstRelogio = Info.Lotten.Perdizes
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "saocaetano":
		EstRelogio = Info.Lotten.SaoCaetano
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "pinheiros":
		EstRelogio = Info.Lotten.Pinheiros
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "morumbi":
		EstRelogio = Info.Lotten.Morumbi
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "berrini":
		EstRelogio = Info.Lotten.Berrini
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "vilamariana":
		EstRelogio = Info.Lotten.VilaMariana
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "vilaolimpia":
		EstRelogio = Info.Lotten.VilaOlimpia
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "itaim":
		EstRelogio = Info.Lotten.Itaim
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "garulhos":
		EstRelogio = Info.Lotten.Guarulhos
		BancoAtribui(EstRelogio, word)


def LeBancoElRio(relogio_lido,word):

	if relogio_lido == "botafogomuniz":
		EstRelogio = Info.ElRio.BotafogoMuniz
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "botafogopraia":
		EstRelogio = Info.ElRio.BotafogoPraia
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "boulevard":
		EstRelogio = Info.ElRio.Boulevard
		BancoAtribui(EstRelogio, word)
	
	elif relogio_lido == "carioca":
		EstRelogio = Info.ElRio.Carioca
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "centro1":
		EstRelogio = Info.ElRio.Centro1
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "centro2":
		EstRelogio = Info.ElRio.Centro2
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "centro3":
		EstRelogio = Info.ElRio.Centro3
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "fashion":
		EstRelogio = Info.ElRio.Fashion
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "flamengo":
		EstRelogio = Info.ElRio.Flamengo
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "leblon":
		EstRelogio = Info.ElRio.Leblon
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "novaamerica":
		EstRelogio = Info.ElRio.NovaAmerica
		BancoAtribui(EstRelogio, word)
		

	elif relogio_lido == "shopgrande":
		EstRelogio = Info.ElRio.ShopGrande
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "shopmacae":
		EstRelogio = Info.ElRio.ShopMacae
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "shopnorte":
		EstRelogio = Info.ElRio.ShopNorte
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "backup1":
		EstRelogio = Info.ElRio.Backup1
		BancoAtribui(EstRelogio, word)
		
	elif relogio_lido == "backup2":
		EstRelogio = Info.ElRio.Backup2
		BancoAtribui(EstRelogio, word)


def LeBancoSBCP(relogio_lido,word):
	if relogio_lido == "nacional":
		EstRelogio = Info.SBCP.Nacional
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "es":
		EstRelogio = Info.SBCP.ES
		BancoAtribui(EstRelogio, word)
		


	elif relogio_lido == "df":
		EstRelogio = Info.SBCP.DF
		BancoAtribui(EstRelogio, word)
		


	elif relogio_lido == "ce":
		EstRelogio = Info.SBCP.CE
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "ba":
		EstRelogio = Info.SBCP.BA
		BancoAtribui(EstRelogio, word)
		


	elif relogio_lido == "sp":
		EstRelogio = Info.SBCP.SP
		BancoAtribui(EstRelogio, word)
		

	elif relogio_lido == "sc":
		EstRelogio = Info.SBCP.SC
		BancoAtribui(EstRelogio, word)
		

	elif relogio_lido == "rs":
		EstRelogio = Info.SBCP.RS
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "rj":
		EstRelogio = Info.SBCP.RJ
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "pr":
		EstRelogio = Info.SBCP.PR
		BancoAtribui(EstRelogio, word)


	elif relogio_lido == "pe":
		EstRelogio = Info.SBCP.PE
		BancoAtribui(EstRelogio, word)
		

	elif relogio_lido == "mg":
		EstRelogio = Info.SBCP.MG
		BancoAtribui(EstRelogio, word)

	elif relogio_lido == "go":
		EstRelogio = Info.SBCP.GO
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



		if empresa_lido == "building":
			LeBancoBuilding(relogio_lido,word)
			
		elif empresa_lido == "predman":
			LeBancoPredman(relogio_lido,word)

		elif empresa_lido == "olimpark":
			LeBancoOlimpark(relogio_lido,word)

		elif empresa_lido == "gravex":
			LeBancoGravex(relogio_lido,word)

		elif empresa_lido == "laser":
			LeBancoLaser(relogio_lido,word)

		elif empresa_lido == "casacristo":
			LeBancoCasaCristo(relogio_lido,word)

		elif empresa_lido == "bestinclass":
			LeBancoBestInCLass(relogio_lido,word)
			
		elif empresa_lido == "isoradiologia":
			LeBancoIsoRadiologia(relogio_lido,word)
			
		elif empresa_lido == "gruponk":
			LeBancoGrupoNk(relogio_lido,word)

		elif empresa_lido == "lotten":
			LeBancoLotten(relogio_lido,word)

		elif empresa_lido == "elrio":
			LeBancoElRio(relogio_lido,word)

		elif empresa_lido == "sbcp":
			LeBancoSBCP(relogio_lido,word)