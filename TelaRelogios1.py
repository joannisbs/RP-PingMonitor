

from Tkinter import *


from Thread import *
from Var import *
from Popups import *


class TelaRelogios1(object):


	def __init__(self,root):

		self.Create_container(root)

		self.Create_Building()

		self.Create_CasaCristo()
	
		self.Create_BestInClass()

		self.Create_Predman()

		self.Create_Lotten()

		self.Create_Tarek()

		self.Create_Uniman()

		self.Create_Laser()

		self.Create_MilenioErvas()

		self.Create_Gravex()

		self.Create_IsoRadio()

		self.Create_GrupoNK()

		self.Create_SBCP()




	def Create_IsoRadio(self):

		self.msgIsoRad 									= Label (self.ContainerIsoRadio,text = "Iso Radiologia")
		self.msgIsoRad 									["height"] = 1
		self.msgIsoRad.grid 							(row=0,column=0,sticky = "N")


		self.msgIsoRadCont 								= Label (self.ContainerIsoRadio,text = str(Info.IsoRadio.Status.Contage)+"/"
																							+str(Info.IsoRadio.Status.TotalRelogios))
		self.msgIsoRadCont 								["height"] = 1
		self.msgIsoRadCont.grid 						(row=0,column=1,sticky = "N")



		self.botaoIsoRadioSantana                      		           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSantana              			["text"]       = "Santana"
		self.botaoIsoRadioSantana              			["background"] = Info.IsoRadio.Santana.ModuloCor
		self.botaoIsoRadioSantana              			["width"]      = 13
		self.botaoIsoRadioSantana              			["height"]     = 1
		self.botaoIsoRadioSantana.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Santana",
														Info.IsoRadio.Santana.IP, 
														Info.IsoRadio.Santana.Porta, 
														Info.IsoRadio.Santana.NumeroRep, 
														Info.IsoRadio.Santana.Responsavel, 
														Info.IsoRadio.Santana.Telefone))
		self.botaoIsoRadioSantana.grid         			(row=1, column=0, sticky = "N")

		self.botaoIsoRadioSantanaRelogio                      		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSantanaRelogio       			["text"]       = "R"
		self.botaoIsoRadioSantanaRelogio       			["background"] = Info.IsoRadio.Santana.RelogioCor
		self.botaoIsoRadioSantanaRelogio       			["width"]      = 1
		self.botaoIsoRadioSantanaRelogio       			["height"]     = 1
		self.botaoIsoRadioSantanaRelogio.grid  			(row=1, column=1, sticky = "N")



		self.botaoIsoRadioSaoMatheus                    	           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSaoMatheus              		["text"]       = "Sao Matheus"
		self.botaoIsoRadioSaoMatheus              		["background"] = Info.IsoRadio.SaoMatheus.ModuloCor
		self.botaoIsoRadioSaoMatheus              		["width"]      = 13
		self.botaoIsoRadioSaoMatheus              		["height"]     = 1
		self.botaoIsoRadioSaoMatheus.bind         		("<Button-1>",lambda e: popup("Iso Radiologia","Sao Matheus",
														Info.IsoRadio.SaoMatheus.IP, 
														Info.IsoRadio.SaoMatheus.Porta, 
														Info.IsoRadio.SaoMatheus.NumeroRep, 
														Info.IsoRadio.SaoMatheus.Responsavel, 
														Info.IsoRadio.SaoMatheus.Telefone))
		self.botaoIsoRadioSaoMatheus.grid         		(row=2, column=0, sticky = "N")

		self.botaoIsoRadioSaoMatheusRelogio                    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSaoMatheusRelogio       		["text"]       = "R"
		self.botaoIsoRadioSaoMatheusRelogio       		["background"] = Info.IsoRadio.SaoMatheus.RelogioCor
		self.botaoIsoRadioSaoMatheusRelogio       		["width"]      = 1
		self.botaoIsoRadioSaoMatheusRelogio       		["height"]     = 1
		self.botaoIsoRadioSaoMatheusRelogio.grid  		(row=2, column=1, sticky = "N")


		self.botaoIsoRadioVMariana                    	               = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioVMariana              		["text"]       = "Vila Mariana"
		self.botaoIsoRadioVMariana              		["background"] = Info.IsoRadio.SaoMatheus.ModuloCor
		self.botaoIsoRadioVMariana              		["width"]      = 13
		self.botaoIsoRadioVMariana              		["height"]     = 1
		self.botaoIsoRadioVMariana.bind         		("<Button-1>",lambda e: popup("Iso Radiologia","Vila Mariana",
														Info.IsoRadio.VilaMariana.IP, 
														Info.IsoRadio.VilaMariana.Porta, 
														Info.IsoRadio.VilaMariana.NumeroRep, 
														Info.IsoRadio.VilaMariana.Responsavel, 
														Info.IsoRadio.VilaMariana.Telefone))
		self.botaoIsoRadioVMariana.grid         		(row=3, column=0, sticky = "N")

		self.botaoIsoRadioVMarianaRelogio                    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioVMarianaRelogio       		["text"]       = "R"
		self.botaoIsoRadioVMarianaRelogio       		["background"] = Info.IsoRadio.VilaMariana.RelogioCor
		self.botaoIsoRadioVMarianaRelogio       		["width"]      = 1
		self.botaoIsoRadioVMarianaRelogio       		["height"]     = 1
		self.botaoIsoRadioVMarianaRelogio.grid  		(row=3, column=1, sticky = "N")






		self.botaoIsoRadioLapa                    	                   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioLapa              			["text"]       = "Lapa"
		self.botaoIsoRadioLapa              			["background"] = Info.IsoRadio.Lapa.ModuloCor
		self.botaoIsoRadioLapa              			["width"]      = 13
		self.botaoIsoRadioLapa              			["height"]     = 1
		self.botaoIsoRadioLapa.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Lapa",
														Info.IsoRadio.Lapa.IP, 
														Info.IsoRadio.Lapa.Porta, 
														Info.IsoRadio.Lapa.NumeroRep, 
														Info.IsoRadio.Lapa.Responsavel, 
														Info.IsoRadio.Lapa.Telefone))
		self.botaoIsoRadioLapa.grid         			(row=4, column=0, sticky = "N")

		self.botaoIsoRadioLapaRelogio                    		       = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioLapaRelogio       			["text"]       = "R"
		self.botaoIsoRadioLapaRelogio       			["background"] = Info.IsoRadio.Lapa.RelogioCor
		self.botaoIsoRadioLapaRelogio       			["width"]      = 1
		self.botaoIsoRadioLapaRelogio       			["height"]     = 1
		self.botaoIsoRadioLapaRelogio.grid  			(row=4, column=1, sticky = "N")






		self.botaoIsoRadioSAmaro                    		           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSAmaro              			["text"]       = "Santo Amaro"
		self.botaoIsoRadioSAmaro              			["background"] = Info.IsoRadio.SAmaro.ModuloCor
		self.botaoIsoRadioSAmaro              			["width"]      = 13
		self.botaoIsoRadioSAmaro              			["height"]     = 1
		self.botaoIsoRadioSAmaro.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Santo Amaro",
														Info.IsoRadio.SAmaro.IP, 
														Info.IsoRadio.SAmaro.Porta, 
														Info.IsoRadio.SAmaro.NumeroRep, 
														Info.IsoRadio.SAmaro.Responsavel, 
														Info.IsoRadio.SAmaro.Telefone))
		self.botaoIsoRadioSAmaro.grid         			(row=5, column=0, sticky = "N")

		self.botaoIsoRadioSAmaroRelogio             	       		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioSAmaroRelogio       			["text"]       = "R"
		self.botaoIsoRadioSAmaroRelogio       			["background"] = Info.IsoRadio.SAmaro.RelogioCor
		self.botaoIsoRadioSAmaroRelogio       			["width"]      = 1
		self.botaoIsoRadioSAmaroRelogio       			["height"]     = 1
		self.botaoIsoRadioSAmaroRelogio.grid  			(row=5, column=1, sticky = "N")






		self.botaoIsoRadioCDutra                    		           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioCDutra              			["text"]       = "Cidade Dutra"
		self.botaoIsoRadioCDutra              			["background"] = Info.IsoRadio.CDutra.ModuloCor
		self.botaoIsoRadioCDutra              			["width"]      = 13
		self.botaoIsoRadioCDutra              			["height"]     = 1
		self.botaoIsoRadioCDutra.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Cidade Dutra",
														Info.IsoRadio.CDutra.IP, 
														Info.IsoRadio.CDutra.Porta, 
														Info.IsoRadio.CDutra.NumeroRep, 
														Info.IsoRadio.CDutra.Responsavel, 
														Info.IsoRadio.CDutra.Telefone))
		self.botaoIsoRadioCDutra.grid         			(row=6, column=0, sticky = "N")

		self.botaoIsoRadioCDutraRelogio                	    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioCDutraRelogio       			["text"]       = "R"
		self.botaoIsoRadioCDutraRelogio       			["background"] = Info.IsoRadio.CDutra.RelogioCor
		self.botaoIsoRadioCDutraRelogio       			["width"]      = 1
		self.botaoIsoRadioCDutraRelogio       			["height"]     = 1
		self.botaoIsoRadioCDutraRelogio.grid  			(row=6, column=1, sticky = "N")






		self.botaoIsoRadioTatuape                   	 	           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioTatuape              			["text"]       = "Tatuape"
		self.botaoIsoRadioTatuape              			["background"] = Info.IsoRadio.Tatuape.ModuloCor
		self.botaoIsoRadioTatuape              			["width"]      = 13
		self.botaoIsoRadioTatuape              			["height"]     = 1
		self.botaoIsoRadioTatuape.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Tatuape",
														Info.IsoRadio.Tatuape.IP, 
														Info.IsoRadio.Tatuape.Porta, 
														Info.IsoRadio.Tatuape.NumeroRep, 
														Info.IsoRadio.Tatuape.Responsavel, 
														Info.IsoRadio.Tatuape.Telefone))
		self.botaoIsoRadioTatuape.grid         			(row=7, column=0, sticky = "N")

		self.botaoIsoRadioTatuapeRelogio                    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioTatuapeRelogio       			["text"]       = "R"
		self.botaoIsoRadioTatuapeRelogio       			["background"] = Info.IsoRadio.Tatuape.RelogioCor
		self.botaoIsoRadioTatuapeRelogio       			["width"]      = 1
		self.botaoIsoRadioTatuapeRelogio       			["height"]     = 1
		self.botaoIsoRadioTatuapeRelogio.grid  			(row=7, column=1, sticky = "N")






		self.botaoIsoRadioCLimpo                    		           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioCLimpo              			["text"]       = "Campo Limpo"
		self.botaoIsoRadioCLimpo              			["background"] = Info.IsoRadio.CLimpo.ModuloCor
		self.botaoIsoRadioCLimpo              			["width"]      = 13
		self.botaoIsoRadioCLimpo              			["height"]     = 1
		self.botaoIsoRadioCLimpo.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Campo Limpo",
														Info.IsoRadio.CLimpo.IP, 
														Info.IsoRadio.CLimpo.Porta, 
														Info.IsoRadio.CLimpo.NumeroRep, 
														Info.IsoRadio.CLimpo.Responsavel, 
														Info.IsoRadio.CLimpo.Telefone))
		self.botaoIsoRadioCLimpo.grid         			(row=8, column=0, sticky = "N")

		self.botaoIsoRadioCLimpoRelogio            	        		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioCLimpoRelogio       			["text"]       = "R"
		self.botaoIsoRadioCLimpoRelogio       			["background"] = Info.IsoRadio.CLimpo.RelogioCor
		self.botaoIsoRadioCLimpoRelogio       			["width"]      = 1
		self.botaoIsoRadioCLimpoRelogio       			["height"]     = 1
		self.botaoIsoRadioCLimpoRelogio.grid  			(row=8, column=1, sticky = "N")





		self.botaoIsoRadioIpiranga                   	 	           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioIpiranga              		["text"]       = "Ipiranga"
		self.botaoIsoRadioIpiranga              		["background"] = Info.IsoRadio.Ipiranga.ModuloCor
		self.botaoIsoRadioIpiranga              		["width"]      = 13
		self.botaoIsoRadioIpiranga              		["height"]     = 1
		self.botaoIsoRadioIpiranga.bind         		("<Button-1>",lambda e: popup("Iso Radiologia","Ipiranga",
														Info.IsoRadio.Ipiranga.IP, 
														Info.IsoRadio.Ipiranga.Porta, 
														Info.IsoRadio.Ipiranga.NumeroRep, 
														Info.IsoRadio.Ipiranga.Responsavel, 
														Info.IsoRadio.Ipiranga.Telefone))
		self.botaoIsoRadioIpiranga.grid         		(row=9, column=0, sticky = "N")

		self.botaoIsoRadioIpirangaRelogio                    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioIpirangaRelogio       		["text"]       = "R"
		self.botaoIsoRadioIpirangaRelogio       		["background"] = Info.IsoRadio.Ipiranga.RelogioCor
		self.botaoIsoRadioIpirangaRelogio       		["width"]      = 1
		self.botaoIsoRadioIpirangaRelogio       		["height"]     = 1
		self.botaoIsoRadioIpirangaRelogio.grid  		(row=9, column=1, sticky = "N")





		self.botaoIsoRadioAnaRosa                    		           = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioAnaRosa              			["text"]       = "Ana Rosa"
		self.botaoIsoRadioAnaRosa              			["background"] = Info.IsoRadio.AnaRosa.ModuloCor
		self.botaoIsoRadioAnaRosa              			["width"]      = 13
		self.botaoIsoRadioAnaRosa              			["height"]     = 1
		self.botaoIsoRadioAnaRosa.bind         			("<Button-1>",lambda e: popup("Iso Radiologia","Ana Rosa",
														Info.IsoRadio.AnaRosa.IP, 
														Info.IsoRadio.AnaRosa.Porta, 
														Info.IsoRadio.AnaRosa.NumeroRep, 
														Info.IsoRadio.AnaRosa.Responsavel, 
														Info.IsoRadio.AnaRosa.Telefone))
		self.botaoIsoRadioAnaRosa.grid         			(row=10, column=0, sticky = "N")

		self.botaoIsoRadioAnaRosaRelogio                    		   = Button(self.ContainerIsoRadio)
		self.botaoIsoRadioAnaRosaRelogio       			["text"]       = "R"
		self.botaoIsoRadioAnaRosaRelogio       			["background"] = Info.IsoRadio.AnaRosa.RelogioCor
		self.botaoIsoRadioAnaRosaRelogio       			["width"]      = 1
		self.botaoIsoRadioAnaRosaRelogio       			["height"]     = 1
		self.botaoIsoRadioAnaRosaRelogio.grid  			(row=10, column=1, sticky = "N")



	def Create_MilenioErvas(self):


		self.msgMilenioErvas = Label (self.ContainerMilenioErvas,text = "Milenio Ervas")
		self.msgMilenioErvas["height"] = 1
		self.msgMilenioErvas.grid(row=0,column=0,columnspan=2,sticky = "N")




		self.botaoMilenioErvasSBC1620Loja1                             = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC1620Loja1              ["text"]       = "1620 Loja1"
		self.botaoMilenioErvasSBC1620Loja1              ["background"] = Info.MilenioErvas.Loja1.ModuloCor
		self.botaoMilenioErvasSBC1620Loja1              ["width"]      = 13
		self.botaoMilenioErvasSBC1620Loja1              ["height"]     = 1
		self.botaoMilenioErvasSBC1620Loja1.bind         ("<Button-1>",lambda e: popup("MilenioErvas","1620 Loja1",
														Info.MilenioErvas.Loja1.IP, 
														Info.MilenioErvas.Loja1.Porta, 
														Info.MilenioErvas.Loja1.NumeroRep, 
														Info.MilenioErvas.Loja1.Responsavel, 
														Info.MilenioErvas.Loja1.Telefone))
		self.botaoMilenioErvasSBC1620Loja1.grid         (row=1, column=0, sticky = "N")

		self.botaoMilenioErvasSBC1620Loja1Relogio                      = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["text"]       = "R"
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["background"] = Info.MilenioErvas.Loja1.RelogioCor
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["width"]      = 1
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["height"]     = 1
		self.botaoMilenioErvasSBC1620Loja1Relogio.grid  (row=1, column=1, sticky = "N")




		self.botaoMilenioErvasSBC692Loja2                               = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC692Loja2                ["text"]       = "SBC692 Loja2"
		self.botaoMilenioErvasSBC692Loja2                ["background"] = Info.MilenioErvas.Loja2.ModuloCor
		self.botaoMilenioErvasSBC692Loja2                ["width"]      = 13
		self.botaoMilenioErvasSBC692Loja2                ["height"]     = 1
		self.botaoMilenioErvasSBC692Loja2.bind          ("<Button-1>",lambda e: popup("MilenioErvas","SBC692 Loja2",
														Info.MilenioErvas.Loja2.IP, 
														Info.MilenioErvas.Loja2.Porta, 
														Info.MilenioErvas.Loja2.NumeroRep, 
														Info.MilenioErvas.Loja2.Responsavel, 
														Info.MilenioErvas.Loja2.Telefone))
		self.botaoMilenioErvasSBC692Loja2.grid           (row=2,column=0,sticky = "N")

		self.botaoMilenioErvasSBC692Loja2Relogio                        = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC692Loja2Relogio         ["text"]       = "R"
		self.botaoMilenioErvasSBC692Loja2Relogio         ["background"] = Info.MilenioErvas.Loja2.RelogioCor
		self.botaoMilenioErvasSBC692Loja2Relogio         ["width"]      = 1
		self.botaoMilenioErvasSBC692Loja2Relogio         ["height"]     = 1
		self.botaoMilenioErvasSBC692Loja2Relogio.grid    (row=2,column=1,sticky = "N")




		self.botaoMilenioErvasSaoMatheus                                = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSaoMatheus                ["text"]       = "Sao Matheus"
		self.botaoMilenioErvasSaoMatheus                ["background"] = Info.MilenioErvas.SaoMatheus.ModuloCor
		self.botaoMilenioErvasSaoMatheus                ["width"]      = 13
		self.botaoMilenioErvasSaoMatheus                ["height"]     = 1
		self.botaoMilenioErvasSaoMatheus.bind           ("<Button-1>",lambda e: popup("MilenioErvas","Sao Matheus",
														Info.MilenioErvas.SaoMatheus.IP, 
														Info.MilenioErvas.SaoMatheus.Porta, 
														Info.MilenioErvas.SaoMatheus.NumeroRep, 
														Info.MilenioErvas.SaoMatheus.Responsavel, 
														Info.MilenioErvas.SaoMatheus.Telefone))
		self.botaoMilenioErvasSaoMatheus.grid           (row=3,column=0,sticky = "N")

		self.botaoMilenioErvasSaoMatheusRelogio                        = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSaoMatheusRelogio         ["text"]       = "R"
		self.botaoMilenioErvasSaoMatheusRelogio         ["background"] = Info.MilenioErvas.SaoMatheus.RelogioCor
		self.botaoMilenioErvasSaoMatheusRelogio         ["width"]      = 1
		self.botaoMilenioErvasSaoMatheusRelogio         ["height"]     =  1
		self.botaoMilenioErvasSaoMatheusRelogio.grid    (row=3,column=1,sticky = "N")





		self.botaoMilenioErvasDiadema                                 = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasDiadema                  ["text"]       = "Diadema"
		self.botaoMilenioErvasDiadema                  ["background"] = Info.MilenioErvas.Diadema.ModuloCor
		self.botaoMilenioErvasDiadema                  ["width"]      = 13
		self.botaoMilenioErvasDiadema                  ["height"]     = 1
		self.botaoMilenioErvasDiadema.bind             ("<Button-1>",lambda e: popup("MilenioErvas","Diadema",
														Info.MilenioErvas.Diadema.IP, 
														Info.MilenioErvas.Diadema.Porta, 
														Info.MilenioErvas.Diadema.NumeroRep, 
														Info.MilenioErvas.Diadema.Responsavel, 
														Info.MilenioErvas.Diadema.Telefone))
		self.botaoMilenioErvasDiadema.grid             (row=4,column=0,sticky = "N")

		self.botaoMilenioErvasDiademaRelogio                          = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasDiademaRelogio           ["text"]       = "R"
		self.botaoMilenioErvasDiademaRelogio           ["background"] = Info.MilenioErvas.Diadema.RelogioCor
		self.botaoMilenioErvasDiademaRelogio           ["width"]      = 1
		self.botaoMilenioErvasDiademaRelogio           ["height"]     =  1
		self.botaoMilenioErvasDiademaRelogio.grid      (row=4,column=1,sticky = "N")



	def Create_Gravex(self):


		self.msgGravex                              = Label (self.ContainerGravex,text = "Gravex")
		self.msgGravex                              ["height"]     = 1
		self.msgGravex.grid                         (row=0,column=0,sticky = "N")




		self.botaoGravexADM                         = Button(self.ContainerGravex)
		self.botaoGravexADM                         ["text"]       = "ADM"
		self.botaoGravexADM                         ["background"] = Info.Gravex.ADM.ModuloCor
		self.botaoGravexADM                         ["width"]      = 13
		self.botaoGravexADM                         ["height"]     = 1
		self.botaoGravexADM.bind                    ("<Button-1>",lambda e: popup("Gravex","ADM",
													Info.Gravex.ADM.IP, 
													Info.Gravex.ADM.Porta, 
													Info.Gravex.ADM.NumeroRep, 
													Info.Gravex.ADM.Responsavel, 
													Info.Gravex.ADM.Telefone))

		self.botaoGravexADMRelogio                  = Button(self.ContainerGravex)
		self.botaoGravexADMRelogio                  ["text"]       = "R"
		self.botaoGravexADMRelogio                  ["background"] = Info.Gravex.ADM.RelogioCor
		self.botaoGravexADMRelogio                  ["height"]     = 1
		self.botaoGravexADMRelogio                  ["width"]      = 1


		self.botaoGravexADM.grid                    (row=1,column=0,sticky = "N")
		self.botaoGravexADMRelogio.grid             (row=1,column=1,sticky = "N")




		self.botaoGravexLoja                        = Button(self.ContainerGravex)
		self.botaoGravexLoja                        ["text"]       = "Loja"
		self.botaoGravexLoja                        ["background"] = Info.Gravex.Loja1.ModuloCor
		self.botaoGravexLoja                        ["height"]     = 1
		self.botaoGravexLoja                        ["width"]      = 13
		self.botaoGravexLoja.bind                    ("<Button-1>",lambda e: popup("Gravex","Loja",
													Info.Gravex.Loja1.IP, 
													Info.Gravex.Loja1.Porta, 
													Info.Gravex.Loja1.NumeroRep, 
													Info.Gravex.Loja1.Responsavel, 
													Info.Gravex.Loja1.Telefone))

		self.botaoGravexLojaRelogio                 = Button(self.ContainerGravex)
		self.botaoGravexLojaRelogio                 ["text"]       = "R"
		self.botaoGravexLojaRelogio                 ["background"] = Info.Gravex.Loja1.RelogioCor
		self.botaoGravexLojaRelogio                 ["width"]      = 1
		self.botaoGravexLojaRelogio                 ["height"]     = 1

		self.botaoGravexLoja.grid                   (row=2,column=0,sticky = "N")
		self.botaoGravexLojaRelogio.grid            (row=2,column=1,sticky = "N")






		self.botaoGravexMiMarcos                    = Button(self.ContainerGravex)
		self.botaoGravexMiMarcos                    ["text"]       = "Ministro Marcos"
		self.botaoGravexMiMarcos                    ["background"] = Info.Gravex.MiMarcos.ModuloCor
		self.botaoGravexMiMarcos                    ["height"]     = 1
		self.botaoGravexMiMarcos                    ["width"]      = 13
		self.botaoGravexMiMarcos.bind               ("<Button-1>",lambda e: popup("Gravex","Ministro Marcos",
													Info.Gravex.MiMarcos.IP, 
													Info.Gravex.MiMarcos.Porta, 
													Info.Gravex.MiMarcos.NumeroRep, 
													Info.Gravex.MiMarcos.Responsavel, 
													Info.Gravex.MiMarcos.Telefone))

		self.botaoGravexMiMarcosRelogio             = Button(self.ContainerGravex)
		self.botaoGravexMiMarcosRelogio             ["text"]       = "R"
		self.botaoGravexMiMarcosRelogio             ["background"] = Info.Gravex.MiMarcos.RelogioCor
		self.botaoGravexMiMarcosRelogio             ["height"]     = 1
		self.botaoGravexMiMarcosRelogio             ["width"]      = 1


		self.botaoGravexMiMarcos.grid               (row=3,column=0,sticky = "N")
		self.botaoGravexMiMarcosRelogio.grid        (row=3,column=1,sticky = "N")




		self.botaoGravexDantChini                   = Button(self.ContainerGravex)
		self.botaoGravexDantChini                   ["text"]       = "Danti Chini"
		self.botaoGravexDantChini                   ["background"] = Info.Gravex.DantChini.ModuloCor
		self.botaoGravexDantChini                   ["width"]      = 13
		self.botaoGravexDantChini                   ["height"]     = 1
		self.botaoGravexDantChini.bind              ("<Button-1>",lambda e: popup("Gravex","Danti Chini",
													Info.Gravex.DantChini.IP, 
													Info.Gravex.DantChini.Porta, 
													Info.Gravex.DantChini.NumeroRep, 
													Info.Gravex.DantChini.Responsavel, 
													Info.Gravex.DantChini.Telefone))

		self.botaoGravexDantChiniRelogio            = Button(self.ContainerGravex)
		self.botaoGravexDantChiniRelogio            ["text"]       = "R"
		self.botaoGravexDantChiniRelogio            ["background"] = Info.Gravex.DantChini.RelogioCor
		self.botaoGravexDantChiniRelogio            ["width"]      = 1
		self.botaoGravexDantChiniRelogio            ["height"]     = 1


		self.botaoGravexDantChini.grid              (row=4,column=0,sticky = "N")
		self.botaoGravexDantChiniRelogio.grid       (row=4,column=1,sticky = "N")



	def Create_Laser(self):
		


		self.msgLaser = Label (self.ContainerLaser,text = "Laser")
		self.msgLaser["height"]=1
		self.msgLaser.grid(row=0,column=0,sticky = "N")


		self.msgLaserContage = Label (self.ContainerLaser,text = str(Info.Laser.Status.Contage)+"/"+
																	str(Info.Laser.Status.TotalRelogios))
		self.msgLaserContage["height"]=1
		self.msgLaserContage.grid(row=0,column=1,sticky = "N")



		self.botaoAcademia                                         = Button(self.ContainerLaser)
		self.botaoAcademia                          ["text"]       = "Academia"
		self.botaoAcademia                          ["background"] = Info.Laser.Academia.ModuloCor
		self.botaoAcademia                          ["height"]     = 1
		self.botaoAcademia                          ["width"]      = 13
		self.botaoAcademia.bind                     ("<Button-1>",lambda e: popup("Laser","Academia",
													Info.Laser.Academia.IP, 
													Info.Laser.Academia.Porta, 
													Info.Laser.Academia.NumeroRep, 
													Info.Laser.Academia.Responsavel, 
													Info.Laser.Academia.Telefone))

		self.botaoRAcademia                                        = Button(self.ContainerLaser)
		self.botaoRAcademia                         ["text"]       = "R"
		self.botaoRAcademia                         ["height"]     = 1
		self.botaoRAcademia                         ["background"] = Info.Laser.Academia.RelogioCor
		self.botaoRAcademia                         ["width"]      = 1

		self.botaoAcademia.grid                     (row=1,column=0,sticky = "N")
		self.botaoRAcademia.grid                    (row=1,column=1,sticky = "N")


		self.botaoInstituto                                        = Button(self.ContainerLaser)
		self.botaoInstituto                         ["text"]       = "Instituto"
		self.botaoInstituto                         ["background"] = Info.Laser.Instituto.ModuloCor
		self.botaoInstituto                         ["width"]      = 13
		self.botaoInstituto                         ["height"]     = 1
		self.botaoInstituto.bind                    ("<Button-1>",lambda e: popup("Laser","Instituto",
													Info.Laser.Instituto.IP, 
													Info.Laser.Instituto.Porta, 
													Info.Laser.Instituto.NumeroRep, 
													Info.Laser.Instituto.Responsavel, 
													Info.Laser.Instituto.Telefone))

		self.botaoRInstituto                                       = Button(self.ContainerLaser)
		self.botaoRInstituto                        ["text"]       = "R"
		self.botaoRInstituto                        ["background"] = Info.Laser.Instituto.RelogioCor
		self.botaoRInstituto                        ["width"]      = 1
		self.botaoRInstituto                        ["height"]     = 1


		self.botaoInstituto.grid                    (row=2,column=0,sticky = "N")
		self.botaoRInstituto.grid                   (row=2,column=1,sticky = "N")



	def Create_Predman(self):

		self.msgPredman = Label (self.ContainerPredman,text = "Predman")
		self.msgPredman.grid(row=0,column=0,sticky = "N")




		self.botaoPredmanBunge                                    = Button(self.ContainerPredman)
		self.botaoPredmanBunge                     ["text"]       = "Bunge"
		self.botaoPredmanBunge                     ["background"] = Info.Predman.Bunge.ModuloCor
		self.botaoPredmanBunge                     ["width"]      = 13
		self.botaoPredmanBunge                     ["height"]     = 1
		self.botaoPredmanBunge.bind                ("<Button-1>",lambda e: popup("Predman","Bunge",
													Info.Predman.Bunge.IP, 
													Info.Predman.Bunge.Porta, 
													Info.Predman.Bunge.NumeroRep, 
													Info.Predman.Bunge.Responsavel, 
													Info.Predman.Bunge.Telefone))
		self.botaoPredmanBunge.grid                (row=1,column=0,sticky = "N")

		self.botaoPredmanBungeRelogio                             = Button(self.ContainerPredman)
		self.botaoPredmanBungeRelogio              ["text"]       = "R"
		self.botaoPredmanBungeRelogio              ["background"] = Info.Predman.Bunge.RelogioCor
		self.botaoPredmanBungeRelogio              ["width"]      = 1
		self.botaoPredmanBungeRelogio              ["height"]     = 1
		self.botaoPredmanBungeRelogio.grid         (row=1,column=1,sticky = "N")




		self.botaoPredmanCabot                                    = Button(self.ContainerPredman)
		self.botaoPredmanCabot                     ["text"]       = "Cabot"
		self.botaoPredmanCabot                     ["background"] = Info.Predman.Cabot.ModuloCor
		self.botaoPredmanCabot                     ["width"]      = 13
		self.botaoPredmanCabot                     ["height"]     = 1
		self.botaoPredmanCabot.bind                ("<Button-1>",lambda e: popup("Predman","Cabot",
										 			Info.Predman.Cabot.IP, 
													Info.Predman.Cabot.Porta, 
													Info.Predman.Cabot.NumeroRep, 
													Info.Predman.Cabot.Responsavel, 
													Info.Predman.Cabot.Telefone))
		self.botaoPredmanCabot.grid                (row=2,column=0,sticky = "N")

		self.botaoPredmanCabotRelogio                             = Button(self.ContainerPredman)
		self.botaoPredmanCabotRelogio              ["text"]       = "R"
		self.botaoPredmanCabotRelogio              ["background"] = Info.Predman.Cabot.RelogioCor
		self.botaoPredmanCabotRelogio              ["width"]      = 1
		self.botaoPredmanCabotRelogio              ["height"]     = 1		
		self.botaoPredmanCabotRelogio.grid         (row=2,column=1,sticky = "N")




		self.botaoPredmanKellogs                                 = Button(self.ContainerPredman)
		self.botaoPredmanKellogs                  ["text"]       = "Kellogs"
		self.botaoPredmanKellogs                  ["background"] = Info.Predman.Kellogs.ModuloCor
		self.botaoPredmanKellogs                  ["width"]      = 13
		self.botaoPredmanKellogs                  ["height"]     = 1
		self.botaoPredmanKellogs.bind             ("<Button-1>",lambda e: popup("Predman","Kellogs",
													Info.Predman.Kellogs.IP, 
													Info.Predman.Kellogs.Porta, 
													Info.Predman.Kellogs.NumeroRep, 
													Info.Predman.Kellogs.Responsavel, 
													Info.Predman.Kellogs.Telefone))
		self.botaoPredmanKellogs.grid             (row=3,column=0,sticky = "N")

		self.botaoPredmanKellogsRelogio                          = Button(self.ContainerPredman)
		self.botaoPredmanKellogsRelogio           ["text"]       = "R"
		self.botaoPredmanKellogsRelogio           ["background"] = Info.Predman.Kellogs.RelogioCor
		self.botaoPredmanKellogsRelogio           ["width"]      = 1
		self.botaoPredmanKellogsRelogio           ["height"]     = 1		
		self.botaoPredmanKellogsRelogio.grid      (row=3,column=1,sticky = "N")




		self.botaoPredmanMagazine                                = Button(self.ContainerPredman)
		self.botaoPredmanMagazine                 ["text"]       = "Magazine"
		self.botaoPredmanMagazine                 ["background"] = Info.Predman.Magazine.ModuloCor
		self.botaoPredmanMagazine                 ["width"]      = 13
		self.botaoPredmanMagazine                 ["height"]     = 1
		self.botaoPredmanMagazine.bind            ("<Button-1>",lambda e: popup("Predman","Magazine",
													Info.Predman.Magazine.IP, 
													Info.Predman.Magazine.Porta, 
													Info.Predman.Magazine.NumeroRep, 
													Info.Predman.Magazine.Responsavel, 
													Info.Predman.Magazine.Telefone))
		self.botaoPredmanMagazine.grid            (row=4,column=0,sticky = "N")

		self.botaoPredmanMagazineRelogio                         = Button(self.ContainerPredman)
		self.botaoPredmanMagazineRelogio          ["text"]       = "R"
		self.botaoPredmanMagazineRelogio          ["background"] = Info.Predman.Magazine.RelogioCor
		self.botaoPredmanMagazineRelogio          ["width"]      = 1
		self.botaoPredmanMagazineRelogio          ["height"]     = 1
		self.botaoPredmanMagazineRelogio.grid     (row=4,column=1,sticky = "N")




		self.botaoPredmanOxiteno1                                = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno1                 ["text"]       = "Oxiteno 1"
		self.botaoPredmanOxiteno1                 ["background"] = Info.Predman.Oxiteno1.ModuloCor
		self.botaoPredmanOxiteno1                 ["width"]      = 13
		self.botaoPredmanOxiteno1                 ["height"]     = 1
		self.botaoPredmanOxiteno1.bind            ("<Button-1>",lambda e: popup("Predman","Oxiteno 1",
													Info.Predman.Oxiteno1.IP, 
													Info.Predman.Oxiteno1.Porta, 
													Info.Predman.Oxiteno1.NumeroRep, 
													Info.Predman.Oxiteno1.Responsavel, 
													Info.Predman.Oxiteno1.Telefone))
		self.botaoPredmanOxiteno1.grid            (row=5,column=0,sticky = "N")

		self.botaoPredmanOxiteno1Relogio                         = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno1Relogio          ["text"]       = "R"
		self.botaoPredmanOxiteno1Relogio          ["background"] = Info.Predman.Oxiteno1.RelogioCor
		self.botaoPredmanOxiteno1Relogio          ["width"]      = 1
		self.botaoPredmanOxiteno1Relogio          ["height"]     = 1		
		self.botaoPredmanOxiteno1Relogio.grid     (row=5,column=1,sticky = "N")




		self.botaoPredmanOxiteno2                                = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno2                 ["text"]       = "Oxiteno 2"
		self.botaoPredmanOxiteno2                 ["background"] = Info.Predman.Oxiteno2.ModuloCor
		self.botaoPredmanOxiteno2                 ["width"]      = 13
		self.botaoPredmanOxiteno2                 ["height"]     = 1
		self.botaoPredmanOxiteno2.bind            ("<Button-1>",lambda e: popup("Predman","Oxiteno 2",
													Info.Predman.Oxiteno2.IP, 
													Info.Predman.Oxiteno2.Porta, 
													Info.Predman.Oxiteno2.NumeroRep, 
													Info.Predman.Oxiteno2.Responsavel, 
													Info.Predman.Oxiteno2.Telefone))
		self.botaoPredmanOxiteno2.grid            (row=6,column=0,sticky = "N")

		self.botaoPredmanOxiteno2Relogio                         = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno2Relogio          ["text"]       = "R"
		self.botaoPredmanOxiteno2Relogio          ["background"] = Info.Predman.Oxiteno2.RelogioCor
		self.botaoPredmanOxiteno2Relogio          ["width"]      = 1
		self.botaoPredmanOxiteno2Relogio          ["height"]     = 1
		self.botaoPredmanOxiteno2Relogio.grid     (row=6,column=1,sticky = "N")





		self.botaoPredmanOxiteno3                                = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno3                 ["text"]       = "Oxiteno 3"
		self.botaoPredmanOxiteno3                 ["background"] = Info.Predman.Oxiteno3.ModuloCor
		self.botaoPredmanOxiteno3                 ["width"]      = 13
		self.botaoPredmanOxiteno3                 ["height"]     = 1
		self.botaoPredmanOxiteno3.bind            ("<Button-1>",lambda e: popup("Predman","Oxiteno 3",
													Info.Predman.Oxiteno3.IP, 
													Info.Predman.Oxiteno3.Porta, 
													Info.Predman.Oxiteno3.NumeroRep, 
													Info.Predman.Oxiteno3.Responsavel, 
													Info.Predman.Oxiteno3.Telefone))
		self.botaoPredmanOxiteno3.grid           (row=7,column=0,sticky = "N")

		self.botaoPredmanOxiteno3Relogio                         = Button(self.ContainerPredman)
		self.botaoPredmanOxiteno3Relogio          ["text"]       = "R"
		self.botaoPredmanOxiteno3Relogio          ["background"] = Info.Predman.Oxiteno3.RelogioCor
		self.botaoPredmanOxiteno3Relogio          ["width"]      = 1
		self.botaoPredmanOxiteno3Relogio          ["height"]     = 1
		self.botaoPredmanOxiteno3Relogio.grid      (row=7,column=1,sticky = "N")




		self.botaoPredmanPrysmianES                              = Button(self.ContainerPredman)
		self.botaoPredmanPrysmianES               ["text"]       = "Prysmian ES"
		self.botaoPredmanPrysmianES               ["background"] = Info.Predman.PrysmianES.ModuloCor
		self.botaoPredmanPrysmianES               ["width"]      = 13
		self.botaoPredmanPrysmianES               ["height"]     = 1
		self.botaoPredmanPrysmianES.bind          ("<Button-1>",lambda e: popup("Predman","Prysmian ES",
													Info.Predman.PrysmianES.IP, 
													Info.Predman.PrysmianES.Porta, 
													Info.Predman.PrysmianES.NumeroRep, 
													Info.Predman.PrysmianES.Responsavel, 
													Info.Predman.PrysmianES.Telefone))
		self.botaoPredmanPrysmianES.grid          (row=8,column=0,sticky = "N")

		self.botaoPredmanPrysmianESRelogio                       = Button(self.ContainerPredman)
		self.botaoPredmanPrysmianESRelogio        ["text"]       = "R"
		self.botaoPredmanPrysmianESRelogio        ["background"] = Info.Predman.PrysmianES.RelogioCor
		self.botaoPredmanPrysmianESRelogio        ["width"]      = 1
		self.botaoPredmanPrysmianESRelogio        ["height"]     = 1
		self.botaoPredmanPrysmianESRelogio.grid   (row=8,column=1,sticky = "N")




		self.botaoPredmanTradegar                                = Button(self.ContainerPredman)
		self.botaoPredmanTradegar                 ["text"]       = "Tradegar"
		self.botaoPredmanTradegar                 ["background"] = Info.Predman.Tradegar.ModuloCor
		self.botaoPredmanTradegar                 ["width"]      = 13
		self.botaoPredmanTradegar                 ["height"]     = 1
		self.botaoPredmanTradegar.bind            ("<Button-1>",lambda e: popup("Predman","Tradegar",
													Info.Predman.Tradegar.IP, 
													Info.Predman.Tradegar.Porta, 
													Info.Predman.Tradegar.NumeroRep, 
													Info.Predman.Tradegar.Responsavel, 
													Info.Predman.Tradegar.Telefone))
		self.botaoPredmanTradegar.grid            (row=9,column=0,sticky = "N")

		self.botaoPredmanTradegarRelogio                         = Button(self.ContainerPredman)
		self.botaoPredmanTradegarRelogio          ["text"]       = "R"
		self.botaoPredmanTradegarRelogio          ["background"] = Info.Predman.Tradegar.RelogioCor
		self.botaoPredmanTradegarRelogio          ["width"]      = 1
		self.botaoPredmanTradegarRelogio          ["height"]     = 1
		self.botaoPredmanTradegarRelogio.grid     (row=9,column=1,sticky = "N")




		self.botaoPredmanPortao1                                 = Button(self.ContainerPredman)
		self.botaoPredmanPortao1                  ["text"]       = "Sorocaba PP1"
		self.botaoPredmanPortao1                  ["background"] = Info.Predman.Portao1.ModuloCor
		self.botaoPredmanPortao1                  ["width"]      = 13
		self.botaoPredmanPortao1                  ["height"]     = 1
		self.botaoPredmanPortao1.bind             ("<Button-1>",lambda e: popup("Predman","Sorocaba PP1",
													Info.Predman.Portao1.IP, 
													Info.Predman.Portao1.Porta, 
													Info.Predman.Portao1.NumeroRep, 
													Info.Predman.Portao1.Responsavel, 
													Info.Predman.Portao1.Telefone))
		self.botaoPredmanPortao1.grid             (row=10,column=0,sticky = "N")

		self.botaoPredmanPortao1Relogio                          = Button(self.ContainerPredman)
		self.botaoPredmanPortao1Relogio           ["text"]       = "R"
		self.botaoPredmanPortao1Relogio           ["background"] = Info.Predman.Portao1.RelogioCor
		self.botaoPredmanPortao1Relogio           ["width"]      = 1
		self.botaoPredmanPortao1Relogio           ["height"]     = 1
		self.botaoPredmanPortao1Relogio.grid      (row=10,column=1,sticky = "N")




		self.botaoPredmanPortao2                                 = Button(self.ContainerPredman)
		self.botaoPredmanPortao2                  ["text"]       = "Sorocaba PP2"
		self.botaoPredmanPortao2                  ["background"] = Info.Predman.Portao2.ModuloCor
		self.botaoPredmanPortao2                  ["width"]      = 13
		self.botaoPredmanPortao2                  ["height"]     = 1
		self.botaoPredmanPortao2.bind             ("<Button-1>",lambda e: popup("Predman","Sorocaba PP2",
												   	  Info.Predman.Portao2.IP, 
													  Info.Predman.Portao2.Porta, 
													  Info.Predman.Portao2.NumeroRep, 
													  Info.Predman.Portao2.Responsavel, 
													  Info.Predman.Portao2.Telefone))
		self.botaoPredmanPortao2.grid             (row=11,column=0,sticky = "N")

		self.botaoPredmanPortao2                                 = Button(self.ContainerPredman)
		self.botaoPredmanPortao2                  ["text"]       = "R"
		self.botaoPredmanPortao2                  ["background"] = Info.Predman.Portao2.RelogioCor
		self.botaoPredmanPortao2                  ["width"]      = 1
		self.botaoPredmanPortao2                  ["height"]     = 1
		self.botaoPredmanPortao2.grid             (row=11,column=1,sticky = "N")




		self.botaoPredmanSabic                                   = Button(self.ContainerPredman)
		self.botaoPredmanSabic                    ["text"]       = "Sabic"
		self.botaoPredmanSabic                    ["background"] = Info.Predman.Sabic.ModuloCor
		self.botaoPredmanSabic                    ["width"]      = 13
		self.botaoPredmanSabic                    ["height"]     = 1
		self.botaoPredmanSabic.bind               ("<Button-1>",lambda e: popup("Predman","Sabic",
													Info.Predman.Sabic.IP, 
													Info.Predman.Sabic.Porta, 
													Info.Predman.Sabic.NumeroRep, 
													Info.Predman.Sabic.Responsavel, 
													Info.Predman.Sabic.Telefone))
		self.botaoPredmanSabic.grid                (row=12,column=0,sticky = "N")

		self.botaoPredmanSabicRelogio                            = Button(self.ContainerPredman)
		self.botaoPredmanSabicRelogio             ["text"]       = "R"
		self.botaoPredmanSabicRelogio             ["background"] = Info.Predman.Sabic.RelogioCor
		self.botaoPredmanSabicRelogio             ["width"]      = 1
		self.botaoPredmanSabicRelogio             ["height"]     = 1
		self.botaoPredmanSabicRelogio.grid        (row=12,column=1,sticky = "N")




		self.botaoPredmanSantherBraganca                         = Button(self.ContainerPredman)
		self.botaoPredmanSantherBraganca          ["text"]       = "S. Braganca"
		self.botaoPredmanSantherBraganca          ["background"] = Info.Predman.SBraganca.ModuloCor
		self.botaoPredmanSantherBraganca          ["width"]      = 13
		self.botaoPredmanSantherBraganca          ["height"]     = 1
		self.botaoPredmanSantherBraganca.bind     ("<Button-1>",lambda e: popup("Predman","Santher Braganca",
												     	Info.Predman.SBraganca.IP, 
														Info.Predman.SBraganca.Porta, 
														Info.Predman.SBraganca.NumeroRep, 
														Info.Predman.SBraganca.Responsavel, 
														Info.Predman.SBraganca.Telefone))
		self.botaoPredmanSantherBraganca.grid      (row=13,column=0,sticky = "N")

		self.botaoPredmanSantherBragancaRelogio                  = Button(self.ContainerPredman)
		self.botaoPredmanSantherBragancaRelogio   ["text"]       = "R"
		self.botaoPredmanSantherBragancaRelogio   ["background"] = Info.Predman.SBraganca.RelogioCor
		self.botaoPredmanSantherBragancaRelogio   ["width"]      = 1
		self.botaoPredmanSantherBragancaRelogio   ["height"]     = 1
		self.botaoPredmanSantherBragancaRelogio.grid (row=13,column=1,sticky = "N")





		self.botaoPredmanSantherPenha                             = Button(self.ContainerPredman)
		self.botaoPredmanSantherPenha              ["text"]       = "S. Penha"
		self.botaoPredmanSantherPenha              ["background"] = Info.Predman.SPenha.ModuloCor
		self.botaoPredmanSantherPenha              ["width"]      = 13
		self.botaoPredmanSantherPenha              ["height"]     = 1
		self.botaoPredmanSantherPenha.bind         ("<Button-1>",lambda e: popup("Predman","Santher Penha",
												     	Info.Predman.SPenha.IP, 
														Info.Predman.SPenha.Porta, 
														Info.Predman.SPenha.NumeroRep, 
														Info.Predman.SPenha.Responsavel, 
														Info.Predman.SPenha.Telefone))
		self.botaoPredmanSantherPenha.grid         (row=14,column=0,sticky = "N")

		self.botaoPredmanSantherPenhaRelogio                      = Button(self.ContainerPredman)
		self.botaoPredmanSantherPenhaRelogio       ["text"]       = "R"
		self.botaoPredmanSantherPenhaRelogio       ["background"] = Info.Predman.SPenha.RelogioCor
		self.botaoPredmanSantherPenhaRelogio       ["width"]      = 1
		self.botaoPredmanSantherPenhaRelogio       ["height"]     = 1
		self.botaoPredmanSantherPenhaRelogio.grid  (row=14,column=1,sticky = "N")





		self.botaoPredmanFaurencia                               = Button(self.ContainerPredman)
		self.botaoPredmanFaurencia                ["text"]       = "Faurencia"
		self.botaoPredmanFaurencia                ["background"] = Info.Predman.Faurencia.ModuloCor
		self.botaoPredmanFaurencia                ["width"]      = 13
		self.botaoPredmanFaurencia                ["height"]     = 1
		self.botaoPredmanFaurencia.bind           ("<Button-1>",lambda e: popup("Predman","Faurencia",
												     	Info.Predman.Faurencia.IP, 
														Info.Predman.Faurencia.Porta, 
														Info.Predman.Faurencia.NumeroRep, 
														Info.Predman.Faurencia.Responsavel, 
														Info.Predman.Faurencia.Telefone))
		self.botaoPredmanFaurencia.grid           (row=15,column=0,sticky = "N")

		self.botaoPredmanFaurenciaRelogio                        = Button(self.ContainerPredman)
		self.botaoPredmanFaurenciaRelogio         ["text"]       = "R"
		self.botaoPredmanFaurenciaRelogio         ["background"] = Info.Predman.Faurencia.RelogioCor
		self.botaoPredmanFaurenciaRelogio         ["width"]      = 1
		self.botaoPredmanFaurenciaRelogio         ["height"]     = 1
		self.botaoPredmanFaurenciaRelogio.grid    (row=15,column=1,sticky = "N")





		self.botaoPredmanAdmRondonopolis                         = Button(self.ContainerPredman)
		self.botaoPredmanAdmRondonopolis          ["text"]       = "Adm Rond."
		self.botaoPredmanAdmRondonopolis          ["background"] = Info.Predman.AdmRondonopolis.ModuloCor
		self.botaoPredmanAdmRondonopolis          ["width"]      = 13
		self.botaoPredmanAdmRondonopolis          ["height"]     = 1
		self.botaoPredmanAdmRondonopolis.bind     ("<Button-1>",lambda e: popup("Predman","Adm Rondonopolis",
												     	Info.Predman.AdmRondonopolis.IP, 
														Info.Predman.AdmRondonopolis.Porta, 
														Info.Predman.AdmRondonopolis.NumeroRep, 
														Info.Predman.AdmRondonopolis.Responsavel, 
														Info.Predman.AdmRondonopolis.Telefone))
		self.botaoPredmanAdmRondonopolis.grid     (row=16,column=0,sticky = "N")

		self.botaoPredmanAdmRondonopolisRelogio                  = Button(self.ContainerPredman)
		self.botaoPredmanAdmRondonopolisRelogio   ["text"]       = "R"
		self.botaoPredmanAdmRondonopolisRelogio   ["background"] = Info.Predman.AdmRondonopolis.RelogioCor
		self.botaoPredmanAdmRondonopolisRelogio   ["width"]      = 1
		self.botaoPredmanAdmRondonopolisRelogio   ["height"]     = 1
		self.botaoPredmanAdmRondonopolisRelogio.grid  (row=16,column=1,sticky = "N")





		self.botaoPredmanVilaVelha                               = Button(self.ContainerPredman)
		self.botaoPredmanVilaVelha                ["text"]       = "Vila Velha"
		self.botaoPredmanVilaVelha                ["background"] = Info.Predman.VilaVelha.ModuloCor
		self.botaoPredmanVilaVelha                ["width"]      = 13
		self.botaoPredmanVilaVelha                ["height"]     = 1
		self.botaoPredmanVilaVelha.bind           ("<Button-1>",lambda e: popup("Predman","Vila Velha",
												     	Info.Predman.VilaVelha.IP, 
														Info.Predman.VilaVelha.Porta, 
														Info.Predman.VilaVelha.NumeroRep, 
														Info.Predman.VilaVelha.Responsavel, 
														Info.Predman.VilaVelha.Telefone))
		self.botaoPredmanVilaVelha.grid           (row=17,column=0,sticky = "N")

		self.botaoPredmanVilaVelhaRelogio                        = Button(self.ContainerPredman)
		self.botaoPredmanVilaVelhaRelogio         ["text"]       = "R"
		self.botaoPredmanVilaVelhaRelogio         ["background"] = Info.Predman.VilaVelha.RelogioCor
		self.botaoPredmanVilaVelhaRelogio         ["width"]      = 1
		self.botaoPredmanVilaVelhaRelogio         ["height"]     = 1
		self.botaoPredmanVilaVelhaRelogio.grid    (row=17,column=1,sticky = "N")



	def Create_Uniman(self):



		self.msgUniman = Label (self.ContainerUniman,text = "Uniman")
		self.msgUniman["height"] = 1
		self.msgUniman.grid(row=0,column=0,sticky = "N")




		self.botaoUnimanSaintGobain                                  = Button(self.ContainerUniman)
		self.botaoUnimanSaintGobain                   ["text"]       = "Saint Gobain"
		self.botaoUnimanSaintGobain                   ["background"] = Info.Uniman.SaintGobain.ModuloCor
		self.botaoUnimanSaintGobain                   ["width"]      = 13
		self.botaoUnimanSaintGobain                   ["height"]     = 1
		self.botaoUnimanSaintGobain.bind             ("<Button-1>",lambda e: popup("Uniman","Saint Gobain",
														Info.Uniman.SaintGobain.IP, 
														Info.Uniman.SaintGobain.Porta, 
														Info.Uniman.SaintGobain.NumeroRep, 
														Info.Uniman.SaintGobain.Responsavel, 
														Info.Uniman.SaintGobain.Telefone))
		self.botaoUnimanSaintGobain.grid              (row=1, column=0, sticky = "N")

		self.botaoUnimanSaintGobainRelogio                           = Button(self.ContainerUniman)
		self.botaoUnimanSaintGobainRelogio            ["text"]       = "R"
		self.botaoUnimanSaintGobainRelogio            ["background"] = Info.Uniman.SaintGobain.RelogioCor
		self.botaoUnimanSaintGobainRelogio            ["width"]      = 1
		self.botaoUnimanSaintGobainRelogio            ["height"]     = 1
		self.botaoUnimanSaintGobainRelogio.grid       (row=1, column=1, sticky = "N")




		self.botaoUnimanPPMSecoia                                   = Button(self.ContainerUniman)
		self.botaoUnimanPPMSecoia                    ["text"]       = "PPM Secoia"
		self.botaoUnimanPPMSecoia                    ["background"] = Info.Uniman.PPMSecoia.ModuloCor
		self.botaoUnimanPPMSecoia                    ["width"]      = 13
		self.botaoUnimanPPMSecoia                    ["height"]     = 1
		self.botaoUnimanPPMSecoia.bind              ("<Button-1>",lambda e: popup("Uniman","PPM Secoia",
														Info.Uniman.PPMSecoia.IP, 
														Info.Uniman.PPMSecoia.Porta, 
														Info.Uniman.PPMSecoia.NumeroRep, 
														Info.Uniman.PPMSecoia.Responsavel, 
														Info.Uniman.PPMSecoia.Telefone))
		self.botaoUnimanPPMSecoia.grid               (row=2,column=0,sticky = "N")

		self.botaoUnimanPPMSecoiaRelogio                            = Button(self.ContainerUniman)
		self.botaoUnimanPPMSecoiaRelogio             ["text"]       = "R"
		self.botaoUnimanPPMSecoiaRelogio             ["background"] = Info.Uniman.PPMSecoia.RelogioCor
		self.botaoUnimanPPMSecoiaRelogio             ["width"]      = 1
		self.botaoUnimanPPMSecoiaRelogio             ["height"]     = 1
		self.botaoUnimanPPMSecoiaRelogio.grid        (row=2,column=1,sticky = "N")




		self.botaoUnimanTitan                                       = Button(self.ContainerUniman)
		self.botaoUnimanTitan                        ["text"]       = "Titan"
		self.botaoUnimanTitan                        ["background"] = Info.Uniman.Titan.ModuloCor
		self.botaoUnimanTitan                        ["width"]      = 13
		self.botaoUnimanTitan                        ["height"]     = 1
		self.botaoUnimanPPMSecoia.bind               ("<Button-1>",lambda e: popup("Uniman","Titan",
														Info.Uniman.Titan.IP, 
														Info.Uniman.Titan.Porta, 
														Info.Uniman.Titan.NumeroRep, 
														Info.Uniman.Titan.Responsavel, 
														Info.Uniman.Titan.Telefone))
		self.botaoUnimanTitan.grid                   (row=3,column=0,sticky = "N")

		self.botaoUnimanTitanRelogio                                = Button(self.ContainerUniman)
		self.botaoUnimanTitanRelogio                 ["text"]       = "R"
		self.botaoUnimanTitanRelogio                 ["background"] = Info.Uniman.Titan.RelogioCor
		self.botaoUnimanTitanRelogio                 ["width"]      = 1
		self.botaoUnimanTitanRelogio                 ["height"]     =  1
		self.botaoUnimanTitanRelogio.grid            (row=3,column=1,sticky = "N")





		self.botaoUnimanSekurity                                   = Button(self.ContainerUniman)
		self.botaoUnimanSekurity                    ["text"]       = "Sekurity"
		self.botaoUnimanSekurity                    ["background"] = Info.Uniman.Sekurity.ModuloCor
		self.botaoUnimanSekurity                    ["width"]      = 13
		self.botaoUnimanSekurity                    ["height"]     = 1
		self.botaoUnimanSekurity.bind                ("<Button-1>",lambda e: popup("Uniman","Sekurity",
														Info.Uniman.Sekurity.IP, 
														Info.Uniman.Sekurity.Porta, 
														Info.Uniman.Sekurity.NumeroRep, 
														Info.Uniman.Sekurity.Responsavel, 
														Info.Uniman.Sekurity.Telefone))
		self.botaoUnimanSekurity.grid               (row=4,column=0,sticky = "N")

		self.botaoUnimanSekurityRelogio                            = Button(self.ContainerUniman)
		self.botaoUnimanSekurityRelogio             ["text"]       = "R"
		self.botaoUnimanSekurityRelogio             ["background"] = Info.Uniman.Sekurity.RelogioCor
		self.botaoUnimanSekurityRelogio             ["width"]      = 1
		self.botaoUnimanSekurityRelogio             ["height"]     =  1
		self.botaoUnimanSekurityRelogio.grid        (row=4,column=1,sticky = "N")



	def Create_Tarek(self):

		self.msgTarek = Label (self.ContainerTarek,text = "Grupo Tarek")
		self.msgTarek["height"] = 1
		self.msgTarek.grid(row=0,column=0,sticky = "N")




		self.botaoTahine                                         = Button(self.ContainerTarek)
		self.botaoTahine                          ["text"]       = "Tahine"
		self.botaoTahine                          ["background"] = Info.Tarek.Tahine.ModuloCor
		self.botaoTahine                          ["width"]      = 13
		self.botaoTahine                          ["height"]     = 1
		self.botaoTahine.bind                     ("<Button-1>",lambda e: popup("Tarek","Tahine",
													Info.Tarek.Tahine.IP, 
													Info.Tarek.Tahine.Porta, 
													Info.Tarek.Tahine.NumeroRep, 
													Info.Tarek.Tahine.Responsavel, 
													Info.Tarek.Tahine.Telefone))
		self.botaoTahine.grid                     (row=1,column=0,sticky = "N")

		self.botaoTahineRelogio                                  = Button(self.ContainerTarek)
		self.botaoTahineRelogio                   ["text"]       = "R"
		self.botaoTahineRelogio                   ["background"] = Info.Tarek.Tahine.RelogioCor
		self.botaoTahineRelogio                   ["height"]     = 1
		self.botaoTahineRelogio                   ["width"]      = 1
		self.botaoTahineRelogio.grid              (row=1,column=1,sticky = "N")




		self.botaoTarek                                          = Button(self.ContainerTarek)
		self.botaoTarek                           ["text"]       = "Tarek"
		self.botaoTarek                           ["background"] = Info.Tarek.Tarek.ModuloCor
		self.botaoTarek                           ["height"]     = 1
		self.botaoTarek                           ["width"]      = 13
		self.botaoTarek.bind                      ("<Button-1>",lambda e: popup("Tarek","Tarek",
													Info.Tarek.Tarek.IP, 
													Info.Tarek.Tarek.Porta, 
													Info.Tarek.Tarek.NumeroRep, 
													Info.Tarek.Tarek.Responsavel, 
													Info.Tarek.Tarek.Telefone))
		self.botaoTarek.grid                      (row=2,column=0,sticky = "N")

		self.botaoTarekRelogio                                   = Button(self.ContainerTarek)
		self.botaoTarekRelogio                    ["text"]       = "R"
		self.botaoTarekRelogio                    ["background"] = Info.Tarek.Tarek.RelogioCor
		self.botaoTarekRelogio                    ["width"]      = 1
		self.botaoTarekRelogio                    ["height"]     = 1
		self.botaoTarekRelogio.grid               (row=2,column=1,sticky = "N")




		self.botaoTafadalu                                       = Button(self.ContainerTarek)
		self.botaoTafadalu                        ["text"]       = "Tafadalu"
		self.botaoTafadalu                        ["background"] = Info.Tarek.Tafadalu.ModuloCor
		self.botaoTafadalu                        ["height"]     = 1
		self.botaoTafadalu                        ["width"]      = 13
		self.botaoTafadalu.bind                   ("<Button-1>",lambda e: popup("Tarek","Tafadalu",
													Info.Tarek.Tafadalu.IP, 
													Info.Tarek.Tafadalu.Porta, 
													Info.Tarek.Tafadalu.NumeroRep, 
													Info.Tarek.Tafadalu.Responsavel, 
													Info.Tarek.Tafadalu.Telefone))
		self.botaoTafadalu.grid                   (row=3,column=0,sticky = "N")

		self.botaoTafadaluRelogio                               = Button(self.ContainerTarek)
		self.botaoTafadaluRelogio                ["text"]       = "R"
		self.botaoTafadaluRelogio                ["background"] = Info.Tarek.Tafadalu.RelogioCor
		self.botaoTafadaluRelogio                ["height"]     = 1
		self.botaoTafadaluRelogio                ["width"]      = 1
		self.botaoTafadaluRelogio.grid           (row=3,column=1,sticky = "N")




		self.botaoTalami                                        = Button(self.ContainerTarek)
		self.botaoTalami                         ["text"]       = "Talami"
		self.botaoTalami                         ["background"] = Info.Tarek.Talami.ModuloCor
		self.botaoTalami                         ["width"]      = 13
		self.botaoTalami                         ["height"]     = 1
		self.botaoTalami.bind                    ("<Button-1>",lambda e: popup("Tarek","Talami",
													Info.Tarek.Talami.IP, 
													Info.Tarek.Talami.Porta, 
													Info.Tarek.Talami.NumeroRep, 
													Info.Tarek.Talami.Responsavel, 
													Info.Tarek.Talami.Telefone))
		self.botaoTalami.grid                    (row=4,column=0,sticky = "N")

		self.botaoTalamiRelogio                                 = Button(self.ContainerTarek)
		self.botaoTalamiRelogio                  ["text"]       = "R"
		self.botaoTalamiRelogio                  ["background"] = Info.Tarek.Talami.RelogioCor
		self.botaoTalamiRelogio                  ["width"]      = 1
		self.botaoTalamiRelogio                  ["height"]     = 1
		self.botaoTalamiRelogio.grid             (row=4,column=1,sticky = "N")



	def Create_Lotten(self):

		self.msgLotten = Label (self.ContainerLotten,text = "Lotten")
		self.msgLotten.grid(row=0,column=0,sticky = "N")

		self.msgLottenContage = Label (self.ContainerLotten,text=str(Info.Lotten.Status.Contage)+"/"+
														  str(Info.Lotten.Status.TotalRelogios))

		self.msgLottenContage.grid(row=0,column=1,sticky = "N")



		


		self.botaoLottenJardins                                  = Button(self.ContainerLotten)
		self.botaoLottenJardins                   ["text"]       = "Jardins"
		self.botaoLottenJardins                   ["background"] = Info.Lotten.Jardins.ModuloCor
		self.botaoLottenJardins                   ["width"]      = 13
		self.botaoLottenJardins                   ["height"]     = 1
		self.botaoLottenJardins.bind              ("<Button-1>",lambda e: popup("Lotten","Jardins",
													Info.Lotten.Jardins.IP, 
													Info.Lotten.Jardins.Porta, 
													Info.Lotten.Jardins.NumeroRep, 
													Info.Lotten.Jardins.Responsavel, 
													Info.Lotten.Jardins.Telefone))
		self.botaoLottenJardins.grid              (row=1,column=0,sticky = "N")

		self.botaoLottenJardinsRelogio                           = Button(self.ContainerLotten)
		self.botaoLottenJardinsRelogio            ["text"]       = "R"
		self.botaoLottenJardinsRelogio            ["background"] = Info.Lotten.Jardins.RelogioCor
		self.botaoLottenJardinsRelogio            ["width"]      = 1
		self.botaoLottenJardinsRelogio            ["height"]     = 1
		self.botaoLottenJardinsRelogio.grid       (row=1,column=1,sticky = "N")




		self.botaoLottenAlphaville                               = Button(self.ContainerLotten)
		self.botaoLottenAlphaville                ["text"]       = "Alphaville"
		self.botaoLottenAlphaville                ["background"] = Info.Lotten.Alphaville.ModuloCor
		self.botaoLottenAlphaville                ["width"]      = 13
		self.botaoLottenAlphaville                ["height"]     = 1
		self.botaoLottenAlphaville.bind           ("<Button-1>",lambda e: popup("Lotten","Alphaville",
													Info.Lotten.Alphaville.IP, 
													Info.Lotten.Alphaville.Porta, 
													Info.Lotten.Alphaville.NumeroRep, 
													Info.Lotten.Alphaville.Responsavel, 
													Info.Lotten.Alphaville.Telefone))
		self.botaoLottenAlphaville.grid           (row=2,column=0,sticky = "N")

		self.botaoLottenAlphavilleRelogio                        = Button(self.ContainerLotten)
		self.botaoLottenAlphavilleRelogio         ["text"]       = "R"
		self.botaoLottenAlphavilleRelogio         ["background"] = Info.Lotten.Alphaville.RelogioCor
		self.botaoLottenAlphavilleRelogio         ["width"]      = 1
		self.botaoLottenAlphavilleRelogio         ["height"]     = 1		
		self.botaoLottenAlphavilleRelogio.grid    (row=2,column=1,sticky = "N")




		self.botaoLottenOsasco                                  = Button(self.ContainerLotten)
		self.botaoLottenOsasco                   ["text"]       = "Osasco"
		self.botaoLottenOsasco                   ["background"] = Info.Lotten.Osasco.ModuloCor
		self.botaoLottenOsasco                   ["width"]      = 13
		self.botaoLottenOsasco                   ["height"]     = 1
		self.botaoLottenOsasco.bind              ("<Button-1>",lambda e: popup("Lotten","Osasco",
													Info.Lotten.Osasco.IP, 
													Info.Lotten.Osasco.Porta, 
													Info.Lotten.Osasco.NumeroRep, 
													Info.Lotten.Osasco.Responsavel, 
													Info.Lotten.Osasco.Telefone))
		self.botaoLottenOsasco.grid              (row=3,column=0,sticky = "N")

		self.botaoLottenOsascoRelogio                           = Button(self.ContainerLotten)
		self.botaoLottenOsascoRelogio            ["text"]       = "R"
		self.botaoLottenOsascoRelogio            ["background"] = Info.Lotten.Osasco.RelogioCor
		self.botaoLottenOsascoRelogio            ["width"]      = 1
		self.botaoLottenOsascoRelogio            ["height"]     = 1		
		self.botaoLottenOsascoRelogio.grid       (row=3,column=1,sticky = "N")




		self.botaoLottenSantana                                 = Button(self.ContainerLotten)
		self.botaoLottenSantana                  ["text"]       = "Santana"
		self.botaoLottenSantana                  ["background"] = Info.Lotten.Santana.ModuloCor
		self.botaoLottenSantana                  ["width"]      = 13
		self.botaoLottenSantana                  ["height"]     = 1
		self.botaoLottenSantana.bind             ("<Button-1>",lambda e: popup("Lotten","Santana",
													Info.Lotten.Santana.IP, 
													Info.Lotten.Santana.Porta, 
													Info.Lotten.Santana.NumeroRep, 
													Info.Lotten.Santana.Responsavel, 
													Info.Lotten.Santana.Telefone))
		self.botaoLottenSantana.grid             (row=4,column=0,sticky = "N")

		self.botaoLottenSantanaRelogio                          = Button(self.ContainerLotten)
		self.botaoLottenSantanaRelogio           ["text"]       = "R"
		self.botaoLottenSantanaRelogio           ["background"] = Info.Lotten.Santana.RelogioCor
		self.botaoLottenSantanaRelogio           ["width"]      = 1
		self.botaoLottenSantanaRelogio           ["height"]     = 1
		self.botaoLottenSantanaRelogio.grid      (row=4,column=1,sticky = "N")




		self.botaoLottenTatuape                                = Button(self.ContainerLotten)
		self.botaoLottenTatuape                 ["text"]       = "Tatuape"
		self.botaoLottenTatuape                 ["background"] = Info.Lotten.Tatuape.ModuloCor
		self.botaoLottenTatuape                 ["width"]      = 13
		self.botaoLottenTatuape                 ["height"]     = 1
		self.botaoLottenTatuape.bind             ("<Button-1>",lambda e: popup("Lotten","Tatuape",
													Info.Lotten.Tatuape.IP, 
													Info.Lotten.Tatuape.Porta, 
													Info.Lotten.Tatuape.NumeroRep, 
													Info.Lotten.Tatuape.Responsavel, 
													Info.Lotten.Tatuape.Telefone))
		self.botaoLottenTatuape.grid            (row=5,column=0,sticky = "N")

		self.botaoLottenTatuapeRelogio                         = Button(self.ContainerLotten)
		self.botaoLottenTatuapeRelogio          ["text"]       = "R"
		self.botaoLottenTatuapeRelogio          ["background"] = Info.Lotten.Tatuape.RelogioCor
		self.botaoLottenTatuapeRelogio          ["width"]      = 1
		self.botaoLottenTatuapeRelogio          ["height"]     = 1		
		self.botaoLottenTatuapeRelogio.grid     (row=5,column=1,sticky = "N")




		self.botaoLottenMoema                                  = Button(self.ContainerLotten)
		self.botaoLottenMoema                   ["text"]       = "Moema"
		self.botaoLottenMoema                   ["background"] = Info.Lotten.Moema.ModuloCor
		self.botaoLottenMoema                   ["width"]      = 13
		self.botaoLottenMoema                   ["height"]     = 1
		self.botaoLottenMoema.bind              ("<Button-1>",lambda e: popup("Lotten","Moema",
													Info.Lotten.Moema.IP, 
													Info.Lotten.Moema.Porta, 
													Info.Lotten.Moema.NumeroRep, 
													Info.Lotten.Moema.Responsavel, 
													Info.Lotten.Moema.Telefone))
		self.botaoLottenMoema.grid              (row=6,column=0,sticky = "N")

		self.botaoLottenMoemaRelogio                           = Button(self.ContainerLotten)
		self.botaoLottenMoemaRelogio            ["text"]       = "R"
		self.botaoLottenMoemaRelogio            ["background"] = Info.Lotten.Moema.RelogioCor
		self.botaoLottenMoemaRelogio            ["width"]      = 1
		self.botaoLottenMoemaRelogio            ["height"]     = 1
		self.botaoLottenMoemaRelogio.grid       (row=6,column=1,sticky = "N")





		self.botaoLottenJardimSul                              = Button(self.ContainerLotten)
		self.botaoLottenJardimSul               ["text"]       = "Jardim Sul"
		self.botaoLottenJardimSul               ["background"] = Info.Lotten.JardimSul.ModuloCor
		self.botaoLottenJardimSul               ["width"]      = 13
		self.botaoLottenJardimSul               ["height"]     = 1
		self.botaoLottenMoema.bind              ("<Button-1>",lambda e: popup("Lotten","Jardim Sul",
													Info.Lotten.JardimSul.IP, 
													Info.Lotten.JardimSul.Porta, 
													Info.Lotten.JardimSul.NumeroRep, 
													Info.Lotten.JardimSul.Responsavel, 
													Info.Lotten.JardimSul.Telefone))
		self.botaoLottenJardimSul.grid          (row=7,column=0,sticky = "N")

		self.botaoLottenJardimSulRelogio                       = Button(self.ContainerLotten)
		self.botaoLottenJardimSulRelogio        ["text"]       = "R"
		self.botaoLottenJardimSulRelogio        ["background"] = Info.Lotten.JardimSul.RelogioCor
		self.botaoLottenJardimSulRelogio        ["width"]      = 1
		self.botaoLottenJardimSulRelogio        ["height"]     = 1
		self.botaoLottenJardimSulRelogio.grid   (row=7,column=1,sticky = "N")




		self.botaoLottenConceicao                              = Button(self.ContainerLotten)
		self.botaoLottenConceicao               ["text"]       = "Conceicao"
		self.botaoLottenConceicao               ["background"] = Info.Lotten.Conceicao.ModuloCor
		self.botaoLottenConceicao               ["width"]      = 13
		self.botaoLottenConceicao               ["height"]     = 1
		self.botaoLottenConceicao.bind          ("<Button-1>",lambda e: popup("Lotten","Conceicao",
													Info.Lotten.Conceicao.IP, 
													Info.Lotten.Conceicao.Porta, 
													Info.Lotten.Conceicao.NumeroRep, 
													Info.Lotten.Conceicao.Responsavel, 
													Info.Lotten.Conceicao.Telefone))
		self.botaoLottenConceicao.grid          (row=8,column=0,sticky = "N")

		self.botaoLottenConceicaoRelogio                       = Button(self.ContainerLotten)
		self.botaoLottenConceicaoRelogio        ["text"]       = "R"
		self.botaoLottenConceicaoRelogio        ["background"] = Info.Lotten.Conceicao.RelogioCor
		self.botaoLottenConceicaoRelogio        ["width"]      = 1
		self.botaoLottenConceicaoRelogio        ["height"]     = 1
		self.botaoLottenConceicaoRelogio.grid   (row=8,column=1,sticky = "N")




		self.botaoLottenPerdizes                               = Button(self.ContainerLotten)
		self.botaoLottenPerdizes                ["text"]       = "Perdizes"
		self.botaoLottenPerdizes                ["background"] = Info.Lotten.Perdizes.ModuloCor
		self.botaoLottenPerdizes                ["width"]      = 13
		self.botaoLottenPerdizes                ["height"]     = 1
		self.botaoLottenPerdizes.bind           ("<Button-1>",lambda e: popup("Lotten","Perdizes",
													Info.Lotten.Perdizes.IP, 
													Info.Lotten.Perdizes.Porta, 
													Info.Lotten.Perdizes.NumeroRep, 
													Info.Lotten.Perdizes.Responsavel, 
													Info.Lotten.Perdizes.Telefone))
		self.botaoLottenPerdizes.grid           (row=9,column=0,sticky = "N")

		self.botaoLottenPerdizesRelogio                        = Button(self.ContainerLotten)
		self.botaoLottenPerdizesRelogio         ["text"]       = "R"
		self.botaoLottenPerdizesRelogio         ["background"] = Info.Lotten.Perdizes.RelogioCor
		self.botaoLottenPerdizesRelogio         ["width"]      = 1
		self.botaoLottenPerdizesRelogio         ["height"]     = 1
		self.botaoLottenPerdizesRelogio.grid    (row=9,column=1,sticky = "N")




		self.botaoLottenLapa                                   = Button(self.ContainerLotten)
		self.botaoLottenLapa                    ["text"]       = "Lapa"
		self.botaoLottenLapa                    ["background"] = Info.Lotten.Lapa.ModuloCor
		self.botaoLottenLapa                    ["width"]      = 13
		self.botaoLottenLapa                    ["height"]     = 1
		self.botaoLottenLapa.bind               ("<Button-1>",lambda e: popup("Lotten","Lapa",
													Info.Lotten.Lapa.IP, 
													Info.Lotten.Lapa.Porta, 
													Info.Lotten.Lapa.NumeroRep, 
													Info.Lotten.Lapa.Responsavel, 
													Info.Lotten.Lapa.Telefone))
		self.botaoLottenLapa.grid               (row=10,column=0,sticky = "N")

		self.botaoLottenLapaRelogio                            = Button(self.ContainerLotten)
		self.botaoLottenLapaRelogio             ["text"]       = "R"
		self.botaoLottenLapaRelogio             ["background"] = Info.Lotten.Lapa.RelogioCor
		self.botaoLottenLapaRelogio             ["width"]      = 1
		self.botaoLottenLapaRelogio             ["height"]     = 1
		self.botaoLottenLapaRelogio.grid        (row=10,column=1,sticky = "N")




		self.botaoLottenSaoCaetano                             = Button(self.ContainerLotten)
		self.botaoLottenSaoCaetano              ["text"]       = "Sao Caetano"
		self.botaoLottenSaoCaetano              ["background"] = Info.Lotten.SaoCaetano.ModuloCor
		self.botaoLottenSaoCaetano              ["width"]      = 13
		self.botaoLottenSaoCaetano              ["height"]     = 1
		self.botaoLottenSaoCaetano.bind         ("<Button-1>",lambda e: popup("Lotten","SaoCaetano",
													Info.Lotten.SaoCaetano.IP, 
													Info.Lotten.SaoCaetano.Porta, 
													Info.Lotten.SaoCaetano.NumeroRep, 
													Info.Lotten.SaoCaetano.Responsavel, 
													Info.Lotten.SaoCaetano.Telefone))
		self.botaoLottenSaoCaetano.grid         (row=11,column=0,sticky = "N")

		self.botaoLottenSaoCaetanoRelogio                      = Button(self.ContainerLotten)
		self.botaoLottenSaoCaetanoRelogio       ["text"]       = "R"
		self.botaoLottenSaoCaetanoRelogio       ["background"] = Info.Lotten.SaoCaetano.RelogioCor
		self.botaoLottenSaoCaetanoRelogio       ["width"]      = 1
		self.botaoLottenSaoCaetanoRelogio       ["height"]     = 1
		self.botaoLottenSaoCaetanoRelogio.grid  (row=11,column=1,sticky = "N")




		self.botaoLottenPinheiros                              = Button(self.ContainerLotten)
		self.botaoLottenPinheiros               ["text"]       = "Pinheiros"
		self.botaoLottenPinheiros               ["background"] = Info.Lotten.Pinheiros.ModuloCor
		self.botaoLottenPinheiros               ["width"]      = 13
		self.botaoLottenPinheiros               ["height"]     = 1
		self.botaoLottenPinheiros.bind          ("<Button-1>",lambda e: popup("Lotten","Pinheiros",
													Info.Lotten.Pinheiros.IP, 
													Info.Lotten.Pinheiros.Porta, 
													Info.Lotten.Pinheiros.NumeroRep, 
													Info.Lotten.Pinheiros.Responsavel, 
													Info.Lotten.Pinheiros.Telefone))
		self.botaoLottenPinheiros.grid          (row=12,column=0,sticky = "N")

		self.botaoLottenPinheirosRelogio                       = Button(self.ContainerLotten)
		self.botaoLottenPinheirosRelogio        ["text"]       = "R"
		self.botaoLottenPinheirosRelogio        ["background"] = Info.Lotten.Pinheiros.RelogioCor
		self.botaoLottenPinheirosRelogio        ["width"]      = 1
		self.botaoLottenPinheirosRelogio        ["height"]     = 1
		self.botaoLottenPinheirosRelogio.grid   (row=12,column=1,sticky = "N")




		self.botaoLottenMorumbi                                = Button(self.ContainerLotten)
		self.botaoLottenMorumbi                 ["text"]       = "Morumbi"
		self.botaoLottenMorumbi                 ["background"] = Info.Lotten.Morumbi.ModuloCor
		self.botaoLottenMorumbi                 ["width"]      = 13
		self.botaoLottenMorumbi                 ["height"]     = 1
		self.botaoLottenMorumbi.bind            ("<Button-1>",lambda e: popup("Lotten","Morumbi",
													Info.Lotten.Morumbi.IP, 
													Info.Lotten.Morumbi.Porta, 
													Info.Lotten.Morumbi.NumeroRep, 
													Info.Lotten.Morumbi.Responsavel, 
													Info.Lotten.Morumbi.Telefone))
		self.botaoLottenMorumbi.grid            (row=13,column=0,sticky = "N")

		self.botaoLottenMorumbiRelogio                         = Button(self.ContainerLotten)
		self.botaoLottenMorumbiRelogio          ["text"]       = "R"
		self.botaoLottenMorumbiRelogio          ["background"] = Info.Lotten.Morumbi.RelogioCor
		self.botaoLottenMorumbiRelogio          ["width"]      = 1
		self.botaoLottenMorumbiRelogio          ["height"]     = 1
		self.botaoLottenMorumbiRelogio.grid     (row=13,column=1,sticky = "N")





		self.botaoLottenBerrini                                = Button(self.ContainerLotten)
		self.botaoLottenBerrini                 ["text"]       = "Berrini"
		self.botaoLottenBerrini                 ["background"] = Info.Lotten.Berrini.ModuloCor
		self.botaoLottenBerrini                 ["width"]      = 13
		self.botaoLottenBerrini                 ["height"]     = 1
		self.botaoLottenBerrini.bind            ("<Button-1>",lambda e: popup("Lotten","Berrini",
													Info.Lotten.Berrini.IP, 
													Info.Lotten.Berrini.Porta, 
													Info.Lotten.Berrini.NumeroRep, 
													Info.Lotten.Berrini.Responsavel, 
													Info.Lotten.Berrini.Telefone))
		self.botaoLottenBerrini.grid            (row=14,column=0,sticky = "N")

		self.botaoLottenBerriniRelogio                         = Button(self.ContainerLotten)
		self.botaoLottenBerriniRelogio          ["text"]       = "R"
		self.botaoLottenBerriniRelogio          ["background"] = Info.Lotten.Berrini.RelogioCor
		self.botaoLottenBerriniRelogio          ["width"]      = 1
		self.botaoLottenBerriniRelogio          ["height"]     = 1
		self.botaoLottenBerriniRelogio.grid     (row=14,column=1,sticky = "N")





		self.botaoLottenVilaMariana                            = Button(self.ContainerLotten)
		self.botaoLottenVilaMariana             ["text"]       = "Vila Mariana"
		self.botaoLottenVilaMariana             ["background"] = Info.Lotten.VilaMariana.ModuloCor
		self.botaoLottenVilaMariana             ["width"]      = 13
		self.botaoLottenVilaMariana             ["height"]     = 1
		self.botaoLottenVilaMariana.bind        ("<Button-1>",lambda e: popup("Lotten","Vila Mariana",
													Info.Lotten.VilaMariana.IP, 
													Info.Lotten.VilaMariana.Porta, 
													Info.Lotten.VilaMariana.NumeroRep, 
													Info.Lotten.VilaMariana.Responsavel, 
													Info.Lotten.VilaMariana.Telefone))
		self.botaoLottenVilaMariana.grid        (row=15,column=0,sticky = "N")

		self.botaoLottenVilaMarianaRelogio                     = Button(self.ContainerLotten)
		self.botaoLottenVilaMarianaRelogio      ["text"]       = "R"
		self.botaoLottenVilaMarianaRelogio      ["background"] = Info.Lotten.VilaMariana.RelogioCor
		self.botaoLottenVilaMarianaRelogio      ["width"]      = 1
		self.botaoLottenVilaMarianaRelogio      ["height"]     = 1
		self.botaoLottenVilaMarianaRelogio.grid (row=15,column=1,sticky = "N")





		self.botaoLottenVilaOlimpia                            = Button(self.ContainerLotten)
		self.botaoLottenVilaOlimpia             ["text"]       = "Vila Olimpia"
		self.botaoLottenVilaOlimpia             ["background"] = Info.Lotten.VilaOlimpia.ModuloCor
		self.botaoLottenVilaOlimpia             ["width"]      = 13
		self.botaoLottenVilaOlimpia             ["height"]     = 1
		self.botaoLottenVilaOlimpia.bind        ("<Button-1>",lambda e: popup("Lotten","Vila Olimpia",
											     	Info.Lotten.VilaOlimpia.IP, 
													Info.Lotten.VilaOlimpia.Porta, 
													Info.Lotten.VilaOlimpia.NumeroRep, 
													Info.Lotten.VilaOlimpia.Responsavel, 
													Info.Lotten.VilaOlimpia.Telefone))
		self.botaoLottenVilaOlimpia.grid        (row=16,column=0,sticky = "N")

		self.botaoLottenVilaOlimpiaRelogio                     = Button(self.ContainerLotten)
		self.botaoLottenVilaOlimpiaRelogio      ["text"]       = "R"
		self.botaoLottenVilaOlimpiaRelogio      ["background"] = Info.Lotten.VilaOlimpia.RelogioCor
		self.botaoLottenVilaOlimpiaRelogio      ["width"]      = 1
		self.botaoLottenVilaOlimpiaRelogio      ["height"]     = 1
		self.botaoLottenVilaOlimpiaRelogio.grid (row=16,column=1,sticky = "N")





		self.botaoLottenItaim                                 = Button(self.ContainerLotten)
		self.botaoLottenItaim                  ["text"]       = "Itaim"
		self.botaoLottenItaim                  ["background"] = Info.Lotten.Itaim.ModuloCor
		self.botaoLottenItaim                  ["width"]      = 13
		self.botaoLottenItaim                  ["height"]     = 1
		self.botaoLottenItaim.bind             ("<Button-1>",lambda e: popup("Lotten","Itaim",
													Info.Lotten.Itaim.IP, 
													Info.Lotten.Itaim.Porta, 
													Info.Lotten.Itaim.NumeroRep, 
													Info.Lotten.Itaim.Responsavel, 
													Info.Lotten.Itaim.Telefone))
		self.botaoLottenItaim.grid             (row=17,column=0,sticky = "N")

		self.botaoLottenItaimRelogio                          = Button(self.ContainerLotten)
		self.botaoLottenItaimRelogio           ["text"]       = "R"
		self.botaoLottenItaimRelogio           ["background"] = Info.Lotten.Itaim.RelogioCor
		self.botaoLottenItaimRelogio           ["width"]      = 1
		self.botaoLottenItaimRelogio           ["height"]     = 1
		self.botaoLottenItaimRelogio.grid      (row=17,column=1,sticky = "N")






		self.botaoLottenGuarulhos                              = Button(self.ContainerLotten)
		self.botaoLottenGuarulhos               ["text"]       = "Guarulhos"
		self.botaoLottenGuarulhos               ["background"] = Info.Lotten.Guarulhos.ModuloCor
		self.botaoLottenGuarulhos               ["width"]      = 13
		self.botaoLottenGuarulhos               ["height"]     = 1
		self.botaoLottenGuarulhos.bind          ("<Button-1>",lambda e: popup("Lotten","Guarulhos",
													Info.Lotten.Guarulhos.IP, 
													Info.Lotten.Guarulhos.Porta, 
													Info.Lotten.Guarulhos.NumeroRep, 
													Info.Lotten.Guarulhos.Responsavel, 
													Info.Lotten.Guarulhos.Telefone))
		self.botaoLottenGuarulhos.grid          (row=18,column=0,sticky = "N")

		self.botaoLottenGuarulhosRelogio                       = Button(self.ContainerLotten)
		self.botaoLottenGuarulhosRelogio        ["text"]       = "R"
		self.botaoLottenGuarulhosRelogio        ["background"] = Info.Lotten.Guarulhos.RelogioCor
		self.botaoLottenGuarulhosRelogio        ["width"]      = 1
		self.botaoLottenGuarulhosRelogio        ["height"]     = 1
		self.botaoLottenGuarulhosRelogio.grid   (row=18,column=1,sticky = "N")



	def Create_BestInClass(self):

		self.msgBestInClass = Label (self.ContainerBestInClass,text = "Best In Class")
		self.msgBestInClassCont = Label (self.ContainerBestInClass,text = str(Info.BestInClass.Status.Contage)+"/"
															+str(Info.BestInClass.Status.TotalRelogios))

		self.msgBestInClass.grid                   (row=0,column=0,sticky = "N")
		self.msgBestInClassCont.grid             (row=0,column=1,sticky = "N")






		self.botaoBestInClassRecife                               = Button(self.ContainerBestInClass)
		self.botaoBestInClassRecife                ["text"]       = "Recife"
		self.botaoBestInClassRecife                ["background"] = Info.BestInClass.Recife.ModuloCor
		self.botaoBestInClassRecife                ["width"]      = 13
		self.botaoBestInClassRecife                ["height"]     = 1
		self.botaoBestInClassRecife.bind           ("<Button-1>",lambda e: popup("Best In Class","Recife",
													Info.BestInClass.Recife.IP, 
													Info.BestInClass.Recife.Porta, 
													Info.BestInClass.Recife.NumeroRep, 
													Info.BestInClass.Recife.Responsavel, 
													Info.BestInClass.Recife.Telefone))

		self.botaoBestInClassRecifeRelogio                        = Button(self.ContainerBestInClass)
		self.botaoBestInClassRecifeRelogio         ["text"]       = "R"
		self.botaoBestInClassRecifeRelogio         ["background"] = Info.BestInClass.Recife.RelogioCor
		self.botaoBestInClassRecifeRelogio         ["width"]      = 1
		self.botaoBestInClassRecifeRelogio         ["height"]     = 1

		self.botaoBestInClassRecife.grid           (row=1,column=0,sticky = "N")
		self.botaoBestInClassRecifeRelogio.grid    (row=1,column=1,sticky = "N")






		self.botaoBestInClassItaquera                             = Button(self.ContainerBestInClass)
		self.botaoBestInClassItaquera              ["text"]       = "Itaquera"
		self.botaoBestInClassItaquera              ["background"] = Info.BestInClass.Itaquera.ModuloCor
		self.botaoBestInClassItaquera              ["width"]      = 13
		self.botaoBestInClassItaquera              ["height"]     = 1
		self.botaoBestInClassItaquera.bind         ("<Button-1>",lambda e: popup("Best In Class","Itaquera",
													Info.BestInClass.Itaquera.IP, 
													Info.BestInClass.Itaquera.Porta, 
													Info.BestInClass.Itaquera.NumeroRep, 
													Info.BestInClass.Itaquera.Responsavel, 
													Info.BestInClass.Itaquera.Telefone))


		self.botaoBestInClassItaqueraRelogio                      = Button(self.ContainerBestInClass)
		self.botaoBestInClassItaqueraRelogio       ["text"]       = "R"
		self.botaoBestInClassItaqueraRelogio       ["background"] = Info.BestInClass.Itaquera.RelogioCor
		self.botaoBestInClassItaqueraRelogio       ["width"]      = 1
		self.botaoBestInClassItaqueraRelogio       ["height"]     = 1		

		self.botaoBestInClassItaquera.grid         (row=2,column=0,sticky = "N")
		self.botaoBestInClassItaqueraRelogio.grid  (row=2,column=1,sticky = "N")






		self.botaoBestInClassItapevi                              = Button(self.ContainerBestInClass)
		self.botaoBestInClassItapevi               ["text"]       = "Itapevi"
		self.botaoBestInClassItapevi               ["background"] = Info.BestInClass.Itapevi.ModuloCor
		self.botaoBestInClassItapevi               ["width"]      = 13
		self.botaoBestInClassItapevi               ["height"]     = 1
		self.botaoBestInClassItapevi.bind          ("<Button-1>",lambda e: popup("Best In Class","Itapevi",
													Info.BestInClass.Itapevi.IP, 
													Info.BestInClass.Itapevi.Porta, 
													Info.BestInClass.Itapevi.NumeroRep, 
													Info.BestInClass.Itapevi.Responsavel, 
													Info.BestInClass.Itapevi.Telefone))


		self.botaoBestInClassItapeviRelogio                       = Button(self.ContainerBestInClass)
		self.botaoBestInClassItapeviRelogio        ["text"]       = "R"
		self.botaoBestInClassItapeviRelogio        ["background"] = Info.BestInClass.Itapevi.RelogioCor
		self.botaoBestInClassItapeviRelogio        ["width"]      = 1
		self.botaoBestInClassItapeviRelogio        ["height"]     = 1		

		self.botaoBestInClassItapevi.grid          (row=3,column=0,sticky = "N")
		self.botaoBestInClassItapeviRelogio.grid   (row=3,column=1,sticky = "N")





		self.botaoBestInClassSorocaba                             = Button(self.ContainerBestInClass)
		self.botaoBestInClassSorocaba              ["text"]       = "Sorocaba"
		self.botaoBestInClassSorocaba              ["background"] = Info.BestInClass.Sorocaba.ModuloCor
		self.botaoBestInClassSorocaba              ["width"]      = 13
		self.botaoBestInClassSorocaba              ["height"]     = 1
		self.botaoBestInClassSorocaba.bind          ("<Button-1>",lambda e: popup("Best In Class","Sorocaba",
													Info.BestInClass.Sorocaba.IP, 
													Info.BestInClass.Sorocaba.Porta, 
													Info.BestInClass.Sorocaba.NumeroRep, 
													Info.BestInClass.Sorocaba.Responsavel, 
													Info.BestInClass.Sorocaba.Telefone))

		self.botaoBestInClassSorocabaRelogio                      = Button(self.ContainerBestInClass)
		self.botaoBestInClassSorocabaRelogio       ["text"]       = "R"
		self.botaoBestInClassSorocabaRelogio       ["background"] = Info.BestInClass.Sorocaba.RelogioCor
		self.botaoBestInClassSorocabaRelogio       ["width"]      = 1
		self.botaoBestInClassSorocabaRelogio       ["height"]     = 1

		self.botaoBestInClassSorocaba.grid         (row=4,column=0,sticky = "N")
		self.botaoBestInClassSorocabaRelogio.grid  (row=4,column=1,sticky = "N")




		self.botaoBestInClassSeteLagoas                           = Button(self.ContainerBestInClass)
		self.botaoBestInClassSeteLagoas            ["text"]       = "Sete Lagoas"
		self.botaoBestInClassSeteLagoas            ["background"] = Info.BestInClass.SeteLagoas.ModuloCor
		self.botaoBestInClassSeteLagoas            ["width"]      = 13
		self.botaoBestInClassSeteLagoas            ["height"]     = 1
		self.botaoBestInClassSeteLagoas.bind          ("<Button-1>",lambda e: popup("Best In Class","Sete Lagoas",
													Info.BestInClass.SeteLagoas.IP, 
													Info.BestInClass.SeteLagoas.Porta, 
													Info.BestInClass.SeteLagoas.NumeroRep, 
													Info.BestInClass.SeteLagoas.Responsavel, 
													Info.BestInClass.SeteLagoas.Telefone))

		self.botaoBestInClassSeteLagoasRelogio                    = Button(self.ContainerBestInClass)
		self.botaoBestInClassSeteLagoasRelogio     ["text"]       = "R"
		self.botaoBestInClassSeteLagoasRelogio     ["background"] = Info.BestInClass.SeteLagoas.RelogioCor
		self.botaoBestInClassSeteLagoasRelogio     ["width"]      = 1
		self.botaoBestInClassSeteLagoasRelogio     ["height"]     = 1		

		self.botaoBestInClassSeteLagoas.grid       (row=5,column=0,sticky = "N")
		self.botaoBestInClassSeteLagoasRelogio.grid(row=5,column=1,sticky = "N")




		self.botaoBestInClassCuritiba                             = Button(self.ContainerBestInClass)
		self.botaoBestInClassCuritiba              ["text"]       = "Curitiba"
		self.botaoBestInClassCuritiba              ["background"] = Info.BestInClass.Curitiba.ModuloCor
		self.botaoBestInClassCuritiba              ["width"]      = 13
		self.botaoBestInClassCuritiba              ["height"]     = 1
		self.botaoBestInClassCuritiba.bind          ("<Button-1>",lambda e: popup("Best In Class","Curitiba",
													Info.BestInClass.Curitiba.IP, 
													Info.BestInClass.Curitiba.Porta, 
													Info.BestInClass.Curitiba.NumeroRep, 
													Info.BestInClass.Curitiba.Responsavel, 
													Info.BestInClass.Curitiba.Telefone))


		self.botaoBestInClassCuritibaRelogio                      = Button(self.ContainerBestInClass)
		self.botaoBestInClassCuritibaRelogio       ["text"]       = "R"
		self.botaoBestInClassCuritibaRelogio       ["background"] = Info.BestInClass.Curitiba.RelogioCor
		self.botaoBestInClassCuritibaRelogio       ["width"]      = 1
		self.botaoBestInClassCuritibaRelogio       ["height"]     = 1

		self.botaoBestInClassCuritiba.grid         (row=6,column=0,sticky = "N")
		self.botaoBestInClassCuritibaRelogio.grid  (row=6,column=1,sticky = "N")






		self.botaoBestInClassSFsat                                = Button(self.ContainerBestInClass)
		self.botaoBestInClassSFsat                 ["text"]       = "F Santana"
		self.botaoBestInClassSFsat                 ["background"] = Info.BestInClass.Fsantana.ModuloCor
		self.botaoBestInClassSFsat                 ["width"]      = 13
		self.botaoBestInClassSFsat                 ["height"]     = 1
		self.botaoBestInClassSFsat.bind            ("<Button-1>",lambda e: popup("Best In Class","Feira De Santana",
													Info.BestInClass.Fsantana.IP, 
													Info.BestInClass.Fsantana.Porta, 
													Info.BestInClass.Fsantana.NumeroRep, 
													Info.BestInClass.Fsantana.Responsavel, 
													Info.BestInClass.Fsantana.Telefone))

		self.botaoBestInClassSFsatRelogio                         = Button(self.ContainerBestInClass)
		self.botaoBestInClassSFsatRelogio          ["text"]       = "R"
		self.botaoBestInClassSFsatRelogio          ["background"] = Info.BestInClass.Fsantana.RelogioCor
		self.botaoBestInClassSFsatRelogio          ["width"]      = 1
		self.botaoBestInClassSFsatRelogio          ["height"]     = 1

		self.botaoBestInClassSFsat.grid            (row=7,column=0,sticky = "N")
		self.botaoBestInClassSFsatRelogio.grid     (row=7,column=1,sticky = "N")







		self.botaoBestInClassItu                                  = Button(self.ContainerBestInClass)
		self.botaoBestInClassItu                   ["text"]       = "Itu"
		self.botaoBestInClassItu                   ["background"] = Info.BestInClass.Itu.ModuloCor
		self.botaoBestInClassItu                   ["width"]      = 13
		self.botaoBestInClassItu                   ["height"]     = 1
		self.botaoBestInClassItu.bind              ("<Button-1>",lambda e: popup("Best In Class","Itu",
													Info.BestInClass.Itu.IP, 
													Info.BestInClass.Itu.Porta, 
													Info.BestInClass.Itu.NumeroRep, 
													Info.BestInClass.Itu.Responsavel, 
													Info.BestInClass.Itu.Telefone))

		self.botaoBestInClassItuRelogio                           = Button(self.ContainerBestInClass)
		self.botaoBestInClassItuRelogio            ["text"]       = "R"
		self.botaoBestInClassItuRelogio            ["background"] = Info.BestInClass.Itu.RelogioCor
		self.botaoBestInClassItuRelogio            ["width"]      = 1
		self.botaoBestInClassItuRelogio            ["height"]     = 1


		self.botaoBestInClassItu.grid              (row=8,column=0,sticky = "N")
		self.botaoBestInClassItuRelogio.grid       (row=8,column=1,sticky = "N")







		self.botaoBestInClassGuarulhos                             = Button(self.ContainerBestInClass)
		self.botaoBestInClassGuarulhos              ["text"]       = "Guraulhos"
		self.botaoBestInClassGuarulhos              ["background"] = Info.BestInClass.Guarulhos.ModuloCor
		self.botaoBestInClassGuarulhos              ["width"]      = 13
		self.botaoBestInClassGuarulhos              ["height"]     = 1
		self.botaoBestInClassGuarulhos.bind         ("<Button-1>",lambda e: popup("Best In Class","Guarulhos",
													Info.BestInClass.Guarulhos.IP, 
													Info.BestInClass.Guarulhos.Porta, 
													Info.BestInClass.Guarulhos.NumeroRep, 
													Info.BestInClass.Guarulhos.Responsavel, 
													Info.BestInClass.Guarulhos.Telefone))

		self.botaoBestInClassGuarulhosRelogio                      = Button(self.ContainerBestInClass)
		self.botaoBestInClassGuarulhosRelogio       ["text"]       = "R"
		self.botaoBestInClassGuarulhosRelogio       ["background"] = Info.BestInClass.Guarulhos.RelogioCor
		self.botaoBestInClassGuarulhosRelogio       ["width"]      = 1
		self.botaoBestInClassGuarulhosRelogio       ["height"]     = 1


		self.botaoBestInClassGuarulhos.grid         (row=9,column=0,sticky = "N")
		self.botaoBestInClassGuarulhosRelogio.grid  (row=9,column=1,sticky = "N")







		self.botaoBestInClassItaporanga                            = Button(self.ContainerBestInClass)
		self.botaoBestInClassItaporanga             ["text"]       = "Itaporanga"
		self.botaoBestInClassItaporanga             ["background"] = Info.BestInClass.Itaporanga.ModuloCor
		self.botaoBestInClassItaporanga             ["width"]      = 13
		self.botaoBestInClassItaporanga             ["height"]     = 1
		self.botaoBestInClassItaporanga.bind        ("<Button-1>",lambda e: popup("Best In Class","Itaporanga",
													Info.BestInClass.Itaporanga.IP, 
													Info.BestInClass.Itaporanga.Porta, 
													Info.BestInClass.Itaporanga.NumeroRep, 
													Info.BestInClass.Itaporanga.Responsavel, 
													Info.BestInClass.Itaporanga.Telefone))

		self.botaoBestInClassItaporangaRelogio                     = Button(self.ContainerBestInClass)
		self.botaoBestInClassItaporangaRelogio      ["text"]       = "R"
		self.botaoBestInClassItaporangaRelogio      ["background"] = Info.BestInClass.Itaporanga.RelogioCor
		self.botaoBestInClassItaporangaRelogio      ["width"]      = 1
		self.botaoBestInClassItaporangaRelogio      ["height"]     = 1


		self.botaoBestInClassItaporanga.grid        (row=10,column=0,sticky = "N")
		self.botaoBestInClassItaporangaRelogio.grid (row=10,column=1,sticky = "N")






		self.botaoBestInClassLinhares                              = Button(self.ContainerBestInClass)
		self.botaoBestInClassLinhares               ["text"]       = "Linhares"
		self.botaoBestInClassLinhares               ["background"] = Info.BestInClass.Linhares.ModuloCor
		self.botaoBestInClassLinhares               ["width"]      = 13
		self.botaoBestInClassLinhares               ["height"]     = 1
		self.botaoBestInClassLinhares.bind          ("<Button-1>",lambda e: popup("Best In Class","Linhares",
													Info.BestInClass.Linhares.IP, 
													Info.BestInClass.Linhares.Porta, 
													Info.BestInClass.Linhares.NumeroRep, 
													Info.BestInClass.Linhares.Responsavel, 
													Info.BestInClass.Linhares.Telefone))

		self.botaoBestInClassLinharesRelogio                       = Button(self.ContainerBestInClass)
		self.botaoBestInClassLinharesRelogio        ["text"]       = "R"
		self.botaoBestInClassLinharesRelogio        ["background"] = Info.BestInClass.Linhares.RelogioCor
		self.botaoBestInClassLinharesRelogio        ["width"]      = 1
		self.botaoBestInClassLinharesRelogio        ["height"]     = 1

		self.botaoBestInClassLinhares.grid          (row=11,column=0,sticky = "N")
		self.botaoBestInClassLinharesRelogio.grid   (row=11,column=1,sticky = "N")



	def Create_CasaCristo(self):


		self.msgCasaCristo = Label (self.ContainerCasaCristo,text = "Casa do Cristo")
		self.msgCasaCristoContage = Label (self.ContainerCasaCristo,text = str(Info.CasaCristo.Status.Contage)+"/"+
																			str(Info.CasaCristo.Status.TotalRelogios))

		self.msgCasaCristo.grid(row=0,column=0, sticky = "N")
		self.msgCasaCristoContage.grid(row=0,column=1, sticky = "N")




		self.botaoCasaCristoADM                                   = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoADM                    ["text"]       = "ADM"
		self.botaoCasaCristoADM                    ["background"] = Info.CasaCristo.ADM.ModuloCor
		self.botaoCasaCristoADM                    ["width"]      = 13
		self.botaoCasaCristoADM.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","ADM",
													Info.CasaCristo.ADM.IP, 
													Info.CasaCristo.ADM.Porta, 
													Info.CasaCristo.ADM.NumeroRep, 
													Info.CasaCristo.ADM.Responsavel, 
													Info.CasaCristo.ADM.Telefone))

		self.botaoCasaCristoADMRelogio                            = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoADMRelogio             ["text"]       = "R"
		self.botaoCasaCristoADMRelogio             ["background"] = Info.CasaCristo.ADM.RelogioCor
		self.botaoCasaCristoADMRelogio             ["width"]      = 1

		self.botaoCasaCristoADM.grid               (row=1,column=0,sticky = "N")
		self.botaoCasaCristoADMRelogio.grid        (row=1,column=1,sticky = "N")





		self.botaoCasaCristoCEI1                                  = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI1                   ["text"]       = "CEI1"
		self.botaoCasaCristoCEI1                   ["background"] = Info.CasaCristo.CEI1.ModuloCor
		self.botaoCasaCristoCEI1                   ["width"]      = 13
		self.botaoCasaCristoCEI1.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI1",
													Info.CasaCristo.CEI1.IP, 
													Info.CasaCristo.CEI1.Porta, 
													Info.CasaCristo.CEI1.NumeroRep, 
													Info.CasaCristo.CEI1.Responsavel, 
													Info.CasaCristo.CEI1.Telefone))

		self.botaoCasaCristoCEI1Relogio                           = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI1Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI1Relogio            ["background"] = Info.CasaCristo.CEI1.RelogioCor
		self.botaoCasaCristoCEI1Relogio            ["width"]      = 1

		self.botaoCasaCristoCEI1.grid              (row=2,column=0,sticky = "N")
		self.botaoCasaCristoCEI1Relogio.grid       (row=2,column=1,sticky = "N")





		self.botaoCasaCristoCEI2                                  = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI2                   ["text"]       = "CEI2"
		self.botaoCasaCristoCEI2                   ["background"] = Info.CasaCristo.CEI2.ModuloCor
		self.botaoCasaCristoCEI2                   ["width"]      = 13
		self.botaoCasaCristoCEI2.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI2",
													Info.CasaCristo.CEI2.IP, 
													Info.CasaCristo.CEI2.Porta, 
													Info.CasaCristo.CEI2.NumeroRep, 
													Info.CasaCristo.CEI2.Responsavel, 
													Info.CasaCristo.CEI2.Telefone))

		self.botaoCasaCristoCEI2Relogio                           = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI2Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI2Relogio            ["background"] = Info.CasaCristo.CEI2.RelogioCor
		self.botaoCasaCristoCEI2Relogio            ["width"]=1

		self.botaoCasaCristoCEI2.grid              (row=3,column=0,sticky = "N")
		self.botaoCasaCristoCEI2Relogio.grid       (row=3,column=1,sticky = "N")
		





		self.botaoCasaCristoCEI3                                  = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI3                   ["text"]       = "CEI3"
		self.botaoCasaCristoCEI3                   ["background"] = Info.CasaCristo.CEI3.ModuloCor
		self.botaoCasaCristoCEI3                   ["width"]      = 13
		self.botaoCasaCristoCEI3.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI3",
													Info.CasaCristo.CEI3.IP, 
													Info.CasaCristo.CEI3.Porta, 
													Info.CasaCristo.CEI3.NumeroRep, 
													Info.CasaCristo.CEI3.Responsavel, 
													Info.CasaCristo.CEI3.Telefone))

		self.botaoCasaCristoCEI3Relogio                           = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoCEI3Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI3Relogio            ["background"] = Info.CasaCristo.CEI3.RelogioCor
		self.botaoCasaCristoCEI3Relogio            ["width"]      = 1

		self.botaoCasaCristoCEI3.grid              (row=4,column=0,sticky = "N")
		self.botaoCasaCristoCEI3Relogio.grid       (row=4,column=1,sticky = "N")





		self.botaoCasaCristoVMatilde                              = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoVMatilde               ["text"]       = "Vovo Matilde"
		self.botaoCasaCristoVMatilde               ["background"] = Info.CasaCristo.VovoMatilde.ModuloCor
		self.botaoCasaCristoVMatilde               ["width"]      = 13
		self.botaoCasaCristoVMatilde.bind          ("<Button-1>",lambda e: popup("Casa do Cristo","Vovo Matilde",
													Info.CasaCristo.VovoMatilde.IP, 
													Info.CasaCristo.VovoMatilde.Porta, 
													Info.CasaCristo.VovoMatilde.NumeroRep, 
													Info.CasaCristo.VovoMatilde.Responsavel, 
													Info.CasaCristo.VovoMatilde.Telefone))

		self.botaoCasaCristoVMatildeRelogio                       = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoVMatildeRelogio        ["text"]       = "R"
		self.botaoCasaCristoVMatildeRelogio        ["background"] = Info.CasaCristo.VovoMatilde.RelogioCor
		self.botaoCasaCristoVMatildeRelogio        ["width"]      = 1

		self.botaoCasaCristoVMatilde.grid          (row=5,column=0,sticky = "N")
		self.botaoCasaCristoVMatildeRelogio.grid   (row=5,column=1,sticky = "N")



	def Create_Building(self):


		self.msgBuilding                            = Label (self.ContainerBuilding,text = "Building")
		self.msgBuilding                            ["height"]     = 1
		self.msgBuilding.grid                       (row=0,column=0,sticky = "N")

		self.msgBuildingCont                        = Label (self.ContainerBuilding,text = str(Info.Building.Status.Contage)+"/3")
		self.msgBuildingCont                        ["height"]     = 1
		self.msgBuildingCont.grid                   (row=0,column=1,sticky = "N")






		self.botaoBuildingAllianz                                  = Button(self.ContainerBuilding)
		self.botaoBuildingAllianz                   ["text"]       = "Allianz"
		self.botaoBuildingAllianz                   ["background"] = Info.Building.Allianz.ModuloCor
		self.botaoBuildingAllianz                   ["width"]      = 13
		self.botaoBuildingAllianz                   ["height"]     = 1
		self.botaoBuildingAllianz.bind              ("<Button-1>",lambda e: popup("Building","Allianz",
													Info.Building.Allianz.IP, 
													Info.Building.Allianz.Porta, 
													Info.Building.Allianz.NumeroRep, 
													Info.Building.Allianz.Responsavel, 
													Info.Building.Allianz.Telefone))

		self.botaoBuildingAllianzRelogio                           = Button(self.ContainerBuilding)
		self.botaoBuildingAllianzRelogio            ["text"]       = "R"
		self.botaoBuildingAllianzRelogio            ["background"] = Info.Building.Allianz.RelogioCor
		self.botaoBuildingAllianzRelogio            ["width"]      = 1
		self.botaoBuildingAllianzRelogio            ["height"]     = 1

		self.botaoBuildingAllianz.grid       		(row=1, column=0, sticky = "N")
		self.botaoBuildingAllianzRelogio.grid       (row=1, column=1, sticky = "N")






		self.botaoBuildingWTorre                                   = Button(self.ContainerBuilding)
		self.botaoBuildingWTorre                    ["text"]       = "WTorre"
		self.botaoBuildingWTorre                    ["background"] = Info.Building.WTorre.ModuloCor
		self.botaoBuildingWTorre                    ["width"]      = 13
		self.botaoBuildingWTorre                    ["height"]     = 1
		self.botaoBuildingWTorre.bind              ("<Button-1>",lambda e: popup("Building","WTorre",
													Info.Building.WTorre.IP, 
													Info.Building.WTorre.Porta, 
													Info.Building.WTorre.NumeroRep, 
													Info.Building.WTorre.Responsavel, 
													Info.Building.WTorre.Telefone))

		self.botaoBuildingWTorreRelogio                            = Button(self.ContainerBuilding)
		self.botaoBuildingWTorreRelogio             ["text"]       = "R"
		self.botaoBuildingWTorreRelogio             ["background"] = Info.Building.WTorre.RelogioCor
		self.botaoBuildingWTorreRelogio             ["width"]      = 1
		self.botaoBuildingWTorreRelogio             ["height"]     = 1

		self.botaoBuildingWTorre.grid               (row=2,column=0,sticky = "N")
		self.botaoBuildingWTorreRelogio.grid        (row=2,column=1,sticky = "N")






		self.botaoBuildingRioJaneiro                               = Button(self.ContainerBuilding)
		self.botaoBuildingRioJaneiro                ["text"]       = "Rio De Janeiro"
		self.botaoBuildingRioJaneiro                ["background"] = Info.Building.RioJaneiro.ModuloCor
		self.botaoBuildingRioJaneiro                ["width"]      = 13
		self.botaoBuildingRioJaneiro                ["height"]     = 1
		self.botaoBuildingRioJaneiro.bind           ("<Button-1>",lambda e: popup("Building","Rio de Janeiro",
													Info.Building.RioJaneiro.IP, 
													Info.Building.RioJaneiro.Porta, 
													Info.Building.RioJaneiro.NumeroRep, 
													Info.Building.RioJaneiro.Responsavel, 
													Info.Building.RioJaneiro.Telefone))

		self.botaoBuildingRioJaneiroRelogio                        = Button(self.ContainerBuilding)
		self.botaoBuildingRioJaneiroRelogio         ["text"]       = "R"
		self.botaoBuildingRioJaneiroRelogio         ["background"] = Info.Building.RioJaneiro.RelogioCor
		self.botaoBuildingRioJaneiroRelogio         ["width"]      = 1
		self.botaoBuildingRioJaneiroRelogio         ["height"]     =  1


		self.botaoBuildingRioJaneiro.grid           (row=3,column=0,sticky = "N")
		self.botaoBuildingRioJaneiroRelogio.grid    (row=3,column=1,sticky = "N")



	def Create_GrupoNK(self):


		self.msgGrupoNk                            		= Label (self.ContainerGrupoNk,text = "Grupo Nk")
		self.msgGrupoNk                            		["height"]     = 1
		self.msgGrupoNk.grid                       		(row=0,column=0,sticky = "N")

		self.msgGrupoNkContage                        	= Label (self.ContainerGrupoNk,text=str(Info.GrupoNk.Status.Contage)+"/"+
																								str(Info.GrupoNk.Status.TotalRelogios))	
		self.msgGrupoNkContage                        	["height"]     = 1
		self.msgGrupoNkContage.grid                   	(row=0,column=1,sticky = "N")



		self.botaoGrupoNkNelsonKioshi                                  = Button(self.ContainerGrupoNk)
		self.botaoGrupoNkNelsonKioshi                  	["text"]       = "Nelson Kioshi"
		self.botaoGrupoNkNelsonKioshi                   ["background"] = Info.GrupoNk.NelsonKioshi.ModuloCor
		self.botaoGrupoNkNelsonKioshi                   ["width"]      = 13
		self.botaoGrupoNkNelsonKioshi                   ["height"]     = 1
		self.botaoGrupoNkNelsonKioshi.bind              ("<Button-1>",lambda e: popup("GrupoNk","Nelson Kioshi",
														Info.GrupoNk.NelsonKioshi.IP, 
														Info.GrupoNk.NelsonKioshi.Porta, 
														Info.GrupoNk.NelsonKioshi.NumeroRep, 
														Info.GrupoNk.NelsonKioshi.Responsavel, 
														Info.GrupoNk.NelsonKioshi.Telefone))

		self.botaoGrupoNkNelsonKioshiRelogio                           = Button(self.ContainerGrupoNk)
		self.botaoGrupoNkNelsonKioshiRelogio            ["text"]       = "R"
		self.botaoGrupoNkNelsonKioshiRelogio            ["background"] = Info.GrupoNk.NelsonKioshi.RelogioCor
		self.botaoGrupoNkNelsonKioshiRelogio            ["width"]      = 1
		self.botaoGrupoNkNelsonKioshiRelogio            ["height"]     = 1

		self.botaoGrupoNkNelsonKioshi.grid       		(row=1, column=0, sticky = "N")
		self.botaoGrupoNkNelsonKioshiRelogio.grid       (row=1, column=1, sticky = "N")






		self.botaoGrupoNkRDFurukawa                                   	= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkRDFurukawa                    	["text"]        = "RD Furukawa"
		self.botaoGrupoNkRDFurukawa                    	["background"]  = Info.GrupoNk.RDFurukawa.ModuloCor
		self.botaoGrupoNkRDFurukawa                    	["width"]       = 13
		self.botaoGrupoNkRDFurukawa                   	["height"]      = 1
		self.botaoGrupoNkRDFurukawa.bind              	("<Button-1>",lambda e: popup("GrupoNk","RD Furukawa",
														Info.GrupoNk.RDFurukawa.IP, 
														Info.GrupoNk.RDFurukawa.Porta, 
														Info.GrupoNk.RDFurukawa.NumeroRep, 
														Info.GrupoNk.RDFurukawa.Responsavel, 
														Info.GrupoNk.RDFurukawa.Telefone))

		self.botaoGrupoNkRDFurukawaRelogio                            	= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkRDFurukawaRelogio              ["text"]        = "R"
		self.botaoGrupoNkRDFurukawaRelogio              ["background"]  = Info.GrupoNk.RDFurukawa.RelogioCor
		self.botaoGrupoNkRDFurukawaRelogio              ["width"]       = 1
		self.botaoGrupoNkRDFurukawaRelogio              ["height"]      = 1

		self.botaoGrupoNkRDFurukawa.grid                (row=2,column=0,sticky = "N")
		self.botaoGrupoNkRDFurukawaRelogio.grid         (row=2,column=1,sticky = "N")






		self.botaoGrupoNkKio1                               			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkKio1                			["text"]        = "Kio 1"
		self.botaoGrupoNkKio1                			["background"]  = Info.GrupoNk.Kio1.ModuloCor
		self.botaoGrupoNkKio1                			["width"]       = 13
		self.botaoGrupoNkKio1                			["height"]      = 1
		self.botaoGrupoNkKio1.bind           			("<Button-1>",lambda e: popup("GrupoNk","Kio 1",
														Info.GrupoNk.Kio1.IP, 
														Info.GrupoNk.Kio1.Porta, 
														Info.GrupoNk.Kio1.NumeroRep, 
														Info.GrupoNk.Kio1.Responsavel, 
														Info.GrupoNk.Kio1.Telefone))

		self.botaoGrupoNkKio1Relogio         		               		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkKio1Relogio         			["text"]        = "R"
		self.botaoGrupoNkKio1Relogio         			["background"]  = Info.GrupoNk.Kio1.RelogioCor
		self.botaoGrupoNkKio1Relogio         			["width"]       = 1
		self.botaoGrupoNkKio1Relogio         			["height"]      = 1


		self.botaoGrupoNkKio1.grid           			(row=3,column=0,sticky = "N")
		self.botaoGrupoNkKio1Relogio.grid    			(row=3,column=1,sticky = "N")





		self.botaoGrupoNkKio2                               			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkKio2                			["text"]        = "Kio 2"
		self.botaoGrupoNkKio2                			["background"]  = Info.GrupoNk.Kio2.ModuloCor
		self.botaoGrupoNkKio2                			["width"]       = 13
		self.botaoGrupoNkKio2                			["height"]      = 1
		self.botaoGrupoNkKio2.bind           			("<Button-1>",lambda e: popup("GrupoNk","Kio 2",
														Info.GrupoNk.Kio2.IP, 
														Info.GrupoNk.Kio2.Porta, 
														Info.GrupoNk.Kio2.NumeroRep, 
														Info.GrupoNk.Kio2.Responsavel, 
														Info.GrupoNk.Kio2.Telefone))

		self.botaoGrupoNkKio2Relogio         		               		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkKio2Relogio         			["text"]        = "R"
		self.botaoGrupoNkKio2Relogio         			["background"]  = Info.GrupoNk.Kio2.RelogioCor
		self.botaoGrupoNkKio2Relogio         			["width"]       = 1
		self.botaoGrupoNkKio2Relogio         			["height"]      = 1


		self.botaoGrupoNkKio2.grid           			(row=4,column=0,sticky = "N")
		self.botaoGrupoNkKio2Relogio.grid    			(row=4,column=1,sticky = "N")


		self.botaoGrupoNkGranjaViana                          			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkGranjaViana                	["text"]        = "Granja Viana"
		self.botaoGrupoNkGranjaViana                	["background"]  = Info.GrupoNk.GranjaViana.ModuloCor
		self.botaoGrupoNkGranjaViana                	["width"]       = 13
		self.botaoGrupoNkGranjaViana                	["height"]      = 1
		self.botaoGrupoNkGranjaViana.bind           	("<Button-1>",lambda e: popup("GrupoNk","Granja Viana",
														Info.GrupoNk.GranjaViana.IP, 
														Info.GrupoNk.GranjaViana.Porta, 
														Info.GrupoNk.GranjaViana.NumeroRep, 
														Info.GrupoNk.GranjaViana.Responsavel, 
														Info.GrupoNk.GranjaViana.Telefone))

		self.botaoGrupoNkGranjaVianaRelogio         		            = Button(self.ContainerGrupoNk)
		self.botaoGrupoNkGranjaVianaRelogio         	["text"]        = "R"
		self.botaoGrupoNkGranjaVianaRelogio         	["background"]  = Info.GrupoNk.GranjaViana.RelogioCor
		self.botaoGrupoNkGranjaVianaRelogio         	["width"]       = 1
		self.botaoGrupoNkGranjaVianaRelogio         	["height"]      = 1


		self.botaoGrupoNkGranjaViana.grid           	(row=5,column=0,sticky = "N")
		self.botaoGrupoNkGranjaVianaRelogio.grid    	(row=5,column=1,sticky = "N")



		self.botaoGrupoNkSantaCecilia                               	= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkSantaCecilia                	["text"]        = "Santa Cecilia"
		self.botaoGrupoNkSantaCecilia                	["background"]  = Info.GrupoNk.SantaCecilia.ModuloCor
		self.botaoGrupoNkSantaCecilia                	["width"]       = 13
		self.botaoGrupoNkSantaCecilia                	["height"]      = 1
		self.botaoGrupoNkSantaCecilia.bind           	("<Button-1>",lambda e: popup("GrupoNk","Santa Cecilia",
														Info.GrupoNk.SantaCecilia.IP, 
														Info.GrupoNk.SantaCecilia.Porta, 
														Info.GrupoNk.SantaCecilia.NumeroRep, 
														Info.GrupoNk.SantaCecilia.Responsavel, 
														Info.GrupoNk.SantaCecilia.Telefone))

		self.botaoGrupoNkSantaCeciliaRelogio         	           		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkSantaCeciliaRelogio         	["text"]        = "R"
		self.botaoGrupoNkSantaCeciliaRelogio         	["background"]  = Info.GrupoNk.SantaCecilia.RelogioCor
		self.botaoGrupoNkSantaCeciliaRelogio         	["width"]       = 1
		self.botaoGrupoNkSantaCeciliaRelogio         	["height"]      = 1


		self.botaoGrupoNkSantaCecilia.grid           	(row=6,column=0,sticky = "N")
		self.botaoGrupoNkSantaCeciliaRelogio.grid    	(row=6,column=1,sticky = "N")


		self.botaoGrupoNkTransfruit                            			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkTransfruit                		["text"]        = "Transfruit"
		self.botaoGrupoNkTransfruit                		["background"]  = Info.GrupoNk.Transfruit.ModuloCor
		self.botaoGrupoNkTransfruit                		["width"]       = 13
		self.botaoGrupoNkTransfruit                		["height"]      = 1
		self.botaoGrupoNkTransfruit.bind           		("<Button-1>",lambda e: popup("GrupoNk","Transfruit",
														Info.GrupoNk.Transfruit.IP, 
														Info.GrupoNk.Transfruit.Porta, 
														Info.GrupoNk.Transfruit.NumeroRep, 
														Info.GrupoNk.Transfruit.Responsavel, 
														Info.GrupoNk.Transfruit.Telefone))

		self.botaoGrupoNkTransfruitRelogio         		           		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkTransfruitRelogio         		["text"]        = "R"
		self.botaoGrupoNkTransfruitRelogio         		["background"]  = Info.GrupoNk.Transfruit.RelogioCor
		self.botaoGrupoNkTransfruitRelogio         		["width"]       = 1
		self.botaoGrupoNkTransfruitRelogio         		["height"]      = 1

		self.botaoGrupoNkTransfruit.grid           		(row=7,column=0,sticky = "N")
		self.botaoGrupoNkTransfruitRelogio.grid    		(row=7,column=1,sticky = "N")


		self.botaoGrupoNkDistribuidora                         			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkDistribuidora                	["text"]        = "Distribuidora"
		self.botaoGrupoNkDistribuidora                	["background"]  = Info.GrupoNk.Distribuidora.ModuloCor
		self.botaoGrupoNkDistribuidora                	["width"]       = 13
		self.botaoGrupoNkDistribuidora                	["height"]      = 1
		self.botaoGrupoNkDistribuidora.bind           	("<Button-1>",lambda e: popup("GrupoNk","Distribuidora",
														Info.GrupoNk.Distribuidora.IP, 
														Info.GrupoNk.Distribuidora.Porta, 
														Info.GrupoNk.Distribuidora.NumeroRep, 
														Info.GrupoNk.Distribuidora.Responsavel, 
														Info.GrupoNk.Distribuidora.Telefone))

		self.botaoGrupoNkDistribuidoraRelogio         	           		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkDistribuidoraRelogio         	["text"]        = "R"
		self.botaoGrupoNkDistribuidoraRelogio         	["background"]  = Info.GrupoNk.Distribuidora.RelogioCor
		self.botaoGrupoNkDistribuidoraRelogio         	["width"]       = 1
		self.botaoGrupoNkDistribuidoraRelogio         	["height"]      = 1

		self.botaoGrupoNkDistribuidora.grid           	(row=8,column=0,sticky = "N")
		self.botaoGrupoNkDistribuidoraRelogio.grid    	(row=8,column=1,sticky = "N")



		self.botaoGrupoNkNKFilial                             			= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkNKFilial                		["text"]        = "NK Filial"
		self.botaoGrupoNkNKFilial                		["background"]  = Info.GrupoNk.NKFilial.ModuloCor
		self.botaoGrupoNkNKFilial                		["width"]       = 13
		self.botaoGrupoNkNKFilial                		["height"]      = 1
		self.botaoGrupoNkNKFilial.bind           		("<Button-1>",lambda e: popup("GrupoNk","NK Filial",
														Info.GrupoNk.NKFilial.IP,  
														Info.GrupoNk.NKFilial.Porta, 
														Info.GrupoNk.NKFilial.NumeroRep, 
														Info.GrupoNk.NKFilial.Responsavel, 
														Info.GrupoNk.NKFilial.Telefone))

		self.botaoGrupoNkNKFilialRelogio         		           		= Button(self.ContainerGrupoNk)
		self.botaoGrupoNkNKFilialRelogio         		["text"]        = "R"
		self.botaoGrupoNkNKFilialRelogio         		["background"]  = Info.GrupoNk.NKFilial.RelogioCor
		self.botaoGrupoNkNKFilialRelogio         		["width"]       = 1
		self.botaoGrupoNkNKFilialRelogio         		["height"]      = 1

		self.botaoGrupoNkNKFilial.grid           		(row=9,column=0,sticky = "N")
		self.botaoGrupoNkNKFilialRelogio.grid    		(row=9,column=1,sticky = "N")



	def Create_SBCP(self):

		self.msgSBCP                              		= Label (self.ContainerSBCP,text = "SBCP")
		self.msgSBCP                              		["height"]     = 1
		self.msgSBCP.grid                         		(row=0,column=0,sticky = "N")


		self.msgSBCPCount                              	= Label (self.ContainerSBCP,text str(Info.SBCP.Status.Contage)+"/"+
																						 str(Info.SBCP.Status.TotalRelogios))	

		self.msgSBCPCount                              	["height"]     = 1
		self.msgSBCPCount.grid                         	(row=0,column=1,sticky = "N")




		self.botaoSBCPNacional                         	= Button(self.ContainerSBCP)
		self.botaoSBCPNacional                         	["text"]       = "Nacional"
		self.botaoSBCPNacional                         	["background"] = Info.SBCP.Nacional.ModuloCor
		self.botaoSBCPNacional                         	["width"]      = 13
		self.botaoSBCPNacional                         	["height"]     = 1
		self.botaoSBCPNacional.bind                    	("<Button-1>",lambda e: popup("SBCP","Nacional",
														Info.SBCP.Nacional.IP, 
														Info.SBCP.Nacional.Porta, 
														Info.SBCP.Nacional.NumeroRep, 
														Info.SBCP.Nacional.Responsavel, 
														Info.SBCP.Nacional.Telefone))

		self.botaoSBCPNacionalRelogio                  	= Button(self.ContainerSBCP)
		self.botaoSBCPNacionalRelogio                  	["text"]       = "R"
		self.botaoSBCPNacionalRelogio                  	["background"] = Info.SBCP.Nacional.RelogioCor
		self.botaoSBCPNacionalRelogio                  	["height"]     = 1
		self.botaoSBCPNacionalRelogio                  	["width"]      = 1


		self.botaoSBCPNacional.grid                    	(row=1,column=0,sticky = "N")
		self.botaoSBCPNacionalRelogio.grid             	(row=1,column=1,sticky = "N")








		self.botaoSBCPES                         		= Button(self.ContainerSBCP)
		self.botaoSBCPES                         		["text"]       = "ES"
		self.botaoSBCPES                         		["background"] = Info.SBCP.ES.ModuloCor
		self.botaoSBCPES                         		["width"]      = 13
		self.botaoSBCPES                         		["height"]     = 1
		self.botaoSBCPES.bind                    		("<Button-1>",lambda e: popup("SBCP","ES",
														Info.SBCP.ES.IP, 
														Info.SBCP.ES.Porta, 
														Info.SBCP.ES.NumeroRep, 
														Info.SBCP.ES.Responsavel, 
														Info.SBCP.ES.Telefone))

		self.botaoSBCPESRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPESRelogio                  		["text"]       = "R"
		self.botaoSBCPESRelogio                  		["background"] = Info.SBCP.ES.RelogioCor
		self.botaoSBCPESRelogio                  		["height"]     = 1
		self.botaoSBCPESRelogio                  		["width"]      = 1


		self.botaoSBCPES.grid                    		(row=2,column=0,sticky = "N")
		self.botaoSBCPESRelogio.grid             		(row=2,column=1,sticky = "N")








		self.botaoSBCPDF                         		= Button(self.ContainerSBCP)
		self.botaoSBCPDF                         		["text"]       = "DF"
		self.botaoSBCPDF                         		["background"] = Info.SBCP.DF.ModuloCor
		self.botaoSBCPDF                         		["width"]      = 13
		self.botaoSBCPDF                         		["height"]     = 1
		self.botaoSBCPDF.bind                    		("<Button-1>",lambda e: popup("SBCP","DF",
														Info.SBCP.DF.IP, 
														Info.SBCP.DF.Porta, 
														Info.SBCP.DF.NumeroRep, 
														Info.SBCP.DF.Responsavel, 
														Info.SBCP.DF.Telefone))

		self.botaoSBCPDFRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPDFRelogio                  		["text"]       = "R"
		self.botaoSBCPDFRelogio                  		["background"] = Info.SBCP.DF.RelogioCor
		self.botaoSBCPDFRelogio                  		["height"]     = 1
		self.botaoSBCPDFRelogio                  		["width"]      = 1


		self.botaoSBCPDF.grid                    		(row=3,column=0,sticky = "N")
		self.botaoSBCPDFRelogio.grid             		(row=3,column=1,sticky = "N")








		self.botaoSBCPCE                         		= Button(self.ContainerSBCP)
		self.botaoSBCPCE                         		["text"]       = "CE"
		self.botaoSBCPCE                         		["background"] = Info.SBCP.CE.ModuloCor
		self.botaoSBCPCE                         		["width"]      = 13
		self.botaoSBCPCE                         		["height"]     = 1
		self.botaoSBCPCE.bind                    		("<Button-1>",lambda e: popup("SBCP","CE",
														Info.SBCP.CE.IP, 
														Info.SBCP.CE.Porta, 
														Info.SBCP.CE.NumeroRep, 
														Info.SBCP.CE.Responsavel, 
														Info.SBCP.CE.Telefone))

		self.botaoSBCPCERelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPCERelogio                  		["text"]       = "R"
		self.botaoSBCPCERelogio                  		["background"] = Info.SBCP.CE.RelogioCor
		self.botaoSBCPCERelogio                  		["height"]     = 1
		self.botaoSBCPCERelogio                  		["width"]      = 1


		self.botaoSBCPCE.grid                    		(row=4,column=0,sticky = "N")
		self.botaoSBCPCERelogio.grid             		(row=4,column=1,sticky = "N")








		self.botaoSBCPBA                         		= Button(self.ContainerSBCP)
		self.botaoSBCPBA                         		["text"]       = "BA"
		self.botaoSBCPBA                         		["background"] = Info.SBCP.BA.ModuloCor
		self.botaoSBCPBA                         		["width"]      = 13
		self.botaoSBCPBA                         		["height"]     = 1
		self.botaoSBCPBA.bind                    		("<Button-1>",lambda e: popup("SBCP","BA",
														Info.SBCP.BA.IP, 
														Info.SBCP.BA.Porta, 
														Info.SBCP.BA.NumeroRep, 
														Info.SBCP.BA.Responsavel, 
														Info.SBCP.BA.Telefone))

		self.botaoSBCPBARelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPBARelogio                  		["text"]       = "R"
		self.botaoSBCPBARelogio                  		["background"] = Info.SBCP.BA.RelogioCor
		self.botaoSBCPBARelogio                  		["height"]     = 1
		self.botaoSBCPBARelogio                  		["width"]      = 1


		self.botaoSBCPBA.grid                    		(row=5,column=0,sticky = "N")
		self.botaoSBCPBARelogio.grid             		(row=5,column=1,sticky = "N")








		self.botaoSBCPSP                         		= Button(self.ContainerSBCP)
		self.botaoSBCPSP                         		["text"]       = "SP"
		self.botaoSBCPSP                         		["background"] = Info.SBCP.SP.ModuloCor
		self.botaoSBCPSP                         		["width"]      = 13
		self.botaoSBCPSP                         		["height"]     = 1
		self.botaoSBCPSP.bind                    		("<Button-1>",lambda e: popup("SBCP","SP",
														Info.SBCP.SP.IP, 
														Info.SBCP.SP.Porta, 
														Info.SBCP.SP.NumeroRep, 
														Info.SBCP.SP.Responsavel, 
														Info.SBCP.SP.Telefone))

		self.botaoSBCPSPRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPSPRelogio                  		["text"]       = "R"
		self.botaoSBCPSPRelogio                  		["background"] = Info.SBCP.SP.RelogioCor
		self.botaoSBCPSPRelogio                  		["height"]     = 1
		self.botaoSBCPSPRelogio                  		["width"]      = 1


		self.botaoSBCPSP.grid                    		(row=6,column=0,sticky = "N")
		self.botaoSBCPSPRelogio.grid             		(row=6,column=1,sticky = "N")








		self.botaoSBCPSC                         		= Button(self.ContainerSBCP)
		self.botaoSBCPSC                         		["text"]       = "SC"
		self.botaoSBCPSC                         		["background"] = Info.SBCP.SC.ModuloCor
		self.botaoSBCPSC                         		["width"]      = 13
		self.botaoSBCPSC                         		["height"]     = 1
		self.botaoSBCPSC.bind                    		("<Button-1>",lambda e: popup("SBCP","SC",
														Info.SBCP.SC.IP, 
														Info.SBCP.SC.Porta, 
														Info.SBCP.SC.NumeroRep, 
														Info.SBCP.SC.Responsavel, 
														Info.SBCP.SC.Telefone))

		self.botaoSBCPSCRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPSCRelogio                  		["text"]       = "R"
		self.botaoSBCPSCRelogio                  		["background"] = Info.SBCP.SC.RelogioCor
		self.botaoSBCPSCRelogio                  		["height"]     = 1
		self.botaoSBCPSCRelogio                  		["width"]      = 1


		self.botaoSBCPSC.grid                    		(row=7,column=0,sticky = "N")
		self.botaoSBCPSCRelogio.grid             		(row=7,column=1,sticky = "N")








		self.botaoSBCPRS                         		= Button(self.ContainerSBCP)
		self.botaoSBCPRS                         		["text"]       = "RS"
		self.botaoSBCPRS                         		["background"] = Info.SBCP.RS.ModuloCor
		self.botaoSBCPRS                         		["width"]      = 13
		self.botaoSBCPRS                         		["height"]     = 1
		self.botaoSBCPRS.bind                    		("<Button-1>",lambda e: popup("SBCP","RS",
														Info.SBCP.RS.IP, 
														Info.SBCP.RS.Porta, 
														Info.SBCP.RS.NumeroRep, 
														Info.SBCP.RS.Responsavel, 
														Info.SBCP.RS.Telefone))

		self.botaoSBCPRSRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPRSRelogio                  		["text"]       = "R"
		self.botaoSBCPRSRelogio                  		["background"] = Info.SBCP.RS.RelogioCor
		self.botaoSBCPRSRelogio                  		["height"]     = 1
		self.botaoSBCPRSRelogio                  		["width"]      = 1


		self.botaoSBCPRS.grid                    		(row=8,column=0,sticky = "N")
		self.botaoSBCPRSRelogio.grid             		(row=8,column=1,sticky = "N")








		self.botaoSBCPRJ                         		= Button(self.ContainerSBCP)
		self.botaoSBCPRJ                         		["text"]       = "RJ"
		self.botaoSBCPRJ                         		["background"] = Info.SBCP.RJ.ModuloCor
		self.botaoSBCPRJ                         		["width"]      = 13
		self.botaoSBCPRJ                         		["height"]     = 1
		self.botaoSBCPRJ.bind                    		("<Button-1>",lambda e: popup("SBCP","RJ",
														Info.SBCP.RJ.IP, 
														Info.SBCP.RJ.Porta, 
														Info.SBCP.RJ.NumeroRep, 
														Info.SBCP.RJ.Responsavel, 
														Info.SBCP.RJ.Telefone))

		self.botaoSBCPRJRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPRJRelogio                  		["text"]       = "R"
		self.botaoSBCPRJRelogio                  		["background"] = Info.SBCP.RJ.RelogioCor
		self.botaoSBCPRJRelogio                  		["height"]     = 1
		self.botaoSBCPRJRelogio                  		["width"]      = 1


		self.botaoSBCPRJ.grid                    		(row=9,column=0,sticky = "N")
		self.botaoSBCPRJRelogio.grid             		(row=9,column=1,sticky = "N")








		self.botaoSBCPPR                         		= Button(self.ContainerSBCP)
		self.botaoSBCPPR                         		["text"]       = "PR"
		self.botaoSBCPPR                         		["background"] = Info.SBCP.PR.ModuloCor
		self.botaoSBCPPR                         		["width"]      = 13
		self.botaoSBCPPR                         		["height"]     = 1
		self.botaoSBCPPR.bind                    		("<Button-1>",lambda e: popup("SBCP","PR",
														Info.SBCP.PR.IP, 
														Info.SBCP.PR.Porta, 
														Info.SBCP.PR.NumeroRep, 
														Info.SBCP.PR.Responsavel, 
														Info.SBCP.PR.Telefone))

		self.botaoSBCPPRRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPPRRelogio                  		["text"]       = "R"
		self.botaoSBCPPRRelogio                  		["background"] = Info.SBCP.PR.RelogioCor
		self.botaoSBCPPRRelogio                  		["height"]     = 1
		self.botaoSBCPPRRelogio                  		["width"]      = 1


		self.botaoSBCPPR.grid                    		(row=10,column=0,sticky = "N")
		self.botaoSBCPPRRelogio.grid             		(row=10,column=1,sticky = "N")








		self.botaoSBCPPE                         		= Button(self.ContainerSBCP)
		self.botaoSBCPPE                         		["text"]       = "PE"
		self.botaoSBCPPE                         		["background"] = Info.SBCP.PE.ModuloCor
		self.botaoSBCPPE                         		["width"]      = 13
		self.botaoSBCPPE                         		["height"]     = 1
		self.botaoSBCPPE.bind                    		("<Button-1>",lambda e: popup("SBCP","PE",
														Info.SBCP.PE.IP, 
														Info.SBCP.PE.Porta, 
														Info.SBCP.PE.NumeroRep, 
														Info.SBCP.PE.Responsavel, 
														Info.SBCP.PE.Telefone))

		self.botaoSBCPPERelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPPERelogio                  		["text"]       = "R"
		self.botaoSBCPPERelogio                  		["background"] = Info.SBCP.PE.RelogioCor
		self.botaoSBCPPERelogio                  		["height"]     = 1
		self.botaoSBCPPERelogio                  		["width"]      = 1


		self.botaoSBCPPE.grid                    		(row=11,column=0,sticky = "N")
		self.botaoSBCPPERelogio.grid             		(row=11,column=1,sticky = "N")








		self.botaoSBCPMG                         		= Button(self.ContainerSBCP)
		self.botaoSBCPMG                         		["text"]       = "MG"
		self.botaoSBCPMG                         		["background"] = Info.SBCP.MG.ModuloCor
		self.botaoSBCPMG                         		["width"]      = 13
		self.botaoSBCPMG                         		["height"]     = 1
		self.botaoSBCPMG.bind                    		("<Button-1>",lambda e: popup("SBCP","MG",
														Info.SBCP.MG.IP, 
														Info.SBCP.MG.Porta, 
														Info.SBCP.MG.NumeroRep, 
														Info.SBCP.MG.Responsavel, 
														Info.SBCP.MG.Telefone))

		self.botaoSBCPMGRelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPMGRelogio                  		["text"]       = "R"
		self.botaoSBCPMGRelogio                  		["background"] = Info.SBCP.MG.RelogioCor
		self.botaoSBCPMGRelogio                  		["height"]     = 1
		self.botaoSBCPMGRelogio                  		["width"]      = 1


		self.botaoSBCPMG.grid                    		(row=12,column=0,sticky = "N")
		self.botaoSBCPMGRelogio.grid             		(row=12,column=1,sticky = "N")








		self.botaoSBCPGO                         		= Button(self.ContainerSBCP)
		self.botaoSBCPGO                         		["text"]       = "GO"
		self.botaoSBCPGO                         		["background"] = Info.SBCP.GO.ModuloCor
		self.botaoSBCPGO                         		["width"]      = 13
		self.botaoSBCPGO                         		["height"]     = 1
		self.botaoSBCPGO.bind                    		("<Button-1>",lambda e: popup("SBCP","GO",
														Info.SBCP.GO.IP, 
														Info.SBCP.GO.Porta, 
														Info.SBCP.GO.NumeroRep, 
														Info.SBCP.GO.Responsavel, 
														Info.SBCP.GO.Telefone))

		self.botaoSBCPGORelogio                  		= Button(self.ContainerSBCP)
		self.botaoSBCPGORelogio                  		["text"]       = "R"
		self.botaoSBCPGORelogio                  		["background"] = Info.SBCP.GO.RelogioCor
		self.botaoSBCPGORelogio                  		["height"]     = 1
		self.botaoSBCPGORelogio                  		["width"]      = 1


		self.botaoSBCPGO.grid                    		(row=13,column=0,sticky = "N")
		self.botaoSBCPGORelogio.grid             		(row=13,column=1,sticky = "N")




	def Create_ContainerGeral(self,root):

		self.ContainerRelogios		      = Frame (root)
		self.ContainerRelogios.grid               (row=0, sticky = N + S + E + W)



	def Create_ContainerColuna0(self,root):


		self.ContainerColuna0             			= Frame (self.ContainerRelogios)
		self.ContainerBuilding           			= Frame (self.ContainerColuna0)
		self.ContainerCasaCristo          			= Frame (self.ContainerColuna0)
		self.ContainerBestInClass         			= Frame (self.ContainerColuna0)
		self.ContainerIsoRadio			  			= Frame (self.ContainerColuna0)


		self.ContainerColuna0.grid                	(row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerBuilding.grid               	(row=0, column=0,pady=5, padx=1, columnspan=1 ,sticky="N")
		self.ContainerCasaCristo.grid             	(row=1, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerBestInClass.grid            	(row=2, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerIsoRadio.grid               	(row=3, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna1(self,root):


		self.ContainerColuna1             			= Frame (self.ContainerRelogios)
		self.ContainerLaser               			= Frame (self.ContainerColuna1)
		self.ContainerLotten              			= Frame (self.ContainerColuna1)
		self.ContainerGrupoNk             			= Frame (self.ContainerColuna1)


		self.ContainerColuna1.grid                	(row=0, column=1,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerLaser.grid                  	(row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerLotten.grid                 	(row=2, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerGrupoNk.grid                 	(row=3, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna2(self,root):


		self.ContainerColuna2             = Frame (self.ContainerRelogios)
		self.ContainerGravex              = Frame (self.ContainerColuna2)
		self.ContainerSBCP				  = Frame (self.ContainerColuna2)

		self.ContainerColuna2.grid                	(row=0, column=2,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerGravex.grid                 	(row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerSBCP.grid 					(row=1, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna3(self,root):


		self.ContainerColuna3             = Frame (self.ContainerRelogios)
		self.ContainerPredman             = Frame (self.ContainerColuna3)

		self.ContainerColuna3.grid                (row=0, column=3,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerPredman.grid                (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna4(self,root):


		self.ContainerColuna4             = Frame (self.ContainerRelogios)
		self.ContainerTarek               = Frame (self.ContainerColuna4)


		self.ContainerColuna4.grid                (row=0, column=4,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerTarek.grid                  (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna5(self,root):


		self.ContainerColuna5             = Frame (self.ContainerRelogios)
		self.ContainerMilenioErvas        = Frame (self.ContainerColuna5)


		self.ContainerColuna5.grid                (row=0, column=5,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerMilenioErvas.grid           (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna6(self,root):


		self.ContainerColuna6             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna6)


		self.ContainerColuna6.grid                (row=0, column=6,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna7(self,root):

		self.ContainerColuna7             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna7)

		self.ContainerColuna7.grid                (row=0, column=7,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna8(self,root):


		self.ContainerColuna8             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna8)
		

		self.ContainerColuna8.grid                (row=0, column=8,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna9(self,root):

		self.ContainerColuna9             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna9)
		

		self.ContainerColuna9.grid                (row=0, column=9,pady=5, padx=1, columnspan=1, sticky="N")

		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna10(self,root):

	
		self.ContainerColuna10             = Frame (self.ContainerRelogios)
		
		self.ContainerUniman              = Frame (self.ContainerColuna10)

		self.ContainerColuna10.grid                (row=0, column=10,pady=5, padx=1, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna11(self,root):


		self.ContainerColuna11             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna11)
		

		self.ContainerColuna11.grid                (row=0, column=11,pady=5, padx=1, columnspan=1, sticky="N")

		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_container(self,root):


		self.Create_ContainerGeral(root)

		self.Create_ContainerColuna0(root)

		self.Create_ContainerColuna1(root)

		self.Create_ContainerColuna2(root)

		self.Create_ContainerColuna3(root)

		self.Create_ContainerColuna4(root)

		self.Create_ContainerColuna5(root)

		self.Create_ContainerColuna6(root)

		self.Create_ContainerColuna7(root)

		self.Create_ContainerColuna8(root)

		self.Create_ContainerColuna9(root)

		self.Create_ContainerColuna10(root)

		self.Create_ContainerColuna11(root)








	def updateLaser2(self, relogio):

		if relogio == "instituto":
		
			self.botaoAcademia.configure                    		(bg=Info.Laser.Academia.ModuloCor)
			self.botaoRAcademia.configure                    		(bg=Info.Laser.Academia.RelogioCor)


		if relogio == "academia":

			self.botaoInstituto.configure                    		(bg=Info.Laser.Instituto.ModuloCor)
			self.botaoRInstituto.configure                   		(bg=Info.Laser.Instituto.RelogioCor)

		self.msgLaserContage.configure								(text=str(Info.Laser.Status.Contage)+"/"+
																	str(Info.Laser.Status.TotalRelogios)								)



	def updateLaser(self):

			
		self.botaoAcademia.configure                    		(bg=Info.Laser.Academia.ModuloCor)
		self.botaoRAcademia.configure                    		(bg=Info.Laser.Academia.RelogioCor)


		self.botaoInstituto.configure                    		(bg=Info.Laser.Instituto.ModuloCor)
		self.botaoRInstituto.configure                   		(bg=Info.Laser.Instituto.RelogioCor)



	def updateBuilding(self, relogio):
		if relogio == "allianz":	
			
			self.botaoBuildingAllianz.configure                  	(bg=Info.Building.Allianz.ModuloCor)
			self.botaoBuildingAllianzRelogio.configure           	(bg=Info.Building.Allianz.RelogioCor)

		elif relogio == "wtorre":
			
			self.botaoBuildingWTorre.configure                   	(bg=Info.Building.WTorre.ModuloCor)
			self.botaoBuildingWTorreRelogio.configure            	(bg=Info.Building.WTorre.RelogioCor)

		elif relogio == "riojaneiro":

			self.botaoBuildingRioJaneiro.configure               	(bg=Info.Building.RioJaneiro.ModuloCor)
			self.botaoBuildingRioJaneiroRelogio.configure        	(bg=Info.Building.RioJaneiro.RelogioCor)

		self.msgBuildingCont.configure								(text=str(Info.Building.Status.Contage)+"/"+
																	str(Info.Building.Status.TotalRelogios)								)



	def updateGravex(self, relogio):
		if relogio == "adm":


			self.botaoGravexADM.configure 							(bg=Info.Gravex.ADM.ModuloCor)
			self.botaoGravexADMRelogio.configure 					(bg=Info.Gravex.ADM.RelogioCor)


		elif relogio == "loja":

			self.botaoGravexLoja.configure							(bg=Info.Gravex.Loja1.ModuloCor)
			self.botaoGravexLojaRelogio.configure 					(bg=Info.Gravex.Loja1.RelogioCor)
		

		elif relogio == "mimarcos":

			self.botaoGravexMiMarcos.configure						(bg=Info.Gravex.MiMarcos.ModuloCor)
			self.botaoGravexMiMarcosRelogio.configure 				(bg=Info.Gravex.MiMarcos.RelogioCor)


		elif relogio == "dantchini":


			self.botaoGravexDantChini.configure						(bg=Info.Gravex.DantChini.ModuloCor)
			self.botaoGravexDantChiniRelogio.configure 				(bg=Info.Gravex.DantChini.RelogioCor)



	def updateGrupoNk(self, relogio):
		if relogio == "nelson":

			self.botaoGrupoNkNelsonKioshi.configure               		(bg=Info.GrupoNk.NelsonKioshi.ModuloCor)
			self.botaoGrupoNkNelsonKioshiRelogio.configure        		(bg=Info.GrupoNk.NelsonKioshi.RelogioCor)

		elif relogio == "furukawa":

			self.botaoGrupoNkRDFurukawa.configure               		(bg=Info.GrupoNk.RDFurukawa.ModuloCor)
			self.botaoGrupoNkRDFurukawaRelogio.configure        		(bg=Info.GrupoNk.RDFurukawa.RelogioCor)

		elif relogio == "kio1":

			self.botaoGrupoNkKio1.configure               				(bg=Info.GrupoNk.Kio1.ModuloCor)
			self.botaoGrupoNkKio1Relogio.configure        				(bg=Info.GrupoNk.Kio1.RelogioCor)

		elif relogio == "kio2":

			self.botaoGrupoNkKio2.configure               				(bg=Info.GrupoNk.Kio2.ModuloCor)
			self.botaoGrupoNkKio2Relogio.configure        				(bg=Info.GrupoNk.Kio2.RelogioCor)


		elif relogio == "granjaviana":

			self.botaoGrupoNkGranjaViana.configure               		(bg=Info.GrupoNk.GranjaViana.ModuloCor)
			self.botaoGrupoNkGranjaVianaRelogio.configure        		(bg=Info.GrupoNk.GranjaViana.RelogioCor)

		elif relogio == "santacecilia":

			self.botaoGrupoNkSantaCecilia.configure               		(bg=Info.GrupoNk.SantaCecilia.ModuloCor)
			self.botaoGrupoNkSantaCeciliaRelogio.configure        		(bg=Info.GrupoNk.SantaCecilia.RelogioCor)

		elif relogio == "transfruit":

			self.botaoGrupoNkTransfruit.configure               		(bg=Info.GrupoNk.Transfruit.ModuloCor)
			self.botaoGrupoNkTransfruitRelogio.configure        		(bg=Info.GrupoNk.Transfruit.RelogioCor)

		elif relogio == "distrdefrutas":

			self.botaoGrupoNkDistribuidora.configure               		(bg=Info.GrupoNk.Distribuidora.ModuloCor)
			self.botaoGrupoNkDistribuidoraRelogio.configure        		(bg=Info.GrupoNk.Distribuidora.RelogioCor)

		elif relogio == "nkhortifruit":

			self.botaoGrupoNkNKFilial.configure               			(bg=Info.GrupoNk.NKFilial.ModuloCor)
			self.botaoGrupoNkNKFilialRelogio.configure        			(bg=Info.GrupoNk.NKFilial.RelogioCor)

		self.msgGrupoNkContage.configure								(text=str(Info.GrupoNk.Status.Contage)+"/"+
																	str(Info.GrupoNk.Status.TotalRelogios)								)



	def updateLotten(self, relogio):

		if relogio == "sfjardins":

			self.botaoLottenJardins.configure               		(bg=Info.Lotten.Jardins.ModuloCor)
			self.botaoLottenJardinsRelogio.configure        		(bg=Info.Lotten.Jardins.RelogioCor)	

		elif relogio == "alphaville":

			self.botaoLottenAlphaville.configure               		(bg=Info.Lotten.Alphaville.ModuloCor)
			self.botaoLottenAlphavilleRelogio.configure        		(bg=Info.Lotten.Alphaville.RelogioCor)	

		elif relogio == "osasco":

			self.botaoLottenOsasco.configure               			(bg=Info.Lotten.Osasco.ModuloCor)
			self.botaoLottenOsascoRelogio.configure        			(bg=Info.Lotten.Osasco.RelogioCor)	

		elif relogio == "santana":

			self.botaoLottenSantana.configure               		(bg=Info.Lotten.Santana.ModuloCor)
			self.botaoLottenSantanaRelogio.configure        		(bg=Info.Lotten.Santana.RelogioCor)	

		elif relogio == "tatuape":

			self.botaoLottenTatuape.configure               		(bg=Info.Lotten.Tatuape.ModuloCor)
			self.botaoLottenTatuapeRelogio.configure        		(bg=Info.Lotten.Tatuape.RelogioCor)	

		elif relogio == "moema":

			self.botaoLottenMoema.configure               			(bg=Info.Lotten.Moema.ModuloCor)
			self.botaoLottenMoemaRelogio.configure        			(bg=Info.Lotten.Moema.RelogioCor)	

		elif relogio == "jardimsul":

			self.botaoLottenJardimSul.configure               		(bg=Info.Lotten.JardimSul.ModuloCor)
			self.botaoLottenJardimSulRelogio.configure        		(bg=Info.Lotten.JardimSul.RelogioCor)	

		elif relogio == "conceicao":

			self.botaoLottenConceicao.configure               		(bg=Info.Lotten.Conceicao.ModuloCor)
			self.botaoLottenConceicaoRelogio.configure        		(bg=Info.Lotten.Conceicao.RelogioCor)	


		elif relogio == "lapa":

			self.botaoLottenLapa.configure               			(bg=Info.Lotten.Lapa.ModuloCor)
			self.botaoLottenLapaRelogio.configure        			(bg=Info.Lotten.Lapa.RelogioCor)	


		elif relogio == "perdizes":

			self.botaoLottenPerdizes.configure               		(bg=Info.Lotten.Perdizes.ModuloCor)
			self.botaoLottenPerdizesRelogio.configure        		(bg=Info.Lotten.Perdizes.RelogioCor)


		elif relogio == "saocaetano":

			self.botaoLottenSaoCaetano.configure               		(bg=Info.Lotten.SaoCaetano.ModuloCor)
			self.botaoLottenSaoCaetanoRelogio.configure        		(bg=Info.Lotten.SaoCaetano.RelogioCor)	

		elif relogio == "pinheiros":

			self.botaoLottenPinheiros.configure               		(bg=Info.Lotten.Pinheiros.ModuloCor)
			self.botaoLottenPinheirosRelogio.configure        		(bg=Info.Lotten.Pinheiros.RelogioCor)	

		elif relogio == "morumbi":

			self.botaoLottenMorumbi.configure               		(bg=Info.Lotten.Morumbi.ModuloCor)
			self.botaoLottenMorumbiRelogio.configure        		(bg=Info.Lotten.Morumbi.RelogioCor)	

		elif relogio == "berrini":

			self.botaoLottenBerrini.configure               		(bg=Info.Lotten.Berrini.ModuloCor)
			self.botaoLottenBerriniRelogio.configure        		(bg=Info.Lotten.Berrini.RelogioCor)	

		elif relogio == "vilamariana":

			self.botaoLottenVilaMariana.configure               	(bg=Info.Lotten.VilaMariana.ModuloCor)
			self.botaoLottenVilaMarianaRelogio.configure        	(bg=Info.Lotten.VilaMariana.RelogioCor)	

		elif relogio == "vilaolimpia":

			self.botaoLottenVilaOlimpia.configure               	(bg=Info.Lotten.VilaOlimpia.ModuloCor)
			self.botaoLottenVilaOlimpiaRelogio.configure        	(bg=Info.Lotten.VilaOlimpia.RelogioCor)	


		elif relogio == "itaim":

			self.botaoLottenItaim.configure               			(bg=Info.Lotten.Itaim.ModuloCor)
			self.botaoLottenItaimRelogio.configure        			(bg=Info.Lotten.Itaim.RelogioCor)	


		elif relogio == "garulhos":

			self.botaoLottenGuarulhos.configure               		(bg=Info.Lotten.Guarulhos.ModuloCor)
			self.botaoLottenGuarulhosRelogio.configure        		(bg=Info.Lotten.Guarulhos.RelogioCor)	

		self.msgLottenContage.configure								(text=str(Info.Lotten.Status.Contage)+"/"+
																	str(Info.Lotten.Status.TotalRelogios))



	def updateCasaCristo(self, relogio):

		if relogio == "adm":

			self.botaoCasaCristoADM.configure               		(bg=Info.CasaCristo.ADM.ModuloCor)
			self.botaoCasaCristoADMRelogio.configure        		(bg=Info.CasaCristo.ADM.RelogioCor)

		elif relogio == "cei1":

			self.botaoCasaCristoCEI1.configure               		(bg=Info.CasaCristo.CEI1.ModuloCor)
			self.botaoCasaCristoCEI1Relogio.configure        		(bg=Info.CasaCristo.CEI1.RelogioCor)

		elif relogio == "cei2":

			self.botaoCasaCristoCEI2.configure               		(bg=Info.CasaCristo.CEI2.ModuloCor)
			self.botaoCasaCristoCEI2Relogio.configure        		(bg=Info.CasaCristo.CEI2.RelogioCor)

		elif relogio == "cei3":

			self.botaoCasaCristoCEI3.configure               		(bg=Info.CasaCristo.CEI3.ModuloCor)
			self.botaoCasaCristoCEI3Relogio.configure        		(bg=Info.CasaCristo.CEI3.RelogioCor)

		elif relogio == "vovomatilde":

			self.botaoCasaCristoVMatilde.configure               	(bg=Info.CasaCristo.VovoMatilde.ModuloCor)
			self.botaoCasaCristoVMatildeRelogio.configure        	(bg=Info.CasaCristo.VovoMatilde.RelogioCor)

		self.msgCasaCristoContage.configure							(text=str(Info.CasaCristo.Status.Contage)+"/"+
																	str(Info.CasaCristo.Status.TotalRelogios))	



	def updateBestInClass(self, relogio):

		if relogio == "recife":

			self.botaoBestInClassRecife.configure					(bg=Info.BestInClass.Recife.ModuloCor)
			self.botaoBestInClassRecifeRelogio.configure			(bg=Info.BestInClass.Recife.RelogioCor)
			

		elif relogio == "itaquera":

			self.botaoBestInClassItaquera.configure					(bg=Info.BestInClass.Itaquera.ModuloCor)
			self.botaoBestInClassItaqueraRelogio.configure			(bg=Info.BestInClass.Itaquera.RelogioCor)

		elif relogio == "itapevi":

			self.botaoBestInClassItapevi.configure					(bg=Info.BestInClass.Itapevi.ModuloCor)
			self.botaoBestInClassItapeviRelogio.configure			(bg=Info.BestInClass.Itapevi.RelogioCor)


		elif relogio == "sorocaba":

			self.botaoBestInClassSorocaba.configure					(bg=Info.BestInClass.Sorocaba.ModuloCor)
			self.botaoBestInClassSorocabaRelogio.configure			(bg=Info.BestInClass.Sorocaba.RelogioCor)


		elif relogio == "setelagoas":


			self.botaoBestInClassSeteLagoas.configure				(bg=Info.BestInClass.SeteLagoas.ModuloCor)
			self.botaoBestInClassSeteLagoasRelogio.configure		(bg=Info.BestInClass.SeteLagoas.RelogioCor)


		elif relogio == "curitiba":

			
			self.botaoBestInClassCuritiba.configure					(bg=Info.BestInClass.Curitiba.ModuloCor)
			self.botaoBestInClassCuritibaRelogio.configure			(bg=Info.BestInClass.Curitiba.RelogioCor)


		elif relogio == "fsant":

			self.botaoBestInClassSFsat.configure					(bg=Info.BestInClass.Fsantana.ModuloCor)
			self.botaoBestInClassSFsatRelogio.configure				(bg=Info.BestInClass.Fsantana.RelogioCor)


		elif relogio == "itu":

			self.botaoBestInClassItu.configure						(bg=Info.BestInClass.Itu.ModuloCor)
			self.botaoBestInClassItuRelogio.configure				(bg=Info.BestInClass.Itu.RelogioCor)
			
		elif relogio == "guarulhos":

			self.botaoBestInClassGuarulhos.configure				(bg=Info.BestInClass.Guarulhos.ModuloCor)
			self.botaoBestInClassGuarulhosRelogio.configure			(bg=Info.BestInClass.Guarulhos.RelogioCor)

		elif relogio == "itaporanga":

			self.botaoBestInClassItaporanga.configure				(bg=Info.BestInClass.Itaporanga.ModuloCor)
			self.botaoBestInClassItaporangaRelogio.configure		(bg=Info.BestInClass.Itaporanga.RelogioCor)


		elif relogio == "linhares":

			self.botaoBestInClassLinhares.configure					(bg=Info.BestInClass.Linhares.ModuloCor)
			self.botaoBestInClassLinharesRelogio.configure			(bg=Info.BestInClass.Linhares.RelogioCor)

		self.msgBestInClassCont.configure 							(text=str(Info.BestInClass.Status.Contage)+"/"+
																	str(Info.BestInClass.Status.TotalRelogios))



	def updateIsoRadio(self, relogio):

		if relogio == "santana":

			self.botaoIsoRadioSantana.configure						(bg=Info.IsoRadio.Santana.ModuloCor)
			self.botaoIsoRadioSantanaRelogio.configure				(bg=Info.IsoRadio.Santana.RelogioCor)
			

		elif relogio == "saomatheus":

			self.botaoIsoRadioSaoMatheus.configure					(bg=Info.IsoRadio.SaoMatheus.ModuloCor)
			self.botaoIsoRadioSaoMatheusRelogio.configure			(bg=Info.IsoRadio.SaoMatheus.RelogioCor)

		elif relogio == "vilamariana":

			self.botaoIsoRadioVMariana.configure					(bg=Info.IsoRadio.VilaMariana.ModuloCor)
			self.botaoIsoRadioVMarianaRelogio.configure				(bg=Info.IsoRadio.VilaMariana.RelogioCor)

		elif relogio == "lapa":

			self.botaoIsoRadioLapa.configure						(bg=Info.IsoRadio.Lapa.ModuloCor)
			self.botaoIsoRadioLapaRelogio.configure					(bg=Info.IsoRadio.Lapa.RelogioCor)


		elif relogio == "santoamaro":

			self.botaoIsoRadioSAmaro.configure						(bg=Info.IsoRadio.SAmaro.ModuloCor)
			self.botaoIsoRadioSAmaroRelogio.configure				(bg=Info.IsoRadio.SAmaro.RelogioCor)


		elif relogio == "cidadedutra":

			self.botaoIsoRadioCDutra.configure						(bg=Info.IsoRadio.CDutra.ModuloCor)
			self.botaoIsoRadioCDutraRelogio.configure				(bg=Info.IsoRadio.CDutra.RelogioCor)

		elif relogio == "tatuape":

			self.botaoIsoRadioTatuape.configure						(bg=Info.IsoRadio.Tatuape.ModuloCor)
			self.botaoIsoRadioTatuapeRelogio.configure				(bg=Info.IsoRadio.Tatuape.RelogioCor)

		elif relogio == "campolimpo":

			self.botaoIsoRadioCLimpo.configure						(bg=Info.IsoRadio.CLimpo.ModuloCor)
			self.botaoIsoRadioCLimpoRelogio.configure				(bg=Info.IsoRadio.CLimpo.RelogioCor)


		elif relogio == "ipiranga":

			self.botaoIsoRadioIpiranga.configure					(bg=Info.IsoRadio.Ipiranga.ModuloCor)
			self.botaoIsoRadioIpirangaRelogio.configure				(bg=Info.IsoRadio.Ipiranga.RelogioCor)

		elif relogio == "anarosa":

			self.botaoIsoRadioAnaRosa.configure						(bg=Info.IsoRadio.AnaRosa.ModuloCor)
			self.botaoIsoRadioAnaRosaRelogio.configure				(bg=Info.IsoRadio.AnaRosa.RelogioCor)

		self.msgIsoRadCont.configure	  						(text=str(Info.IsoRadio.Status.Contage)+"/"+
																str(Info.IsoRadio.Status.TotalRelogios))


	def updateSBCP(self, relogio):


		if relogio == "nacional":

			self.botaoSBCPNacional.configure						(bg=Info.SBCP.Nacional.ModuloCor)
			self.botaoSBCPNacionalRelogio.configure					(bg=Info.SBCP.Nacional.RelogioCor)


		elif relogio == "es":

			self.botaoSBCPES.configure								(bg=Info.SBCP.ES.ModuloCor)
			self.botaoSBCPESRelogio.configure						(bg=Info.SBCP.ES.RelogioCor)



		elif relogio == "df":

			self.botaoSBCPDF.configure								(bg=Info.SBCP.DF.ModuloCor)
			self.botaoSBCPDFRelogio.configure						(bg=Info.SBCP.DF.RelogioCor)



		elif relogio == "ce":

			self.botaoSBCPCE.configure								(bg=Info.SBCP.CE.ModuloCor)
			self.botaoSBCPCERelogio.configure						(bg=Info.SBCP.CE.RelogioCor)



		elif relogio == "ba":

			self.botaoSBCPBA.configure								(bg=Info.SBCP.BA.ModuloCor)
			self.botaoSBCPBARelogio.configure						(bg=Info.SBCP.BA.RelogioCor)



		elif relogio == "sp":

			self.botaoSBCPSP.configure								(bg=Info.SBCP.SP.ModuloCor)
			self.botaoSBCPSPRelogio.configure						(bg=Info.SBCP.SP.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPSC.configure								(bg=Info.SBCP.SC.ModuloCor)
			self.botaoSBCPSCRelogio.configure						(bg=Info.SBCP.SC.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPRS.configure								(bg=Info.SBCP.RS.ModuloCor)
			self.botaoSBCPRSRelogio.configure						(bg=Info.SBCP.RS.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPRJ.configure								(bg=Info.SBCP.RJ.ModuloCor)
			self.botaoSBCPRJRelogio.configure						(bg=Info.SBCP.RJ.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPPR.configure								(bg=Info.SBCP.PR.ModuloCor)
			self.botaoSBCPPRRelogio.configure						(bg=Info.SBCP.PR.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPPE.configure								(bg=Info.SBCP.PE.ModuloCor)
			self.botaoSBCPPERelogio.configure						(bg=Info.SBCP.PE.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPMG.configure								(bg=Info.SBCP.MG.ModuloCor)
			self.botaoSBCPMGRelogio.configure						(bg=Info.SBCP.MG.RelogioCor)



		elif relogio == "nacional":

			self.botaoSBCPGO.configure								(bg=Info.SBCP.GO.ModuloCor)
			self.botaoSBCPGORelogio.configure						(bg=Info.SBCP.GO.RelogioCor)




		

	def update(self,empresa,relogio):


		if empresa == "laser":
			self.updateLaser2(relogio)



		elif empresa == "building":
			self.updateBuilding(relogio)
		


		elif empresa == "gravex":
			self.updateBuilding(relogio)
			


		elif empresa == "gruponk":
			self.updateGrupoNk(relogio)

			
			
		elif empresa == "lotten":
			self.updateLotten(relogio)



		elif empresa == "casacristo":
			self.updateCasaCristo(relogio)
			


		elif empresa == "bestinclass":
			self.updateBestInClass(relogio)			



		elif empresa == "isoradiologia":
			self.updateIsoRadio(relogio)


			
