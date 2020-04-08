from tkinter import *
from tkinter import ttk

#------ VARIABLES GLOBALES ------------#
origen =" "
destino =" "

#------ DEFINICIÓN DE LA RAIZ ---------#
root = Tk() 
root.title("PROYECTO BÚSQUEDAS")
root.resizable(False,False)
root.iconbitmap("Grafo\Contenido\icono")


#-------FUNCIONES A EVENTOS ---------#
def showFrameGrafo():
    ventana= Tk()
    ventana.geometry("300x300")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("GRAFO")
    ventana.mainloop()
def showFrameSearchs():
    ventana= Tk()
    ventana.geometry("300x300")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("BÚSQUEDAS")
    ventana.mainloop()
def showFrameCities():
    ventana= Tk()
    ventana.geometry("400x240")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("CIUDADES")
    frame = Frame(ventana, width=400, height=240)
    frame.pack()
    Label(frame,text="CIUDADES",font=("Arial",20)).place(x="135", y="20")
    Label(frame,text="ORIGEN",font=("Arial",12)).place(x="50", y="70")
    Label(frame,text="DESTINO",font=("Arial",12)).place(x="250", y="70")
    comboOrigen = ttk.Combobox(frame, values=[ "1", "2", "3","4"])
    comboOrigen.grid(column=0, row=1)
    comboOrigen.current(1)
    comboOrigen.place(x="30",y="110")
    comboDestino = ttk.Combobox(frame, values=[ "1", "2", "3","4"])
    comboDestino.grid(column=0, row=1)
    comboDestino.current(1)
    comboDestino.place(x="240",y="110")
    Button(frame,text="GUARDAR",font=12).place(x="160",y="150")
    Button(frame,text="SALIR", command=lambda :ventana.destroy() ).place(x="350",y="210")
    ventana.mainloop()
def exit():
    ventana= Tk()
    ventana.geometry("300x300")
    ventana.mainloop()

def more():
    ventana= Tk()
    ventana.geometry("300x300")
    ventana.mainloop()


#------ DEFINICIÓN DEL MENU ---------#
menu=Menu(root)
root.config(menu=menu,width=300,height=200)
menuGraph=Menu(menu, tearoff=False)
menuSearch=Menu(menu, tearoff=False)
menuCities=Menu(menu, tearoff=False)
menuExit=Menu(menu, tearoff=False)
menuMore=Menu(menu, tearoff=False)
menuGraph.add_command(label="Ver Grafo", command=showFrameGrafo)
menuSearch.add_command(label="Ver Búsquedas", command=showFrameSearchs)
menuCities.add_command(label="Ciudad Origen y Destino",command=showFrameCities)
menu.add_cascade(label="Grafo",menu=menuGraph)
menu.add_cascade(label="Búsquedas",menu=menuSearch)
menu.add_cascade(label="Ciudades",menu=menuCities)
menu.add_cascade(label="Acerca De",menu=menuMore, command=more)
menu.add_cascade(label="Salir",menu=menuExit,command=lambda : root.destroy() )





root.mainloop()  