from ListaEnlazada import ListaEnlazada
class Vertice:

    def __init__(self,etiqueta):
        self.etiqueta=etiqueta
        self.adyacencias=ListaEnlazada()
        self.__g=0#A*
        self.__f=0#A*
        self.__come_from=None#A*

    def addAdjacency(self, vertice,peso=1):
        if(vertice is None):
            return False

        self.adyacencias.add_to_rear(dict(neighboor=vertice,weight=peso))
        return True
        
    def is_neighborhood(self, vertice):
        if self.adyacencias.is_empty() or vertice==self:
            return False

        iterador=iter(self.adyacencias)
        while(iterador.has_next()):
            if(next(iterador)['neighboor']==vertice):
                return True
                    
        return False

    def __str__(self):
        temp=self.etiqueta
        if(self.adyacencias.is_empty()):
            temp+='Vertice Aislado'
        else:
            iterador=iter(self.adyacencias)
            while(iterador.has_next()):
                verticeActual=next(iterador)
                nomVecino=verticeActual['neighboor'].etiqueta
                pesoVecino=verticeActual['weight']
                temp+=f'-> {nomVecino} ({pesoVecino} km)'
        return temp

    def get_g(self): 
        return self.__g

    def set_g(self,value): 
        self.__g=value

    def get_f(self): 
        return self.__f

    def set_f(self,value): 
        self.__f=value

    def get_come_from(self): 
        return self.__come_from

    def set_come_from(self,value): 
        self.__come_from=value

    g=property(get_g, set_g)
    f=property(get_f, set_f)
    come_from=property(get_come_from, set_come_from)