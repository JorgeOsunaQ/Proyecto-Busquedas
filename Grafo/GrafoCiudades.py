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
        first=(source, GrafoCiudades.heuristics(source,dest))
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
                    vecino=(vecino,GrafoCiudades.heuristics(vecino,dest))
                    abiertos.append(vecino)
            abiertos.sort(key=itemgetter(1))
        return False

    def branch_and_bound_search(self,source,dest):
        #Cola de vertices abiertos
        abiertos=[]
        first=(0,[source])
        abiertos=[first]
        #Cola de vertices cerrados
        path_found=[]
        cerrados=[]
        while(len(abiertos)!=0):
            #Esto es unicamente una prueba del algoritmo Branch and Bound
            print('------------')
            print('\nABIERTOS:')
            for i in abiertos:
                etiquetas=[x.etiqueta for x in i[1]]
                print(f'{etiquetas} {i[0]}')
            print('\nCERRADOS')
            for i in cerrados:
                print(i.etiqueta)
            print('------------')

            #ads
            pathLength,actual_path=abiertos.pop(0)
            temp=actual_path[-1]

            if(path_found!=[]):
                return path_found
            #if(temp==dest):
                #return actual_path
            
            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)
            #Obtenemos los descendientes inmediatos del vertice
            iterador=temp.adyacencias.iterator()

            for value in iterador:
                vecino=value['neighboor']
                distancia=value['weight']
                #Si el vertice no ha sido abierto aún se agrega a la cola de abiertos
                if(vecino not in cerrados):
                    if(vecino not in actual_path):
                        if(vecino==dest):
                            path_found=actual_path+[vecino]
                        abiertos.append((distancia+pathLength, actual_path+[vecino]))
            abiertos.sort(key=itemgetter(0))          
        return False

    def A_star_search(self,source,dest):
        #Lista de nodos por visitar
        abiertos=[]
        #Lista de nodos visitados
        cerrados=[]
        #Obtenemos el nodo de salida y lo asignamos a la variable "temp"
        actual=source
        actual.set_f(0+GrafoCiudades.heuristics(source,dest))
        while(actual != dest):
            iterador=actual.adyacencias.iterator()
            for value in iterador:
                vecino=value['neighboor']
                if ((vecino not in abiertos) and (vecino not in cerrados)):
                    abiertos.append(vecino)
                    gPadre=actual.get_g()
                    gvecino=value['weight']
                    g=gPadre+gvecino
                    f=g+GrafoCiudades.heuristics(vecino,dest)
                    if ((vecino.get_f()==0) or (f<vecino.get_f())):
                        vecino.set_f(f)
                        vecino.set_g(g)
                        vecino.set_parent(actual)
            cerrados.append(actual)
            '''menor=999999999
            indice=0
            c=0
            for i in abiertos:
                if (i.get_f()<menor):
                    menor=i.get_f()
                    indice=c
                    c+=1'''
            abiertos.sort(key=Grafo.order_by_f)
            #actual=abiertos.pop(indice)
            actual=abiertos.pop(0)
        self.previos(actual)
        return

    def previos(self,dest):
        if (dest==None):
            return
        
        self.previos(dest.parent)

        print (str(dest.etiqueta))
        print ('G:'+str(dest.g)+' F:'+str(dest.f)+' H:'+str(dest.f-dest.g))
        dest.set_g(0)
        dest.set_f(0)
        dest.set_parent(None)

    @classmethod
    def heuristics(cls,node,goal):
        coor1=(node.latitud,node.longitud)
        coor2=(goal.latitud,goal.longitud)
        return round(Rutinas.haversine_function(coor1,coor2),2)