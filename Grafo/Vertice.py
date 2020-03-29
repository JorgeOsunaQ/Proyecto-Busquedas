from ListaEnlazada import ListaEnlazada
class Vertice:

    def __init__(self,etiqueta):
        self.etiqueta=etiqueta
        self.adyacencias=ListaEnlazada()

    def addAdjacency(self, vertice,peso=1):
        if(vertice is None):
            return False

        self.adyacencias.add_to_rear(dict(neighboor=vertice,weight=peso))
        return True
        
    def is_neighborhood(self, vertice):
        if self.adyacencias.is_empty() or vertice==self:
            return False

        iterador=self.adyacencias.iterator()
        while(iterador.has_next()):
            if(next(iterador)['neighboor']==vertice):
                return True
                    
        return False

    def __str__(self):
        temp=self.etiqueta+'-> '
        if(self.adyacencias.is_empty()):
            temp+='Vertice Aislado'
        else:
            iterador=self.adyacencias.iterator()
            while(iterador.has_next()):
                verticeActual=next(iterador)
                nomVecino=verticeActual['neighboor'].etiqueta
                pesoVecino=verticeActual['weight']
                temp+=f'Vecino: {nomVecino}, Distancia:{pesoVecino} km-> '
        return temp