import threading
import socket
import os
import shutil
from datetime import datetime

from Tkinter import *
import os

from Thread import *
from Var import *



class MonitorPing(object):


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





		#AQUI E DEFINIDO O QUE TEM DENTRO DE CADA BLOCO DE CADA EMPRESA. 


	####################################################################################################################
	############################################## BOTOES ##############################################################
	####################################################################################################################




		############################################## BARRA DE STATUS #################################################

		
		self.msgStaus = Label (self.ContainerStatus,text = "Servico")
		self.msgStaus["height"] = 1
		self.msgStaus.grid(row=0,column=0)


		self.botaoStatus                    = Button(self.ContainerStatus)
		self.botaoStatus     ["text"]       = Controle.StatusWord
		self.botaoStatus     ["background"] = Controle.Status
		self.botaoStatus     ["height"]     = 1
		self.botaoStatus     ["width"]      = 15
		self.botaoStatus.bind("<Button-1>",self.Inicia)
		self.botaoStatus.grid(row=0,column=1)



		self.msgInformativaON = Label (self.ContainerStatus,text = "On-Line : ")
		self.msgInformativaON["height"] = 1
		self.msgInformativaON.grid(row=0,column=2)

		self.msgStatusON = Label (self.ContainerStatus,text = "0")
		self.msgStatusON["height"] = 1
		self.msgStatusON.grid(row=0,column=3)

		self.msgInformativaTotal = Label (self.ContainerStatus,text = "Total : ")
		self.msgInformativaTotal["height"] = 1
		self.msgInformativaTotal.grid(row=0,column=4)

		self.msgStatusTotal = Label (self.ContainerStatus,text = "0")
		self.msgStatusTotal["height"] = 1
		self.msgStatusTotal.grid(row=0,column=5)












	def Create_MilenioErvas(self):


		self.msgMilenioErvas = Label (self.ContainerMilenioErvas,text = "Milenio Ervas")
		self.msgMilenioErvas["height"] = 1
		self.msgMilenioErvas.grid(row=0,column=0,columnspan=2,sticky = "N")




		self.botaoMilenioErvasSBC1620Loja1                             = Button(self.ContainerMilenioErvas)
		self.botaoMilenioErvasSBC1620Loja1              ["text"]       = "1620 Loja1"
		self.botaoMilenioErvasSBC1620Loja1              ["background"] = Info.MilenioErvas.Loja1.ModuloCor
		self.botaoMilenioErvasSBC1620Loja1              ["width"]      = 15
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
		self.botaoMilenioErvasSBC692Loja2                ["width"]      = 15
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
		self.botaoMilenioErvasSaoMatheus                ["width"]      = 15
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
		self.botaoMilenioErvasDiadema                  ["width"]      = 15
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
		self.botaoGravexADM                         ["width"]      = 15
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
		self.botaoGravexLoja                        ["width"]      = 15
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
		self.botaoGravexMiMarcos                    ["width"]      = 15
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
		self.botaoGravexDantChini                   ["width"]      = 15
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




		self.botaoAcademia                                         = Button(self.ContainerLaser)
		self.botaoAcademia                          ["text"]       = "Academia"
		self.botaoAcademia                          ["background"] = Info.Laser.Academia.ModuloCor
		self.botaoAcademia                          ["height"]     = 1
		self.botaoAcademia                          ["width"]      = 15
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
		self.botaoInstituto                         ["width"]      = 15
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
		self.botaoPredmanBunge                     ["width"]      = 15
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
		self.botaoPredmanCabot                     ["width"]      = 15
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
		self.botaoPredmanKellogs                  ["width"]      = 15
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
		self.botaoPredmanMagazine                 ["width"]      = 15
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
		self.botaoPredmanOxiteno1                 ["width"]      = 15
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
		self.botaoPredmanOxiteno2                 ["width"]      = 15
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
		self.botaoPredmanOxiteno3                 ["width"]      = 15
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
		self.botaoPredmanPrysmianES               ["width"]      = 15
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
		self.botaoPredmanTradegar                 ["width"]      = 15
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
		self.botaoPredmanPortao1                  ["width"]      = 15
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
		self.botaoPredmanPortao2                  ["width"]      = 15
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
		self.botaoPredmanSabic                    ["width"]      = 15
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
		self.botaoPredmanSantherBraganca          ["width"]      = 15
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
		self.botaoPredmanSantherPenha              ["width"]      = 15
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
		self.botaoPredmanFaurencia                ["width"]      = 15
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
		self.botaoPredmanAdmRondonopolis          ["width"]      = 15
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
		self.botaoPredmanVilaVelha                ["width"]      = 15
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
		self.botaoUnimanSaintGobain                   ["width"]      = 15
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
		self.botaoUnimanPPMSecoia                    ["width"]      = 15
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
		self.botaoUnimanTitan                        ["width"]      = 15
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
		self.botaoUnimanSekurity                    ["width"]      = 15
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
		self.botaoTahine                          ["width"]      = 15
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
		self.botaoTarek                           ["width"]      = 15
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
		self.botaoTafadalu                        ["width"]=15
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
		self.botaoTalami                         ["width"]      = 15
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




		self.botaoLottenJardins                                  = Button(self.ContainerLotten)
		self.botaoLottenJardins                   ["text"]       = "Jardins"
		self.botaoLottenJardins                   ["background"] = Info.Lotten.Jardins.ModuloCor
		self.botaoLottenJardins                   ["width"]      = 15
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
		self.botaoLottenAlphaville                ["width"]      = 15
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
		self.botaoLottenOsasco                   ["width"]      = 15
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
		self.botaoLottenSantana                  ["width"]      = 15
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
		self.botaoLottenTatuape                 ["width"]      = 15
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
		self.botaoLottenMoema                   ["width"]      = 15
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
		self.botaoLottenJardimSul               ["width"]      = 15
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
		self.botaoLottenConceicao               ["width"]      = 15
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
		self.botaoLottenPerdizes                ["width"]      = 15
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
		self.botaoLottenLapa                    ["width"]      = 15
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
		self.botaoLottenSaoCaetano              ["width"]      = 15
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
		self.botaoLottenPinheiros               ["width"]      = 15
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
		self.botaoLottenMorumbi                 ["width"]      = 15
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
		self.botaoLottenBerrini                 ["width"]      = 15
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
		self.botaoLottenVilaMariana             ["width"]      = 15
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
		self.botaoLottenVilaOlimpia             ["width"]      = 15
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
		self.botaoLottenItaim                  ["width"]      = 15
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
		self.botaoLottenGuarulhos               ["width"]      = 15
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
		self.msgBestInClassCont = Label (self.ContainerBestInClass,text = "5/11")

		self.msgBestInClass.grid                   (row=0,column=0,sticky = "N")
		self.msgBestInClassCont.grid             (row=0,column=1,sticky = "N")






		self.botaoBestInClassRecife                               = Button(self.ContainerBestInClass)
		self.botaoBestInClassRecife                ["text"]       = "Recife"
		self.botaoBestInClassRecife                ["background"] = Info.BestInClass.Recife.ModuloCor
		self.botaoBestInClassRecife                ["width"]      = 15
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
		self.botaoBestInClassItaquera              ["width"]      = 15
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
		self.botaoBestInClassItapevi               ["width"]      = 15
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
		self.botaoBestInClassSorocaba              ["width"]      = 15
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
		self.botaoBestInClassSeteLagoas            ["width"]      = 15
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
		self.botaoBestInClassCuritiba              ["width"]      = 15
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
		self.botaoBestInClassSFsat                 ["width"]      = 15
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
		self.botaoBestInClassItu                   ["width"]      = 15
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
		self.botaoBestInClassGuarulhos              ["width"]      = 15
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
		self.botaoBestInClassItaporanga             ["width"]      = 15
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
		self.botaoBestInClassLinhares               ["width"]      = 15
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
		self.msgCasaCristoContage = Label (self.ContainerCasaCristo,text = str(Info.CasaCristo.Status.Contage)+"/5")

		self.msgCasaCristo.grid(row=0,column=0, sticky = "N")
		self.msgCasaCristoContage.grid(row=0,column=1, sticky = "N")




		self.botaoCasaCristoADM                                   = Button(self.ContainerCasaCristo)
		self.botaoCasaCristoADM                    ["text"]       = "ADM"
		self.botaoCasaCristoADM                    ["background"] = Info.CasaCristo.ADM.ModuloCor
		self.botaoCasaCristoADM                    ["width"]      = 15
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
		self.botaoCasaCristoCEI1                   ["width"]      = 15
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
		self.botaoCasaCristoCEI2                   ["width"]      = 15
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
		self.botaoCasaCristoCEI3                   ["width"]      = 15
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
		self.botaoCasaCristoVMatilde               ["width"]      = 15
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
		self.botaoBuildingAllianz                   ["width"]      = 15
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
		self.botaoBuildingWTorre                    ["width"]      = 15
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
		self.botaoBuildingRioJaneiro                ["width"]      = 15
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


	def Create_container(self,root):


		############################################## BLOCO STATUS E BOTOES ###########################################


		self.ContainerStatus              = Frame (root)
		self.ContainerStatus.grid                 (row=0, sticky = "N")

		self.ContainerRelogios		      = Frame (root)
		self.ContainerRelogios.grid               (row=1, sticky = "N")


		############################################## COLUMN 0 ########################################################

		self.ContainerColuna0             = Frame (self.ContainerRelogios)
		self.ContainerBuilding            = Frame (self.ContainerColuna0)
		self.ContainerCasaCristo          = Frame (self.ContainerColuna0)
		self.ContainerBestInClass         = Frame (self.ContainerColuna0)

		self.ContainerColuna0.grid                (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerBuilding.grid               (row=0, column=0,pady=5, padx=5, columnspan=1 ,sticky="N")
		self.ContainerCasaCristo.grid             (row=1, column=0,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerBestInClass.grid            (row=2, column=0,pady=5, padx=5, columnspan=1, sticky="N")


		############################################## COLUMN 1 ########################################################

		self.ContainerColuna1             = Frame (self.ContainerRelogios)
		self.ContainerLaser               = Frame (self.ContainerColuna1)
		self.ContainerLotten              = Frame (self.ContainerColuna1)

		self.ContainerColuna1.grid                (row=0, column=1,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerLaser.grid                  (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerLotten.grid                 (row=2, column=0,pady=5, padx=5, columnspan=1, sticky="N")

		############################################## COLUMN 2 ########################################################

	
		self.ContainerColuna2             = Frame (self.ContainerRelogios)
		self.ContainerGravex              = Frame (self.ContainerColuna2)

		self.ContainerColuna2.grid                (row=0, column=2,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerGravex.grid                 (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")


		############################################## COLUMN 3 ########################################################

		self.ContainerColuna3             = Frame (self.ContainerRelogios)
		self.ContainerPredman             = Frame (self.ContainerColuna3)

		self.ContainerColuna3.grid                (row=0, column=3,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerPredman.grid                (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")

		############################################## COLUMN 4 ########################################################

		self.ContainerColuna4             = Frame (self.ContainerRelogios)
		self.ContainerTarek               = Frame (self.ContainerColuna4)


		self.ContainerColuna4.grid                (row=0, column=4,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerTarek.grid                  (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")

		############################################## COLUMN 5 ########################################################

		self.ContainerColuna5             = Frame (self.ContainerRelogios)
		self.ContainerMilenioErvas        = Frame (self.ContainerColuna5)


		self.ContainerColuna5.grid                (row=0, column=5,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerMilenioErvas.grid           (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")

		############################################## COLUMN 6 ########################################################

		self.ContainerColuna6             = Frame (self.ContainerRelogios)
		self.ContainerUniman              = Frame (self.ContainerColuna6)


		self.ContainerColuna6.grid                (row=0, column=6,pady=5, padx=5, columnspan=1, sticky="N")
		self.ContainerUniman.grid                 (row=0, column=0,pady=5, padx=5, columnspan=1, sticky="N")


	def update(self,empresa,relogio):

		if empresa == "building":

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




		elif empresa == "gravex":
			
			if relogio == "adm":


				self.botaoGravexADM.configure 							(bg=Info.Gravex.ADM.ModuloCor)
				self.botaoGravexADMRelogio.configure 					(bg=Info.Gravex.ADM.RelogioCor)


			elif relogio == "loja":

				self.botaoGravexLoja.configure							(bg=Info.Gravex.Loja1.ModuloCor)
				self.botaoGravexLojaRelogio.configure 					(bg=Info.Gravex.Loja1.RelogioCor)
			

			elif relogio == "mimarcos":

				self.botaoGravexMiMarcos.configure						(bg=Info.Gravex.Mimarcos.ModuloCor)
				self.botaoGravexMiMarcosRelogio.configure 				(bg=Info.Gravex.Mimarcos.RelogioCor)


			elif relogio == "dantchini":


				self.botaoGravexDantChini.configure						(bg=Info.Gravex.DantChini.ModuloCor)
				self.botaoGravexDantChiniRelogio.configure 				(bg=Info.Gravex.DantChini.RelogioCor)



		elif empresa == "laser":
			
			if relogio == "instituto":
			
				self.botaoAcademia.configure                    		(bg=Info.Laser.Academia.ModuloCor)
				self.botaoRAcademia.configure                    		(bg=Info.Laser.Academia.RelogioCor)


			if relogio == "academia":

				self.botaoInstituto.configure                    		(bg=Info.Laser.Instituto.ModuloCor)
				self.botaoRInstituto.configure                   		(bg=Info.Laser.Instituto.RelogioCor)



		elif empresa == "casacristo":
		
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
			
			self.msgCasaCristoContage.configure	  						(text=str(Info.CasaCristo.Status.Contage)+"/"+
																		str(Info.CasaCristo.Status.TotalRelogios))
 


		elif empresa == "bestinclass":
			
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





		self.msgStatusON.configure										(text=str(Controle.TotalON))
		self.msgStatusTotal.configure									(text=str(Controle.TotalRelogios))


	def Inicia(self,event):
		if self.botaoStatus["background"]=="red":
			self.botaoStatus["background"] = "green"

			self.botaoStatus["text"] = "Rodando"
			Controle.StatusWord = "Rodando"
			Controle.Status = "green"
			Controle.Stop = False
			#loopthread.doemon = True
			Threadloop0().start()
			Threadloop1().start()




		else:
			self.botaoStatus["text"] = "Parado"
			self.botaoStatus["background"] = "red"
			Controle.StatusWord = "Parado"
			Controle.Status = "red"
			Controle.Stop = True




