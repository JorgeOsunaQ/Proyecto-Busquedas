from Grafo import Grafo
import pandas as pd 
class AplGrafoCiudades:

    def __init__(self):
        self.grafo=Grafo()
        #Falta manejo de excepciones (en todo el código)
        self.df_ciudades=pd.read_csv('Grafo\CSV\ciudades.csv')
        self.df_aristas=pd.read_csv('Grafo\CSV\conexiones.csv')

    def agrega_ciudades(self):
        for ciudad in self.df_ciudades['Ciudad']:
            self.grafo.add_vertice(ciudad)

    def agrega_colindantes(self):
        for index, arista in self.df_aristas.iterrows():
            self.grafo.add_arista(arista['Src'],arista['Dest'],arista['Distancia'])

if __name__ == "__main__":
    apl=AplGrafoCiudades()
    apl.agrega_ciudades()
    apl.agrega_colindantes()
    #apl.grafo.breadth_first_search('Culiacán','Saltillo')
    apl.grafo.Depth_First_Search('Culiacán','Saltillo')

