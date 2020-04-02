from Grafo import Grafo
from Ciudad import Ciudad
from operator import itemgetter
from Rutinas import Rutinas


class GrafoCiudades(Grafo): 
    def __init__(self):
        super(GrafoCiudades,self).__init__()
    
    def add_ciudad(self,etiqueta,latitud,longitud):
        ciudad=self.search_vertice(etiqueta)
        if(not ciudad):
            self.vertices.add_to_rear(Ciudad(etiqueta,latitud,longitud))
    
    def best_first_search(self,source,dest):
        #Cola de vertices abiertos
        abiertos=[]
        first=(source, self.heuristics(source,dest))
        abiertos.append(first)
        #Cola de vertices cerrados
        cerrados=[]
        while(len(abiertos)!=0):

            #Esto es unicamente una prueba de la Best-First Search
            print('------------')
            print('\nABIERTOS:')
            for i in abiertos:
                print(f'{i[0].etiqueta} {i[1]}')
            print('\nCERRADOS')
            for i in cerrados:
                print(i.etiqueta)
            print('------------')

            #Removemos el primer elemento de la cola de abiertos
            temp=abiertos.pop(0)[0]

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
                if(not any(filter(lambda x: x[0]==vecino,abiertos)) and (vecino not in cerrados)):
                    #Obtenemos la estimación heuristica o distancia restante del vertice al nodo meta
                    vecino=(vecino,self.heuristics(vecino,dest))
                    abiertos.append(vecino)
            abiertos.sort(key=itemgetter(1))
        return False

    def branch_and_bound_search(self,source,dest):
        #Cola de vertices abiertos
        abiertos=[]
        first=(source, 0)
        abiertos.append(first)
        #Cola de vertices cerrados
        cerrados=[]
        while(len(abiertos)!=0):

            #Esto es unicamente una prueba de la Best-First Search
            print('------------')
            print('\nABIERTOS:')
            for i in abiertos:
                print(f'{i[0].etiqueta} {i[1]} Km')
            print('\nCERRADOS')
            for i in cerrados:
                print(i.etiqueta)
            print('------------')

            #Removemos el primer elemento de la cola de abiertos
            temporal=abiertos.pop(0)
            pesoPadre = temporal[1]
            temp= temporal[0]
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
                if(not any(filter(lambda x: x[0]==vecino,abiertos)) and (vecino not in cerrados)):
                    #Obtenemos la estimación heuristica o distancia restante del vertice al nodo meta
                    vecino=(vecino,value['weight'] + pesoPadre)
                    abiertos.append(vecino)
            abiertos.sort(key=itemgetter(1))
        return False

    def heuristics(self,node,goal):
        coor1=(node.latitud,node.longitud)
        coor2=(goal.latitud,goal.longitud)
        return round(Rutinas.haversine_function(coor1,coor2),2)