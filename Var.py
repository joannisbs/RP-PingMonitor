from datetime import datetime

class GetTime(object):
	
	def __init__(self):
		now = datetime.now()
		self.hora = now.hour
		self.minuto = now.minute
		self.segundo = now.second

	def horaminuto(self):
		
		horaminuto = 	(str(self.hora).zfill(2) +":"+ 
						str(self.minuto).zfill(2) ) 
						
		return horaminuto

		

class Info(object):

	class Building(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 3
			Atencao 		= "green3"

		class Allianz(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class WTorre(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class RioJaneiro(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class CasaCristo(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 5
			Atencao 		= "green3"

		class ADM(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class CEI1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class CEI2(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class CEI3(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class VovoMatilde(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class BestInClass(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 11
			Atencao 		= "green3"

		class Recife(object):
	
			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Itaquera(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Itapevi(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Sorocaba(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class SeteLagoas(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Curitiba(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Fsantana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Itu(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Guarulhos(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Linhares(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Itaporanga(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class Lotten(object):


		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 18
			Atencao 		= "green3"


		class Jardins(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Alphaville(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Osasco(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Santana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Tatuape(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Moema(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class JardimSul(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class SaoCaetano(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Conceicao(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Perdizes(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Lapa(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Pinheiros(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Morumbi(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Berrini(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class VilaMariana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class VilaOlimpia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Itaim(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Guarulhos(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class Laser(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 2
			Atencao 		= "green3"


		class Academia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Instituto(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class Gravex(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 4
			Atencao 		= "green3"


		class ADM(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Loja1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class MiMarcos(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class DantChini(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class Predman(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 17
			Atencao 		= "green3"


		class Bunge(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Cabot(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Kelloggs(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Magazine(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Oxiteno1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Oxiteno2(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class SantoAndre(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class PrysmianES(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Tradegar(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Portao1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Portao2(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Sabic(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class SBraganca(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class SPenha(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Faurencia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class AdmRondonopolis(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class VilaVelha(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class Tarek(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 16
			Atencao 		= "green3"


		class Tahine(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Tarek(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Tafadalu(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Talami(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class MilenioErvas(object):

		class Status(object):
			Horaultima         = "00:00"


			Contage         = 0
			TotalRelogios   = 4
			Atencao 		= "green3"


		class Loja1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Loja2(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class SaoMatheus(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Diadema(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
	
	class Uniman(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 4
			Atencao 		= "green3"

		class SaintGobain(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class PPMSecoia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"
		class Sekurity(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Titan(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class IsoRadio(object):

		class Status(object):
			Horaultima         = "00:00"


			Contage         = 0
			TotalRelogios   = 10
			Atencao 		= "green3"


		class Santana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class SaoMatheus(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class VilaMariana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Lapa(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class SAmaro(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class CDutra(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Tatuape(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class CLimpo(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Ipiranga(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class AnaRosa(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class GrupoNk(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 9
			Atencao 		= "green3"

		class NelsonKioshi(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class RDFurukawa(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class Kio1(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Kio2(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class GranjaViana(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class SantaCecilia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Transfruit(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Distribuidora(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class NKFilial(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
		
	class SBCP(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			Atencao 		= "green3"
			TotalRelogios   = 13

		class Nacional(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class ES(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class DF(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class CE(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class BA(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class SP(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class SC(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class RS(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class RJ(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class PR(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class PE(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class MG(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class GO(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class ElRio(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 16
			Atencao 		= "green3"

		class Centro2(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Leblon(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class BotafogoPraia(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Centro1(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class ShopGrande(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Carioca(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class ShopNorte(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class NovaAmerica(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Boulevard(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Fashion(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class BotafogoMuniz(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Flamengo(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Centro3(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class ShopMacae(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Backup1(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Backup2(object):


			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class Olimpark(object):

		class Status(object):
			Horaultima         = "00:00"

			Contage         = 0
			TotalRelogios   = 6
			Atencao 		= "green3"

		class JdPaulista(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class SantaCecilia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class VilaOlimpia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Previdencia(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Belezinho(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


		class Santana(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class Fancold1(object):

		class Status(object):
			Horaultima         = "00:00"
			Contage         = 0
			TotalRelogios   = 30
			Atencao 		= "green3"


		class Givaudan(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"


		class Yamaha(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class Odebrecht(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class HospJundiai(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class EscritRioNegro(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class MorumbiPrime(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class HospMarioCovas(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class CondVerboDivino(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class HelborBerrini(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class PortoAtlantico(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class AwpFreiGaspar(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class PrestCold(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class UnimedSantos(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class CruzadaBandeirante(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class ColgateAnchieta(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class MDCaieiras(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class CondMandarim(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class RhodiaPoliamida(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class BarraTradePrime(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class NovaSPCMF(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class UnimedPamplona(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class Ushin(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class CondManagerCenter(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class ChoiceSublimeRJ(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class HelborMogiDasCruzes(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class AWPTomeDeSouza(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class EmilioRibas(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class OnThePark(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class MaayanRJ(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

		class CyrellaJK(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"
			HoraOn          = "00:00"
			HoraOff         = "00:00"

	class NaciCorretores(object):

		class Status(object):
			Horaultima         = "00:00"


			Contage         = 0
			TotalRelogios   = 10
			Atencao 		= "green3"


		class ShopMund(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Portal(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class FocoForca(object):

		class Status(object):
			Horaultima         = "00:00"


			Contage         = 0
			TotalRelogios   = 10
			Atencao 		= "green3"


		class IFSP_SC(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class ShopHB(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

	class Helca(object):

		class Status(object):
			Horaultima         = "00:00"


			Contage         = 0
			TotalRelogios   = 10
			Atencao 		= "green3"


		class Barral(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class NewBone(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"

		class Orthomedical(object):

			Empresa         = "None"
			Relogio         = "None"
			ModuloCor		= "yellow"
			RelogioCor		= "yellow"
			IP 				= "None"
			Porta           = "None"
			NumeroRep       = "None"
			Responsavel     = "None"
			Telefone        = "None"


class Controle(object):

	Status 		      		        = "red"
	Stop							= False
	StatusWord                      = "Parado"
	TotalON							= 0
	TotalRelogios					= 0


class Telas(object):

	GUI_Tela1 							= "null"
	GUI_Tela2							= "null"
	GUI_Monitor							= "null"
	root 								= "null"

class Flag(object):

	quit = False