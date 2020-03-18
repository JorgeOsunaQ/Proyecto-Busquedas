from ListaEnlazada import ListaEnlazada
from Vertice import Vertice
class Grafo:

    def __init__(self):
        self.__vertices=None
    
    def addVertice(self,etiqueta):
        if(self.vertices is None):
            self.__vertices=ListaEnlazada()
        self.__vertices.addToRear(Vertice(etiqueta))

    def addAdyancencia(self, source,dest):
        pass

    def get_vertices(self):
        return self.__vertices
    
    vertices=property(get_vertices)
