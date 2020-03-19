from ListaEnlazada import ListaEnlazada
class Vertice:

    def __init__(self,etiqueta):
        self.__etiqueta=etiqueta
        self.__adyacencias=ListaEnlazada()

    def get_etiqueta(self): 
        return self.__etiqueta

    def get_adyacencias(self): 
        return self.__adyacencias

    def addAdjacency(self, vertice,peso=1):
        if(vertice is None):
            return False

        self.__adyacencias.add_to_rear(dict(neighboor=vertice,weight=peso))
        return True
        
    def is_neighborhood(self, vertice):
        if self.__adyacencias.is_empty() or vertice==self:
            return False

        iterador=self.__adyacencias.iterator()
        while(iterador.has_next()):
            if(next(iterador)['neighboor']==vertice):
                return True
                    
        return False

    def __str__(self):
        temp=self.__etiqueta+'-> '
        if(self.__adyacencias.is_empty()):
            temp+='Vertice Aislado'
        else:
            iterador=self.__adyacencias.iterator()
            while(iterador.has_next()):
                verticeActual=next(iterador)
                nomVecino=verticeActual['neighboor'].__etiqueta
                pesoVecino=verticeActual['weight']
                temp+=f'Vecino: {nomVecino}, Distancia:{pesoVecino}-> '
        return temp

    etiqueta=property(get_etiqueta)
    adyacencias=property(get_adyacencias)
