from ListaEnlazada import ListaEnlazada
from Vertice import Vertice
class Grafo:

    def __init__(self):
        self.vertices=ListaEnlazada()
    
    def add_vertice(self,etiqueta):
        vertice=self.search_vertice(etiqueta)
        if(not vertice):
            self.vertices.add_to_rear(Vertice(etiqueta))

    def add_arista(self, src,dst,peso=1):
        source=self.search_vertice(src)
        dest=self.search_vertice(dst)

        if((not dest) or (not source)):
            return 0

        if(dest.is_neighborhood(source) or source.is_neighborhood(dest)):
            return 1

        source.addAdjacency(dest,peso)
        dest.addAdjacency(source,peso)
        return 3

    def search_vertice(self,etiqueta):
        iterador=self.vertices.iterator()

        while(iterador.has_next()):
            actual=next(iterador)
            if(etiqueta==actual.etiqueta):
                return actual

        return False

    #Algoritmo para trazar busqueda en amplitud
    def breadth_first_search(self,source,dest):
        abiertos=[]
        abiertos.append(source)
        #Cola de vertices cerrados
        cerrados=[]
        #Mientras la cola de abiertos no esté vacía
        while(len(abiertos)!=0):
            #Esto es unicamente una prueba de la busqueda en amplitud:
            print('------------')
            print('\nABIERTOS:')
            for i in abiertos:
                print(i.etiqueta)
            print('\nCERRADOS')
            for i in cerrados:
                print(i.etiqueta)
            print('------------')
            #Removemos el primer elemento de la cola de abiertos
            temp=abiertos.pop(0)
            #Si es igual al vertice de destino entonces se encontró la ruta
            if(temp==dest):
                cerrados.append(temp)
                return cerrados
            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)
            #Obtenemos los descendientes inmediatos del vertice
            iterador=temp.adyacencias.iterator()
            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la cola de abiertos
                if((vecino not in abiertos) and (vecino not in cerrados)):
                    abiertos.append(vecino)
        return False

    #Algoritmo para trazar busqueda en profundidad
    def depth_first_search(self,source,dest):
        #Cola de vertices abiertos (Agregamos el vertice de salida al inicio)
        abiertos=[]
        abiertos.append(source)
        #Cola de vertices cerrados
        cerrados=[]
        #Mientras la cola de abiertos no esté vacía
        while(len(abiertos)!=0):
            
            #Esto es unicamente una prueba de la busqueda en profundidad:
            print('------------')
            print('\nABIERTOS:')
            for i in abiertos:
                print(i.etiqueta)
            print('\nCERRADOS')
            for i in cerrados:
                print(i.etiqueta)
            print('------------')
            
            #Removemos el primer elemento de la pila de abiertos
            temp=abiertos.pop(0)
            #Si es igual al vertice de destino entonces se encontró la ruta
            if(temp==dest):
                cerrados.insert(0,temp)
                return cerrados
            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.insert(0,temp)
            #Obtenemos los descendientes inmediatos del vertice
            iterador=temp.adyacencias.iterator()
            listTemp=[]
            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la pila de abiertos
                if((vecino not in abiertos) and (vecino not in cerrados)):
                    listTemp.append(vecino)
            abiertos=listTemp+abiertos
        return False

    def __str__(self):
        temp=''
        if(self.vertices.is_empty()):
            return'Sin Vertices'

        iterador=self.vertices.iterator()
        while(iterador.has_next()):
            temp+=str(next(iterador))+'\n'
        return temp

    @classmethod
    def order_by_f(cls,vertice):
        if(isinstance(vertice,Vertice)):
            return vertice.get_f()
            