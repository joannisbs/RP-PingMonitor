from Tkinter import *


from TelaRelogios1 import*
from Var import *
from Thread import *
from TestFuncions import *





def popup(empresa,name,ip,porta,numerorep,responsavel,telefone):

	show = Tk()
	show.wm_title("Dados do REP")

	lable1 = Label(show, text = "Empresa: "  + empresa)
	lable1.grid(row=0,pady=5,padx=20)

	lable1 = Label(show, text = "Unidade: "  + name)
	lable1.grid(row=1,pady=5,padx=20)

	lable = Label(show, text = "IP: " + ip)
	lable.grid(row=2,pady=5,padx=20)

	lable2 = Label(show, text = "Porta Testada: "  + porta)
	lable2.grid(row=3,pady=5,padx=20)

	lable3 = Label(show, text = "Numero do Rep: " + numerorep)
	lable3.grid(row=4,pady=5,padx=20)

	lable4 = Label(show, text = "Responsavel: "  + responsavel)
	lable4.grid(row=5,pady=5,padx=20)

	lable5 = Label(show, text = "Telefone: " + telefone)
	lable5.grid(row=6,pady=5,padx=20)

	botaos = Button(show, text="Ok", command=show.destroy)
	botaos.grid(row=7,pady=5,padx=20)
	#root.update()


Contagem()
leBanco()
root = Tk()
root.title("Monitor Ping")
Telas.Tela1 = MonitorPing(root)

root.mainloop()







