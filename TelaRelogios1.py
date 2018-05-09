

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

		self.Create_ElRio()

		self.Create_Olimpark()

		self.Create_Fancold1()


	def Create_IsoRadio(self):

		self.msgIsoRad 									= Label (self.ContainerIsoRadio,text = "Iso Radiologia", font = "arialblack 12 bold",bg="black",fg="white")
		self.msgIsoRad 									["height"] = 1
		self.msgIsoRad.grid 							(row=0,column=0,sticky = "N")



		self.botaoIsoRadAtencao                                        = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadAtencao                         ["text"]       = "A"
		self.botaoIsoRadAtencao                         ["height"]     = 1
		self.botaoIsoRadAtencao                         ["background"] = "green3"
		self.botaoIsoRadAtencao                         ["width"]      = 2

		self.botaoIsoRadAtencao.grid                     (row=0,column=1,sticky = "N")







		self.msgIsoRadCont 								= Label (self.ContainerIsoRadio,text = str(Info.IsoRadio.Status.Contage)+"/"
																			+str(Info.IsoRadio.Status.TotalRelogios),font="arial 11",bg="black",fg="white")
		self.msgIsoRadCont 								["height"] = 1
		self.msgIsoRadCont.grid 						(row=1,column=1,pady=3.5,sticky = "N")


		self.msgIsoRadHora = Label (self.ContainerIsoRadio,text = "00:00",font="arial 11",bg="black",fg="white")
																			
		self.msgIsoRadHora.grid(row=1,column=0,pady=3.5, sticky = "N")

		self.botaoIsoRadioSantana                      		           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioSantana.grid         			(row=2, column=0, sticky = "N")

		self.botaoIsoRadioSantanaRelogio                      		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioSantanaRelogio       			["text"]       = "R"
		self.botaoIsoRadioSantanaRelogio       			["background"] = Info.IsoRadio.Santana.RelogioCor
		self.botaoIsoRadioSantanaRelogio       			["width"]      = 2
		self.botaoIsoRadioSantanaRelogio       			["height"]     = 1
		self.botaoIsoRadioSantanaRelogio.grid  			(row=2, column=1, sticky = "N")



		self.botaoIsoRadioSaoMatheus                    	           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioSaoMatheus.grid         		(row=3, column=0, sticky = "N")

		self.botaoIsoRadioSaoMatheusRelogio                    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioSaoMatheusRelogio       		["text"]       = "R"
		self.botaoIsoRadioSaoMatheusRelogio       		["background"] = Info.IsoRadio.SaoMatheus.RelogioCor
		self.botaoIsoRadioSaoMatheusRelogio       		["width"]      = 2
		self.botaoIsoRadioSaoMatheusRelogio       		["height"]     = 1
		self.botaoIsoRadioSaoMatheusRelogio.grid  		(row=3, column=1, sticky = "N")


		self.botaoIsoRadioVMariana                    	               = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioVMariana.grid         		(row=4, column=0, sticky = "N")

		self.botaoIsoRadioVMarianaRelogio                    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioVMarianaRelogio       		["text"]       = "R"
		self.botaoIsoRadioVMarianaRelogio       		["background"] = Info.IsoRadio.VilaMariana.RelogioCor
		self.botaoIsoRadioVMarianaRelogio       		["width"]      = 2
		self.botaoIsoRadioVMarianaRelogio       		["height"]     = 1
		self.botaoIsoRadioVMarianaRelogio.grid  		(row=4, column=1, sticky = "N")






		self.botaoIsoRadioLapa                    	                   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioLapa.grid         			(row=5, column=0, sticky = "N")

		self.botaoIsoRadioLapaRelogio                    		       = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioLapaRelogio       			["text"]       = "R"
		self.botaoIsoRadioLapaRelogio       			["background"] = Info.IsoRadio.Lapa.RelogioCor
		self.botaoIsoRadioLapaRelogio       			["width"]      = 2
		self.botaoIsoRadioLapaRelogio       			["height"]     = 1
		self.botaoIsoRadioLapaRelogio.grid  			(row=5, column=1, sticky = "N")






		self.botaoIsoRadioSAmaro                    		           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioSAmaro.grid         			(row=6, column=0, sticky = "N")

		self.botaoIsoRadioSAmaroRelogio             	       		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioSAmaroRelogio       			["text"]       = "R"
		self.botaoIsoRadioSAmaroRelogio       			["background"] = Info.IsoRadio.SAmaro.RelogioCor
		self.botaoIsoRadioSAmaroRelogio       			["width"]      = 2
		self.botaoIsoRadioSAmaroRelogio       			["height"]     = 1
		self.botaoIsoRadioSAmaroRelogio.grid  			(row=6, column=1, sticky = "N")






		self.botaoIsoRadioCDutra                    		           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioCDutra.grid         			(row=7, column=0, sticky = "N")

		self.botaoIsoRadioCDutraRelogio                	    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioCDutraRelogio       			["text"]       = "R"
		self.botaoIsoRadioCDutraRelogio       			["background"] = Info.IsoRadio.CDutra.RelogioCor
		self.botaoIsoRadioCDutraRelogio       			["width"]      = 2
		self.botaoIsoRadioCDutraRelogio       			["height"]     = 1
		self.botaoIsoRadioCDutraRelogio.grid  			(row=7, column=1, sticky = "N")






		self.botaoIsoRadioTatuape                   	 	           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioTatuape.grid         			(row=8, column=0, sticky = "N")

		self.botaoIsoRadioTatuapeRelogio                    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioTatuapeRelogio       			["text"]       = "R"
		self.botaoIsoRadioTatuapeRelogio       			["background"] = Info.IsoRadio.Tatuape.RelogioCor
		self.botaoIsoRadioTatuapeRelogio       			["width"]      = 2
		self.botaoIsoRadioTatuapeRelogio       			["height"]     = 1
		self.botaoIsoRadioTatuapeRelogio.grid  			(row=8, column=1, sticky = "N")






		self.botaoIsoRadioCLimpo                    		           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioCLimpo.grid         			(row=9, column=0, sticky = "N")

		self.botaoIsoRadioCLimpoRelogio            	        		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioCLimpoRelogio       			["text"]       = "R"
		self.botaoIsoRadioCLimpoRelogio       			["background"] = Info.IsoRadio.CLimpo.RelogioCor
		self.botaoIsoRadioCLimpoRelogio       			["width"]      = 2
		self.botaoIsoRadioCLimpoRelogio       			["height"]     = 1
		self.botaoIsoRadioCLimpoRelogio.grid  			(row=9, column=1, sticky = "N")





		self.botaoIsoRadioIpiranga                   	 	           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioIpiranga.grid         		(row=10, column=0, sticky = "N")

		self.botaoIsoRadioIpirangaRelogio                    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioIpirangaRelogio       		["text"]       = "R"
		self.botaoIsoRadioIpirangaRelogio       		["background"] = Info.IsoRadio.Ipiranga.RelogioCor
		self.botaoIsoRadioIpirangaRelogio       		["width"]      = 2
		self.botaoIsoRadioIpirangaRelogio       		["height"]     = 1
		self.botaoIsoRadioIpirangaRelogio.grid  		(row=10, column=1, sticky = "N")





		self.botaoIsoRadioAnaRosa                    		           = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
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
		self.botaoIsoRadioAnaRosa.grid         			(row=11, column=0, sticky = "N")

		self.botaoIsoRadioAnaRosaRelogio                    		   = Button(self.ContainerIsoRadio, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoIsoRadioAnaRosaRelogio       			["text"]       = "R"
		self.botaoIsoRadioAnaRosaRelogio       			["background"] = Info.IsoRadio.AnaRosa.RelogioCor
		self.botaoIsoRadioAnaRosaRelogio       			["width"]      = 2
		self.botaoIsoRadioAnaRosaRelogio       			["height"]     = 1
		self.botaoIsoRadioAnaRosaRelogio.grid  			(row=11, column=1, sticky = "N")



	def Create_MilenioErvas(self):


		self.msgMilenioErvas = Label (self.ContainerMilenioErvas,text = "Milenio Ervas")
		self.msgMilenioErvas["height"] = 1
		self.msgMilenioErvas.grid(row=0,column=0,columnspan=2,sticky = "N")




		self.botaoMilenioErvasSBC1620Loja1                             = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC1620Loja1              ["text"]       = "1620 Loja1"
		self.botaoMilenioErvasSBC1620Loja1              ["background"] = Info.MilenioErvas.Loja1.ModuloCor
		self.botaoMilenioErvasSBC1620Loja1               ["width"]      = 13
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
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["width"]      = 2
		self.botaoMilenioErvasSBC1620Loja1Relogio       ["height"]     = 1
		self.botaoMilenioErvasSBC1620Loja1Relogio.grid  (row=1, column=1, sticky = "N")




		self.botaoMilenioErvasSBC692Loja2                               = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC692Loja2                ["text"]       = "SBC692 Loja2"
		self.botaoMilenioErvasSBC692Loja2                ["background"] = Info.MilenioErvas.Loja2.ModuloCor
		self.botaoMilenioErvasSBC692Loja2                 ["width"]      = 13
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
		self.botaoMilenioErvasSBC692Loja2Relogio         ["width"]      = 2
		self.botaoMilenioErvasSBC692Loja2Relogio         ["height"]     = 1
		self.botaoMilenioErvasSBC692Loja2Relogio.grid    (row=2,column=1,sticky = "N")




		self.botaoMilenioErvasSaoMatheus                                = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSaoMatheus                ["text"]       = "Sao Matheus"
		self.botaoMilenioErvasSaoMatheus                ["background"] = Info.MilenioErvas.SaoMatheus.ModuloCor
		self.botaoMilenioErvasSaoMatheus                 ["width"]      = 13
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
		self.botaoMilenioErvasSaoMatheusRelogio         ["width"]      = 2
		self.botaoMilenioErvasSaoMatheusRelogio         ["height"]     =  1
		self.botaoMilenioErvasSaoMatheusRelogio.grid    (row=3,column=1,sticky = "N")





		self.botaoMilenioErvasDiadema                                 = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasDiadema                  ["text"]       = "Diadema"
		self.botaoMilenioErvasDiadema                  ["background"] = Info.MilenioErvas.Diadema.ModuloCor
		self.botaoMilenioErvasDiadema                   ["width"]      = 13
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
		self.botaoMilenioErvasDiademaRelogio           ["width"]      = 2
		self.botaoMilenioErvasDiademaRelogio           ["height"]     =  1
		self.botaoMilenioErvasDiademaRelogio.grid      (row=4,column=1,sticky = "N")



	def Create_Gravex(self):


		self.msgGravex                              	= Label (self.ContainerGravex,text = "Gravex", font = "arialblack 12 bold",
															bg="black",fg="white")
		self.msgGravex                              	["height"]     = 1
		self.msgGravex.grid                         	(row=0,column=0,sticky = "N")



		self.msgGravexCount                              = Label (self.ContainerGravex,text = str(Info.Gravex.Status.Contage)+"/"+
																						 str(Info.Gravex.Status.TotalRelogios),
																						 font = "arial 11",bg="black",fg="white")	


		self.msgGravexCount                              ["height"]     = 1
		self.msgGravexCount.grid                         (row=1,column=1,pady=3.5,sticky = "N")



		self.botaoGravexAtencao                                        = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexAtencao                         ["text"]       = "A"
		self.botaoGravexAtencao                         ["height"]     = 1
		self.botaoGravexAtencao                         ["background"] = Info.ElRio.Status.Atencao
		self.botaoGravexAtencao                         ["width"]      = 2

		self.botaoGravexAtencao.grid                     (row=0,column=1,sticky = "N")

		self.msgGravexHora                            		= Label (self.ContainerGravex,
															text =Info.Gravex.Status.Horaultima,font = "arial 11",
																			bg="black",fg="white")
		self.msgGravexHora                            		["height"]     = 1
		self.msgGravexHora.grid                       		(row=1,column=0,pady=3.5,sticky = "N")








		self.botaoGravexADM                         = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexADM                         ["text"]       = "ADM"
		self.botaoGravexADM                         ["background"] = Info.Gravex.ADM.ModuloCor
		self.botaoGravexADM                          ["width"]      = 13
		self.botaoGravexADM                         ["height"]     = 1
		self.botaoGravexADM.bind                    ("<Button-1>",lambda e: popup("Gravex","ADM",
													Info.Gravex.ADM.IP, 
													Info.Gravex.ADM.Porta, 
													Info.Gravex.ADM.NumeroRep, 
													Info.Gravex.ADM.Responsavel, 
													Info.Gravex.ADM.Telefone))

		self.botaoGravexADMRelogio                  = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexADMRelogio                  ["text"]       = "R"
		self.botaoGravexADMRelogio                  ["background"] = Info.Gravex.ADM.RelogioCor
		self.botaoGravexADMRelogio                  ["height"]     = 1
		self.botaoGravexADMRelogio                  ["width"]      = 2


		self.botaoGravexADM.grid                    (row=2,column=0,sticky = "N")
		self.botaoGravexADMRelogio.grid             (row=2,column=1,sticky = "N")




		self.botaoGravexLoja                        = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexLoja                        ["text"]       = "Loja"
		self.botaoGravexLoja                        ["background"] = Info.Gravex.Loja1.ModuloCor
		self.botaoGravexLoja                        ["height"]     = 1
		self.botaoGravexLoja                         ["width"]      = 13
		self.botaoGravexLoja.bind                    ("<Button-1>",lambda e: popup("Gravex","Loja",
													Info.Gravex.Loja1.IP, 
													Info.Gravex.Loja1.Porta, 
													Info.Gravex.Loja1.NumeroRep, 
													Info.Gravex.Loja1.Responsavel, 
													Info.Gravex.Loja1.Telefone))

		self.botaoGravexLojaRelogio                 = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexLojaRelogio                 ["text"]       = "R"
		self.botaoGravexLojaRelogio                 ["background"] = Info.Gravex.Loja1.RelogioCor
		self.botaoGravexLojaRelogio                 ["width"]      = 2
		self.botaoGravexLojaRelogio                 ["height"]     = 1

		self.botaoGravexLoja.grid                   (row=3,column=0,sticky = "N")
		self.botaoGravexLojaRelogio.grid            (row=3,column=1,sticky = "N")






		self.botaoGravexMiMarcos                    = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexMiMarcos                    ["text"]       = "Ministro Marcos"
		self.botaoGravexMiMarcos                    ["background"] = Info.Gravex.MiMarcos.ModuloCor
		self.botaoGravexMiMarcos                    ["height"]     = 1
		self.botaoGravexMiMarcos                     ["width"]      = 13
		self.botaoGravexMiMarcos.bind               ("<Button-1>",lambda e: popup("Gravex","Ministro Marcos",
													Info.Gravex.MiMarcos.IP, 
													Info.Gravex.MiMarcos.Porta, 
													Info.Gravex.MiMarcos.NumeroRep, 
													Info.Gravex.MiMarcos.Responsavel, 
													Info.Gravex.MiMarcos.Telefone))

		self.botaoGravexMiMarcosRelogio             = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexMiMarcosRelogio             ["text"]       = "R"
		self.botaoGravexMiMarcosRelogio             ["background"] = Info.Gravex.MiMarcos.RelogioCor
		self.botaoGravexMiMarcosRelogio             ["height"]     = 1
		self.botaoGravexMiMarcosRelogio             ["width"]      = 2


		self.botaoGravexMiMarcos.grid               (row=4,column=0,sticky = "N")
		self.botaoGravexMiMarcosRelogio.grid        (row=4,column=1,sticky = "N")




		self.botaoGravexDantChini                   = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexDantChini                   ["text"]       = "Danti Chini"
		self.botaoGravexDantChini                   ["background"] = Info.Gravex.DantChini.ModuloCor
		self.botaoGravexDantChini                    ["width"]      = 13
		self.botaoGravexDantChini                   ["height"]     = 1
		self.botaoGravexDantChini.bind              ("<Button-1>",lambda e: popup("Gravex","Danti Chini",
													Info.Gravex.DantChini.IP, 
													Info.Gravex.DantChini.Porta, 
													Info.Gravex.DantChini.NumeroRep, 
													Info.Gravex.DantChini.Responsavel, 
													Info.Gravex.DantChini.Telefone))

		self.botaoGravexDantChiniRelogio            = Button(self.ContainerGravex, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGravexDantChiniRelogio            ["text"]       = "R"
		self.botaoGravexDantChiniRelogio            ["background"] = Info.Gravex.DantChini.RelogioCor
		self.botaoGravexDantChiniRelogio            ["width"]      = 2
		self.botaoGravexDantChiniRelogio            ["height"]     = 1


		self.botaoGravexDantChini.grid              (row=5,column=0,sticky = "N")
		self.botaoGravexDantChiniRelogio.grid       (row=5,column=1,sticky = "N")



	def Create_Laser(self):
		
		hora = "10:30"

		self.msgLaser = Label (self.ContainerLaser,text = "Laser", font = "arialblack 12 bold")
		self.msgLaser["height"]=1
		self.msgLaser.grid(row=0,column=0,sticky = "N")


		self.botaoLaserAtencao                                        = Button(self.ContainerLaser)
		self.botaoLaserAtencao                         ["text"]       = "A"
		self.botaoLaserAtencao                         ["height"]     = 1
		self.botaoLaserAtencao                         ["background"] = "green"
		self.botaoLaserAtencao                         ["width"]      = 2

		self.botaoLaserAtencao.grid                     (row=0,column=1,sticky = "N")
	




		self.msgLaserContage = Label (self.ContainerLaser,text = str(Info.Laser.Status.Contage)+"/"+
																	str(Info.Laser.Status.TotalRelogios)
																	,font="arial 11")
		self.msgLaserContage["height"]=1
		self.msgLaserContage.grid(row=1,column=1,sticky = "N")


		self.msgLaserHora = Label (self.ContainerLaser,text = "00:00",font="arial 11")
																			
		self.msgLaserHora.grid(row=1,column=0, sticky = "N")



		self.botaoAcademia                                         = Button(self.ContainerLaser)
		self.botaoAcademia                          ["text"]       = "Academia"
		self.botaoAcademia                          ["background"] = Info.Laser.Academia.ModuloCor
		self.botaoAcademia                          ["height"]     = 1
		self.botaoAcademia                           ["width"]      = 13
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
		self.botaoRAcademia                         ["width"]      = 2

		self.botaoAcademia.grid                     (row=2,column=0,sticky = "N")
		self.botaoRAcademia.grid                    (row=2,column=1,sticky = "N")


		self.botaoInstituto                                        = Button(self.ContainerLaser)
		self.botaoInstituto                         ["text"]       = "Instituto"
		self.botaoInstituto                         ["background"] = Info.Laser.Instituto.ModuloCor
		self.botaoInstituto                          ["width"]      = 13
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
		self.botaoRInstituto                        ["width"]      = 2
		self.botaoRInstituto                        ["height"]     = 1


		self.botaoInstituto.grid                    (row=3,column=0,sticky = "N")
		self.botaoRInstituto.grid                   (row=3,column=1,sticky = "N")



	def Create_Predman(self):

		self.msgPredman = Label (self.ContainerPredman,text = "Predman",font="arialblack 12 bold",bg="black",fg="white")
		self.msgPredman.grid(row=0,column=0,sticky = "N")


		self.msgPredmancount = Label (self.ContainerPredman,text = str(Info.Predman.Status.Contage)+"/"+
																	str(Info.Predman.Status.TotalRelogios),
																	font="arial 11",bg="black",fg="white")

		self.msgPredmancount.grid(row=1,column=1,pady=3.5,sticky = "N")





		self.botaoPredmanAtencao                                        = Button(self.ContainerPredman,  highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoPredmanAtencao                         ["text"]       = "A"
		self.botaoPredmanAtencao                         ["height"]     = 1
		self.botaoPredmanAtencao                         ["background"] = Info.Predman.Status.Atencao
		self.botaoPredmanAtencao                         ["width"]      = 2

		self.botaoPredmanAtencao.grid                     (row=0,column=1,sticky = "N")






		self.msgPredmanHora = Label (self.ContainerPredman,text = Info.Predman.Status.Horaultima,font="arial 11",bg="black",fg="white")
																			
		self.msgPredmanHora.grid(row=1,column=0,pady=3.5, sticky = "N")
		







		self.botaoPredmanBunge                                   =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoPredmanBunge                     ["text"]       = "Bunge"
		self.botaoPredmanBunge                     ["background"] = Info.Predman.Bunge.ModuloCor
		self.botaoPredmanBunge                      ["width"]      = 13
		self.botaoPredmanBunge                     ["height"]     = 1
		self.botaoPredmanBunge.bind                ("<Button-1>",lambda e: popup("Predman","Bunge",
													Info.Predman.Bunge.IP, 
													Info.Predman.Bunge.Porta, 
													Info.Predman.Bunge.NumeroRep, 
													Info.Predman.Bunge.Responsavel, 
													Info.Predman.Bunge.Telefone))
		self.botaoPredmanBunge.grid                (row=2,column=0,sticky = "N")

		self.botaoPredmanBungeRelogio                             =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanBungeRelogio              ["text"]       = "R"
		self.botaoPredmanBungeRelogio              ["background"] = Info.Predman.Bunge.RelogioCor
		self.botaoPredmanBungeRelogio              ["width"]      = 2
		self.botaoPredmanBungeRelogio              ["height"]     = 1
		self.botaoPredmanBungeRelogio.grid         (row=2,column=1,sticky = "N")




		self.botaoPredmanCabot                                    =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanCabot                     ["text"]       = "Cabot"
		self.botaoPredmanCabot                     ["background"] = Info.Predman.Cabot.ModuloCor
		self.botaoPredmanCabot                      ["width"]      = 13
		self.botaoPredmanCabot                     ["height"]     = 1
		self.botaoPredmanCabot.bind                ("<Button-1>",lambda e: popup("Predman","Cabot",
										 			Info.Predman.Cabot.IP, 
													Info.Predman.Cabot.Porta, 
													Info.Predman.Cabot.NumeroRep, 
													Info.Predman.Cabot.Responsavel, 
													Info.Predman.Cabot.Telefone))
		self.botaoPredmanCabot.grid                (row=3,column=0,sticky = "N")

		self.botaoPredmanCabotRelogio                             =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanCabotRelogio              ["text"]       = "R"
		self.botaoPredmanCabotRelogio              ["background"] = Info.Predman.Cabot.RelogioCor
		self.botaoPredmanCabotRelogio              ["width"]      = 2
		self.botaoPredmanCabotRelogio              ["height"]     = 1		
		self.botaoPredmanCabotRelogio.grid         (row=3,column=1,sticky = "N")




		self.botaoPredmanKelloggs                                 =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanKelloggs                  ["text"]       = "Kelloggs"
		self.botaoPredmanKelloggs                  ["background"] = Info.Predman.Kelloggs.ModuloCor
		self.botaoPredmanKelloggs                   ["width"]      = 13
		self.botaoPredmanKelloggs                  ["height"]     = 1
		self.botaoPredmanKelloggs.bind             ("<Button-1>",lambda e: popup("Predman","Kelloggs",
													Info.Predman.Kelloggs.IP, 
													Info.Predman.Kelloggs.Porta, 
													Info.Predman.Kelloggs.NumeroRep, 
													Info.Predman.Kelloggs.Responsavel, 
													Info.Predman.Kelloggs.Telefone))
		self.botaoPredmanKelloggs.grid             (row=4,column=0,sticky = "N")

		self.botaoPredmanKelloggsRelogio                          =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanKelloggsRelogio           ["text"]       = "R"
		self.botaoPredmanKelloggsRelogio           ["background"] = Info.Predman.Kelloggs.RelogioCor
		self.botaoPredmanKelloggsRelogio           ["width"]      = 2
		self.botaoPredmanKelloggsRelogio           ["height"]     = 1		
		self.botaoPredmanKelloggsRelogio.grid      (row=4,column=1,sticky = "N")




		self.botaoPredmanMagazine                                =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanMagazine                 ["text"]       = "Magazine"
		self.botaoPredmanMagazine                 ["background"] = Info.Predman.Magazine.ModuloCor
		self.botaoPredmanMagazine                  ["width"]      = 13
		self.botaoPredmanMagazine                 ["height"]     = 1
		self.botaoPredmanMagazine.bind            ("<Button-1>",lambda e: popup("Predman","Magazine",
													Info.Predman.Magazine.IP, 
													Info.Predman.Magazine.Porta, 
													Info.Predman.Magazine.NumeroRep, 
													Info.Predman.Magazine.Responsavel, 
													Info.Predman.Magazine.Telefone))
		self.botaoPredmanMagazine.grid            (row=5,column=0,sticky = "N")

		self.botaoPredmanMagazineRelogio                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanMagazineRelogio          ["text"]       = "R"
		self.botaoPredmanMagazineRelogio          ["background"] = Info.Predman.Magazine.RelogioCor
		self.botaoPredmanMagazineRelogio          ["width"]      = 2
		self.botaoPredmanMagazineRelogio          ["height"]     = 1
		self.botaoPredmanMagazineRelogio.grid     (row=5,column=1,sticky = "N")




		self.botaoPredmanOxiteno1                                =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanOxiteno1                 ["text"]       = "Oxiteno 1"
		self.botaoPredmanOxiteno1                 ["background"] = Info.Predman.Oxiteno1.ModuloCor
		self.botaoPredmanOxiteno1                  ["width"]      = 13
		self.botaoPredmanOxiteno1                 ["height"]     = 1
		self.botaoPredmanOxiteno1.bind            ("<Button-1>",lambda e: popup("Predman","Oxiteno 1",
													Info.Predman.Oxiteno1.IP, 
													Info.Predman.Oxiteno1.Porta, 
													Info.Predman.Oxiteno1.NumeroRep, 
													Info.Predman.Oxiteno1.Responsavel, 
													Info.Predman.Oxiteno1.Telefone))
		self.botaoPredmanOxiteno1.grid            (row=6,column=0,sticky = "N")

		self.botaoPredmanOxiteno1Relogio                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanOxiteno1Relogio          ["text"]       = "R"
		self.botaoPredmanOxiteno1Relogio          ["background"] = Info.Predman.Oxiteno1.RelogioCor
		self.botaoPredmanOxiteno1Relogio          ["width"]      = 2
		self.botaoPredmanOxiteno1Relogio          ["height"]     = 1		
		self.botaoPredmanOxiteno1Relogio.grid     (row=6,column=1,sticky = "N")




		self.botaoPredmanOxiteno2                                =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanOxiteno2                 ["text"]       = "Oxiteno 2"
		self.botaoPredmanOxiteno2                 ["background"] = Info.Predman.Oxiteno2.ModuloCor
		self.botaoPredmanOxiteno2                  ["width"]      = 13
		self.botaoPredmanOxiteno2                 ["height"]     = 1
		self.botaoPredmanOxiteno2.bind            ("<Button-1>",lambda e: popup("Predman","Oxiteno 2",
													Info.Predman.Oxiteno2.IP, 
													Info.Predman.Oxiteno2.Porta, 
													Info.Predman.Oxiteno2.NumeroRep, 
													Info.Predman.Oxiteno2.Responsavel, 
													Info.Predman.Oxiteno2.Telefone))
		self.botaoPredmanOxiteno2.grid            (row=7,column=0,sticky = "N")

		self.botaoPredmanOxiteno2Relogio                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanOxiteno2Relogio          ["text"]       = "R"
		self.botaoPredmanOxiteno2Relogio          ["background"] = Info.Predman.Oxiteno2.RelogioCor
		self.botaoPredmanOxiteno2Relogio          ["width"]      = 2
		self.botaoPredmanOxiteno2Relogio          ["height"]     = 1
		self.botaoPredmanOxiteno2Relogio.grid     (row=7,column=1,sticky = "N")





		self.botaoPredmanSantoAndre                                =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantoAndre                 ["text"]       = "Santo Andre"
		self.botaoPredmanSantoAndre                 ["background"] = Info.Predman.SantoAndre.ModuloCor
		self.botaoPredmanSantoAndre                  ["width"]      = 13
		self.botaoPredmanSantoAndre                 ["height"]     = 1
		self.botaoPredmanSantoAndre.bind            ("<Button-1>",lambda e: popup("Predman","Santo Andre",
													Info.Predman.SantoAndre.IP, 
													Info.Predman.SantoAndre.Porta, 
													Info.Predman.SantoAndre.NumeroRep, 
													Info.Predman.SantoAndre.Responsavel, 
													Info.Predman.SantoAndre.Telefone))
		self.botaoPredmanSantoAndre.grid           (row=8,column=0,sticky = "N")

		self.botaoPredmanSantoAndreRelogio                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantoAndreRelogio          ["text"]       = "R"
		self.botaoPredmanSantoAndreRelogio          ["background"] = Info.Predman.SantoAndre.RelogioCor
		self.botaoPredmanSantoAndreRelogio          ["width"]      = 2
		self.botaoPredmanSantoAndreRelogio          ["height"]     = 1
		self.botaoPredmanSantoAndreRelogio.grid      (row=8,column=1,sticky = "N")




		self.botaoPredmanPrysmianES                              =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPrysmianES               ["text"]       = "Prysmian ES"
		self.botaoPredmanPrysmianES               ["background"] = Info.Predman.PrysmianES.ModuloCor
		self.botaoPredmanPrysmianES                ["width"]      = 13
		self.botaoPredmanPrysmianES               ["height"]     = 1
		self.botaoPredmanPrysmianES.bind          ("<Button-1>",lambda e: popup("Predman","Prysmian ES",
													Info.Predman.PrysmianES.IP, 
													Info.Predman.PrysmianES.Porta, 
													Info.Predman.PrysmianES.NumeroRep, 
													Info.Predman.PrysmianES.Responsavel, 
													Info.Predman.PrysmianES.Telefone))
		self.botaoPredmanPrysmianES.grid          (row=9,column=0,sticky = "N")

		self.botaoPredmanPrysmianESRelogio                       =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPrysmianESRelogio        ["text"]       = "R"
		self.botaoPredmanPrysmianESRelogio        ["background"] = Info.Predman.PrysmianES.RelogioCor
		self.botaoPredmanPrysmianESRelogio        ["width"]      = 2
		self.botaoPredmanPrysmianESRelogio        ["height"]     = 1
		self.botaoPredmanPrysmianESRelogio.grid   (row=9,column=1,sticky = "N")




		self.botaoPredmanTradegar                                =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanTradegar                 ["text"]       = "Tradegar"
		self.botaoPredmanTradegar                 ["background"] = Info.Predman.Tradegar.ModuloCor
		self.botaoPredmanTradegar                  ["width"]      = 13
		self.botaoPredmanTradegar                 ["height"]     = 1
		self.botaoPredmanTradegar.bind            ("<Button-1>",lambda e: popup("Predman","Tradegar",
													Info.Predman.Tradegar.IP, 
													Info.Predman.Tradegar.Porta, 
													Info.Predman.Tradegar.NumeroRep, 
													Info.Predman.Tradegar.Responsavel, 
													Info.Predman.Tradegar.Telefone))
		self.botaoPredmanTradegar.grid            (row=10,column=0,sticky = "N")

		self.botaoPredmanTradegarRelogio                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanTradegarRelogio          ["text"]       = "R"
		self.botaoPredmanTradegarRelogio          ["background"] = Info.Predman.Tradegar.RelogioCor
		self.botaoPredmanTradegarRelogio          ["width"]      = 2
		self.botaoPredmanTradegarRelogio          ["height"]     = 1
		self.botaoPredmanTradegarRelogio.grid     (row=10,column=1,sticky = "N")




		self.botaoPredmanPortao1                                 =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPortao1                  ["text"]       = "Sorocaba PP1"
		self.botaoPredmanPortao1                  ["background"] = Info.Predman.Portao1.ModuloCor
		self.botaoPredmanPortao1                   ["width"]      = 13
		self.botaoPredmanPortao1                  ["height"]     = 1
		self.botaoPredmanPortao1.bind             ("<Button-1>",lambda e: popup("Predman","Sorocaba PP1",
													Info.Predman.Portao1.IP, 
													Info.Predman.Portao1.Porta, 
													Info.Predman.Portao1.NumeroRep, 
													Info.Predman.Portao1.Responsavel, 
													Info.Predman.Portao1.Telefone))
		self.botaoPredmanPortao1.grid             (row=11,column=0,sticky = "N")

		self.botaoPredmanPortao1Relogio                          =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPortao1Relogio           ["text"]       = "R"
		self.botaoPredmanPortao1Relogio           ["background"] = Info.Predman.Portao1.RelogioCor
		self.botaoPredmanPortao1Relogio           ["width"]      = 2
		self.botaoPredmanPortao1Relogio           ["height"]     = 1
		self.botaoPredmanPortao1Relogio.grid      (row=11,column=1,sticky = "N")




		self.botaoPredmanPortao2                                 =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPortao2                  ["text"]       = "Sorocaba PP2"
		self.botaoPredmanPortao2                  ["background"] = Info.Predman.Portao2.ModuloCor
		self.botaoPredmanPortao2                   ["width"]      = 13
		self.botaoPredmanPortao2                  ["height"]     = 1
		self.botaoPredmanPortao2.bind             ("<Button-1>",lambda e: popup("Predman","Sorocaba PP2",
												   	  Info.Predman.Portao2.IP, 
													  Info.Predman.Portao2.Porta, 
													  Info.Predman.Portao2.NumeroRep, 
													  Info.Predman.Portao2.Responsavel, 
													  Info.Predman.Portao2.Telefone))
		self.botaoPredmanPortao2.grid             (row=12,column=0,sticky = "N")

		self.botaoPredmanPortao2Relogio                                 =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanPortao2Relogio              ["text"]       = "R"
		self.botaoPredmanPortao2Relogio                  ["background"] = Info.Predman.Portao2.RelogioCor
		self.botaoPredmanPortao2Relogio                  ["width"]      = 2
		self.botaoPredmanPortao2Relogio                  ["height"]     = 1
		self.botaoPredmanPortao2Relogio.grid             (row=12,column=1,sticky = "N")




		self.botaoPredmanSabic                                   =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSabic                    ["text"]       = "Sabic"
		self.botaoPredmanSabic                    ["background"] = Info.Predman.Sabic.ModuloCor
		self.botaoPredmanSabic                     ["width"]      = 13
		self.botaoPredmanSabic                    ["height"]     = 1
		self.botaoPredmanSabic.bind               ("<Button-1>",lambda e: popup("Predman","Sabic",
													Info.Predman.Sabic.IP, 
													Info.Predman.Sabic.Porta, 
													Info.Predman.Sabic.NumeroRep, 
													Info.Predman.Sabic.Responsavel, 
													Info.Predman.Sabic.Telefone))
		self.botaoPredmanSabic.grid                (row=13,column=0,sticky = "N")

		self.botaoPredmanSabicRelogio                            =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSabicRelogio             ["text"]       = "R"
		self.botaoPredmanSabicRelogio             ["background"] = Info.Predman.Sabic.RelogioCor
		self.botaoPredmanSabicRelogio             ["width"]      = 2
		self.botaoPredmanSabicRelogio             ["height"]     = 1
		self.botaoPredmanSabicRelogio.grid        (row=13,column=1,sticky = "N")




		self.botaoPredmanSantherBraganca                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantherBraganca          ["text"]       = "S. Braganca"
		self.botaoPredmanSantherBraganca          ["background"] = Info.Predman.SBraganca.ModuloCor
		self.botaoPredmanSantherBraganca           ["width"]      = 13
		self.botaoPredmanSantherBraganca          ["height"]     = 1
		self.botaoPredmanSantherBraganca.bind     ("<Button-1>",lambda e: popup("Predman","Santher Braganca",
												     	Info.Predman.SBraganca.IP, 
														Info.Predman.SBraganca.Porta, 
														Info.Predman.SBraganca.NumeroRep, 
														Info.Predman.SBraganca.Responsavel, 
														Info.Predman.SBraganca.Telefone))
		self.botaoPredmanSantherBraganca.grid      (row=14,column=0,sticky = "N")

		self.botaoPredmanSantherBragancaRelogio                  =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantherBragancaRelogio   ["text"]       = "R"
		self.botaoPredmanSantherBragancaRelogio   ["background"] = Info.Predman.SBraganca.RelogioCor
		self.botaoPredmanSantherBragancaRelogio   ["width"]      = 2
		self.botaoPredmanSantherBragancaRelogio   ["height"]     = 1
		self.botaoPredmanSantherBragancaRelogio.grid (row=14,column=1,sticky = "N")





		self.botaoPredmanSantherPenha                             =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantherPenha              ["text"]       = "S. Penha"
		self.botaoPredmanSantherPenha              ["background"] = Info.Predman.SPenha.ModuloCor
		self.botaoPredmanSantherPenha               ["width"]      = 13
		self.botaoPredmanSantherPenha              ["height"]     = 1
		self.botaoPredmanSantherPenha.bind         ("<Button-1>",lambda e: popup("Predman","Santher Penha",
												     	Info.Predman.SPenha.IP, 
														Info.Predman.SPenha.Porta, 
														Info.Predman.SPenha.NumeroRep, 
														Info.Predman.SPenha.Responsavel, 
														Info.Predman.SPenha.Telefone))
		self.botaoPredmanSantherPenha.grid         (row=15,column=0,sticky = "N")

		self.botaoPredmanSantherPenhaRelogio                      =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanSantherPenhaRelogio       ["text"]       = "R"
		self.botaoPredmanSantherPenhaRelogio       ["background"] = Info.Predman.SPenha.RelogioCor
		self.botaoPredmanSantherPenhaRelogio       ["width"]      = 2
		self.botaoPredmanSantherPenhaRelogio       ["height"]     = 1
		self.botaoPredmanSantherPenhaRelogio.grid  (row=15,column=1,sticky = "N")





		self.botaoPredmanFaurencia                               =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanFaurencia                ["text"]       = "Faurencia"
		self.botaoPredmanFaurencia                ["background"] = Info.Predman.Faurencia.ModuloCor
		self.botaoPredmanFaurencia                 ["width"]      = 13
		self.botaoPredmanFaurencia                ["height"]     = 1
		self.botaoPredmanFaurencia.bind           ("<Button-1>",lambda e: popup("Predman","Faurencia",
												     	Info.Predman.Faurencia.IP, 
														Info.Predman.Faurencia.Porta, 
														Info.Predman.Faurencia.NumeroRep, 
														Info.Predman.Faurencia.Responsavel, 
														Info.Predman.Faurencia.Telefone))
		self.botaoPredmanFaurencia.grid           (row=16,column=0,sticky = "N")

		self.botaoPredmanFaurenciaRelogio                        =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanFaurenciaRelogio         ["text"]       = "R"
		self.botaoPredmanFaurenciaRelogio         ["background"] = Info.Predman.Faurencia.RelogioCor
		self.botaoPredmanFaurenciaRelogio         ["width"]      = 2
		self.botaoPredmanFaurenciaRelogio         ["height"]     = 1
		self.botaoPredmanFaurenciaRelogio.grid    (row=16,column=1,sticky = "N")





		self.botaoPredmanAdmRondonopolis                         =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanAdmRondonopolis          ["text"]       = "Adm Rond."
		self.botaoPredmanAdmRondonopolis          ["background"] = Info.Predman.AdmRondonopolis.ModuloCor
		self.botaoPredmanAdmRondonopolis           ["width"]      = 13
		self.botaoPredmanAdmRondonopolis          ["height"]     = 1
		self.botaoPredmanAdmRondonopolis.bind     ("<Button-1>",lambda e: popup("Predman","Adm Rondonopolis",
												     	Info.Predman.AdmRondonopolis.IP, 
														Info.Predman.AdmRondonopolis.Porta, 
														Info.Predman.AdmRondonopolis.NumeroRep, 
														Info.Predman.AdmRondonopolis.Responsavel, 
														Info.Predman.AdmRondonopolis.Telefone))
		self.botaoPredmanAdmRondonopolis.grid     (row=17,column=0,sticky = "N")

		self.botaoPredmanAdmRondonopolisRelogio                  =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanAdmRondonopolisRelogio   ["text"]       = "R"
		self.botaoPredmanAdmRondonopolisRelogio   ["background"] = Info.Predman.AdmRondonopolis.RelogioCor
		self.botaoPredmanAdmRondonopolisRelogio   ["width"]      = 2
		self.botaoPredmanAdmRondonopolisRelogio   ["height"]     = 1
		self.botaoPredmanAdmRondonopolisRelogio.grid  (row=17,column=1,sticky = "N")





		self.botaoPredmanVilaVelha                               =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanVilaVelha                ["text"]       = "Vila Velha"
		self.botaoPredmanVilaVelha                ["background"] = Info.Predman.VilaVelha.ModuloCor
		self.botaoPredmanVilaVelha                 ["width"]      = 13
		self.botaoPredmanVilaVelha                ["height"]     = 1
		self.botaoPredmanVilaVelha.bind           ("<Button-1>",lambda e: popup("Predman","Vila Velha",
												     	Info.Predman.VilaVelha.IP, 
														Info.Predman.VilaVelha.Porta, 
														Info.Predman.VilaVelha.NumeroRep, 
														Info.Predman.VilaVelha.Responsavel, 
														Info.Predman.VilaVelha.Telefone))
		self.botaoPredmanVilaVelha.grid           (row=18,column=0,sticky = "N")

		self.botaoPredmanVilaVelhaRelogio                        =  Button(self.ContainerPredman, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
		
		self.botaoPredmanVilaVelhaRelogio         ["text"]       = "R"
		self.botaoPredmanVilaVelhaRelogio         ["background"] = Info.Predman.VilaVelha.RelogioCor
		self.botaoPredmanVilaVelhaRelogio         ["width"]      = 2
		self.botaoPredmanVilaVelhaRelogio         ["height"]     = 1
		self.botaoPredmanVilaVelhaRelogio.grid    (row=18,column=1,sticky = "N")



	def Create_Uniman(self):



		self.msgUniman 									= Label (self.ContainerUniman,
																text = "Uniman",
																font= "arialblack 12 bold",
																bg="black",
																fg="white")



		self.msgUniman 									["height"] = 1

		self.msgUniman.grid 							(row=0,column=0,sticky = "N")



		
		self.msgUnimanContage  							= Label (self.ContainerUniman,
																text = str(Info.Uniman.Status.Contage)+"/"+
																str(Info.Uniman.Status.TotalRelogios),
																font="arial 11",
																bg="black",
																fg="white")

	


		self.botaoUnimanAtencao                      	= Button(self.ContainerUniman, 
														highlightbackground="black",
														activebackground="black",
														activeforeground="white")

		self.botaoUnimanAtencao                         ["text"]       = "A"
		self.botaoUnimanAtencao                         ["height"]     = 1
		self.botaoUnimanAtencao                         ["background"] = Info.Uniman.Status.Atencao
		self.botaoUnimanAtencao                         ["width"]      = 2

		self.botaoUnimanAtencao.grid                     (row=0,column=1,sticky = "N")





		self.msgUnimanContage.grid 						(row=1,column=1,pady=3.5, sticky = "N")



		self.msgUnimanHora  							= Label (self.ContainerUniman,
														text = Info.Uniman.Status.Horaultima,
														font="arial 11",
														bg="black",
														fg="white")
																			
		self.msgUnimanHora.grid 						(row=1,column=0,pady=3.5, sticky = "N")







		relo=Info.Uniman.SaintGobain
		self.botaoUnimanSaintGobain                    	= Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanSaintGobain                   	["text"]       = "Saint Gobain"
		self.botaoUnimanSaintGobain                   	["background"] = relo.ModuloCor
		self.botaoUnimanSaintGobain                  	["width"]      = 13
		self.botaoUnimanSaintGobain                  	["height"]     = 1
		self.botaoUnimanSaintGobain.bind             	("<Button-1>",lambda e: popup(
														"Uniman",
														"Saint Gobain",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))

		self.botaoUnimanSaintGobain.grid              	(row=2, column=0, sticky = "N")

		self.botaoUnimanSaintGobainRelogio                           = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanSaintGobainRelogio            	["text"]       = "R"
		self.botaoUnimanSaintGobainRelogio            	["background"] = relo.RelogioCor
		self.botaoUnimanSaintGobainRelogio            	["width"]      = 2
		self.botaoUnimanSaintGobainRelogio            	["height"]     = 1
		self.botaoUnimanSaintGobainRelogio.grid       	(row=2, column=1, sticky = "N")








		relo=Info.Uniman.PPMSecoia
		self.botaoUnimanPPMSecoia                       = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanPPMSecoia                    	["text"]       = "PPM Secoia"
		self.botaoUnimanPPMSecoia                    	["background"] = relo.ModuloCor
		self.botaoUnimanPPMSecoia                     	["width"]      = 13
		self.botaoUnimanPPMSecoia                    	["height"]     = 1
		self.botaoUnimanPPMSecoia.bind              	("<Button-1>",lambda e: popup(
														"Uniman",
														"PPM Secoia",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoUnimanPPMSecoia.grid               	(row=3,column=0,sticky = "N")


		self.botaoUnimanPPMSecoiaRelogio                = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanPPMSecoiaRelogio             	["text"]       = "R"
		self.botaoUnimanPPMSecoiaRelogio             	["background"] = relo.RelogioCor
		self.botaoUnimanPPMSecoiaRelogio             	["width"]      = 2
		self.botaoUnimanPPMSecoiaRelogio             	["height"]     = 1
		self.botaoUnimanPPMSecoiaRelogio.grid        	(row=3,column=1,sticky = "N")







		relo=Info.Uniman.Titan
		self.botaoUnimanTitan                           = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanTitan                        	["text"]       = "Titan"
		self.botaoUnimanTitan                        	["background"] = relo.ModuloCor
		self.botaoUnimanTitan                         	["width"]      = 13
		self.botaoUnimanTitan                        	["height"]     = 1
		self.botaoUnimanTitan.bind               	("<Button-1>",lambda e: popup("Uniman","Titan",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoUnimanTitan.grid                   	(row=4,column=0,sticky = "N")

		self.botaoUnimanTitanRelogio                    = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")


		self.botaoUnimanTitanRelogio                 	["text"]       = "R"
		self.botaoUnimanTitanRelogio                 	["background"] = relo.RelogioCor
		self.botaoUnimanTitanRelogio                 	["width"]      = 2
		self.botaoUnimanTitanRelogio                 	["height"]     =  1
		self.botaoUnimanTitanRelogio.grid            	(row=4,column=1,sticky = "N")





		relo=Info.Uniman.Sekurity
		self.botaoUnimanSekurity                        = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanSekurity                    	["text"]       = "Sekurity"
		self.botaoUnimanSekurity                    	["background"] = relo.ModuloCor
		self.botaoUnimanSekurity                     	["width"]      = 13
		self.botaoUnimanSekurity                    	["height"]     = 1
		self.botaoUnimanSekurity.bind                	("<Button-1>",lambda e: popup("Uniman","Sekurity",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoUnimanSekurity.grid               	(row=5,column=0,sticky = "N")

		self.botaoUnimanSekurityRelogio                            = Button(self.ContainerUniman, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoUnimanSekurityRelogio             	["text"]       = "R"
		self.botaoUnimanSekurityRelogio             	["background"] = relo.RelogioCor
		self.botaoUnimanSekurityRelogio             	["width"]      = 2
		self.botaoUnimanSekurityRelogio             	["height"]     =  1
		self.botaoUnimanSekurityRelogio.grid        	(row=5,column=1,sticky = "N")



	def Create_Tarek(self):

		self.msgTarek = Label (self.ContainerTarek,text = "Grupo Tarek")
		self.msgTarek["height"] = 1
		self.msgTarek.grid(row=0,column=0,sticky = "N")




		self.botaoTahine                                         = Button(self.ContainerTarek)
		self.botaoTahine                          ["text"]       = "Tahine"
		self.botaoTahine                          ["background"] = Info.Tarek.Tahine.ModuloCor
		self.botaoTahine                           ["width"]      = 13
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
		self.botaoTahineRelogio                   ["width"]      = 2
		self.botaoTahineRelogio.grid              (row=1,column=1,sticky = "N")




		self.botaoTarek                                          = Button(self.ContainerTarek)
		self.botaoTarek                           ["text"]       = "Tarek"
		self.botaoTarek                           ["background"] = Info.Tarek.Tarek.ModuloCor
		self.botaoTarek                           ["height"]     = 1
		self.botaoTarek                            ["width"]      = 13
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
		self.botaoTarekRelogio                    ["width"]      = 2
		self.botaoTarekRelogio                    ["height"]     = 1
		self.botaoTarekRelogio.grid               (row=2,column=1,sticky = "N")




		self.botaoTafadalu                                       = Button(self.ContainerTarek)
		self.botaoTafadalu                        ["text"]       = "Tafadalu"
		self.botaoTafadalu                        ["background"] = Info.Tarek.Tafadalu.ModuloCor
		self.botaoTafadalu                        ["height"]     = 1
		self.botaoTafadalu                         ["width"]      = 13
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
		self.botaoTafadaluRelogio                ["width"]      = 2
		self.botaoTafadaluRelogio.grid           (row=3,column=1,sticky = "N")




		self.botaoTalami                                        = Button(self.ContainerTarek)
		self.botaoTalami                         ["text"]       = "Talami"
		self.botaoTalami                         ["background"] = Info.Tarek.Talami.ModuloCor
		self.botaoTalami                          ["width"]      = 13
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
		self.botaoTalamiRelogio                  ["width"]      = 2
		self.botaoTalamiRelogio                  ["height"]     = 1
		self.botaoTalamiRelogio.grid             (row=4,column=1,sticky = "N")



	def Create_Lotten(self):

		
		self.msgLotten = Label (self.ContainerLotten,text = "Lotten", font = "arialblack 12 bold",bg="black",fg="white")
		self.msgLotten.grid(row=0,column=0,sticky = "N")


		self.botaoLottenAtencao                                        = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenAtencao                         ["text"]       = "A"
		self.botaoLottenAtencao                         ["height"]     = 1
		self.botaoLottenAtencao                         ["background"] = Info.Lotten.Status.Atencao
		self.botaoLottenAtencao                         ["width"]      = 2

		self.botaoLottenAtencao.grid                     (row=0,column=1,sticky = "N")






		self.msgLottenContage = Label (self.ContainerLotten,text=str(Info.Lotten.Status.Contage)+"/"+
														  str(Info.Lotten.Status.TotalRelogios),
														  font="arial 11",bg="black",fg="white")

		self.msgLottenContage.grid(row=1,column=1,pady=3.5,sticky = "N")

		self.msgLottenHora = Label (self.ContainerLotten,text = Info.Lotten.Status.Horaultima,font="arial 11",bg="black",fg="white")
																			
		self.msgLottenHora.grid(row=1,column=0, pady=3.5,sticky = "N")



		


		self.botaoLottenJardins                                  = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenJardins                   ["text"]       = "Jardins"
		self.botaoLottenJardins                   ["background"] = Info.Lotten.Jardins.ModuloCor
		self.botaoLottenJardins                    ["width"]      = 13
		self.botaoLottenJardins                   ["height"]     = 1
		self.botaoLottenJardins.bind              ("<Button-1>",lambda e: popup("Lotten","Jardins",
													Info.Lotten.Jardins.IP, 
													Info.Lotten.Jardins.Porta, 
													Info.Lotten.Jardins.NumeroRep, 
													Info.Lotten.Jardins.Responsavel, 
													Info.Lotten.Jardins.Telefone))
		self.botaoLottenJardins.grid              (row=2,column=0,sticky = "N")

		self.botaoLottenJardinsRelogio                           = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenJardinsRelogio            ["text"]       = "R"
		self.botaoLottenJardinsRelogio            ["background"] = Info.Lotten.Jardins.RelogioCor
		self.botaoLottenJardinsRelogio            ["width"]      = 2
		self.botaoLottenJardinsRelogio            ["height"]     = 1
		self.botaoLottenJardinsRelogio.grid       (row=2,column=1,sticky = "N")




		self.botaoLottenAlphaville                               = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenAlphaville                ["text"]       = "Alphaville"
		self.botaoLottenAlphaville                ["background"] = Info.Lotten.Alphaville.ModuloCor
		self.botaoLottenAlphaville                 ["width"]      = 13
		self.botaoLottenAlphaville                ["height"]     = 1
		self.botaoLottenAlphaville.bind           ("<Button-1>",lambda e: popup("Lotten","Alphaville",
													Info.Lotten.Alphaville.IP, 
													Info.Lotten.Alphaville.Porta, 
													Info.Lotten.Alphaville.NumeroRep, 
													Info.Lotten.Alphaville.Responsavel, 
													Info.Lotten.Alphaville.Telefone))
		self.botaoLottenAlphaville.grid           (row=3,column=0,sticky = "N")

		self.botaoLottenAlphavilleRelogio                        = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenAlphavilleRelogio         ["text"]       = "R"
		self.botaoLottenAlphavilleRelogio         ["background"] = Info.Lotten.Alphaville.RelogioCor
		self.botaoLottenAlphavilleRelogio         ["width"]      = 2
		self.botaoLottenAlphavilleRelogio         ["height"]     = 1		
		self.botaoLottenAlphavilleRelogio.grid    (row=3,column=1,sticky = "N")




		self.botaoLottenOsasco                                  = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenOsasco                   ["text"]       = "Osasco"
		self.botaoLottenOsasco                   ["background"] = Info.Lotten.Osasco.ModuloCor
		self.botaoLottenOsasco                    ["width"]      = 13
		self.botaoLottenOsasco                   ["height"]     = 1
		self.botaoLottenOsasco.bind              ("<Button-1>",lambda e: popup("Lotten","Osasco",
													Info.Lotten.Osasco.IP, 
													Info.Lotten.Osasco.Porta, 
													Info.Lotten.Osasco.NumeroRep, 
													Info.Lotten.Osasco.Responsavel, 
													Info.Lotten.Osasco.Telefone))
		self.botaoLottenOsasco.grid              (row=4,column=0,sticky = "N")

		self.botaoLottenOsascoRelogio                           = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenOsascoRelogio            ["text"]       = "R"
		self.botaoLottenOsascoRelogio            ["background"] = Info.Lotten.Osasco.RelogioCor
		self.botaoLottenOsascoRelogio            ["width"]      = 2
		self.botaoLottenOsascoRelogio            ["height"]     = 1		
		self.botaoLottenOsascoRelogio.grid       (row=4,column=1,sticky = "N")




		self.botaoLottenSantana                                 = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenSantana                  ["text"]       = "Santana"
		self.botaoLottenSantana                  ["background"] = Info.Lotten.Santana.ModuloCor
		self.botaoLottenSantana                   ["width"]      = 13
		self.botaoLottenSantana                  ["height"]     = 1
		self.botaoLottenSantana.bind             ("<Button-1>",lambda e: popup("Lotten","Santana",
													Info.Lotten.Santana.IP, 
													Info.Lotten.Santana.Porta, 
													Info.Lotten.Santana.NumeroRep, 
													Info.Lotten.Santana.Responsavel, 
													Info.Lotten.Santana.Telefone))
		self.botaoLottenSantana.grid             (row=5,column=0,sticky = "N")

		self.botaoLottenSantanaRelogio                          = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenSantanaRelogio           ["text"]       = "R"
		self.botaoLottenSantanaRelogio           ["background"] = Info.Lotten.Santana.RelogioCor
		self.botaoLottenSantanaRelogio           ["width"]      = 2
		self.botaoLottenSantanaRelogio           ["height"]     = 1
		self.botaoLottenSantanaRelogio.grid      (row=5,column=1,sticky = "N")




		self.botaoLottenTatuape                                = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenTatuape                 ["text"]       = "Tatuape"
		self.botaoLottenTatuape                 ["background"] = Info.Lotten.Tatuape.ModuloCor
		self.botaoLottenTatuape                  ["width"]      = 13
		self.botaoLottenTatuape                 ["height"]     = 1
		self.botaoLottenTatuape.bind             ("<Button-1>",lambda e: popup("Lotten","Tatuape",
													Info.Lotten.Tatuape.IP, 
													Info.Lotten.Tatuape.Porta, 
													Info.Lotten.Tatuape.NumeroRep, 
													Info.Lotten.Tatuape.Responsavel, 
													Info.Lotten.Tatuape.Telefone))
		self.botaoLottenTatuape.grid            (row=6,column=0,sticky = "N")

		self.botaoLottenTatuapeRelogio                         = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenTatuapeRelogio          ["text"]       = "R"
		self.botaoLottenTatuapeRelogio          ["background"] = Info.Lotten.Tatuape.RelogioCor
		self.botaoLottenTatuapeRelogio          ["width"]      = 2
		self.botaoLottenTatuapeRelogio          ["height"]     = 1		
		self.botaoLottenTatuapeRelogio.grid     (row=6,column=1,sticky = "N")




		self.botaoLottenMoema                                  = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenMoema                   ["text"]       = "Moema"
		self.botaoLottenMoema                   ["background"] = Info.Lotten.Moema.ModuloCor
		self.botaoLottenMoema                    ["width"]      = 13
		self.botaoLottenMoema                   ["height"]     = 1
		self.botaoLottenMoema.bind              ("<Button-1>",lambda e: popup("Lotten","Moema",
													Info.Lotten.Moema.IP, 
													Info.Lotten.Moema.Porta, 
													Info.Lotten.Moema.NumeroRep, 
													Info.Lotten.Moema.Responsavel, 
													Info.Lotten.Moema.Telefone))
		self.botaoLottenMoema.grid              (row=7,column=0,sticky = "N")

		self.botaoLottenMoemaRelogio                           = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenMoemaRelogio            ["text"]       = "R"
		self.botaoLottenMoemaRelogio            ["background"] = Info.Lotten.Moema.RelogioCor
		self.botaoLottenMoemaRelogio            ["width"]      = 2
		self.botaoLottenMoemaRelogio            ["height"]     = 1
		self.botaoLottenMoemaRelogio.grid       (row=7,column=1,sticky = "N")





		self.botaoLottenJardimSul                              = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenJardimSul               ["text"]       = "Jardim Sul"
		self.botaoLottenJardimSul               ["background"] = Info.Lotten.JardimSul.ModuloCor
		self.botaoLottenJardimSul                ["width"]      = 13
		self.botaoLottenJardimSul               ["height"]     = 1
		self.botaoLottenMoema.bind              ("<Button-1>",lambda e: popup("Lotten","Jardim Sul",
													Info.Lotten.JardimSul.IP, 
													Info.Lotten.JardimSul.Porta, 
													Info.Lotten.JardimSul.NumeroRep, 
													Info.Lotten.JardimSul.Responsavel, 
													Info.Lotten.JardimSul.Telefone))
		self.botaoLottenJardimSul.grid          (row=8,column=0,sticky = "N")

		self.botaoLottenJardimSulRelogio                       = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenJardimSulRelogio        ["text"]       = "R"
		self.botaoLottenJardimSulRelogio        ["background"] = Info.Lotten.JardimSul.RelogioCor
		self.botaoLottenJardimSulRelogio        ["width"]      = 2
		self.botaoLottenJardimSulRelogio        ["height"]     = 1
		self.botaoLottenJardimSulRelogio.grid   (row=8,column=1,sticky = "N")




		self.botaoLottenConceicao                              = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenConceicao               ["text"]       = "Conceicao"
		self.botaoLottenConceicao               ["background"] = Info.Lotten.Conceicao.ModuloCor
		self.botaoLottenConceicao                ["width"]      = 13
		self.botaoLottenConceicao               ["height"]     = 1
		self.botaoLottenConceicao.bind          ("<Button-1>",lambda e: popup("Lotten","Conceicao",
													Info.Lotten.Conceicao.IP, 
													Info.Lotten.Conceicao.Porta, 
													Info.Lotten.Conceicao.NumeroRep, 
													Info.Lotten.Conceicao.Responsavel, 
													Info.Lotten.Conceicao.Telefone))
		self.botaoLottenConceicao.grid          (row=9,column=0,sticky = "N")

		self.botaoLottenConceicaoRelogio                       = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenConceicaoRelogio        ["text"]       = "R"
		self.botaoLottenConceicaoRelogio        ["background"] = Info.Lotten.Conceicao.RelogioCor
		self.botaoLottenConceicaoRelogio        ["width"]      = 2
		self.botaoLottenConceicaoRelogio        ["height"]     = 1
		self.botaoLottenConceicaoRelogio.grid   (row=9,column=1,sticky = "N")




		self.botaoLottenPerdizes                               = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenPerdizes                ["text"]       = "Perdizes"
		self.botaoLottenPerdizes                ["background"] = Info.Lotten.Perdizes.ModuloCor
		self.botaoLottenPerdizes                 ["width"]      = 13
		self.botaoLottenPerdizes                ["height"]     = 1
		self.botaoLottenPerdizes.bind           ("<Button-1>",lambda e: popup("Lotten","Perdizes",
													Info.Lotten.Perdizes.IP, 
													Info.Lotten.Perdizes.Porta, 
													Info.Lotten.Perdizes.NumeroRep, 
													Info.Lotten.Perdizes.Responsavel, 
													Info.Lotten.Perdizes.Telefone))
		self.botaoLottenPerdizes.grid           (row=10,column=0,sticky = "N")

		self.botaoLottenPerdizesRelogio                        = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenPerdizesRelogio         ["text"]       = "R"
		self.botaoLottenPerdizesRelogio         ["background"] = Info.Lotten.Perdizes.RelogioCor
		self.botaoLottenPerdizesRelogio         ["width"]      = 2
		self.botaoLottenPerdizesRelogio         ["height"]     = 1
		self.botaoLottenPerdizesRelogio.grid    (row=10,column=1,sticky = "N")




		self.botaoLottenLapa                                   = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenLapa                    ["text"]       = "Lapa"
		self.botaoLottenLapa                    ["background"] = Info.Lotten.Lapa.ModuloCor
		self.botaoLottenLapa                     ["width"]      = 13
		self.botaoLottenLapa                    ["height"]     = 1
		self.botaoLottenLapa.bind               ("<Button-1>",lambda e: popup("Lotten","Lapa",
													Info.Lotten.Lapa.IP, 
													Info.Lotten.Lapa.Porta, 
													Info.Lotten.Lapa.NumeroRep, 
													Info.Lotten.Lapa.Responsavel, 
													Info.Lotten.Lapa.Telefone))
		self.botaoLottenLapa.grid               (row=11,column=0,sticky = "N")

		self.botaoLottenLapaRelogio                            = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenLapaRelogio             ["text"]       = "R"
		self.botaoLottenLapaRelogio             ["background"] = Info.Lotten.Lapa.RelogioCor
		self.botaoLottenLapaRelogio             ["width"]      = 2
		self.botaoLottenLapaRelogio             ["height"]     = 1
		self.botaoLottenLapaRelogio.grid        (row=11,column=1,sticky = "N")




		self.botaoLottenSaoCaetano                             = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenSaoCaetano              ["text"]       = "Sao Caetano"
		self.botaoLottenSaoCaetano              ["background"] = Info.Lotten.SaoCaetano.ModuloCor
		self.botaoLottenSaoCaetano               ["width"]      = 13
		self.botaoLottenSaoCaetano              ["height"]     = 1
		self.botaoLottenSaoCaetano.bind         ("<Button-1>",lambda e: popup("Lotten","SaoCaetano",
													Info.Lotten.SaoCaetano.IP, 
													Info.Lotten.SaoCaetano.Porta, 
													Info.Lotten.SaoCaetano.NumeroRep, 
													Info.Lotten.SaoCaetano.Responsavel, 
													Info.Lotten.SaoCaetano.Telefone))
		self.botaoLottenSaoCaetano.grid         (row=12,column=0,sticky = "N")

		self.botaoLottenSaoCaetanoRelogio                      = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenSaoCaetanoRelogio       ["text"]       = "R"
		self.botaoLottenSaoCaetanoRelogio       ["background"] = Info.Lotten.SaoCaetano.RelogioCor
		self.botaoLottenSaoCaetanoRelogio       ["width"]      = 2
		self.botaoLottenSaoCaetanoRelogio       ["height"]     = 1
		self.botaoLottenSaoCaetanoRelogio.grid  (row=12,column=1,sticky = "N")




		self.botaoLottenPinheiros                              = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenPinheiros               ["text"]       = "Pinheiros"
		self.botaoLottenPinheiros               ["background"] = Info.Lotten.Pinheiros.ModuloCor
		self.botaoLottenPinheiros                ["width"]      = 13
		self.botaoLottenPinheiros               ["height"]     = 1
		self.botaoLottenPinheiros.bind          ("<Button-1>",lambda e: popup("Lotten","Pinheiros",
													Info.Lotten.Pinheiros.IP, 
													Info.Lotten.Pinheiros.Porta, 
													Info.Lotten.Pinheiros.NumeroRep, 
													Info.Lotten.Pinheiros.Responsavel, 
													Info.Lotten.Pinheiros.Telefone))
		self.botaoLottenPinheiros.grid          (row=13,column=0,sticky = "N")

		self.botaoLottenPinheirosRelogio                       = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenPinheirosRelogio        ["text"]       = "R"
		self.botaoLottenPinheirosRelogio        ["background"] = Info.Lotten.Pinheiros.RelogioCor
		self.botaoLottenPinheirosRelogio        ["width"]      = 2
		self.botaoLottenPinheirosRelogio        ["height"]     = 1
		self.botaoLottenPinheirosRelogio.grid   (row=13,column=1,sticky = "N")




		self.botaoLottenMorumbi                                = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenMorumbi                 ["text"]       = "Morumbi"
		self.botaoLottenMorumbi                 ["background"] = Info.Lotten.Morumbi.ModuloCor
		self.botaoLottenMorumbi                  ["width"]      = 13
		self.botaoLottenMorumbi                 ["height"]     = 1
		self.botaoLottenMorumbi.bind            ("<Button-1>",lambda e: popup("Lotten","Morumbi",
													Info.Lotten.Morumbi.IP, 
													Info.Lotten.Morumbi.Porta, 
													Info.Lotten.Morumbi.NumeroRep, 
													Info.Lotten.Morumbi.Responsavel, 
													Info.Lotten.Morumbi.Telefone))
		self.botaoLottenMorumbi.grid            (row=14,column=0,sticky = "N")

		self.botaoLottenMorumbiRelogio                         = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenMorumbiRelogio          ["text"]       = "R"
		self.botaoLottenMorumbiRelogio          ["background"] = Info.Lotten.Morumbi.RelogioCor
		self.botaoLottenMorumbiRelogio          ["width"]      = 2
		self.botaoLottenMorumbiRelogio          ["height"]     = 1
		self.botaoLottenMorumbiRelogio.grid     (row=14,column=1,sticky = "N")





		self.botaoLottenBerrini                                = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenBerrini                 ["text"]       = "Berrini"
		self.botaoLottenBerrini                 ["background"] = Info.Lotten.Berrini.ModuloCor
		self.botaoLottenBerrini                  ["width"]      = 13
		self.botaoLottenBerrini                 ["height"]     = 1
		self.botaoLottenBerrini.bind            ("<Button-1>",lambda e: popup("Lotten","Berrini",
													Info.Lotten.Berrini.IP, 
													Info.Lotten.Berrini.Porta, 
													Info.Lotten.Berrini.NumeroRep, 
													Info.Lotten.Berrini.Responsavel, 
													Info.Lotten.Berrini.Telefone))
		self.botaoLottenBerrini.grid            (row=15,column=0,sticky = "N")

		self.botaoLottenBerriniRelogio                         = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenBerriniRelogio          ["text"]       = "R"
		self.botaoLottenBerriniRelogio          ["background"] = Info.Lotten.Berrini.RelogioCor
		self.botaoLottenBerriniRelogio          ["width"]      = 2
		self.botaoLottenBerriniRelogio          ["height"]     = 1
		self.botaoLottenBerriniRelogio.grid     (row=15,column=1,sticky = "N")





		self.botaoLottenVilaMariana                            = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenVilaMariana             ["text"]       = "Vila Mariana"
		self.botaoLottenVilaMariana             ["background"] = Info.Lotten.VilaMariana.ModuloCor
		self.botaoLottenVilaMariana              ["width"]      = 13
		self.botaoLottenVilaMariana             ["height"]     = 1
		self.botaoLottenVilaMariana.bind        ("<Button-1>",lambda e: popup("Lotten","Vila Mariana",
													Info.Lotten.VilaMariana.IP, 
													Info.Lotten.VilaMariana.Porta, 
													Info.Lotten.VilaMariana.NumeroRep, 
													Info.Lotten.VilaMariana.Responsavel, 
													Info.Lotten.VilaMariana.Telefone))
		self.botaoLottenVilaMariana.grid        (row=16,column=0,sticky = "N")

		self.botaoLottenVilaMarianaRelogio                     = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenVilaMarianaRelogio      ["text"]       = "R"
		self.botaoLottenVilaMarianaRelogio      ["background"] = Info.Lotten.VilaMariana.RelogioCor
		self.botaoLottenVilaMarianaRelogio      ["width"]      = 2
		self.botaoLottenVilaMarianaRelogio      ["height"]     = 1
		self.botaoLottenVilaMarianaRelogio.grid (row=16,column=1,sticky = "N")





		self.botaoLottenVilaOlimpia                            = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenVilaOlimpia             ["text"]       = "Vila Olimpia"
		self.botaoLottenVilaOlimpia             ["background"] = Info.Lotten.VilaOlimpia.ModuloCor
		self.botaoLottenVilaOlimpia              ["width"]      = 13
		self.botaoLottenVilaOlimpia             ["height"]     = 1
		self.botaoLottenVilaOlimpia.bind        ("<Button-1>",lambda e: popup("Lotten","Vila Olimpia",
											     	Info.Lotten.VilaOlimpia.IP, 
													Info.Lotten.VilaOlimpia.Porta, 
													Info.Lotten.VilaOlimpia.NumeroRep, 
													Info.Lotten.VilaOlimpia.Responsavel, 
													Info.Lotten.VilaOlimpia.Telefone))
		self.botaoLottenVilaOlimpia.grid        (row=17,column=0,sticky = "N")

		self.botaoLottenVilaOlimpiaRelogio                     = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenVilaOlimpiaRelogio      ["text"]       = "R"
		self.botaoLottenVilaOlimpiaRelogio      ["background"] = Info.Lotten.VilaOlimpia.RelogioCor
		self.botaoLottenVilaOlimpiaRelogio      ["width"]      = 2
		self.botaoLottenVilaOlimpiaRelogio      ["height"]     = 1
		self.botaoLottenVilaOlimpiaRelogio.grid (row=17,column=1,sticky = "N")





		self.botaoLottenItaim                                 = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenItaim                  ["text"]       = "Itaim"
		self.botaoLottenItaim                  ["background"] = Info.Lotten.Itaim.ModuloCor
		self.botaoLottenItaim                   ["width"]      = 13
		self.botaoLottenItaim                  ["height"]     = 1
		self.botaoLottenItaim.bind             ("<Button-1>",lambda e: popup("Lotten","Itaim",
													Info.Lotten.Itaim.IP, 
													Info.Lotten.Itaim.Porta, 
													Info.Lotten.Itaim.NumeroRep, 
													Info.Lotten.Itaim.Responsavel, 
													Info.Lotten.Itaim.Telefone))
		self.botaoLottenItaim.grid             (row=18,column=0,sticky = "N")

		self.botaoLottenItaimRelogio                          = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenItaimRelogio           ["text"]       = "R"
		self.botaoLottenItaimRelogio           ["background"] = Info.Lotten.Itaim.RelogioCor
		self.botaoLottenItaimRelogio           ["width"]      = 2
		self.botaoLottenItaimRelogio           ["height"]     = 1
		self.botaoLottenItaimRelogio.grid      (row=18,column=1,sticky = "N")






		self.botaoLottenGuarulhos                              = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenGuarulhos               ["text"]       = "Guarulhos"
		self.botaoLottenGuarulhos               ["background"] = Info.Lotten.Guarulhos.ModuloCor
		self.botaoLottenGuarulhos                ["width"]      = 13
		self.botaoLottenGuarulhos               ["height"]     = 1
		self.botaoLottenGuarulhos.bind          ("<Button-1>",lambda e: popup("Lotten","Guarulhos",
													Info.Lotten.Guarulhos.IP, 
													Info.Lotten.Guarulhos.Porta, 
													Info.Lotten.Guarulhos.NumeroRep, 
													Info.Lotten.Guarulhos.Responsavel, 
													Info.Lotten.Guarulhos.Telefone))
		self.botaoLottenGuarulhos.grid          (row=19,column=0,sticky = "N")

		self.botaoLottenGuarulhosRelogio                       = Button(self.ContainerLotten, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoLottenGuarulhosRelogio        ["text"]       = "R"
		self.botaoLottenGuarulhosRelogio        ["background"] = Info.Lotten.Guarulhos.RelogioCor
		self.botaoLottenGuarulhosRelogio        ["width"]      = 2
		self.botaoLottenGuarulhosRelogio        ["height"]     = 1
		self.botaoLottenGuarulhosRelogio.grid   (row=19,column=1,sticky = "N")



	def Create_BestInClass(self):

		self.msgBestInClass = Label (self.ContainerBestInClass,text = "Best In Class",font = "arialblack 12 bold",bg="black",fg="white")
		self.msgBestInClassCont = Label (self.ContainerBestInClass,text = str(Info.BestInClass.Status.Contage)+"/"
															+str(Info.BestInClass.Status.TotalRelogios),
															font="arial 11",bg="black",fg="white")

		self.msgBestInClass.grid                   	(row=0,column=0,sticky = "N")


		self.botaoBestInClassAtencao                                        = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassAtencao                         ["text"]       = "A"
		self.botaoBestInClassAtencao                         ["height"]     = 1
		self.botaoBestInClassAtencao                         ["background"] = Info.BestInClass.Status.Atencao
		self.botaoBestInClassAtencao                         ["width"]      = 2

		self.botaoBestInClassAtencao.grid                     (row=0,column=1,sticky = "N")
	




		self.msgBestInClassCont.grid             	(row=1,column=1,pady=3.5,sticky = "N")

		self.msgBestInClassHora = Label (self.ContainerBestInClass,text = Info.BestInClass.Status.Horaultima,font="arial 11",bg="black",fg="white")
																			
		self.msgBestInClassHora.grid(row=1,column=0,pady=3.5, sticky = "N")
		




		self.botaoBestInClassRecife                               = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassRecife                ["text"]       = "Recife"
		self.botaoBestInClassRecife                ["background"] = Info.BestInClass.Recife.ModuloCor
		self.botaoBestInClassRecife                 ["width"]      = 13
		self.botaoBestInClassRecife                ["height"]     = 1
		self.botaoBestInClassRecife.bind           ("<Button-1>",lambda e: popup("Best In Class","Recife",
													Info.BestInClass.Recife.IP, 
													Info.BestInClass.Recife.Porta, 
													Info.BestInClass.Recife.NumeroRep, 
													Info.BestInClass.Recife.Responsavel, 
													Info.BestInClass.Recife.Telefone))

		self.botaoBestInClassRecifeRelogio                        = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassRecifeRelogio         ["text"]       = "R"
		self.botaoBestInClassRecifeRelogio         ["background"] = Info.BestInClass.Recife.RelogioCor
		self.botaoBestInClassRecifeRelogio         ["width"]      = 2
		self.botaoBestInClassRecifeRelogio         ["height"]     = 1

		self.botaoBestInClassRecife.grid           (row=2,column=0,sticky = "N")
		self.botaoBestInClassRecifeRelogio.grid    (row=2,column=1,sticky = "N")






		self.botaoBestInClassItaquera                             = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItaquera              ["text"]       = "Itaquera"
		self.botaoBestInClassItaquera              ["background"] = Info.BestInClass.Itaquera.ModuloCor
		self.botaoBestInClassItaquera               ["width"]      = 13
		self.botaoBestInClassItaquera              ["height"]     = 1
		self.botaoBestInClassItaquera.bind         ("<Button-1>",lambda e: popup("Best In Class","Itaquera",
													Info.BestInClass.Itaquera.IP, 
													Info.BestInClass.Itaquera.Porta, 
													Info.BestInClass.Itaquera.NumeroRep, 
													Info.BestInClass.Itaquera.Responsavel, 
													Info.BestInClass.Itaquera.Telefone))


		self.botaoBestInClassItaqueraRelogio                      = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItaqueraRelogio       ["text"]       = "R"
		self.botaoBestInClassItaqueraRelogio       ["background"] = Info.BestInClass.Itaquera.RelogioCor
		self.botaoBestInClassItaqueraRelogio       ["width"]      = 2
		self.botaoBestInClassItaqueraRelogio       ["height"]     = 1		

		self.botaoBestInClassItaquera.grid         (row=3,column=0,sticky = "N")
		self.botaoBestInClassItaqueraRelogio.grid  (row=3,column=1,sticky = "N")






		self.botaoBestInClassItapevi                              = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItapevi               ["text"]       = "Itapevi"
		self.botaoBestInClassItapevi               ["background"] = Info.BestInClass.Itapevi.ModuloCor
		self.botaoBestInClassItapevi                ["width"]      = 13
		self.botaoBestInClassItapevi               ["height"]     = 1
		self.botaoBestInClassItapevi.bind          ("<Button-1>",lambda e: popup("Best In Class","Itapevi",
													Info.BestInClass.Itapevi.IP, 
													Info.BestInClass.Itapevi.Porta, 
													Info.BestInClass.Itapevi.NumeroRep, 
													Info.BestInClass.Itapevi.Responsavel, 
													Info.BestInClass.Itapevi.Telefone))


		self.botaoBestInClassItapeviRelogio                       = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItapeviRelogio        ["text"]       = "R"
		self.botaoBestInClassItapeviRelogio        ["background"] = Info.BestInClass.Itapevi.RelogioCor
		self.botaoBestInClassItapeviRelogio        ["width"]      = 2
		self.botaoBestInClassItapeviRelogio        ["height"]     = 1		

		self.botaoBestInClassItapevi.grid          (row=4,column=0,sticky = "N")
		self.botaoBestInClassItapeviRelogio.grid   (row=4,column=1,sticky = "N")





		self.botaoBestInClassSorocaba                             = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSorocaba              ["text"]       = "Sorocaba"
		self.botaoBestInClassSorocaba              ["background"] = Info.BestInClass.Sorocaba.ModuloCor
		self.botaoBestInClassSorocaba               ["width"]      = 13
		self.botaoBestInClassSorocaba              ["height"]     = 1
		self.botaoBestInClassSorocaba.bind          ("<Button-1>",lambda e: popup("Best In Class","Sorocaba",
													Info.BestInClass.Sorocaba.IP, 
													Info.BestInClass.Sorocaba.Porta, 
													Info.BestInClass.Sorocaba.NumeroRep, 
													Info.BestInClass.Sorocaba.Responsavel, 
													Info.BestInClass.Sorocaba.Telefone))

		self.botaoBestInClassSorocabaRelogio                      = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSorocabaRelogio       ["text"]       = "R"
		self.botaoBestInClassSorocabaRelogio       ["background"] = Info.BestInClass.Sorocaba.RelogioCor
		self.botaoBestInClassSorocabaRelogio       ["width"]      = 2
		self.botaoBestInClassSorocabaRelogio       ["height"]     = 1

		self.botaoBestInClassSorocaba.grid         (row=5,column=0,sticky = "N")
		self.botaoBestInClassSorocabaRelogio.grid  (row=5,column=1,sticky = "N")




		self.botaoBestInClassSeteLagoas                           = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSeteLagoas            ["text"]       = "Sete Lagoas"
		self.botaoBestInClassSeteLagoas            ["background"] = Info.BestInClass.SeteLagoas.ModuloCor
		self.botaoBestInClassSeteLagoas             ["width"]      = 13
		self.botaoBestInClassSeteLagoas            ["height"]     = 1
		self.botaoBestInClassSeteLagoas.bind          ("<Button-1>",lambda e: popup("Best In Class","Sete Lagoas",
													Info.BestInClass.SeteLagoas.IP, 
													Info.BestInClass.SeteLagoas.Porta, 
													Info.BestInClass.SeteLagoas.NumeroRep, 
													Info.BestInClass.SeteLagoas.Responsavel, 
													Info.BestInClass.SeteLagoas.Telefone))

		self.botaoBestInClassSeteLagoasRelogio                    = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSeteLagoasRelogio     ["text"]       = "R"
		self.botaoBestInClassSeteLagoasRelogio     ["background"] = Info.BestInClass.SeteLagoas.RelogioCor
		self.botaoBestInClassSeteLagoasRelogio     ["width"]      = 2
		self.botaoBestInClassSeteLagoasRelogio     ["height"]     = 1		

		self.botaoBestInClassSeteLagoas.grid       (row=6,column=0,sticky = "N")
		self.botaoBestInClassSeteLagoasRelogio.grid(row=6,column=1,sticky = "N")




		self.botaoBestInClassCuritiba                             = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassCuritiba              ["text"]       = "Curitiba"
		self.botaoBestInClassCuritiba              ["background"] = Info.BestInClass.Curitiba.ModuloCor
		self.botaoBestInClassCuritiba               ["width"]      = 13
		self.botaoBestInClassCuritiba              ["height"]     = 1
		self.botaoBestInClassCuritiba.bind          ("<Button-1>",lambda e: popup("Best In Class","Curitiba",
													Info.BestInClass.Curitiba.IP, 
													Info.BestInClass.Curitiba.Porta, 
													Info.BestInClass.Curitiba.NumeroRep, 
													Info.BestInClass.Curitiba.Responsavel, 
													Info.BestInClass.Curitiba.Telefone))


		self.botaoBestInClassCuritibaRelogio                      = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassCuritibaRelogio       ["text"]       = "R"
		self.botaoBestInClassCuritibaRelogio       ["background"] = Info.BestInClass.Curitiba.RelogioCor
		self.botaoBestInClassCuritibaRelogio       ["width"]      = 2
		self.botaoBestInClassCuritibaRelogio       ["height"]     = 1

		self.botaoBestInClassCuritiba.grid         (row=7,column=0,sticky = "N")
		self.botaoBestInClassCuritibaRelogio.grid  (row=7,column=1,sticky = "N")






		self.botaoBestInClassSFsat                                = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSFsat                 ["text"]       = "F Santana"
		self.botaoBestInClassSFsat                 ["background"] = Info.BestInClass.Fsantana.ModuloCor
		self.botaoBestInClassSFsat                  ["width"]      = 13
		self.botaoBestInClassSFsat                 ["height"]     = 1
		self.botaoBestInClassSFsat.bind            ("<Button-1>",lambda e: popup("Best In Class","Feira De Santana",
													Info.BestInClass.Fsantana.IP, 
													Info.BestInClass.Fsantana.Porta, 
													Info.BestInClass.Fsantana.NumeroRep, 
													Info.BestInClass.Fsantana.Responsavel, 
													Info.BestInClass.Fsantana.Telefone))

		self.botaoBestInClassSFsatRelogio                         = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassSFsatRelogio          ["text"]       = "R"
		self.botaoBestInClassSFsatRelogio          ["background"] = Info.BestInClass.Fsantana.RelogioCor
		self.botaoBestInClassSFsatRelogio          ["width"]      = 2
		self.botaoBestInClassSFsatRelogio          ["height"]     = 1

		self.botaoBestInClassSFsat.grid            (row=8,column=0,sticky = "N")
		self.botaoBestInClassSFsatRelogio.grid     (row=8,column=1,sticky = "N")







		self.botaoBestInClassItu                                  = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItu                   ["text"]       = "Itu"
		self.botaoBestInClassItu                   ["background"] = Info.BestInClass.Itu.ModuloCor
		self.botaoBestInClassItu                    ["width"]      = 13
		self.botaoBestInClassItu                   ["height"]     = 1
		self.botaoBestInClassItu.bind              ("<Button-1>",lambda e: popup("Best In Class","Itu",
													Info.BestInClass.Itu.IP, 
													Info.BestInClass.Itu.Porta, 
													Info.BestInClass.Itu.NumeroRep, 
													Info.BestInClass.Itu.Responsavel, 
													Info.BestInClass.Itu.Telefone))

		self.botaoBestInClassItuRelogio                           = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItuRelogio            ["text"]       = "R"
		self.botaoBestInClassItuRelogio            ["background"] = Info.BestInClass.Itu.RelogioCor
		self.botaoBestInClassItuRelogio            ["width"]      = 2
		self.botaoBestInClassItuRelogio            ["height"]     = 1


		self.botaoBestInClassItu.grid              (row=9,column=0,sticky = "N")
		self.botaoBestInClassItuRelogio.grid       (row=9,column=1,sticky = "N")







		self.botaoBestInClassGuarulhos                             = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassGuarulhos              ["text"]       = "Guraulhos"
		self.botaoBestInClassGuarulhos              ["background"] = Info.BestInClass.Guarulhos.ModuloCor
		self.botaoBestInClassGuarulhos               ["width"]      = 13
		self.botaoBestInClassGuarulhos              ["height"]     = 1
		self.botaoBestInClassGuarulhos.bind         ("<Button-1>",lambda e: popup("Best In Class","Guarulhos",
													Info.BestInClass.Guarulhos.IP, 
													Info.BestInClass.Guarulhos.Porta, 
													Info.BestInClass.Guarulhos.NumeroRep, 
													Info.BestInClass.Guarulhos.Responsavel, 
													Info.BestInClass.Guarulhos.Telefone))

		self.botaoBestInClassGuarulhosRelogio                      = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassGuarulhosRelogio       ["text"]       = "R"
		self.botaoBestInClassGuarulhosRelogio       ["background"] = Info.BestInClass.Guarulhos.RelogioCor
		self.botaoBestInClassGuarulhosRelogio       ["width"]      = 2
		self.botaoBestInClassGuarulhosRelogio       ["height"]     = 1


		self.botaoBestInClassGuarulhos.grid         (row=10,column=0,sticky = "N")
		self.botaoBestInClassGuarulhosRelogio.grid  (row=10,column=1,sticky = "N")







		self.botaoBestInClassItaporanga                            = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItaporanga             ["text"]       = "Itaporanga"
		self.botaoBestInClassItaporanga             ["background"] = Info.BestInClass.Itaporanga.ModuloCor
		self.botaoBestInClassItaporanga              ["width"]      = 13
		self.botaoBestInClassItaporanga             ["height"]     = 1
		self.botaoBestInClassItaporanga.bind        ("<Button-1>",lambda e: popup("Best In Class","Itaporanga",
													Info.BestInClass.Itaporanga.IP, 
													Info.BestInClass.Itaporanga.Porta, 
													Info.BestInClass.Itaporanga.NumeroRep, 
													Info.BestInClass.Itaporanga.Responsavel, 
													Info.BestInClass.Itaporanga.Telefone))

		self.botaoBestInClassItaporangaRelogio                     = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassItaporangaRelogio      ["text"]       = "R"
		self.botaoBestInClassItaporangaRelogio      ["background"] = Info.BestInClass.Itaporanga.RelogioCor
		self.botaoBestInClassItaporangaRelogio      ["width"]      = 2
		self.botaoBestInClassItaporangaRelogio      ["height"]     = 1


		self.botaoBestInClassItaporanga.grid        (row=11,column=0,sticky = "N")
		self.botaoBestInClassItaporangaRelogio.grid (row=11,column=1,sticky = "N")






		self.botaoBestInClassLinhares                              = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassLinhares               ["text"]       = "Linhares"
		self.botaoBestInClassLinhares               ["background"] = Info.BestInClass.Linhares.ModuloCor
		self.botaoBestInClassLinhares                ["width"]      = 13
		self.botaoBestInClassLinhares               ["height"]     = 1
		self.botaoBestInClassLinhares.bind          ("<Button-1>",lambda e: popup("Best In Class","Linhares",
													Info.BestInClass.Linhares.IP, 
													Info.BestInClass.Linhares.Porta, 
													Info.BestInClass.Linhares.NumeroRep, 
													Info.BestInClass.Linhares.Responsavel, 
													Info.BestInClass.Linhares.Telefone))

		self.botaoBestInClassLinharesRelogio                       = Button(self.ContainerBestInClass, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoBestInClassLinharesRelogio        ["text"]       = "R"
		self.botaoBestInClassLinharesRelogio        ["background"] = Info.BestInClass.Linhares.RelogioCor
		self.botaoBestInClassLinharesRelogio        ["width"]      = 2
		self.botaoBestInClassLinharesRelogio        ["height"]     = 1

		self.botaoBestInClassLinhares.grid          (row=12,column=0,sticky = "N")
		self.botaoBestInClassLinharesRelogio.grid   (row=12,column=1,sticky = "N")



	def Create_CasaCristo(self):


		self.msgCasaCristo = Label (self.ContainerCasaCristo,text = "Casa Cristo",font= "arialblack 12 bold",bg="black",fg="white")

		self.msgCasaCristoContage = Label (self.ContainerCasaCristo,text = str(Info.CasaCristo.Status.Contage)+"/"+
																			str(Info.CasaCristo.Status.TotalRelogios)
																			,font="arial 11",bg="black",fg="white")

		self.msgCasaCristo.grid(row=0, column=0 , sticky = "N")


		self.botaoCasaCristoAtencao                                        = Button(self.ContainerCasaCristo,  highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoAtencao                         ["text"]       = "A"
		self.botaoCasaCristoAtencao                         ["height"]     = 1
		self.botaoCasaCristoAtencao                         ["background"] = Info.CasaCristo.Status.Atencao
		self.botaoCasaCristoAtencao                         ["width"]      = 2

		self.botaoCasaCristoAtencao.grid                     (row=0,column=1,sticky = "N")





		self.msgCasaCristoContage.grid(row=1,column=1,pady=3.5, sticky = "N")



		self.msgCasaCristoHora = Label (self.ContainerCasaCristo,text = Info.CasaCristo.Status.Horaultima,font="arial 11",bg="black",fg="white")
																			
		self.msgCasaCristoHora.grid(row=1,column=0,pady=3.5, sticky = "N")
		

		self.botaoCasaCristoADM                                   = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoADM                    ["text"]       = "ADM"
		self.botaoCasaCristoADM                    ["background"] = Info.CasaCristo.ADM.ModuloCor
		self.botaoCasaCristoADM                     ["width"]      = 13
		self.botaoCasaCristoADM.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","ADM",
													Info.CasaCristo.ADM.IP, 
													Info.CasaCristo.ADM.Porta, 
													Info.CasaCristo.ADM.NumeroRep, 
													Info.CasaCristo.ADM.Responsavel, 
													Info.CasaCristo.ADM.Telefone))

		self.botaoCasaCristoADMRelogio                            = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoADMRelogio             ["text"]       = "R"
		self.botaoCasaCristoADMRelogio             ["background"] = Info.CasaCristo.ADM.RelogioCor
		self.botaoCasaCristoADMRelogio             ["width"]      = 2

		self.botaoCasaCristoADM.grid               (row=2,column=0,sticky = "N")
		self.botaoCasaCristoADMRelogio.grid        (row=2,column=1,sticky = "N")





		self.botaoCasaCristoCEI1                                  = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI1                   ["text"]       = "CEI1"
		self.botaoCasaCristoCEI1                   ["background"] = Info.CasaCristo.CEI1.ModuloCor
		self.botaoCasaCristoCEI1                    ["width"]      = 13
		self.botaoCasaCristoCEI1.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI1",
													Info.CasaCristo.CEI1.IP, 
													Info.CasaCristo.CEI1.Porta, 
													Info.CasaCristo.CEI1.NumeroRep, 
													Info.CasaCristo.CEI1.Responsavel, 
													Info.CasaCristo.CEI1.Telefone))

		self.botaoCasaCristoCEI1Relogio                           = Button(self.ContainerCasaCristo,highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI1Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI1Relogio            ["background"] = Info.CasaCristo.CEI1.RelogioCor
		self.botaoCasaCristoCEI1Relogio            ["width"]      = 2

		self.botaoCasaCristoCEI1.grid              (row=3,column=0,sticky = "N")
		self.botaoCasaCristoCEI1Relogio.grid       (row=3,column=1,sticky = "N")





		self.botaoCasaCristoCEI2                                  = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI2                   ["text"]       = "CEI2"
		self.botaoCasaCristoCEI2                   ["background"] = Info.CasaCristo.CEI2.ModuloCor
		self.botaoCasaCristoCEI2                    ["width"]      = 13
		self.botaoCasaCristoCEI2.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI2",
													Info.CasaCristo.CEI2.IP, 
													Info.CasaCristo.CEI2.Porta, 
													Info.CasaCristo.CEI2.NumeroRep, 
													Info.CasaCristo.CEI2.Responsavel, 
													Info.CasaCristo.CEI2.Telefone))

		self.botaoCasaCristoCEI2Relogio                           = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI2Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI2Relogio            ["background"] = Info.CasaCristo.CEI2.RelogioCor
		self.botaoCasaCristoCEI2Relogio            ["width"]=2

		self.botaoCasaCristoCEI2.grid              (row=4,column=0,sticky = "N")
		self.botaoCasaCristoCEI2Relogio.grid       (row=4,column=1,sticky = "N")
		





		self.botaoCasaCristoCEI3                                  = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI3                   ["text"]       = "CEI3"
		self.botaoCasaCristoCEI3                   ["background"] = Info.CasaCristo.CEI3.ModuloCor
		self.botaoCasaCristoCEI3                    ["width"]      = 13
		self.botaoCasaCristoCEI3.bind               ("<Button-1>",lambda e: popup("Casa do Cristo","CEI3",
													Info.CasaCristo.CEI3.IP, 
													Info.CasaCristo.CEI3.Porta, 
													Info.CasaCristo.CEI3.NumeroRep, 
													Info.CasaCristo.CEI3.Responsavel, 
													Info.CasaCristo.CEI3.Telefone))

		self.botaoCasaCristoCEI3Relogio                           = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoCEI3Relogio            ["text"]       = "R"
		self.botaoCasaCristoCEI3Relogio            ["background"] = Info.CasaCristo.CEI3.RelogioCor
		self.botaoCasaCristoCEI3Relogio            ["width"]      = 2

		self.botaoCasaCristoCEI3.grid              (row=5,column=0,sticky = "N")
		self.botaoCasaCristoCEI3Relogio.grid       (row=5,column=1,sticky = "N")





		self.botaoCasaCristoVMatilde                              = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoVMatilde               ["text"]       = "Vovo Matilde"
		self.botaoCasaCristoVMatilde               ["background"] = Info.CasaCristo.VovoMatilde.ModuloCor
		self.botaoCasaCristoVMatilde                ["width"]      = 13
		self.botaoCasaCristoVMatilde.bind          ("<Button-1>",lambda e: popup("Casa do Cristo","Vovo Matilde",
													Info.CasaCristo.VovoMatilde.IP, 
													Info.CasaCristo.VovoMatilde.Porta, 
													Info.CasaCristo.VovoMatilde.NumeroRep, 
													Info.CasaCristo.VovoMatilde.Responsavel, 
													Info.CasaCristo.VovoMatilde.Telefone))

		self.botaoCasaCristoVMatildeRelogio                       = Button(self.ContainerCasaCristo, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoCasaCristoVMatildeRelogio        ["text"]       = "R"
		self.botaoCasaCristoVMatildeRelogio        ["background"] = Info.CasaCristo.VovoMatilde.RelogioCor
		self.botaoCasaCristoVMatildeRelogio        ["width"]      = 2

		self.botaoCasaCristoVMatilde.grid          (row=6,column=0,sticky = "N")
		self.botaoCasaCristoVMatildeRelogio.grid   (row=6,column=1,sticky = "N")



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
		self.botaoBuildingAllianz                    ["width"]      = 13
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
		self.botaoBuildingAllianzRelogio            ["width"]      = 2
		self.botaoBuildingAllianzRelogio            ["height"]     = 1

		self.botaoBuildingAllianz.grid       		(row=1, column=0, sticky = "N")
		self.botaoBuildingAllianzRelogio.grid       (row=1, column=1, sticky = "N")






		self.botaoBuildingWTorre                                   = Button(self.ContainerBuilding)
		self.botaoBuildingWTorre                    ["text"]       = "WTorre"
		self.botaoBuildingWTorre                    ["background"] = Info.Building.WTorre.ModuloCor
		self.botaoBuildingWTorre                     ["width"]      = 13
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
		self.botaoBuildingWTorreRelogio             ["width"]      = 2
		self.botaoBuildingWTorreRelogio             ["height"]     = 1

		self.botaoBuildingWTorre.grid               (row=2,column=0,sticky = "N")
		self.botaoBuildingWTorreRelogio.grid        (row=2,column=1,sticky = "N")






		self.botaoBuildingRioJaneiro                               = Button(self.ContainerBuilding)
		self.botaoBuildingRioJaneiro                ["text"]       = "Rio De Janeiro"
		self.botaoBuildingRioJaneiro                ["background"] = Info.Building.RioJaneiro.ModuloCor
		self.botaoBuildingRioJaneiro                 ["width"]      = 13
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
		self.botaoBuildingRioJaneiroRelogio         ["width"]      = 2
		self.botaoBuildingRioJaneiroRelogio         ["height"]     =  1


		self.botaoBuildingRioJaneiro.grid           (row=3,column=0,sticky = "N")
		self.botaoBuildingRioJaneiroRelogio.grid    (row=3,column=1,sticky = "N")



	def Create_GrupoNK(self):

		
		self.msgGrupoNk                            		= Label (self.ContainerGrupoNk,text = "Grupo Nk",font = "arialblack 12 bold",bg="black",fg="white")
		self.msgGrupoNk                            		["height"]     = 1
		self.msgGrupoNk.grid                       		(row=0,column=0,sticky = "N")

		self.msgGrupoNkContage                        	= Label (self.ContainerGrupoNk,text=str(Info.GrupoNk.Status.Contage)+"/"+
																		str(Info.GrupoNk.Status.TotalRelogios),font = "arial 11",bg="black",fg="white")	

		self.msgGrupoNkContage                        	["height"]     = 1
		self.msgGrupoNkContage.grid                   	(row=1,column=1,pady=3.5,sticky = "N")


		self.botaoGrupoNkAtencao                                        = Button(self.ContainerGrupoNk, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoGrupoNkAtencao                         ["text"]       = "A"
		self.botaoGrupoNkAtencao                         ["height"]     = 1
		self.botaoGrupoNkAtencao                         ["background"] = Info.GrupoNk.Status.Atencao
		self.botaoGrupoNkAtencao                         ["width"]      = 2

		self.botaoGrupoNkAtencao.grid                     (row=0,column=1,sticky = "N")

		self.msgGrupoNkHora                            		= Label (self.ContainerGrupoNk,
															text =Info.GrupoNk.Status.Horaultima,font = "arial 11",bg="black",fg="white")
		self.msgGrupoNkHora                            		["height"]     = 1
		self.msgGrupoNkHora.grid                       		(row=1,column=0,pady=3.5,sticky = "N")



		self.botaoGrupoNkNelsonKioshi                                  = Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkNelsonKioshi                  	["text"]       = "Nelson Kioshi"
		self.botaoGrupoNkNelsonKioshi                   ["background"] = Info.GrupoNk.NelsonKioshi.ModuloCor
		self.botaoGrupoNkNelsonKioshi                    ["width"]      = 13
		self.botaoGrupoNkNelsonKioshi                   ["height"]     = 1
		self.botaoGrupoNkNelsonKioshi.bind              ("<Button-1>",lambda e: popup("GrupoNk","Nelson Kioshi",
														Info.GrupoNk.NelsonKioshi.IP, 
														Info.GrupoNk.NelsonKioshi.Porta, 
														Info.GrupoNk.NelsonKioshi.NumeroRep, 
														Info.GrupoNk.NelsonKioshi.Responsavel, 
														Info.GrupoNk.NelsonKioshi.Telefone))

		self.botaoGrupoNkNelsonKioshiRelogio                           = Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkNelsonKioshiRelogio            ["text"]       = "R"
		self.botaoGrupoNkNelsonKioshiRelogio            ["background"] = Info.GrupoNk.NelsonKioshi.RelogioCor
		self.botaoGrupoNkNelsonKioshiRelogio            ["width"]      = 2
		self.botaoGrupoNkNelsonKioshiRelogio            ["height"]     = 1

		self.botaoGrupoNkNelsonKioshi.grid       		(row=2, column=0, sticky = "N")
		self.botaoGrupoNkNelsonKioshiRelogio.grid       (row=2, column=1, sticky = "N")






		self.botaoGrupoNkRDFurukawa                                   	= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkRDFurukawaRelogio                            	= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkRDFurukawaRelogio              ["text"]        = "R"
		self.botaoGrupoNkRDFurukawaRelogio              ["background"]  = Info.GrupoNk.RDFurukawa.RelogioCor
		self.botaoGrupoNkRDFurukawaRelogio              ["width"]       = 1
		self.botaoGrupoNkRDFurukawaRelogio              ["height"]      = 1

		self.botaoGrupoNkRDFurukawa.grid                (row=3,column=0,sticky = "N")
		self.botaoGrupoNkRDFurukawaRelogio.grid         (row=3,column=1,sticky = "N")






		self.botaoGrupoNkKio1                               			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkKio1Relogio         		               		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkKio1Relogio         			["text"]        = "R"
		self.botaoGrupoNkKio1Relogio         			["background"]  = Info.GrupoNk.Kio1.RelogioCor
		self.botaoGrupoNkKio1Relogio         			["width"]       = 1
		self.botaoGrupoNkKio1Relogio         			["height"]      = 1


		self.botaoGrupoNkKio1.grid           			(row=4,column=0,sticky = "N")
		self.botaoGrupoNkKio1Relogio.grid    			(row=4,column=1,sticky = "N")





		self.botaoGrupoNkKio2                               			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkKio2Relogio         		               		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkKio2Relogio         			["text"]        = "R"
		self.botaoGrupoNkKio2Relogio         			["background"]  = Info.GrupoNk.Kio2.RelogioCor
		self.botaoGrupoNkKio2Relogio         			["width"]       = 1
		self.botaoGrupoNkKio2Relogio         			["height"]      = 1


		self.botaoGrupoNkKio2.grid           			(row=5,column=0,sticky = "N")
		self.botaoGrupoNkKio2Relogio.grid    			(row=5,column=1,sticky = "N")


		self.botaoGrupoNkGranjaViana                          			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkGranjaVianaRelogio         		            = Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkGranjaVianaRelogio         	["text"]        = "R"
		self.botaoGrupoNkGranjaVianaRelogio         	["background"]  = Info.GrupoNk.GranjaViana.RelogioCor
		self.botaoGrupoNkGranjaVianaRelogio         	["width"]       = 1
		self.botaoGrupoNkGranjaVianaRelogio         	["height"]      = 1


		self.botaoGrupoNkGranjaViana.grid           	(row=6,column=0,sticky = "N")
		self.botaoGrupoNkGranjaVianaRelogio.grid    	(row=6,column=1,sticky = "N")



		self.botaoGrupoNkSantaCecilia                               	= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkSantaCeciliaRelogio         	           		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkSantaCeciliaRelogio         	["text"]        = "R"
		self.botaoGrupoNkSantaCeciliaRelogio         	["background"]  = Info.GrupoNk.SantaCecilia.RelogioCor
		self.botaoGrupoNkSantaCeciliaRelogio         	["width"]       = 1
		self.botaoGrupoNkSantaCeciliaRelogio         	["height"]      = 1


		self.botaoGrupoNkSantaCecilia.grid           	(row=7,column=0,sticky = "N")
		self.botaoGrupoNkSantaCeciliaRelogio.grid    	(row=7,column=1,sticky = "N")


		self.botaoGrupoNkTransfruit                            			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkTransfruitRelogio         		           		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkTransfruitRelogio         		["text"]        = "R"
		self.botaoGrupoNkTransfruitRelogio         		["background"]  = Info.GrupoNk.Transfruit.RelogioCor
		self.botaoGrupoNkTransfruitRelogio         		["width"]       = 1
		self.botaoGrupoNkTransfruitRelogio         		["height"]      = 1

		self.botaoGrupoNkTransfruit.grid           		(row=8,column=0,sticky = "N")
		self.botaoGrupoNkTransfruitRelogio.grid    		(row=8,column=1,sticky = "N")


		self.botaoGrupoNkDistribuidora                         			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkDistribuidoraRelogio         	           		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkDistribuidoraRelogio         	["text"]        = "R"
		self.botaoGrupoNkDistribuidoraRelogio         	["background"]  = Info.GrupoNk.Distribuidora.RelogioCor
		self.botaoGrupoNkDistribuidoraRelogio         	["width"]       = 1
		self.botaoGrupoNkDistribuidoraRelogio         	["height"]      = 1

		self.botaoGrupoNkDistribuidora.grid           	(row=9,column=0,sticky = "N")
		self.botaoGrupoNkDistribuidoraRelogio.grid    	(row=9,column=1,sticky = "N")



		self.botaoGrupoNkNKFilial                             			= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
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

		self.botaoGrupoNkNKFilialRelogio         		           		= Button(self.ContainerGrupoNk, highlightbackground="black",activebackground="black",activeforeground="white")
		self.botaoGrupoNkNKFilialRelogio         		["text"]        = "R"
		self.botaoGrupoNkNKFilialRelogio         		["background"]  = Info.GrupoNk.NKFilial.RelogioCor
		self.botaoGrupoNkNKFilialRelogio         		["width"]       = 1
		self.botaoGrupoNkNKFilialRelogio         		["height"]      = 1

		self.botaoGrupoNkNKFilial.grid           		(row=10,column=0,sticky = "N")
		self.botaoGrupoNkNKFilialRelogio.grid    		(row=10,column=1,sticky = "N")



	def Create_SBCP(self):

		self.msgSBCP                              		= Label (self.ContainerSBCP,text = "SBCP")
		self.msgSBCP                              		["height"]     = 1
		self.msgSBCP.grid                         		(row=0,column=0,sticky = "N")


		self.msgSBCPCount                              	= Label (self.ContainerSBCP,text= str(Info.SBCP.Status.Contage)+"/"+
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
		self.botaoSBCPNacionalRelogio                  	["width"]      = 2


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
		self.botaoSBCPESRelogio                  		["width"]      = 2


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
		self.botaoSBCPDFRelogio                  		["width"]      = 2


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
		self.botaoSBCPCERelogio                  		["width"]      = 2


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
		self.botaoSBCPBARelogio                  		["width"]      = 2


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
		self.botaoSBCPSPRelogio                  		["width"]      = 2


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
		self.botaoSBCPSCRelogio                  		["width"]      = 2


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
		self.botaoSBCPRSRelogio                  		["width"]      = 2


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
		self.botaoSBCPRJRelogio                  		["width"]      = 2


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
		self.botaoSBCPPRRelogio                  		["width"]      = 2


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
		self.botaoSBCPPERelogio                  		["width"]      = 2


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
		self.botaoSBCPMGRelogio                  		["width"]      = 2


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
		self.botaoSBCPGORelogio                  		["width"]      = 2


		self.botaoSBCPGO.grid                    		(row=13,column=0,sticky = "N")
		self.botaoSBCPGORelogio.grid             		(row=13,column=1,sticky = "N")



	def Create_ElRio(self):

		self.msgElRio                              			= Label (self.ContainerElRio,text = "ElRio",font = "arialblack 12 bold",
															bg="black",fg="white")

		self.msgElRio                              			["height"]     = 1
		self.msgElRio.grid                         			(row=0,column=0,sticky = "N")


		self.msgElRioCount                              	= Label (self.ContainerElRio,text= str(Info.ElRio.Status.Contage)+"/"+
																						 str(Info.ElRio.Status.TotalRelogios),
																						 font = "arial 11",bg="black",fg="white")	

		self.msgElRioCount                              	["height"]     = 1
		self.msgElRioCount.grid                         	(row=1,column=1,pady=3.5,sticky = "N")


		self.botaoElRioAtencao                                        = Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioAtencao                         ["text"]       = "A"
		self.botaoElRioAtencao                         ["height"]     = 1
		self.botaoElRioAtencao                         ["background"] = Info.ElRio.Status.Atencao
		self.botaoElRioAtencao                         ["width"]      = 2

		self.botaoElRioAtencao.grid                     (row=0,column=1,sticky = "N")

		self.msgElRioHora                            		= Label (self.ContainerElRio,
															text =Info.ElRio.Status.Horaultima,font = "arial 11",bg="black",fg="white")
		self.msgElRioHora                            		["height"]     = 1
		self.msgElRioHora.grid                       		(row=1,column=0,pady=3.5,sticky = "N")





		self.botaoElRioBotafogoMuniz                       	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBotafogoMuniz                       	["text"]       = "Botafogo Muniz"
		self.botaoElRioBotafogoMuniz                     	["background"] = Info.ElRio.BotafogoMuniz.ModuloCor
		self.botaoElRioBotafogoMuniz                     	["width"]      = 13
		self.botaoElRioBotafogoMuniz                      	["height"]     = 1
		self.botaoElRioBotafogoMuniz.bind                 	("<Button-1>",lambda e: popup("ElRio","Botafogo Muniz",
															Info.ElRio.BotafogoMuniz.IP, 
															Info.ElRio.BotafogoMuniz.Porta, 
															Info.ElRio.BotafogoMuniz.NumeroRep, 
															Info.ElRio.BotafogoMuniz.Responsavel, 
															Info.ElRio.BotafogoMuniz.Telefone))

		self.botaoElRioBotafogoMunizRelogio                 = Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBotafogoMunizRelogio                 ["text"]       = "R"
		self.botaoElRioBotafogoMunizRelogio                 ["background"] = Info.ElRio.BotafogoMuniz.RelogioCor
		self.botaoElRioBotafogoMunizRelogio                 ["height"]     = 1
		self.botaoElRioBotafogoMunizRelogio                 ["width"]      = 2


		self.botaoElRioBotafogoMuniz.grid                   (row=2,column=0,sticky = "N")
		self.botaoElRioBotafogoMunizRelogio.grid            (row=2,column=1,sticky = "N")






		self.botaoElRioBotafogoPraia                      	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBotafogoPraia                      	["text"]       = "Botafogo Praia"
		self.botaoElRioBotafogoPraia                      	["background"] = Info.ElRio.BotafogoPraia.ModuloCor
		self.botaoElRioBotafogoPraia                      	["width"]      = 13
		self.botaoElRioBotafogoPraia                      	["height"]     = 1
		self.botaoElRioBotafogoPraia.bind               	("<Button-1>",lambda e: popup("ElRio","Botafogo Praia",
															Info.ElRio.BotafogoPraia.IP, 
															Info.ElRio.BotafogoPraia.Porta, 
															Info.ElRio.BotafogoPraia.NumeroRep, 
															Info.ElRio.BotafogoPraia.Responsavel, 
															Info.ElRio.BotafogoPraia.Telefone))

		self.botaoElRioBotafogoPraiaRelogio                 = Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBotafogoPraiaRelogio                 ["text"]       = "R"
		self.botaoElRioBotafogoPraiaRelogio                 ["background"] = Info.ElRio.BotafogoPraia.RelogioCor
		self.botaoElRioBotafogoPraiaRelogio                 ["height"]     = 1
		self.botaoElRioBotafogoPraiaRelogio                 ["width"]      = 2


		self.botaoElRioBotafogoPraia.grid                   (row=3,column=0,sticky = "N")
		self.botaoElRioBotafogoPraiaRelogio.grid            (row=3,column=1,sticky = "N")






		self.botaoElRioBoulevard                         	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBoulevard                         	["text"]       = "Boulevard"
		self.botaoElRioBoulevard                         	["background"] = Info.ElRio.Boulevard.ModuloCor
		self.botaoElRioBoulevard                         	["width"]      = 13
		self.botaoElRioBoulevard                         	["height"]     = 1
		self.botaoElRioBoulevard.bind                    	("<Button-1>",lambda e: popup("ElRio","Boulevard",
															Info.ElRio.Boulevard.IP, 
															Info.ElRio.Boulevard.Porta, 
															Info.ElRio.Boulevard.NumeroRep, 
															Info.ElRio.Boulevard.Responsavel, 
															Info.ElRio.Boulevard.Telefone))

		self.botaoElRioBoulevardRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBoulevardRelogio                  	["text"]       = "R"
		self.botaoElRioBoulevardRelogio                  	["background"] = Info.ElRio.Boulevard.RelogioCor
		self.botaoElRioBoulevardRelogio                  	["height"]     = 1
		self.botaoElRioBoulevardRelogio                  	["width"]      = 2


		self.botaoElRioBoulevard.grid                    	(row=4,column=0,sticky = "N")
		self.botaoElRioBoulevardRelogio.grid             	(row=4,column=1,sticky = "N")






		self.botaoElRioCarioca                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCarioca                         		["text"]       = "Carioca"
		self.botaoElRioCarioca                         		["background"] = Info.ElRio.Carioca.ModuloCor
		self.botaoElRioCarioca                         		["width"]      = 13
		self.botaoElRioCarioca                         		["height"]     = 1
		self.botaoElRioCarioca.bind                    		("<Button-1>",lambda e: popup("ElRio","Carioca",
															Info.ElRio.Carioca.IP, 
															Info.ElRio.Carioca.Porta, 
															Info.ElRio.Carioca.NumeroRep, 
															Info.ElRio.Carioca.Responsavel, 
															Info.ElRio.Carioca.Telefone))

		self.botaoElRioCariocaRelogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCariocaRelogio                  		["text"]       = "R"
		self.botaoElRioCariocaRelogio                  		["background"] = Info.ElRio.Carioca.RelogioCor
		self.botaoElRioCariocaRelogio                  		["height"]     = 1
		self.botaoElRioCariocaRelogio                  		["width"]      = 2


		self.botaoElRioCarioca.grid                    		(row=5,column=0,sticky = "N")
		self.botaoElRioCariocaRelogio.grid             		(row=5,column=1,sticky = "N")






		self.botaoElRioCentro1                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro1                         		["text"]       = "Centro I"
		self.botaoElRioCentro1                         		["background"] = Info.ElRio.Centro1.ModuloCor
		self.botaoElRioCentro1                         		["width"]      = 13
		self.botaoElRioCentro1                         		["height"]     = 1
		self.botaoElRioCentro1.bind                    		("<Button-1>",lambda e: popup("ElRio","Centro I",
															Info.ElRio.Centro1.IP, 
															Info.ElRio.Centro1.Porta, 
															Info.ElRio.Centro1.NumeroRep, 
															Info.ElRio.Centro1.Responsavel, 
															Info.ElRio.Centro1.Telefone))

		self.botaoElRioCentro1Relogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro1Relogio                  		["text"]       = "R"
		self.botaoElRioCentro1Relogio                  		["background"] = Info.ElRio.Centro1.RelogioCor
		self.botaoElRioCentro1Relogio                  		["height"]     = 1
		self.botaoElRioCentro1Relogio                  		["width"]      = 2


		self.botaoElRioCentro1.grid                    		(row=6,column=0,sticky = "N")
		self.botaoElRioCentro1Relogio.grid             		(row=6,column=1,sticky = "N")






		self.botaoElRioCentro2                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro2                         		["text"]       = "Centro II"
		self.botaoElRioCentro2                         		["background"] = Info.ElRio.Centro2.ModuloCor
		self.botaoElRioCentro2                         		["width"]      = 13
		self.botaoElRioCentro2                         		["height"]     = 1
		self.botaoElRioCentro2.bind                    		("<Button-1>",lambda e: popup("ElRio","Centro II",
															Info.ElRio.Centro2.IP, 
															Info.ElRio.Centro2.Porta, 
															Info.ElRio.Centro2.NumeroRep, 
															Info.ElRio.Centro2.Responsavel, 
															Info.ElRio.Centro2.Telefone))

		self.botaoElRioCentro2Relogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro2Relogio                  		["text"]       = "R"
		self.botaoElRioCentro2Relogio                  		["background"] = Info.ElRio.Centro2.RelogioCor
		self.botaoElRioCentro2Relogio                  		["height"]     = 1
		self.botaoElRioCentro2Relogio                  		["width"]      = 2

		self.botaoElRioCentro2.grid                    		(row=7,column=0,sticky = "N")
		self.botaoElRioCentro2Relogio.grid             		(row=7,column=1,sticky = "N")






		self.botaoElRioCentro3                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro3                         		["text"]       = "Centro III"
		self.botaoElRioCentro3                         		["background"] = Info.ElRio.Centro3.ModuloCor
		self.botaoElRioCentro3                         		["width"]      = 13
		self.botaoElRioCentro3                         		["height"]     = 1
		self.botaoElRioCentro3.bind                    		("<Button-1>",lambda e: popup("ElRio","Centro III",
															Info.ElRio.Centro3.IP, 
															Info.ElRio.Centro3.Porta, 
															Info.ElRio.Centro3.NumeroRep, 
															Info.ElRio.Centro3.Responsavel, 
															Info.ElRio.Centro3.Telefone))

		self.botaoElRioCentro3Relogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioCentro3Relogio                  		["text"]       = "R"
		self.botaoElRioCentro3Relogio                  		["background"] = Info.ElRio.Centro3.RelogioCor
		self.botaoElRioCentro3Relogio                  		["height"]     = 1
		self.botaoElRioCentro3Relogio                  		["width"]      = 2


		self.botaoElRioCentro3.grid             	       	(row=8,column=0,sticky = "N")
		self.botaoElRioCentro3Relogio.grid     	        	(row=8,column=1,sticky = "N")







		self.botaoElRioFashion                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioFashion                         		["text"]       = "Fashion"
		self.botaoElRioFashion                         		["background"] = Info.ElRio.Fashion.ModuloCor
		self.botaoElRioFashion                         		["width"]      = 13
		self.botaoElRioFashion                         		["height"]     = 1
		self.botaoElRioFashion.bind                    		("<Button-1>",lambda e: popup("ElRio","Fashion",
															Info.ElRio.Fashion.IP, 
															Info.ElRio.Fashion.Porta, 
															Info.ElRio.Fashion.NumeroRep, 
															Info.ElRio.Fashion.Responsavel, 
															Info.ElRio.Fashion.Telefone))

		self.botaoElRioFashionRelogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioFashionRelogio                  		["text"]       = "R"
		self.botaoElRioFashionRelogio                  		["background"] = Info.ElRio.Fashion.RelogioCor
		self.botaoElRioFashionRelogio                  		["height"]     = 1
		self.botaoElRioFashionRelogio                  		["width"]      = 2


		self.botaoElRioFashion.grid                    		(row=9,column=0,sticky = "N")
		self.botaoElRioFashionRelogio.grid             		(row=9,column=1,sticky = "N")





		self.botaoElRioFlamengo                         	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioFlamengo                         	["text"]       = "Flamengo"
		self.botaoElRioFlamengo                         	["background"] = Info.ElRio.Flamengo.ModuloCor
		self.botaoElRioFlamengo                         	["width"]      = 13
		self.botaoElRioFlamengo                         	["height"]     = 1
		self.botaoElRioFlamengo.bind                    	("<Button-1>",lambda e: popup("ElRio","Flamengo",
															Info.ElRio.Flamengo.IP, 
															Info.ElRio.Flamengo.Porta, 
															Info.ElRio.Flamengo.NumeroRep, 
															Info.ElRio.Flamengo.Responsavel, 
															Info.ElRio.Flamengo.Telefone))

		self.botaoElRioFlamengoRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioFlamengoRelogio                  	["text"]       = "R"
		self.botaoElRioFlamengoRelogio                  	["background"] = Info.ElRio.Flamengo.RelogioCor
		self.botaoElRioFlamengoRelogio                  	["height"]     = 1
		self.botaoElRioFlamengoRelogio                  	["width"]      = 2


		self.botaoElRioFlamengo.grid                    	(row=10,column=0,sticky = "N")
		self.botaoElRioFlamengoRelogio.grid             	(row=10,column=1,sticky = "N")






		self.botaoElRioLeblon                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioLeblon                         		["text"]       = "Leblon"
		self.botaoElRioLeblon                         		["background"] = Info.ElRio.Leblon.ModuloCor
		self.botaoElRioLeblon                         		["width"]      = 13
		self.botaoElRioLeblon                         		["height"]     = 1
		self.botaoElRioLeblon.bind                    		("<Button-1>",lambda e: popup("ElRio","Leblon",
															Info.ElRio.Leblon.IP, 
															Info.ElRio.Leblon.Porta, 
															Info.ElRio.Leblon.NumeroRep, 
															Info.ElRio.Leblon.Responsavel, 
															Info.ElRio.Leblon.Telefone))

		self.botaoElRioLeblonRelogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioLeblonRelogio                  		["text"]       = "R"
		self.botaoElRioLeblonRelogio                  		["background"] = Info.ElRio.Leblon.RelogioCor
		self.botaoElRioLeblonRelogio                  		["height"]     = 1
		self.botaoElRioLeblonRelogio                  		["width"]      = 2


		self.botaoElRioLeblon.grid                    		(row=11,column=0,sticky = "N")
		self.botaoElRioLeblonRelogio.grid             		(row=11,column=1,sticky = "N")






		self.botaoElRioNovaAmerica                      	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioNovaAmerica                         	["text"]       = "Nova America"
		self.botaoElRioNovaAmerica                         	["background"] = Info.ElRio.NovaAmerica.ModuloCor
		self.botaoElRioNovaAmerica                         	["width"]      = 13
		self.botaoElRioNovaAmerica                         	["height"]     = 1
		self.botaoElRioNovaAmerica.bind                    	("<Button-1>",lambda e: popup("ElRio","Nova America",
															Info.ElRio.NovaAmerica.IP, 
															Info.ElRio.NovaAmerica.Porta, 
															Info.ElRio.NovaAmerica.NumeroRep, 
															Info.ElRio.NovaAmerica.Responsavel, 
															Info.ElRio.NovaAmerica.Telefone))

		self.botaoElRioNovaAmericaRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioNovaAmericaRelogio                  	["text"]       = "R"
		self.botaoElRioNovaAmericaRelogio                  	["background"] = Info.ElRio.NovaAmerica.RelogioCor
		self.botaoElRioNovaAmericaRelogio                  	["height"]     = 1
		self.botaoElRioNovaAmericaRelogio                  	["width"]      = 2


		self.botaoElRioNovaAmerica.grid                    	(row=12,column=0,sticky = "N")
		self.botaoElRioNovaAmericaRelogio.grid             	(row=12,column=1,sticky = "N")






		self.botaoElRioShopGrande                         	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopGrande                         	["text"]       = "Shop Grande"
		self.botaoElRioShopGrande                         	["background"] = Info.ElRio.ShopGrande.ModuloCor
		self.botaoElRioShopGrande                         	["width"]      = 13
		self.botaoElRioShopGrande                         	["height"]     = 1
		self.botaoElRioShopGrande.bind                    	("<Button-1>",lambda e: popup("ElRio","Shop Grande",
															Info.ElRio.ShopGrande.IP, 
															Info.ElRio.ShopGrande.Porta, 
															Info.ElRio.ShopGrande.NumeroRep, 
															Info.ElRio.ShopGrande.Responsavel, 
															Info.ElRio.ShopGrande.Telefone))

		self.botaoElRioShopGrandeRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopGrandeRelogio                  	["text"]       = "R"
		self.botaoElRioShopGrandeRelogio                  	["background"] = Info.ElRio.ShopGrande.RelogioCor
		self.botaoElRioShopGrandeRelogio                  	["height"]     = 1
		self.botaoElRioShopGrandeRelogio                  	["width"]      = 2


		self.botaoElRioShopGrande.grid                    	(row=13,column=0,sticky = "N")
		self.botaoElRioShopGrandeRelogio.grid             	(row=13,column=1,sticky = "N")






		self.botaoElRioShopMacae                         	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopMacae                         	["text"]       = "Shop Macae"
		self.botaoElRioShopMacae                         	["background"] = Info.ElRio.ShopMacae.ModuloCor
		self.botaoElRioShopMacae                         	["width"]      = 13
		self.botaoElRioShopMacae                         	["height"]     = 1
		self.botaoElRioShopMacae.bind                    	("<Button-1>",lambda e: popup("ElRio","Shop Macae",
															Info.ElRio.ShopMacae.IP, 
															Info.ElRio.ShopMacae.Porta, 
															Info.ElRio.ShopMacae.NumeroRep, 
															Info.ElRio.ShopMacae.Responsavel, 
															Info.ElRio.ShopMacae.Telefone))

		self.botaoElRioShopMacaeRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopMacaeRelogio                  	["text"]       = "R"
		self.botaoElRioShopMacaeRelogio                  	["background"] = Info.ElRio.ShopMacae.RelogioCor
		self.botaoElRioShopMacaeRelogio                  	["height"]     = 1
		self.botaoElRioShopMacaeRelogio                  	["width"]      = 2


		self.botaoElRioShopMacae.grid                    	(row=14,column=0,sticky = "N")
		self.botaoElRioShopMacaeRelogio.grid             	(row=14,column=1,sticky = "N")






		self.botaoElRioShopNorte                         	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopNorte                         	["text"]       = "Shop Norte"
		self.botaoElRioShopNorte                         	["background"] = Info.ElRio.ShopNorte.ModuloCor
		self.botaoElRioShopNorte                         	["width"]      = 13
		self.botaoElRioShopNorte                         	["height"]     = 1
		self.botaoElRioShopNorte.bind                    	("<Button-1>",lambda e: popup("ElRio","Shop Norte",
															Info.ElRio.ShopNorte.IP, 
															Info.ElRio.ShopNorte.Porta, 
															Info.ElRio.ShopNorte.NumeroRep, 
															Info.ElRio.ShopNorte.Responsavel, 
															Info.ElRio.ShopNorte.Telefone))

		self.botaoElRioShopNorteRelogio                  	= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioShopNorteRelogio                  	["text"]       = "R"
		self.botaoElRioShopNorteRelogio                  	["background"] = Info.ElRio.ShopNorte.RelogioCor
		self.botaoElRioShopNorteRelogio                  	["height"]     = 1
		self.botaoElRioShopNorteRelogio                  	["width"]      = 2


		self.botaoElRioShopNorte.grid                    	(row=15,column=0,sticky = "N")
		self.botaoElRioShopNorteRelogio.grid             	(row=15,column=1,sticky = "N")






		self.botaoElRioBackup1                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBackup1                         		["text"]       = "Backup1"
		self.botaoElRioBackup1                         		["background"] = Info.ElRio.Backup1.ModuloCor
		self.botaoElRioBackup1                         		["width"]      = 13
		self.botaoElRioBackup1                         		["height"]     = 1
		self.botaoElRioBackup1.bind                    		("<Button-1>",lambda e: popup("ElRio","Backup1",
															Info.ElRio.Backup1.IP, 
															Info.ElRio.Backup1.Porta, 
															Info.ElRio.Backup1.NumeroRep, 
															Info.ElRio.Backup1.Responsavel, 
															Info.ElRio.Backup1.Telefone))

		self.botaoElRioBackup1Relogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBackup1Relogio                  		["text"]       = "R"
		self.botaoElRioBackup1Relogio                  		["background"] = Info.ElRio.Backup1.RelogioCor
		self.botaoElRioBackup1Relogio                  		["height"]     = 1
		self.botaoElRioBackup1Relogio                  		["width"]      = 2


		self.botaoElRioBackup1.grid                    		(row=16,column=0,sticky = "N")
		self.botaoElRioBackup1Relogio.grid             		(row=16,column=1,sticky = "N")






		self.botaoElRioBackup2                         		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBackup2                         		["text"]       = "Backup2"
		self.botaoElRioBackup2                         		["background"] = Info.ElRio.Backup2.ModuloCor
		self.botaoElRioBackup2                         		["width"]      = 13
		self.botaoElRioBackup2                         		["height"]     = 1
		self.botaoElRioBackup2.bind                    		("<Button-1>",lambda e: popup("ElRio","Backup2",
															Info.ElRio.Backup2.IP, 
															Info.ElRio.Backup2.Porta, 
															Info.ElRio.Backup2.NumeroRep, 
															Info.ElRio.Backup2.Responsavel, 
															Info.ElRio.Backup2.Telefone))

		self.botaoElRioBackup2Relogio                  		= Button(self.ContainerElRio, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoElRioBackup2Relogio                  		["text"]       = "R"
		self.botaoElRioBackup2Relogio                  		["background"] = Info.ElRio.Backup2.RelogioCor
		self.botaoElRioBackup2Relogio                  		["height"]     = 1
		self.botaoElRioBackup2Relogio                  		["width"]      = 2


		self.botaoElRioBackup2.grid                    		(row=17,column=0,sticky = "N")
		self.botaoElRioBackup2Relogio.grid             		(row=17,column=1,sticky = "N")



	def Create_Olimpark(self):

		self.msgOlimpark                              	= Label (self.ContainerOlimpark,text = "Olimpark",
														font = "arialblack 12 bold",bg="black",fg="white")
		self.msgOlimpark                              	["height"]     = 1
		self.msgOlimpark.grid                         	(row=0,column=0,sticky = "N")


		self.msgOlimparkCount                           = Label (self.ContainerOlimpark,
																text= str(Info.Olimpark.Status.Contage)+"/"+
																	str(Info.Olimpark.Status.TotalRelogios)
																	,font = "arial 11",bg="black",fg="white")	

		self.msgOlimparkCount                           ["height"]     = 1
		self.msgOlimparkCount.grid                      (row=1,column=1,pady=3.5,sticky = "N")



		self.botaoOlimparkAtencao                                        = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")

		self.botaoOlimparkAtencao                         ["text"]       = "A"
		self.botaoOlimparkAtencao                         ["height"]     = 1
		self.botaoOlimparkAtencao                         ["background"] = Info.Olimpark.Status.Atencao
		self.botaoOlimparkAtencao                         ["width"]      = 2

		self.botaoOlimparkAtencao.grid                     (row=0,column=1,sticky = "N")

		self.msgOlimparkHora                            		= Label (self.ContainerOlimpark,
															text =Info.Olimpark.Status.Horaultima,font = "arial 11",bg="black",fg="white")
		self.msgOlimparkHora                            		["height"]     = 1
		self.msgOlimparkHora.grid                       		(row=1,column=0,pady=3.5,sticky = "N")


		relo=Info.Olimpark.JdPaulista
		self.botaoOlimparkPaulista                         	= Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkPaulista                         	["text"]       = "JdPaulista"
		self.botaoOlimparkPaulista                         	["background"] = relo.ModuloCor
		self.botaoOlimparkPaulista                         	["width"]      = 13
		self.botaoOlimparkPaulista                         	["height"]     = 1
		self.botaoOlimparkPaulista.bind                    	("<Button-1>",lambda e: popup("Olimpark","JdPaulista",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkPaulistaRelogio                  	= Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkPaulistaRelogio                  	["text"]       = "R"
		self.botaoOlimparkPaulistaRelogio                  	["background"] = relo.RelogioCor
		self.botaoOlimparkPaulistaRelogio                  	["height"]     = 1
		self.botaoOlimparkPaulistaRelogio                  	["width"]      = 2


		self.botaoOlimparkPaulista.grid                    	(row=2,column=0,sticky = "N")
		self.botaoOlimparkPaulistaRelogio.grid             	(row=2,column=1,sticky = "N")





		relo=Info.Olimpark.SantaCecilia
		self.botaoOlimparkSantaCecilia                      = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkSantaCecilia                      ["text"]       = "Santa Cecilia"
		self.botaoOlimparkSantaCecilia                      ["background"] = relo.ModuloCor
		self.botaoOlimparkSantaCecilia                       ["width"]      = 13
		self.botaoOlimparkSantaCecilia                      ["height"]     = 1
		self.botaoOlimparkSantaCecilia.bind                 ("<Button-1>",lambda e: popup("Olimpark","Santa Cecilia",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkSantaCeciliaRelogio               = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkSantaCeciliaRelogio               ["text"]       = "R"
		self.botaoOlimparkSantaCeciliaRelogio               ["background"] = relo.RelogioCor
		self.botaoOlimparkSantaCeciliaRelogio               ["height"]     = 1
		self.botaoOlimparkSantaCeciliaRelogio               ["width"]      = 2


		self.botaoOlimparkSantaCecilia.grid                 (row=3,column=0,sticky = "N")
		self.botaoOlimparkSantaCeciliaRelogio.grid          (row=3,column=1,sticky = "N")





		relo=Info.Olimpark.VilaOlimpia
		self.botaoOlimparkVilaOlimpia                       = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkVilaOlimpia                       ["text"]       = "Vila Olimpia"
		self.botaoOlimparkVilaOlimpia                       ["background"] = relo.ModuloCor
		self.botaoOlimparkVilaOlimpia                        ["width"]      = 13
		self.botaoOlimparkVilaOlimpia                       ["height"]     = 1
		self.botaoOlimparkVilaOlimpia.bind                  ("<Button-1>",lambda e: popup("Olimpark","Vila Olimpia",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkVilaOlimpiaRelogio            	= Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkVilaOlimpiaRelogio                ["text"]       = "R"
		self.botaoOlimparkVilaOlimpiaRelogio                ["background"] = relo.RelogioCor
		self.botaoOlimparkVilaOlimpiaRelogio                ["height"]     = 1
		self.botaoOlimparkVilaOlimpiaRelogio                ["width"]      = 2


		self.botaoOlimparkVilaOlimpia.grid                  (row=4,column=0,sticky = "N")
		self.botaoOlimparkVilaOlimpiaRelogio.grid           (row=4,column=1,sticky = "N")





		relo=Info.Olimpark.Previdencia
		self.botaoOlimparkPrevidencia                       = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkPrevidencia                       ["text"]       = "Previdencia"
		self.botaoOlimparkPrevidencia                       ["background"] = relo.ModuloCor
		self.botaoOlimparkPrevidencia                        ["width"]      = 13
		self.botaoOlimparkPrevidencia                       ["height"]     = 1
		self.botaoOlimparkPrevidencia.bind                  ("<Button-1>",lambda e: popup("Olimpark","Previdencia",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkPrevidenciaRelogio                = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkPrevidenciaRelogio                ["text"]       = "R"
		self.botaoOlimparkPrevidenciaRelogio                ["background"] = relo.RelogioCor
		self.botaoOlimparkPrevidenciaRelogio                ["height"]     = 1
		self.botaoOlimparkPrevidenciaRelogio                ["width"]      = 2


		self.botaoOlimparkPrevidencia.grid                  (row=5,column=0,sticky = "N")
		self.botaoOlimparkPrevidenciaRelogio.grid           (row=5,column=1,sticky = "N")





		relo=Info.Olimpark.Belezinho
		self.botaoOlimparkBelezinho                         = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkBelezinho                         ["text"]       = "Belezinho"
		self.botaoOlimparkBelezinho                         ["background"] = relo.ModuloCor
		self.botaoOlimparkBelezinho                          ["width"]      = 13
		self.botaoOlimparkBelezinho                         ["height"]     = 1
		self.botaoOlimparkBelezinho.bind                    ("<Button-1>",lambda e: popup("Olimpark","Belezinho",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkBelezinhoRelogio                  = Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkBelezinhoRelogio                  ["text"]       = "R"
		self.botaoOlimparkBelezinhoRelogio                  ["background"] = relo.RelogioCor
		self.botaoOlimparkBelezinhoRelogio                  ["height"]     = 1
		self.botaoOlimparkBelezinhoRelogio                  ["width"]      = 2


		self.botaoOlimparkBelezinho.grid                    (row=6,column=0,sticky = "N")
		self.botaoOlimparkBelezinhoRelogio.grid             (row=6,column=1,sticky = "N")





		relo=Info.Olimpark.Santana
		self.botaoOlimparkSantana                         	= Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkSantana                         	["text"]       = "Santana"
		self.botaoOlimparkSantana                         	["background"] = relo.ModuloCor
		self.botaoOlimparkSantana                         	["width"]      = 13
		self.botaoOlimparkSantana                         	["height"]     = 1
		self.botaoOlimparkSantana.bind                    	("<Button-1>",lambda e: popup("Olimpark","Santana",
															relo.IP, 
															relo.Porta, 
															relo.NumeroRep, 
															relo.Responsavel, 
															relo.Telefone))

		self.botaoOlimparkSantanaRelogio                  	= Button(self.ContainerOlimpark, 
																				highlightbackground="black",
																				activebackground="black",
																				activeforeground="white")
																				
		self.botaoOlimparkSantanaRelogio                  	["text"]       = "R"
		self.botaoOlimparkSantanaRelogio                  	["background"] = relo.RelogioCor
		self.botaoOlimparkSantanaRelogio                  	["height"]     = 1
		self.botaoOlimparkSantanaRelogio                  	["width"]      = 2


		self.botaoOlimparkSantana.grid                    	(row=7,column=0,sticky = "N")
		self.botaoOlimparkSantanaRelogio.grid             	(row=7,column=1,sticky = "N")



	def Create_Fancold1(self):



		self.msgFancold1 									= Label (self.ContainerFancold1,
																text = "Fancold-1",
																font= "arialblack 12 bold",
																bg="black",
																fg="white")



		self.msgFancold1 									["height"] = 1

		self.msgFancold1.grid 							(row=0,column=0,sticky = "N")



		
		self.msgFancold1Contage  							= Label (self.ContainerFancold1,
																text = str(Info.Fancold1.Status.Contage)+"/"+
																str(Info.Fancold1.Status.TotalRelogios),
																font="arial 11",
																bg="black",
																fg="white")

	


		self.botaoFancold1Atencao                      	= Button(self.ContainerFancold1, 
														highlightbackground="black",
														activebackground="black",
														activeforeground="white")

		self.botaoFancold1Atencao                         ["text"]       = "A"
		self.botaoFancold1Atencao                         ["height"]     = 1
		self.botaoFancold1Atencao                         ["background"] = Info.Fancold1.Status.Atencao
		self.botaoFancold1Atencao                         ["width"]      = 2

		self.botaoFancold1Atencao.grid                     (row=0,column=1,sticky = "N")





		self.msgFancold1Contage.grid 						(row=1,column=1,pady=3.5, sticky = "N")



		self.msgFancold1Hora  							= Label (self.ContainerFancold1,
														text = Info.Fancold1.Status.Horaultima,
														font="arial 11",
														bg="black",
														fg="white")
																			
		self.msgFancold1Hora.grid 						(row=1,column=0,pady=3.5, sticky = "N")







		relo=Info.Fancold1.Givaudan
		self.botaoFancold1Givaudan                    	= Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1Givaudan                   	["text"]       = "Givaudan"
		self.botaoFancold1Givaudan                   	["background"] = relo.ModuloCor
		self.botaoFancold1Givaudan                  	["width"]      = 13
		self.botaoFancold1Givaudan                  	["height"]     = 1
		self.botaoFancold1Givaudan.bind             	("<Button-1>",lambda e: popup(
														"Fancold1",
														"Saint Gobain",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))

		self.botaoFancold1Givaudan.grid              	(row=2, column=0, sticky = "N")

		self.botaoFancold1GivaudanRelogio                           = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1GivaudanRelogio            	["text"]       = "R"
		self.botaoFancold1GivaudanRelogio            	["background"] = relo.RelogioCor
		self.botaoFancold1GivaudanRelogio            	["width"]      = 2
		self.botaoFancold1GivaudanRelogio            	["height"]     = 1
		self.botaoFancold1GivaudanRelogio.grid       	(row=2, column=1, sticky = "N")








		relo=Info.Fancold1.Yamaha
		self.botaoFancold1Yamaha                       = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1Yamaha                    	["text"]       = "Yamaha"
		self.botaoFancold1Yamaha                    	["background"] = relo.ModuloCor
		self.botaoFancold1Yamaha                     	["width"]      = 13
		self.botaoFancold1Yamaha                    	["height"]     = 1
		self.botaoFancold1Yamaha.bind               	("<Button-1>",lambda e: popup(
														"Fancold1",
														"PPM Secoia",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1Yamaha.grid               	(row=3,column=0,sticky = "N")


		self.botaoFancold1YamahaRelogio                = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1YamahaRelogio             	["text"]       = "R"
		self.botaoFancold1YamahaRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1YamahaRelogio             	["width"]      = 2
		self.botaoFancold1YamahaRelogio             	["height"]     = 1
		self.botaoFancold1YamahaRelogio.grid        	(row=3,column=1,sticky = "N")







		relo=Info.Fancold1.Odebrecht
		self.botaoFancold1Odebrecht                     = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1Odebrecht                     ["text"]       = "Odebrecht"
		self.botaoFancold1Odebrecht                     ["background"] = relo.ModuloCor
		self.botaoFancold1Odebrecht                     ["width"]      = 13
		self.botaoFancold1Odebrecht                     ["height"]     = 1
		self.botaoFancold1Odebrecht.bind               	("<Button-1>",lambda e: popup("Fancold1","Odebrecht",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1Odebrecht.grid                   	(row=4,column=0,sticky = "N")

		self.botaoFancold1OdebrechtRelogio                    = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")


		self.botaoFancold1OdebrechtRelogio                 	["text"]       = "R"
		self.botaoFancold1OdebrechtRelogio                 	["background"] = relo.RelogioCor
		self.botaoFancold1OdebrechtRelogio                 	["width"]      = 2
		self.botaoFancold1OdebrechtRelogio                 	["height"]     =  1
		self.botaoFancold1OdebrechtRelogio.grid            	(row=4,column=1,sticky = "N")





		relo=Info.Fancold1.HospJundiai
		self.botaoFancold1HospJundiai                        = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HospJundiai                   ["text"]       = "Hosp. Jundiai"
		self.botaoFancold1HospJundiai                   ["background"] = relo.ModuloCor
		self.botaoFancold1HospJundiai                   ["width"]      = 13
		self.botaoFancold1HospJundiai                   ["height"]     = 1
		self.botaoFancold1HospJundiai.bind              ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1HospJundiai.grid               	(row=5,column=0,sticky = "N")

		self.botaoFancold1HospJundiaiRelogio                            = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HospJundiaiRelogio             	["text"]       = "R"
		self.botaoFancold1HospJundiaiRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1HospJundiaiRelogio             	["width"]      = 2
		self.botaoFancold1HospJundiaiRelogio             	["height"]     =  1
		self.botaoFancold1HospJundiaiRelogio.grid        	(row=5,column=1,sticky = "N")




		relo=Info.Fancold1.EscritRioNegro
		self.botaoFancold1EscritRioNegro                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1EscritRioNegro                ["text"]       = "Esc.Rio Negro"
		self.botaoFancold1EscritRioNegro                ["background"] = relo.ModuloCor
		self.botaoFancold1EscritRioNegro                ["width"]      = 13
		self.botaoFancold1EscritRioNegro                ["height"]     = 1
		self.botaoFancold1EscritRioNegro.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1EscritRioNegro.grid               	(row=6,column=0,sticky = "N")

		self.botaoFancold1HospJundiaiRelogio                            = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HospJundiaiRelogio             	["text"]       = "R"
		self.botaoFancold1HospJundiaiRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1HospJundiaiRelogio             	["width"]      = 2
		self.botaoFancold1HospJundiaiRelogio             	["height"]     =  1
		self.botaoFancold1HospJundiaiRelogio.grid        	(row=6,column=1,sticky = "N")




		relo=Info.Fancold1.MorumbiPrime
		self.botaoFancold1MorumbiPrime                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MorumbiPrime                ["text"]       = "Morumbi Prime"
		self.botaoFancold1MorumbiPrime                ["background"] = relo.ModuloCor
		self.botaoFancold1MorumbiPrime                ["width"]      = 13
		self.botaoFancold1MorumbiPrime                ["height"]     = 1
		self.botaoFancold1MorumbiPrime.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1MorumbiPrime.grid               	(row=7,column=0,sticky = "N")

		self.botaoFancold1MorumbiPrimeRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MorumbiPrimeRelogio             	["text"]       = "R"
		self.botaoFancold1MorumbiPrimeRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1MorumbiPrimeRelogio             	["width"]      = 2
		self.botaoFancold1MorumbiPrimeRelogio             	["height"]     =  1
		self.botaoFancold1MorumbiPrimeRelogio.grid        	(row=7,column=1,sticky = "N")




		relo=Info.Fancold1.HospMarioCovas
		self.botaoFancold1HospMarioCovas                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HospMarioCovas                ["text"]       = "Hosp. Mario Covas"
		self.botaoFancold1HospMarioCovas                ["background"] = relo.ModuloCor
		self.botaoFancold1HospMarioCovas                ["width"]      = 13
		self.botaoFancold1HospMarioCovas                ["height"]     = 1
		self.botaoFancold1HospMarioCovas.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1HospMarioCovas.grid               	(row=8,column=0,sticky = "N")

		self.botaoFancold1HospMarioCovasRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HospMarioCovasRelogio             	["text"]       = "R"
		self.botaoFancold1HospMarioCovasRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1HospMarioCovasRelogio             	["width"]      = 2
		self.botaoFancold1HospMarioCovasRelogio             	["height"]     =  1
		self.botaoFancold1HospMarioCovasRelogio.grid        	(row=8,column=1,sticky = "N")




		relo=Info.Fancold1.CondVerboDivino
		self.botaoFancold1CondVerboDivino                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondVerboDivino                ["text"]       = "Cond. Verbo Divino"
		self.botaoFancold1CondVerboDivino                ["background"] = relo.ModuloCor
		self.botaoFancold1CondVerboDivino                ["width"]      = 13
		self.botaoFancold1CondVerboDivino                ["height"]     = 1
		self.botaoFancold1CondVerboDivino.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1CondVerboDivino.grid               	(row=9,column=0,sticky = "N")

		self.botaoFancold1CondVerboDivinoRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondVerboDivinoRelogio             	["text"]       = "R"
		self.botaoFancold1CondVerboDivinoRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1CondVerboDivinoRelogio             	["width"]      = 2
		self.botaoFancold1CondVerboDivinoRelogio             	["height"]     =  1
		self.botaoFancold1CondVerboDivinoRelogio.grid        	(row=9,column=1,sticky = "N")




		relo=Info.Fancold1.HelborBerrini
		self.botaoFancold1HelborBerrini                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HelborBerrini                ["text"]       = "Helbor Berrini"
		self.botaoFancold1HelborBerrini                ["background"] = relo.ModuloCor
		self.botaoFancold1HelborBerrini                ["width"]      = 13
		self.botaoFancold1HelborBerrini                ["height"]     = 1
		self.botaoFancold1HelborBerrini.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1HelborBerrini.grid               	(row=10,column=0,sticky = "N")

		self.botaoFancold1HelborBerriniRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HelborBerriniRelogio             	["text"]       = "R"
		self.botaoFancold1HelborBerriniRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1HelborBerriniRelogio             	["width"]      = 2
		self.botaoFancold1HelborBerriniRelogio             	["height"]     =  1
		self.botaoFancold1HelborBerriniRelogio.grid        	(row=10,column=1,sticky = "N")




		relo=Info.Fancold1.PortoAtlantico
		self.botaoFancold1PortoAtlantico                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1PortoAtlantico                ["text"]       = "Porto Atlantico"
		self.botaoFancold1PortoAtlantico                ["background"] = relo.ModuloCor
		self.botaoFancold1PortoAtlantico                ["width"]      = 13
		self.botaoFancold1PortoAtlantico                ["height"]     = 1
		self.botaoFancold1PortoAtlantico.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1PortoAtlantico.grid               	(row=11,column=0,sticky = "N")

		self.botaoFancold1PortoAtlanticoRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1PortoAtlanticoRelogio             	["text"]       = "R"
		self.botaoFancold1PortoAtlanticoRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1PortoAtlanticoRelogio             	["width"]      = 2
		self.botaoFancold1PortoAtlanticoRelogio             	["height"]     =  1
		self.botaoFancold1PortoAtlanticoRelogio.grid        	(row=11,column=1,sticky = "N")




		relo=Info.Fancold1.AwpFreiGaspar
		self.botaoFancold1AwpFreiGaspar                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1AwpFreiGaspar                ["text"]       = "AWP Frei Gaspar"
		self.botaoFancold1AwpFreiGaspar                ["background"] = relo.ModuloCor
		self.botaoFancold1AwpFreiGaspar                ["width"]      = 13
		self.botaoFancold1AwpFreiGaspar                ["height"]     = 1
		self.botaoFancold1AwpFreiGaspar.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1AwpFreiGaspar.grid               	(row=12,column=0,sticky = "N")

		self.botaoFancold1AwpFreiGasparRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1AwpFreiGasparRelogio             	["text"]       = "R"
		self.botaoFancold1AwpFreiGasparRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1AwpFreiGasparRelogio             	["width"]      = 2
		self.botaoFancold1AwpFreiGasparRelogio             	["height"]     =  1
		self.botaoFancold1AwpFreiGasparRelogio.grid        	(row=12,column=1,sticky = "N")




		relo=Info.Fancold1.PrestCold
		self.botaoFancold1PrestCold                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1PrestCold                ["text"]       = "Prest Cold"
		self.botaoFancold1PrestCold                ["background"] = relo.ModuloCor
		self.botaoFancold1PrestCold                ["width"]      = 13
		self.botaoFancold1PrestCold                ["height"]     = 1
		self.botaoFancold1PrestCold.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1PrestCold.grid               	(row=13,column=0,sticky = "N")

		self.botaoFancold1PrestColdRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1PrestColdRelogio             	["text"]       = "R"
		self.botaoFancold1PrestColdRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1PrestColdRelogio             	["width"]      = 2
		self.botaoFancold1PrestColdRelogio             	["height"]     =  1
		self.botaoFancold1PrestColdRelogio.grid        	(row=13,column=1,sticky = "N")




		relo=Info.Fancold1.UnimedSantos
		self.botaoFancold1UnimedSantos                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1UnimedSantos                ["text"]       = "Unimed Santos"
		self.botaoFancold1UnimedSantos                ["background"] = relo.ModuloCor
		self.botaoFancold1UnimedSantos                ["width"]      = 13
		self.botaoFancold1UnimedSantos                ["height"]     = 1
		self.botaoFancold1UnimedSantos.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1UnimedSantos.grid               	(row=14,column=0,sticky = "N")

		self.botaoFancold1UnimedSantosRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1UnimedSantosRelogio             	["text"]       = "R"
		self.botaoFancold1UnimedSantosRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1UnimedSantosRelogio             	["width"]      = 2
		self.botaoFancold1UnimedSantosRelogio             	["height"]     =  1
		self.botaoFancold1UnimedSantosRelogio.grid        	(row=14,column=1,sticky = "N")




		relo=Info.Fancold1.CruzadaBandeirante
		self.botaoFancold1CruzadaBandeirante                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CruzadaBandeirante                ["text"]       = "Cruzada Bandeirante"
		self.botaoFancold1CruzadaBandeirante                ["background"] = relo.ModuloCor
		self.botaoFancold1CruzadaBandeirante                ["width"]      = 13
		self.botaoFancold1CruzadaBandeirante                ["height"]     = 1
		self.botaoFancold1CruzadaBandeirante.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1CruzadaBandeirante.grid               	(row=15,column=0,sticky = "N")

		self.botaoFancold1CruzadaBandeiranteRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CruzadaBandeiranteRelogio             	["text"]       = "R"
		self.botaoFancold1CruzadaBandeiranteRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1CruzadaBandeiranteRelogio             	["width"]      = 2
		self.botaoFancold1CruzadaBandeiranteRelogio             	["height"]     =  1
		self.botaoFancold1CruzadaBandeiranteRelogio.grid        	(row=15,column=1,sticky = "N")




		relo=Info.Fancold1.ColgateAnchieta
		self.botaoFancold1ColgateAnchieta                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1ColgateAnchieta                ["text"]       = "Colgate Anchieta"
		self.botaoFancold1ColgateAnchieta                ["background"] = relo.ModuloCor
		self.botaoFancold1ColgateAnchieta                ["width"]      = 13
		self.botaoFancold1ColgateAnchieta                ["height"]     = 1
		self.botaoFancold1ColgateAnchieta.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1ColgateAnchieta.grid               	(row=16,column=0,sticky = "N")

		self.botaoFancold1ColgateAnchietaRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1ColgateAnchietaRelogio             	["text"]       = "R"
		self.botaoFancold1ColgateAnchietaRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1ColgateAnchietaRelogio             	["width"]      = 2
		self.botaoFancold1ColgateAnchietaRelogio             	["height"]     =  1
		self.botaoFancold1ColgateAnchietaRelogio.grid        	(row=16,column=1,sticky = "N")




		relo=Info.Fancold1.MDCaieiras
		self.botaoFancold1MDCaieiras                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MDCaieiras                ["text"]       = "MD Caieiras"
		self.botaoFancold1MDCaieiras                ["background"] = relo.ModuloCor
		self.botaoFancold1MDCaieiras                ["width"]      = 13
		self.botaoFancold1MDCaieiras                ["height"]     = 1
		self.botaoFancold1MDCaieiras.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1MDCaieiras.grid               	(row=17,column=0,sticky = "N")

		self.botaoFancold1MDCaieirasRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MDCaieirasRelogio             	["text"]       = "R"
		self.botaoFancold1MDCaieirasRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1MDCaieirasRelogio             	["width"]      = 2
		self.botaoFancold1MDCaieirasRelogio             	["height"]     =  1
		self.botaoFancold1MDCaieirasRelogio.grid        	(row=17,column=1,sticky = "N")




		relo=Info.Fancold1.CondMandarim
		self.botaoFancold1CondMandarim                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondMandarim                ["text"]       = "Cond. Mandarim"
		self.botaoFancold1CondMandarim                ["background"] = relo.ModuloCor
		self.botaoFancold1CondMandarim                ["width"]      = 13
		self.botaoFancold1CondMandarim                ["height"]     = 1
		self.botaoFancold1CondMandarim.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1CondMandarim.grid               	(row=18,column=0,sticky = "N")

		self.botaoFancold1CondMandarimRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondMandarimRelogio             	["text"]       = "R"
		self.botaoFancold1CondMandarimRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1CondMandarimRelogio             	["width"]      = 2
		self.botaoFancold1CondMandarimRelogio             	["height"]     =  1
		self.botaoFancold1CondMandarimRelogio.grid        	(row=18,column=1,sticky = "N")




		relo=Info.Fancold1.RhodiaPoliamida
		self.botaoFancold1RhodiaPoliamida                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1RhodiaPoliamida                ["text"]       = "Rhodia Poliamida"
		self.botaoFancold1RhodiaPoliamida                ["background"] = relo.ModuloCor
		self.botaoFancold1RhodiaPoliamida                ["width"]      = 13
		self.botaoFancold1RhodiaPoliamida                ["height"]     = 1
		self.botaoFancold1RhodiaPoliamida.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1RhodiaPoliamida.grid               	(row=19,column=0,sticky = "N")

		self.botaoFancold1RhodiaPoliamidaRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1RhodiaPoliamidaRelogio             	["text"]       = "R"
		self.botaoFancold1RhodiaPoliamidaRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1RhodiaPoliamidaRelogio             	["width"]      = 2
		self.botaoFancold1RhodiaPoliamidaRelogio             	["height"]     =  1
		self.botaoFancold1RhodiaPoliamidaRelogio.grid        	(row=19,column=1,sticky = "N")




		relo=Info.Fancold1.BarraTradePrime
		self.botaoFancold1BarraTradePrime                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1BarraTradePrime                ["text"]       = "Barra Trade Prime"
		self.botaoFancold1BarraTradePrime                ["background"] = relo.ModuloCor
		self.botaoFancold1BarraTradePrime                ["width"]      = 13
		self.botaoFancold1BarraTradePrime                ["height"]     = 1
		self.botaoFancold1BarraTradePrime.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1BarraTradePrime.grid               	(row=20,column=0,sticky = "N")

		self.botaoFancold1BarraTradePrimeRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1BarraTradePrimeRelogio             	["text"]       = "R"
		self.botaoFancold1BarraTradePrimeRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1BarraTradePrimeRelogio             	["width"]      = 2
		self.botaoFancold1BarraTradePrimeRelogio             	["height"]     =  1
		self.botaoFancold1BarraTradePrimeRelogio.grid        	(row=20,column=1,sticky = "N")




		relo=Info.Fancold1.NovaSPCMF
		self.botaoFancold1NovaSPCMF                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1NovaSPCMF                ["text"]       = "Nova SPCMF"
		self.botaoFancold1NovaSPCMF                ["background"] = relo.ModuloCor
		self.botaoFancold1NovaSPCMF                ["width"]      = 13
		self.botaoFancold1NovaSPCMF                ["height"]     = 1
		self.botaoFancold1NovaSPCMF.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1NovaSPCMF.grid               	(row=21,column=0,sticky = "N")

		self.botaoFancold1NovaSPCMFRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1NovaSPCMFRelogio             	["text"]       = "R"
		self.botaoFancold1NovaSPCMFRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1NovaSPCMFRelogio             	["width"]      = 2
		self.botaoFancold1NovaSPCMFRelogio             	["height"]     =  1
		self.botaoFancold1NovaSPCMFRelogio.grid        	(row=21,column=1,sticky = "N")




		relo=Info.Fancold1.UnimedPamplona
		self.botaoFancold1UnimedPamplona                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1UnimedPamplona                ["text"]       = "Unimed Pamplona"
		self.botaoFancold1UnimedPamplona                ["background"] = relo.ModuloCor
		self.botaoFancold1UnimedPamplona                ["width"]      = 13
		self.botaoFancold1UnimedPamplona                ["height"]     = 1
		self.botaoFancold1UnimedPamplona.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1UnimedPamplona.grid               	(row=22,column=0,sticky = "N")

		self.botaoFancold1UnimedPamplonaRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1UnimedPamplonaRelogio             	["text"]       = "R"
		self.botaoFancold1UnimedPamplonaRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1UnimedPamplonaRelogio             	["width"]      = 2
		self.botaoFancold1UnimedPamplonaRelogio             	["height"]     =  1
		self.botaoFancold1UnimedPamplonaRelogio.grid        	(row=22,column=1,sticky = "N")




		relo=Info.Fancold1.Ushin
		self.botaoFancold1Ushin                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1Ushin                ["text"]       = "Ushin"
		self.botaoFancold1Ushin                ["background"] = relo.ModuloCor
		self.botaoFancold1Ushin                ["width"]      = 13
		self.botaoFancold1Ushin                ["height"]     = 1
		self.botaoFancold1Ushin.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1Ushin.grid               	(row=23,column=0,sticky = "N")

		self.botaoFancold1UshinRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1UshinRelogio             	["text"]       = "R"
		self.botaoFancold1UshinRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1UshinRelogio             	["width"]      = 2
		self.botaoFancold1UshinRelogio             	["height"]     =  1
		self.botaoFancold1UshinRelogio.grid        	(row=23,column=1,sticky = "N")




		relo=Info.Fancold1.CondManagerCenter
		self.botaoFancold1CondManagerCenter                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondManagerCenter                ["text"]       = "Cond. Manager Center"
		self.botaoFancold1CondManagerCenter                ["background"] = relo.ModuloCor
		self.botaoFancold1CondManagerCenter                ["width"]      = 13
		self.botaoFancold1CondManagerCenter                ["height"]     = 1
		self.botaoFancold1CondManagerCenter.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1CondManagerCenter.grid               	(row=24,column=0,sticky = "N")

		self.botaoFancold1CondManagerCenterRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1CondManagerCenterRelogio             	["text"]       = "R"
		self.botaoFancold1CondManagerCenterRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1CondManagerCenterRelogio             	["width"]      = 2
		self.botaoFancold1CondManagerCenterRelogio             	["height"]     =  1
		self.botaoFancold1CondManagerCenterRelogio.grid        	(row=24,column=1,sticky = "N")




		relo=Info.Fancold1.ChoiceSublimeRJ
		self.botaoFancold1ChoiceSublimeRJ                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1ChoiceSublimeRJ                ["text"]       = "Choice Sublime RJ"
		self.botaoFancold1ChoiceSublimeRJ                ["background"] = relo.ModuloCor
		self.botaoFancold1ChoiceSublimeRJ                ["width"]      = 13
		self.botaoFancold1ChoiceSublimeRJ                ["height"]     = 1
		self.botaoFancold1ChoiceSublimeRJ.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1ChoiceSublimeRJ.grid               	(row=25,column=0,sticky = "N")

		self.botaoFancold1ChoiceSublimeRJRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1ChoiceSublimeRJRelogio             	["text"]       = "R"
		self.botaoFancold1ChoiceSublimeRJRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1ChoiceSublimeRJRelogio             	["width"]      = 2
		self.botaoFancold1ChoiceSublimeRJRelogio             	["height"]     =  1
		self.botaoFancold1ChoiceSublimeRJRelogio.grid        	(row=25,column=1,sticky = "N")




		relo=Info.Fancold1.HelborMogiDasCruzes
		self.botaoFancold1HelborMogiDasCruzes                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HelborMogiDasCruzes                ["text"]       = "Helbor Mogi Das Cruzes"
		self.botaoFancold1HelborMogiDasCruzes                ["background"] = relo.ModuloCor
		self.botaoFancold1HelborMogiDasCruzes                ["width"]      = 13
		self.botaoFancold1HelborMogiDasCruzes                ["height"]     = 1
		self.botaoFancold1HelborMogiDasCruzes.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1HelborMogiDasCruzes.grid               	(row=26,column=0,sticky = "N")

		self.botaoFancold1HelborMogiDasCruzesRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1HelborMogiDasCruzesRelogio             	["text"]       = "R"
		self.botaoFancold1HelborMogiDasCruzesRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1HelborMogiDasCruzesRelogio             	["width"]      = 2
		self.botaoFancold1HelborMogiDasCruzesRelogio             	["height"]     =  1
		self.botaoFancold1HelborMogiDasCruzesRelogio.grid        	(row=26,column=1,sticky = "N")



		relo=Info.Fancold1.AWPTomeDeSouza
		self.botaoFancold1AWPTomeDeSouza                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1AWPTomeDeSouza                ["text"]       = "AWP Tome De Souza"
		self.botaoFancold1AWPTomeDeSouza                ["background"] = relo.ModuloCor
		self.botaoFancold1AWPTomeDeSouza                ["width"]      = 13
		self.botaoFancold1AWPTomeDeSouza                ["height"]     = 1
		self.botaoFancold1AWPTomeDeSouza.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1AWPTomeDeSouza.grid               	(row=27,column=0,sticky = "N")

		self.botaoFancold1AWPTomeDeSouzaRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1AWPTomeDeSouzaRelogio             	["text"]       = "R"
		self.botaoFancold1AWPTomeDeSouzaRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1AWPTomeDeSouzaRelogio             	["width"]      = 2
		self.botaoFancold1AWPTomeDeSouzaRelogio             	["height"]     =  1
		self.botaoFancold1AWPTomeDeSouzaRelogio.grid        	(row=27,column=1,sticky = "N")




		relo=Info.Fancold1.EmilioRibas
		self.botaoFancold1EmilioRibas                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1EmilioRibas                ["text"]       = "Emilio Ribas"
		self.botaoFancold1EmilioRibas                ["background"] = relo.ModuloCor
		self.botaoFancold1EmilioRibas                ["width"]      = 13
		self.botaoFancold1EmilioRibas                ["height"]     = 1
		self.botaoFancold1EmilioRibas.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1EmilioRibas.grid               	(row=28,column=0,sticky = "N")

		self.botaoFancold1EmilioRibasRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1EmilioRibasRelogio             	["text"]       = "R"
		self.botaoFancold1EmilioRibasRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1EmilioRibasRelogio             	["width"]      = 2
		self.botaoFancold1EmilioRibasRelogio             	["height"]     =  1
		self.botaoFancold1EmilioRibasRelogio.grid        	(row=28,column=1,sticky = "N")




		relo=Info.Fancold1.OnThePark
		self.botaoFancold1OnThePark                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1OnThePark                ["text"]       = "On The Park"
		self.botaoFancold1OnThePark                ["background"] = relo.ModuloCor
		self.botaoFancold1OnThePark                ["width"]      = 13
		self.botaoFancold1OnThePark                ["height"]     = 1
		self.botaoFancold1OnThePark.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1OnThePark.grid               	(row=29,column=0,sticky = "N")

		self.botaoFancold1OnTheParkRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1OnTheParkRelogio             	["text"]       = "R"
		self.botaoFancold1OnTheParkRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1OnTheParkRelogio             	["width"]      = 2
		self.botaoFancold1OnTheParkRelogio             	["height"]     =  1
		self.botaoFancold1OnTheParkRelogio.grid        	(row=29,column=1,sticky = "N")




		lo=Info.Fancold1.MaayanRJ
		self.botaoFancold1MaayanRJ                      = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MaayanRJ                ["text"]       = "Maayan RJ"
		self.botaoFancold1MaayanRJ                ["background"] = relo.ModuloCor
		self.botaoFancold1MaayanRJ                ["width"]      = 13
		self.botaoFancold1MaayanRJ                ["height"]     = 1
		self.botaoFancold1MaayanRJ.bind           ("<Button-1>",lambda e: popup("Fancold1","HospJundiai",
														relo.IP, 
														relo.Porta, 
														relo.NumeroRep, 
														relo.Responsavel, 
														relo.Telefone))
		self.botaoFancold1MaayanRJ.grid               	(row=30,column=0,sticky = "N")

		self.botaoFancold1MaayanRJRelogio                  = Button(self.ContainerFancold1, 
																	highlightbackground="black",
																	activebackground="black",
																	activeforeground="white")

		self.botaoFancold1MaayanRJRelogio             	["text"]       = "R"
		self.botaoFancold1MaayanRJRelogio             	["background"] = relo.RelogioCor
		self.botaoFancold1MaayanRJRelogio             	["width"]      = 2
		self.botaoFancold1MaayanRJRelogio             	["height"]     =  1
		self.botaoFancold1MaayanRJRelogio.grid        	(row=30,column=1,sticky = "N")


	def resize(self,event):
		self.ContainerPai.config(width=event.width,height=event.height)
		#print event.width 
		#print event.height
		self.cavatura.configure(width=event.width-15,height=event.height-15)

	def on_configure(self,event):
		#canvas_width = event.width
		#self.canvas.itemconfig(self.frame_ID, width = event.width, height=event.height)
		self.cavatura.configure(scrollregion=self.cavatura.bbox('all'))
		#print event.width 
		#print event.height
		#self.cavatura.config(width=event.width,height=event.height)
		



	def Create_ContainerGeral(self,root):

		#self.ContainerRelogios = Frame (root)
		#self.ContainerRelogios.grid               (row=0, column= 0 ,sticky = N + S + E + W)
		self.Create_ContainerGeralResize(root)

	def Create_ContainerGeralResize(self,root):



		self.ContainerPai = Canvas (root,border = 0)
		self.ContainerPai.grid               (row=0, column= 0 ,sticky = N + S + E + W)
		self.ContainerPai.bind('<Configure>', self.resize)

		self.cavatura = Canvas(self.ContainerPai,border = 0)
		self.cavatura.configure(width=800,height=500)
		self.cavatura.grid               (row=0, column= 0 ,sticky = N + S + E + W)	
		self.ContainerRelogios		      = Canvas (self.cavatura,border = 0)
	
		self.ScrollBar					  = Scrollbar(self.ContainerPai,command=self.cavatura.yview,orient = VERTICAL)
		self.ScrollBar.grid(row=0, column= 1 ,sticky = N + S + E + W)
		self.ScrollBar2					  = Scrollbar(self.ContainerPai,command=self.cavatura.xview,orient = HORIZONTAL)
		self.ScrollBar2.grid(row=1, column= 0 ,sticky =  N + S + E + W)
		#self.cavatura.configure(scrollregion=self.cavatura.bbox('all'))
		self.cavatura.config(xscrollcommand = self.ScrollBar2.set,yscrollcommand = self.ScrollBar.set)
							


		self.cavatura.bind('<Configure>', self.on_configure)

	

		self.ContainerPai.configure(bg="black")
		self.cavatura.configure(bg="black")
		self.ScrollBar.configure(bg="gray33",troughcolor="black",activebackground="gray")
		self.ScrollBar2.configure(bg="gray33",troughcolor="black",activebackground="gray")



		self.frame_ID =self.cavatura.create_window((0,0), window = self.ContainerRelogios, anchor='nw')
		#self.ContainerRelogios.grid               (row=0, column= 0 ,sticky = N + S + E + W)

		#self.ContainerPai		      = Frame (root)
		#self.ContainerPai.grid               (row=0, column= 0 ,sticky = N + S + E + W)
		#self.canvas = Canvas(self.ContainerPai)
		#self.canvas.config(height=900,width=1950)
		#self.canvas.pack(side=LEFT,expand = True)


		#self.ScrollBar					  = Scrollbar(self.ContainerPai,command=self.canvas.yview)
		#self.ScrollBar.pack(side=LEFT,fill=Y,expand = True)
		#self.canvas.config(yscrollcommand = self.ScrollBar.set)#,height=800,width=1900)

		#self.canvas.bind('<Configure>', self.on_configure)

		#self.ContainerRelogios		      = Frame (self.canvas)#height=800,width=1900 )
		#self.ContainerRelogios.pack(expand = YES)
		#self.canvas.configure(scrollregion=self.canvas.bbox('all'))
		#self.frame_ID =self.canvas.create_window((0,0), window = self.ContainerRelogios, anchor='nw')
		#self.ContainerRelogios.grid               (row=0, column= 0 ,sticky = N + S + E + W)

	def Create_ContainerColuna0(self,root):


		self.ContainerColuna0             			= Frame (self.ContainerRelogios)
		
		self.ContainerCasaCristo          			= Frame (self.ContainerColuna0)
		self.ContainerBestInClass         			= Frame (self.ContainerColuna0)
		self.ContainerIsoRadio			  			= Frame (self.ContainerColuna0)


		self.ContainerColuna0.grid                	(row=0, column=0,pady=5, padx=3, columnspan=1, sticky="N")
		self.ContainerCasaCristo.grid             	(row=0, column=0,pady=0, padx=3, columnspan=1, sticky="N")
		self.ContainerBestInClass.grid            	(row=1, column=0,pady=0, padx=3, columnspan=1, sticky="N")
		self.ContainerIsoRadio.grid               	(row=2, column=0,pady=0, padx=3, columnspan=1, sticky="N")

		self.ContainerRelogios.configure(bg="black")
		self.ContainerCasaCristo.configure(bg="black")
		self.ContainerBestInClass.configure(bg="black")
		self.ContainerIsoRadio.configure(bg="black")
		self.ContainerColuna0.configure(bg="black")

	def Create_ContainerColuna1(self,root):


		self.ContainerColuna1             			= Frame (self.ContainerRelogios)
		self.ContainerLotten              			= Frame (self.ContainerColuna1)
		self.ContainerGrupoNk             			= Frame (self.ContainerColuna1)


		self.ContainerColuna1.grid                	(row=0, column=1, pady=5 ,padx=3, columnspan=1, sticky="N")
		self.ContainerLotten.grid                 	(row=1, column=0, pady=0 ,padx=3, columnspan=1, sticky="N")
		self.ContainerGrupoNk.grid                 	(row=2, column=0, pady=0 ,padx=3, columnspan=1, sticky="N")

		self.ContainerColuna1.configure(bg="black")
		self.ContainerLotten.configure(bg="black")
		self.ContainerGrupoNk.configure(bg="black")

	def Create_ContainerColuna2(self,root):


		self.ContainerColuna2             			= Frame (self.ContainerRelogios)
		self.ContainerGravex              			= Frame (self.ContainerColuna2)
		self.ContainerElRio							= Frame (self.ContainerColuna2)
		self.ContainerOlimpark						= Frame (self.ContainerColuna2)


		self.ContainerColuna2.grid                	(row=0, column=2,pady=5, padx=3, columnspan=1, sticky="N")
		self.ContainerGravex.grid                 	(row=0, column=0,pady=0, padx=3, columnspan=1, sticky="N")
		self.ContainerElRio.grid 					(row=1, column=0,pady=0, padx=3, columnspan=1, sticky="N")
		self.ContainerOlimpark.grid 				(row=2, column=0,pady=0, padx=3, columnspan=1, sticky="N")


		self.ContainerColuna2.configure(bg="black")
		self.ContainerGravex.configure(bg="black")
		self.ContainerElRio.configure(bg="black")
		self.ContainerOlimpark.configure(bg="black")

	def Create_ContainerColuna3(self,root):


		self.ContainerColuna3             = Frame (self.ContainerRelogios)
		self.ContainerPredman             = Frame (self.ContainerColuna3)
		self.ContainerUniman              = Frame (self.ContainerColuna3)
		self.ContainerMilenioErvas        = Frame (self.ContainerColuna3)
		
		self.ContainerColuna3.grid                	(row=0, column=3,pady=5  , padx=3, columnspan=1, sticky="N")
		self.ContainerPredman.grid                	(row=0, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 	(row=1, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")
		self.ContainerMilenioErvas.grid           	(row=2, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")

	
		self.ContainerColuna3.configure(bg="black")
		self.ContainerPredman.configure(bg="black")
		self.ContainerUniman.configure(bg="black")
		self.ContainerMilenioErvas.configure(bg="black")
	

	def Create_ContainerColuna4(self,root):


		self.ContainerColuna4             			= Frame (self.ContainerRelogios)
		self.ContainerTarek              			= Frame (self.ContainerColuna4)
		self.ContainerBuilding           			= Frame (self.ContainerColuna4)
		self.ContainerLaser               			= Frame (self.ContainerColuna4)
		self.ContainerSBCP				 			= Frame (self.ContainerColuna4)


		self.ContainerColuna4.grid                	(row=0, column=4,pady=5  , padx=3, columnspan=1, sticky="N")
		self.ContainerTarek.grid                  	(row=0, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")
		self.ContainerBuilding.grid               	(row=1, column=0,pady=3.5, padx=3, columnspan=1 ,sticky="N")
		self.ContainerLaser.grid                  	(row=2, column=0,pady=3.5 ,padx=3, columnspan=1, sticky="N")
		self.ContainerSBCP.grid 					(row=3, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")



	def Create_ContainerColuna5(self,root):


		self.ContainerColuna5             			= Frame (self.ContainerRelogios)
		self.ContainerFancold1       				= Frame (self.ContainerColuna5)


		self.ContainerColuna5.grid               	(row=0, column=5,pady=5  , padx=3, columnspan=1, sticky="N")
		self.ContainerFancold1.grid           		(row=0, column=0,pady=3.5, padx=3, columnspan=1, sticky="N")

		self.ContainerFancold1.configure(bg="black")
		self.ContainerColuna5.configure(bg="black")



	def Create_ContainerColuna6(self,root):


		self.ContainerColuna6             = Frame (self.ContainerRelogios)
		#self.ContainerUniman              = Frame (self.ContainerColuna6)


		self.ContainerColuna6.grid                (row=0, column=6,pady=5, padx=1, columnspan=1, sticky="N")
		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna7(self,root):

		self.ContainerColuna7             = Frame (self.ContainerRelogios)
		#self.ContainerUniman              = Frame (self.ContainerColuna7)

		self.ContainerColuna7.grid                (row=0, column=7,pady=5, padx=1, columnspan=1, sticky="N")
		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna8(self,root):


		self.ContainerColuna8             = Frame (self.ContainerRelogios)
		#self.ContainerUniman              = Frame (self.ContainerColuna8)
		

		self.ContainerColuna8.grid                (row=0, column=8,pady=5, padx=1, columnspan=1, sticky="N")
		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna9(self,root):

		self.ContainerColuna9             = Frame (self.ContainerRelogios)
		#self.ContainerUniman              = Frame (self.ContainerColuna9)
		

		self.ContainerColuna9.grid                (row=0, column=9,pady=5, padx=1, columnspan=1, sticky="N")

		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna10(self,root):

	
		self.ContainerColuna10             = Frame (self.ContainerRelogios)
		
		#self.ContainerUniman              = Frame (self.ContainerColuna10)

		self.ContainerColuna10.grid                (row=0, column=10,pady=5, padx=1, columnspan=1, sticky="N")
		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



	def Create_ContainerColuna11(self,root):


		self.ContainerColuna11             = Frame (self.ContainerRelogios)
		#self.ContainerUniman              = Frame (self.ContainerColuna11)
		

		self.ContainerColuna11.grid                (row=0, column=11,pady=5, padx=1, columnspan=1, sticky="N")

		#self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=1, columnspan=1, sticky="N")



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

		self.msgGravexCount.configure								(text=str(Info.Gravex.Status.Contage)+"/"+
																	str(Info.Gravex.Status.TotalRelogios)								)

		self.msgGravexHora.configure 							(text=str(Info.Gravex.Status.Horaultima))



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
		
		self.msgGrupoNkHora.configure									(text = str(Info.GrupoNk.Status.Horaultima))



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

		self.msgLottenHora.configure 								(text=str(Info.Lotten.Status.Horaultima))



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

		self.msgCasaCristoHora.configure 							(text=str(Info.CasaCristo.Status.Horaultima))



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


		self.msgBestInClassHora.configure 							(text=str(Info.BestInClass.Status.Horaultima))





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

		self.msgIsoRadHora.configure	  						(text=str(Info.IsoRadio.Status.Horaultima))



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



		elif relogio == "sc":

			self.botaoSBCPSC.configure								(bg=Info.SBCP.SC.ModuloCor)
			self.botaoSBCPSCRelogio.configure						(bg=Info.SBCP.SC.RelogioCor)



		elif relogio == "rs":

			self.botaoSBCPRS.configure								(bg=Info.SBCP.RS.ModuloCor)
			self.botaoSBCPRSRelogio.configure						(bg=Info.SBCP.RS.RelogioCor)



		elif relogio == "rj":

			self.botaoSBCPRJ.configure								(bg=Info.SBCP.RJ.ModuloCor)
			self.botaoSBCPRJRelogio.configure						(bg=Info.SBCP.RJ.RelogioCor)



		elif relogio == "pr":

			self.botaoSBCPPR.configure								(bg=Info.SBCP.PR.ModuloCor)
			self.botaoSBCPPRRelogio.configure						(bg=Info.SBCP.PR.RelogioCor)



		elif relogio == "pe":

			self.botaoSBCPPE.configure								(bg=Info.SBCP.PE.ModuloCor)
			self.botaoSBCPPERelogio.configure						(bg=Info.SBCP.PE.RelogioCor)



		elif relogio == "mg":

			self.botaoSBCPMG.configure								(bg=Info.SBCP.MG.ModuloCor)
			self.botaoSBCPMGRelogio.configure						(bg=Info.SBCP.MG.RelogioCor)



		elif relogio == "go":

			self.botaoSBCPGO.configure								(bg=Info.SBCP.GO.ModuloCor)
			self.botaoSBCPGORelogio.configure						(bg=Info.SBCP.GO.RelogioCor)


		self.msgSBCPCount.configure	  						(text=str(Info.SBCP.Status.Contage)+"/"+
																str(Info.SBCP.Status.TotalRelogios))

		

	def updateElRio(self, relogio):

		

		if relogio == "botafogomuniz":

			self.botaoElRioBotafogoMuniz.configure					(bg=Info.ElRio.BotafogoMuniz.ModuloCor)
			self.botaoElRioBotafogoMunizRelogio.configure			(bg=Info.ElRio.BotafogoMuniz.RelogioCor)

		elif relogio == "botafogopraia":

			self.botaoElRioBotafogoPraia.configure					(bg=Info.ElRio.BotafogoPraia.ModuloCor)
			self.botaoElRioBotafogoPraiaRelogio.configure			(bg=Info.ElRio.BotafogoPraia.RelogioCor)


		if relogio == "boulevard":


			self.botaoElRioBoulevard.configure						(bg=Info.ElRio.Boulevard.ModuloCor)
			self.botaoElRioBoulevardRelogio.configure				(bg=Info.ElRio.Boulevard.RelogioCor)


		elif relogio == "carioca":

			self.botaoElRioCarioca.configure						(bg=Info.ElRio.Carioca.ModuloCor)
			self.botaoElRioCariocaRelogio.configure					(bg=Info.ElRio.Carioca.RelogioCor)


		elif relogio == "centro1":

			self.botaoElRioCentro1.configure						(bg=Info.ElRio.Centro1.ModuloCor)
			self.botaoElRioCentro1Relogio.configure					(bg=Info.ElRio.Centro1.RelogioCor)


		elif relogio == "centro2":

			self.botaoElRioCentro2.configure						(bg=Info.ElRio.Centro2.ModuloCor)
			self.botaoElRioCentro2Relogio.configure					(bg=Info.ElRio.Centro2.RelogioCor)


		elif relogio == "centro3":

			self.botaoElRioCentro3.configure						(bg=Info.ElRio.Centro3.ModuloCor)
			self.botaoElRioCentro3Relogio.configure					(bg=Info.ElRio.Centro3.RelogioCor)


		elif relogio == "fashion":

			self.botaoElRioFashion.configure						(bg=Info.ElRio.Fashion.ModuloCor)
			self.botaoElRioFashionRelogio.configure					(bg=Info.ElRio.Fashion.RelogioCor)


		elif relogio == "flamengo":

			self.botaoElRioFlamengo.configure						(bg=Info.ElRio.Flamengo.ModuloCor)
			self.botaoElRioFlamengoRelogio.configure				(bg=Info.ElRio.Flamengo.RelogioCor)


		elif relogio == "leblon":

			self.botaoElRioLeblon.configure							(bg=Info.ElRio.Leblon.ModuloCor)
			self.botaoElRioLeblonRelogio.configure					(bg=Info.ElRio.Leblon.RelogioCor)


		elif relogio == "novaamerica":

			self.botaoElRioNovaAmerica.configure					(bg=Info.ElRio.NovaAmerica.ModuloCor)
			self.botaoElRioNovaAmericaRelogio.configure				(bg=Info.ElRio.NovaAmerica.RelogioCor)


		elif relogio == "shopgrande":

			self.botaoElRioShopGrande.configure						(bg=Info.ElRio.ShopGrande.ModuloCor)
			self.botaoElRioShopGrandeRelogio.configure				(bg=Info.ElRio.ShopGrande.RelogioCor)


		elif relogio == "shopmacae":

			self.botaoElRioShopMacae.configure						(bg=Info.ElRio.ShopMacae.ModuloCor)
			self.botaoElRioShopMacaeRelogio.configure				(bg=Info.ElRio.ShopMacae.RelogioCor)


		elif relogio == "shopnorte":

			self.botaoElRioShopNorte.configure						(bg=Info.ElRio.ShopNorte.ModuloCor)
			self.botaoElRioShopNorteRelogio.configure				(bg=Info.ElRio.ShopNorte.RelogioCor)


		elif relogio == "backup1":

			self.botaoElRioBackup1.configure						(bg=Info.ElRio.Backup1.ModuloCor)
			self.botaoElRioBackup1Relogio.configure					(bg=Info.ElRio.Backup1.RelogioCor)


		elif relogio == "backup2":

			self.botaoElRioBackup2.configure						(bg=Info.ElRio.Backup2.ModuloCor)
			self.botaoElRioBackup2Relogio.configure					(bg=Info.ElRio.Backup2.RelogioCor)



		self.msgElRioCount.configure   								(text=str(Info.ElRio.Status.Contage)+"/"+
										 							str(Info.ElRio.Status.TotalRelogios))	

		self.msgElRioHora.configure 							(text=str(Info.ElRio.Status.Horaultima))



	def updatePredman(self, relogio):

		if relogio == "bunge":

			self.botaoPredmanBunge.configure						(bg=Info.Predman.Bunge.ModuloCor)
			self.botaoPredmanBungeRelogio.configure				   	(bg=Info.Predman.Bunge.RelogioCor)
		
		elif relogio == "cabot":

			self.botaoPredmanCabot.configure						(bg=Info.Predman.Cabot.ModuloCor)
			self.botaoPredmanCabotRelogio.configure				   	(bg=Info.Predman.Cabot.RelogioCor)
			
	
		elif relogio == "kelloggs":

			self.botaoPredmanKelloggs.configure						(bg=Info.Predman.Kelloggs.ModuloCor)
			self.botaoPredmanKelloggsRelogio.configure				(bg=Info.Predman.Kelloggs.RelogioCor)
			
	
		elif relogio == "magazine":

			self.botaoPredmanMagazine.configure						(bg=Info.Predman.Magazine.ModuloCor)
			self.botaoPredmanMagazineRelogio.configure				(bg=Info.Predman.Magazine.RelogioCor)
			
	
		elif relogio == "oxiteno1":

			self.botaoPredmanOxiteno1.configure						(bg=Info.Predman.Oxiteno1.ModuloCor)
			self.botaoPredmanOxiteno1Relogio.configure				(bg=Info.Predman.Oxiteno1.RelogioCor)
			
	
		elif relogio == "oxiteno2":

			self.botaoPredmanOxiteno2.configure						(bg=Info.Predman.Oxiteno2.ModuloCor)
			self.botaoPredmanOxiteno2Relogio.configure				(bg=Info.Predman.Oxiteno2.RelogioCor)
			
	
		elif relogio == "santoandre":

			self.botaoPredmanSantoAndre.configure					(bg=Info.Predman.SantoAndre.ModuloCor)
			self.botaoPredmanSantoAndreRelogio.configure			(bg=Info.Predman.SantoAndre.RelogioCor)
			
	
		elif relogio == "pysmianes":

			self.botaoPredmanPrysmianES.configure					(bg=Info.Predman.PrysmianES.ModuloCor)
			self.botaoPredmanPrysmianESRelogio.configure			(bg=Info.Predman.PrysmianES.RelogioCor)
			
	
		elif relogio == "tradegar":

			self.botaoPredmanTradegar.configure						(bg=Info.Predman.Tradegar.ModuloCor)
			self.botaoPredmanTradegarRelogio.configure				(bg=Info.Predman.Tradegar.RelogioCor)
			
	
		elif relogio == "portao1":

			self.botaoPredmanPortao1.configure						(bg=Info.Predman.Portao1.ModuloCor)
			self.botaoPredmanPortao1Relogio.configure				(bg=Info.Predman.Portao1.RelogioCor)
			
	
		elif relogio == "portao2":

			self.botaoPredmanPortao2.configure						(bg=Info.Predman.Portao2.ModuloCor)
			self.botaoPredmanPortao2Relogio.configure				(bg=Info.Predman.Portao2.RelogioCor)
			
	
		elif relogio == "sabic":

			self.botaoPredmanSabic.configure						(bg=Info.Predman.Sabic.ModuloCor)
			self.botaoPredmanSabicRelogio.configure				   	(bg=Info.Predman.Sabic.RelogioCor)
			
	
		elif relogio == "santhebrag":

			self.botaoPredmanSantherBraganca.configure				(bg=Info.Predman.SBraganca.ModuloCor)
			self.botaoPredmanSantherBragancaRelogio.configure		(bg=Info.Predman.SBraganca.RelogioCor)
			
	
		elif relogio == "santhepenha":

			self.botaoPredmanSantherPenha.configure					(bg=Info.Predman.SPenha.ModuloCor)
			self.botaoPredmanSantherPenhaRelogio.configure			(bg=Info.Predman.SPenha.RelogioCor)
			
	
		elif relogio == "faurencia":

			self.botaoPredmanFaurencia.configure					(bg=Info.Predman.Faurencia.ModuloCor)
			self.botaoPredmanFaurenciaRelogio.configure				(bg=Info.Predman.Faurencia.RelogioCor)
			
	
		elif relogio == "admrondo":

			self.botaoPredmanAdmRondonopolis.configure				(bg=Info.Predman.AdmRondonopolis.ModuloCor)
			self.botaoPredmanAdmRondonopolisRelogio.configure		(bg=Info.Predman.AdmRondonopolis.RelogioCor)
			
	
		elif relogio == "vilavelha":

			self.botaoPredmanVilaVelha.configure					(bg=Info.Predman.VilaVelha.ModuloCor)
			self.botaoPredmanVilaVelhaRelogio.configure			   	(bg=Info.Predman.VilaVelha.RelogioCor)
			
		
		self.msgPredmancount.configure 								(text = str(Info.Predman.Status.Contage)+"/"+
																	str(Info.Predman.Status.TotalRelogios))



	def updateOlimpark(self, relogio):

		if relogio == "jdpaulista":

			self.botaoOlimparkPaulista.configure               			(bg=Info.Olimpark.JdPaulista.ModuloCor)
			self.botaoOlimparkPaulistaRelogio.configure        			(bg=Info.Olimpark.JdPaulista.RelogioCor)

		elif relogio == "santacecilia":

			self.botaoOlimparkSantaCecilia.configure               		(bg=Info.Olimpark.SantaCecilia.ModuloCor)
			self.botaoOlimparkSantaCeciliaRelogio.configure        		(bg=Info.Olimpark.SantaCecilia.RelogioCor)

		elif relogio == "vilaolimpia":

			self.botaoOlimparkVilaOlimpia.configure               		(bg=Info.Olimpark.VilaOlimpia.ModuloCor)
			self.botaoOlimparkVilaOlimpiaRelogio.configure        		(bg=Info.Olimpark.VilaOlimpia.RelogioCor)

		elif relogio == "previdencia":

			self.botaoOlimparkPrevidencia.configure               		(bg=Info.Olimpark.Previdencia.ModuloCor)
			self.botaoOlimparkPrevidenciaRelogio.configure        		(bg=Info.Olimpark.Previdencia.RelogioCor)

		elif relogio == "belenzinho":

			self.botaoOlimparkBelezinho.configure               		(bg=Info.Olimpark.Belezinho.ModuloCor)
			self.botaoOlimparkBelezinhoRelogio.configure        		(bg=Info.Olimpark.Belezinho.RelogioCor)

		elif relogio == "santana":

			self.botaoOlimparkSantana.configure               			(bg=Info.Olimpark.Santana.ModuloCor)
			self.botaoOlimparkSantanaRelogio.configure        			(bg=Info.Olimpark.Santana.RelogioCor)


		self.msgOlimparkCount.configure									(text=str(Info.Olimpark.Status.Contage)+"/"+
																		str(Info.Olimpark.Status.TotalRelogios))	

		self.msgOlimparkHora.configure 							(text=str(Info.Olimpark.Status.Horaultima))



	def update(self,empresa,relogio):


		if empresa == "laser":
			self.updateLaser2(relogio)



		elif empresa == "building":
			self.updateBuilding(relogio)
		


		elif empresa == "gravex":
			self.updateGravex(relogio)
			


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



		elif empresa == "sbcp":
			self.updateSBCP(relogio)
	


		elif empresa == "elrio":
			self.updateElRio(relogio)



		elif empresa == "predman":
			self.updatePredman(relogio)



		elif empresa == "olimpark":
			self.updateOlimpark(relogio)




