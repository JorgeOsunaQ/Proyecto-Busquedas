#------ DEPENDECIAS --------#
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from ManejaGrafo import *
import tkinter.messagebox

class GUIFRAFO:

    def __init__(self,grafo,capitales):
        root = Tk() 
        self.grafo = grafo
        root.title("PROYECTO BÚSQUEDAS")
        root.resizable(False,False)
        root.iconbitmap("Grafo\Contenido\icono")
        #------ DEFINICIÓN DEL MENU ---------#
        menu=Menu(root)
        root.config(menu=menu,width=400,height=400)
        menuGraph=Menu(menu, tearoff=False)
        menuSearch=Menu(menu, tearoff=False)
        menuCities=Menu(menu, tearoff=False)
        menuExit=Menu(menu, tearoff=False)
        menuMore=Menu(menu, tearoff=False)
        menuGraph.add_command(label="Ver Grafo", command=lambda :showFrameGrafo(str(self.grafo)))
        menuSearch.add_command(label="Ver Búsquedas", command=lambda : showFrameSearchs(self))
        menuCities.add_command(label="Ciudad Origen y Destino",command=lambda : showFrameCities(self))
        menuMore.add_command(label="Proyecto",command=showmore)
        menu.add_cascade(label="Grafo",menu=menuGraph)
        menu.add_cascade(label="Búsquedas",menu=menuSearch)
        menu.add_cascade(label="Ciudades",menu=menuCities)
        menu.add_cascade(label="Acerca De",menu=menuMore)
        self.origen = ""
        self.destino=" "
        root.mainloop()  


    #-------FUNCIONES A EVENTOS ---------#

#----METODO PARA DESPLEGAR LA VENTANA GRAFO-----
def showFrameGrafo(grafo):
    ventana= Tk()
    ventana.geometry("1300x500")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("GRAFO")
    Label(ventana,text="GRAFO",font=("Arial",20)).place(x="555", y="20")
    Button(ventana,text="SALIR",font="bold", command=lambda :ventana.destroy() ).place(x="1200",y="460")
    textArea= Text(ventana, width="165", height="20",font=("Arial",10))
    textArea.grid(row="4", column="1",padx="10", pady="10")
    textArea.place(x="100", y="80") 
    scrollbar = Scrollbar(ventana, command=textArea.yview)
    scrollbar.grid(row="4", column="2", sticky="nsew")
    scrollbar.place(x="1280", y="190")
    textArea.insert(INSERT,grafo)
    textArea.config(state="disabled")
    ventana.mainloop()

#----METODO PARA DESPLEGAR LA VENTANA BUSQUEDAS-----
def showFrameSearchs(self):
    if self.origen=='' or self.destino=='':
        tkinter.messagebox.showinfo('Busquedas',f'CIUDADES NO SELECCIONADAS')
        return
    ventana= Tk()
    ventana.geometry("750x600")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("BÚSQUEDAS")
    Label(ventana,text="BÚSQUEDAS",font=("Arial",20)).grid(row=0,column=0,pady="20")
    Button(ventana,text="SALIR", command=lambda :ventana.destroy() ).place(x="550",y="360")
    comboBusquedas = ttk.Combobox(ventana, state="readonly", values=[ "Profundidad", "Amplitud", "Best First","Branch And Bound", "A*"])
    comboBusquedas.grid(column=0, row=1)
    comboBusquedas.current(0)
    textArea= Text(ventana, width="80", height="20",font=('Arial',13))
    scrollbar = Scrollbar(ventana, command=textArea.yview)
    textArea['yscrollcommand']=scrollbar.set
    textArea.grid(row=6, column=0,padx="8", pady="10")
    scrollbar.grid(row=6, column=1,sticky='nsew')
    comboBusquedas.bind("<<ComboboxSelected>>", lambda event:selection_changed(comboBusquedas.current(),textArea, self.origen,self.destino,self.grafo))
    ventana.grid_columnconfigure(0,weight=1)
    selection_changed(comboBusquedas.current(),textArea, self.origen,self.destino,self.grafo) 
    Button(ventana,text="SALIR", command=lambda :ventana.destroy()).place(x="700",y="560")
    ventana.mainloop()

#----METODO PARA DESPLEGAR LA VENTANA CIUDADES-----
def showFrameCities(self):
    ventana= Tk()
    ventana.geometry("400x240")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("CIUDADES")
    Label(ventana,text="CIUDADES",font=("Arial",20)).place(x="135", y="20")
    Label(ventana,text="ORIGEN",font=("Arial",12)).place(x="50", y="70")
    Label(ventana,text="DESTINO",font=("Arial",12)).place(x="250", y="70")
    comboOrigen = ttk.Combobox(ventana, state="readonly", values=capitales)
    comboOrigen.grid(column=0, row=1)
    comboOrigen.current(0)
    comboOrigen.place(x="30",y="110")
    capitales.sort()
    comboDestino = ttk.Combobox(ventana, state="readonly", values=capitales)
    comboDestino.grid(column=0, row=1)
    comboDestino.current(0)
    comboDestino.place(x="240",y="110")
    Button(ventana,text="GUARDAR",font=12, command= lambda : saveCities(comboOrigen.get(),comboDestino.get(), self,ventana)).place(x="160",y="150")
    Button(ventana,text="SALIR", command=lambda :ventana.destroy()).place(x="350",y="210")
    ventana.mainloop()

#----METODO PARA DESPLEGAR LA VENTANA ACERCA DE-----
def showmore():
    ventana= Tk()
    ventana.geometry("400x400")
    ventana.iconbitmap("Grafo\Contenido\icono")
    ventana.title("PROYECTO")
    Label(ventana,text="PROYECTO", font=("bold",20)).place(x="125",y="10")
    Label(ventana,text="INTEGRANTES", font=13).place(x="150",y="60")
    Label(ventana,text="ABITIA ROJO ENDHIR FERNANDO").place(x="105",y="85")
    Label(ventana,text="OSUNA QUINTANA JORGE").place(x="125",y="110")
    Label(ventana,text="REYES RIVERA JOEL").place(x="142",y="135")
    Label(ventana,text="DESCRIPCIÓN", font=13).place(x="140",y="175")
    textArea= Text(ventana, width="53", height="9",font=('Arial',10))
    textArea.grid(row=6, column=0,padx="8", pady="10")
    textArea.place(x="20", y="200")
    textArea.insert(INSERT,"En este proyecto se llevó a cabo el desarrollo e implementación de distintos algoritmos de búsqueda ampliamente utilizados en  inteligencia artificial, con la finalidad de apreciar las ventajas y  características propias que ofrece cada uno de ellos. Para ello  se desarrolló una estructura tipo grafo, la cual, está compuesta de un conjunto elementos representados como vértices, y sus   respectivas adyacencias, cada uno de estos con sus propiedad-es básicas y necesarias para formar las aristas, que, represent-an la conexión entre un vértice a otro.")
    Button(ventana,text="SALIR",font="bold", command=lambda :ventana.destroy() ).place(x="330",y="360")

#----METODO PARA GUARDAR CIUDADES-----
def saveCities(comboOrigen, comoDestino, self,ventana ):
    if comboOrigen == comoDestino:
        tkinter.messagebox.showinfo('Guardar',f'ORIGEN Y DESTINO IGUALES\n') 
        return 
    self.origen= comboOrigen
    self.destino = comoDestino
    msg=tkinter.messagebox.showinfo('Guardar',f'GUARDADO\n\nOrigen: {self.origen}\nDestino: {self.destino}')
    if(msg=='ok'):
        ventana.destroy()

#----METODO PARA MOSTRAR LAS BUSQUEDAS EN UN CAMBIO DEL COMBOBOX-----
def selection_changed(busqueda, textArea, origen, destino, grafo):
    textArea.delete(1.0,END)
    source=grafo.search_vertice(origen)
    dest=grafo.search_vertice(destino)
    mayusOrigen= origen.upper()
    mayusDestino = destino.upper()
    temp=f'RUTA: {mayusOrigen} A {mayusDestino}\n'
    if(busqueda==1):
        title= "BUSQUEDA EN AMPLITUD"
        path,dem=grafo.breadth_first_search(source,dest)
    elif(busqueda==0):
        title= "BUSQUEDA EN PROFUNDIDAD"
        path,dem=grafo.depth_first_search(source,dest)
    elif(busqueda==2):
        title= "BUSQUEDA BEST FIRST"
        path,dem=grafo.best_first_search(source,dest)
    elif(busqueda==3):
        title= "BUSQUEDA BRANCH AND BOUND"
        path,dem=grafo.branch_and_bound_search(source,dest)
    elif(busqueda==4):
        title= "BUSQUEDA EN A*"
        path,dem=grafo.A_star_search(source,dest)

    if(path!=None and path):
        path_res='CAMINO ENCONTRADO:\n'
        for x in path:
            path_res+='->'+x.etiqueta
    temp+= f'{title}\n{dem}\n{path_res}\n\n'
    textArea.insert(INSERT,temp)

    #----MAIN----#
if __name__ == "__main__":
    apl=ManejaGrafo()
    apl.agrega_ciudades()
    apl.agrega_colindantes()
    grafo=apl.get_grafo()
    capitales=apl.get_list_ciudades()
    Grafo= GUIFRAFO(grafo,capitales)