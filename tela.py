from Tkinter import *



from TelaRelogios1 import*
from Var import *
from Thread import *
from TestFuncions import *
from TelaMonitoramento import *
import tkMessageBox as messagebox
from BancoELogs import *
from AtualizacaoEContagem import *
import time



Contagem()
leBanco()


def on_closing():
	if messagebox.askokcancel("Quit","Quer realmente sair?"):
		Telas.root.destroy()


class Iniciooo:

	def __init__(self,root):


		Relo1 = Toplevel(master=None)
		Relo1.title("Monitor Relogios 1")
		Relo1.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Tela1 = TelaRelogios1(Relo1)

		Monitor = Toplevel(master=None)
		Monitor.title("Monitoramento e Controle")
		Monitor.protocol("WM_DELETE_WINDOW",on_closing)
		Telas.GUI_Monitor = TelaMonitor(Monitor)
	

		#self.destroy()






Telas.root = Tk()

Iniciooo(Telas.root)


Telas.root.wm_withdraw()


#Relo1.mainloop()
Telas.root.mainloop()






