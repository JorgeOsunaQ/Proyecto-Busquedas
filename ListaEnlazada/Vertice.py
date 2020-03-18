from ListaEnlazada import ListaEnlazada
class Vertice:

    def __init__(self,etiqueta):
        self.__etiqueta=etiqueta
        self.__adyacencias=None

    def addAdjacency(self, vertice,peso=1):
        if(self.adyacencias is None):
            self.__adyacencias=ListaEnlazada()
        self.adyacencias.addToRear(dict(neighboor=vertice,weight=peso))
        
    def isNeighborhood(self, vertice):
        if self.adyacencias.isEmpty() or vertice==self:
            return False

        iterador=self.adyacencias.iterator()
        while(iterador.hasNext()):
                 if(next(iterador)['neighboor']==vertice):
                    return True
        return False

    def get_etiqueta(self): 
        return self.__etiqueta

    def get_adyacencias(self): 
        return self.__adyacencias

    def __str__(self):
        return self.__etiqueta

    etiqueta=property(get_etiqueta)
    adyacencias=property(get_adyacencias)

ver=Vertice('Culiacán')
ver.addAdjacency('Mazatlan')

