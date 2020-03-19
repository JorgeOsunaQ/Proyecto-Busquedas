from ListaEnlazada import ListaEnlazada
from Vertice import Vertice
class Grafo:

    def __init__(self):
        self.__vertices=ListaEnlazada()
    
    def add_vertice(self,etiqueta):
        self.__vertices.add_to_rear(Vertice(etiqueta))

    def add_adyancencia(self, source,dest,peso=1):
        vertice_s=self.search_vertice(source)
        vertice_d=self.search_vertice(dest)

        if((not vertice_d) or (not vertice_s)):
            return 0

        if(vertice_d.is_neighborhood(vertice_s) or vertice_s.is_neighborhood(vertice_d)):
            return 1

        vertice_s.addAdjacency(vertice_d,peso)
        vertice_d.addAdjacency(vertice_s,peso)
        return 3

    def search_vertice(self,etiqueta):
        iterador=self.__vertices.iterator()

        while(iterador.has_next()):
            actual=next(iterador)
            if(etiqueta==actual.etiqueta):
                return actual

        return False
    #Aún sin terminar
    def breadth_first_search(self,source,dest):
        if(self.__vertices.is_empty()):
            return 0

        if(source==dest):
            return 1

        vertice_s=self.search_vertice(source)
        vertice_d=self.search_vertice(dest)

        if((not vertice_d) or (not vertice_s)):
            return 2
        
        iterador=self.__vertices.iterator()
            
        abiertos=[]
        abiertos.append(next(iterador))
        cerrados=[]
        while(len(abiertos)>0):
            temp=abiertos.pop(0)
            return
        

    def __str__(self):
        temp=''
        if(self.__vertices.is_empty()):
            return'Sin Vertices'

        iterador=self.__vertices.iterator()
        while(iterador.has_next()):
            temp+=str(next(iterador))+'\n'
        return temp

    def get_vertices(self):
        return self.__vertices
    
    vertices=property(get_vertices)

grafo=Grafo()
grafo.add_vertice('Culiacan')
grafo.add_vertice('Durango')

grafo.breadth_first_search('Culiacan','Durango')