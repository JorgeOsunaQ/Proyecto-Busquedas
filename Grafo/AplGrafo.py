from GrafoCiudades import GrafoCiudades
import pandas as pd 
class AplGrafoCiudades:

    def __init__(self):
        self.grafo=GrafoCiudades()
        #Falta manejo de excepciones (en todo el código)
        self.df_ciudades=pd.read_csv('Grafo\CSV\ciudades.csv')
        self.df_aristas=pd.read_csv('Grafo\CSV\conexiones.csv')

    def agrega_ciudades(self):
        for index,ciudad in self.df_ciudades.iterrows():
            self.grafo.add_ciudad(ciudad['Ciudad'],ciudad['Latitud'],ciudad['Longitud'])

    def agrega_colindantes(self):
        for index, arista in self.df_aristas.iterrows():
            self.grafo.add_arista(arista['Src'],arista['Dest'],arista['Distancia(KM)'])

def menu(apl):
    res=-1

    while(res!=3):
        try:
            print('----Menu----')
            print('1.-Ingresar Ciudades')
            print('2.-Imprimir Grafo')
            print('3.-Salir')
            res=int(input())

            if(res==1):
                op=busquedas(apl.grafo)
                if(op==0):
                    print('El grafo está vacío')
                elif(op==1):
                    print('La ciudad de origen y destino son iguales')
                elif(op==2):
                    print('Alguna de las ciudades no existe en el grafo. Inténtelo nuevamente.')
            elif(res==2):
                print('wep')
                print(apl.grafo)
            elif(res==3):
                print('Programa Finalizado')

        except ValueError:
            print('\nError: Ingrese un valor entero')

def busquedas(grafo):
    src=input('Ingrese la ciudad de origen: ').strip()
    dest=input('Ingrese la ciudad de destino: ').strip()
    res=-1
    #Verificar que la lista de vertices no se encuentre vacía 
    if(grafo.vertices.is_empty()):
        return 0
    #Verificar que el vertice meta no sea igual al vertice de salida
    if(src==dest):
        return 1
    #Obtenemos los vertices de salida y meta
    source=grafo.search_vertice(src)
    dest=grafo.search_vertice(dest)
    #Verificamos que ambos existan en el grafo
    if((not dest) or (not source)):
        return 2

    while(res!=6):
        try:
            print('\nIngrese la operación a realizar')
            print('1.-Busqueda en amplitud')
            print('2.-Busqueda en profundidad')
            print('3.-Busqueda Best First')
            print('4.-Busqueda Branch and Bound')
            print('5.-Busqueda A*')
            print('6.-Salir')
            res=int(input())
                
            if(res==1):
                print('----Busqueda en amplitud----')
                grafo.breadth_first_search(source,dest)
            elif(res==2):
                print('----Busqueda en profundidad----')
                grafo.depth_first_search(source,dest)
            elif(res==3):
                print('----Busqueda Best First----')
                grafo.best_first_search(source,dest)

        except ValueError:
            print('\nError: Ingrese un valor entero')

if __name__ == "__main__":
    apl=AplGrafoCiudades()
    apl.agrega_ciudades()
    apl.agrega_colindantes()
    menu(apl)  
    #apl.grafo.breadth_first_search('Culiacán','CDMX')
    #apl.grafo.Depth_First_Search('Culiacán','Monterrey')

