from GrafoCiudades import GrafoCiudades
from Rutinas import *
class ManejaGrafo:

    def __init__(self):
        self.grafo=GrafoCiudades()
        #Falta manejo de excepciones (en todo el código)
        self.df_ciudades=Rutinas.get_datos_ciudades()
        self.df_aristas=Rutinas.get_conexiones_ciudades()

    def agrega_ciudades(self):
        for index,ciudad in self.df_ciudades.iterrows():
            self.grafo.add_ciudad(ciudad['Ciudad'],ciudad['Latitud'],ciudad['Longitud'])

    def agrega_colindantes(self):
        for index, arista in self.df_aristas.iterrows():
            self.grafo.add_arista(arista['Src'],arista['Dest'],arista['Distancia(KM)'])

    def get_list_ciudades(self):
        return self.df_ciudades['Ciudad'].tolist()    
        
    def get_grafo(self):
        return self.grafo