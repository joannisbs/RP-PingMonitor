from Tkinter import *



from TelaRelogios1 import*
from Var import *
from Thread import *
from TestFuncions import *
from TelaMonitoramento import *
from BancoELogs import *
from AtualizacaoEContagem import *
import time



Contagem()
leBanco()


class Iniciooo:
	def __init__(self,root):




		lable1 = Label(teste, text = "Real Ponto" )
		lable1.grid(row=0,pady=5,padx=20)
		Relo1 = Toplevel(master=None)
		Relo1.title("Monitor Relogios 1")
		Telas.GUI_Tela1 = TelaRelogios1(Relo1)

		Monitor = Toplevel(master=None)
		Monitor.title("Monitoramento e Controle")

		Telas.GUI_Monitor = TelaMonitor(Monitor)
	

		#self.destroy()

teste = Tk()

Iniciooo(teste)

teste.wm_withdraw()



#Relo1.mainloop()
teste.mainloop()






