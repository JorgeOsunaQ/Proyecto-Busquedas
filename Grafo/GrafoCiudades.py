from Grafo import Grafo
from Ciudad import Ciudad
from operator import itemgetter


class GrafoCiudades(Grafo): 
    def __init__(self):
        super(GrafoCiudades,self).__init__()
    
    def add_ciudad(self,etiqueta,latitud,longitud):
        ciudad=self.search_vertice(etiqueta)
        if(not ciudad):
            self.vertices.add_to_rear(Ciudad(etiqueta,latitud,longitud))
    
    def best_first_search(self,source,dest):
        #Cola de vertices abiertos
        source.f=GrafoCiudades.heuristics(source,dest)
        abiertos=[source]
        #Cola de vertices cerrados
        cerrados=[]
        iteraciones=''
        count=0
        while(len(abiertos)!=0):
            count+=1
            #Guardamos las iteraciones por las que pasa el algoritmo como mera demostración
            iteraciones+=Grafo.get_iteracion(abiertos,cerrados,dest,count,True)

            #Removemos el primer elemento de la cola de abiertos
            temp=abiertos.pop(0)

            #Si es igual al vertice de destino entonces se encontró la ruta
            if(temp==dest):
                cerrados.append(temp)
                Grafo.set_default_values(abiertos)
                Grafo.set_default_values(cerrados)
                return cerrados,iteraciones

            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)

            #Obtenemos los descendientes inmediatos del vertice
            iterador=iter(temp.adyacencias)

            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la cola de abiertos
                if((vecino not in abiertos) and (vecino not in cerrados)):
                    '''Asignamos la estimación heuristica al vértice de acuerdo
                     al algoritmo best-first search, donde el costo total del camino es f(n)=h(n)
                    '''
                    vecino.f=Grafo.heuristics(vecino,dest)
                    abiertos.append(vecino)
            abiertos.sort(key=lambda x: x.f)
        return False,iteraciones

    def A_star_search(self,source,dest):
        #Lista de nodos por visitar
        abiertos=[]
        #Lista de nodos visitados
        cerrados=[]
        #Obtenemos el nodo de salida y lo asignamos a la variable "actual"
        actual=source
        #Inicializamos el valor del costo total f(n) de acuerdo al algoritmo A*
        actual.set_f(0+GrafoCiudades.heuristics(source,dest))
        count=0
        iteraciones=''
        while(actual != dest):
            count+=1
            iterador=iter(actual.adyacencias)          
            #Iteramos sobre los vértices adyacentes del nodo "actual"
            for value in iterador:
                #Solo obtenemos el objeto Vertice del elemento dictionary
                vecino=value['neighboor']
                #Verificamos que el vértice no se encuentre en la lista de nodos visitados y por visitar
                if ((vecino not in abiertos) and (vecino not in cerrados)):
                    #Agregamos la adyacencia a la lista de nodos por visitar
                    abiertos.append(vecino)
                    #Obtenemos la distancia recorrida desde el vértice meta al nodo actual
                    gPadre=actual.get_g()
                    #Obtenemos el peso de la relación del vértice actual con su adyacencia
                    gvecino=value['weight']
                    #Determinamos g(n) con la suma de ambas distancias recorridas
                    g=gPadre+gvecino
                    #Establecemos el costo total del camino f(n)=g(n)+h(n) de acuerdo al algoritmo A*
                    f=g+Grafo.heuristics(vecino,dest)
                    #Si el costo total del camino recorrido por el nodo es igual a cero o menor al costo total calculado
                    if ((vecino.get_f()==0) or (f<vecino.get_f())):
                        #Se agregan los valores de f(n) y g(n) al vértice
                        vecino.set_f(f)
                        vecino.set_g(g)
                        #Fijamos el "padre" del vértice como una referencia al nodo actual
                        vecino.set_come_from(actual)
            #Agregamos al vértice actual a la lista de visitados
            cerrados.append(actual)
            #Ordenamos la lista de visitados de acuerdo al costo total f(n) de los vértices
            abiertos.sort(key=Grafo.sort_by_f)
            iteraciones+=Grafo.get_iteracion(abiertos,cerrados,dest,count,True)

            #actual=abiertos.pop(indice)
            actual=abiertos.pop(0)
        path=[]
        if(actual==dest):
            cerrados.append(actual)
        GrafoCiudades.reconstruct_path(actual,path)
        Grafo.set_default_values(abiertos)
        Grafo.set_default_values(cerrados) 
        return path,iteraciones;