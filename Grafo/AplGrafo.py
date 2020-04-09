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

    def getGrafo(self):
        return self.grafo.__str__()
        
