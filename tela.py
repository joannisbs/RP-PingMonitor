from Tkinter import *


from TelaRelogios1 import*
from Var import *
from Thread import *
from TestFuncions import *
from TelaMonitoramento import *
from BancoELogs import *
from AtualizacaoEContagem import *




Contagem()
leBanco()

Relo1 = Tk()
Relo1.title("Monitor Relogios 1")
Telas.GUI_Tela1 = TelaRelogios1(Relo1)

Monitor = Tk()
Monitor.title("Monitoramento e Controle")

Telas.GUI_Monitor = TelaMonitor(Monitor)

Relo1.mainloop()
Monitor.mainloop()






