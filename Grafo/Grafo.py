from ListaEnlazada import *
from Vertice import *
from Rutinas import *
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
        iterador=iter(self.vertices)

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
        iteraciones=''
        count=0
        while(len(abiertos)!=0):
            count+=1
            #Guardamos las iteraciones por las que pasa el algoritmo como mera demostración 
            iteraciones+=Grafo.get_iteracion(abiertos,cerrados,dest,count,False)
            #Removemos el primer elemento de la cola de abiertos
            temp=abiertos.pop(0)
            #Si es igual al vertice de destino entonces se encontró la ruta
            if(temp==dest):
                cerrados.append(temp)
                return cerrados,iteraciones;

            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)
            #Obtenemos los descendientes inmediatos del vertice
            iterador=iter(temp.adyacencias)
            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la cola de abiertos
                if((vecino not in abiertos) and (vecino not in cerrados)):
                    abiertos.append(vecino)
        return False,iteraciones;

    #Algoritmo para trazar busqueda en profundidad
    def depth_first_search(self,source,dest):
        #Cola de vertices abiertos (Agregamos el vertice de salida al inicio)
        abiertos=[]
        abiertos.append(source)
        #Cola de vertices cerrados
        cerrados=[]
        #Mientras la cola de abiertos no esté vacía
        iteraciones=''
        count=0
        while(len(abiertos)!=0):
            count+=1
            #Guardamos las iteraciones por las que pasa el algoritmo como mera demostración
            iteraciones+=Grafo.get_iteracion(abiertos,cerrados,dest,count,False)

            #Removemos el primer elemento de la pila de abiertos
            temp=abiertos.pop(0)
            #Si es igual al vertice de destino entonces se encontró la ruta
            if(temp==dest):
                cerrados.append(temp)
                return cerrados,iteraciones;
            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)
            #Obtenemos los descendientes inmediatos del vertice
            iterador=iter(temp.adyacencias)
            listTemp=[]
            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la pila de abiertos
                if((vecino not in abiertos) and (vecino not in cerrados)):
                    listTemp.append(vecino)
            abiertos=listTemp+abiertos
        return False,iteraciones;

    #Opción no.1
    def branch_and_bound_search(self,source,dest):
        #Cola de vertices abiertos
        abiertos=[source]
        #Cola de vertices cerrados
        path=[]
        cerrados=[]
        source.f=0
        iteraciones=''
        count=0
        while(len(abiertos)!=0):
            count+=1
            #Guardamos las iteraciones por las que pasa el algoritmo como mera demostración
            iteraciones+=Grafo.get_iteracion(abiertos,cerrados,dest,count,True)

            temp=abiertos.pop(0)
            #Si no está en la cola de cerrados entonces lo agregamos
            if(temp not in cerrados):
                cerrados.append(temp)
            #Si el vértice temp coincide con el vértice de destino entonces reconstruimos su paso para obtener el camino
            if(temp==dest):
                self.reconstruct_path(temp,path)
                Grafo.set_default_values(cerrados) 
                Grafo.set_default_values(abiertos)
                return path,iteraciones;
            #Obtenemos los descendientes inmediatos del vertice
            iterador=iter(temp.adyacencias)
            for value in iterador:
                vecino=value['neighboor']
                #Si el vertice no ha sido abierto aún se agrega a la cola de abiertos
                if(vecino not in cerrados):
                    #Obtenemos la distancia recorrida desde el vértice meta al nodo actual
                    gPadre=temp.g
                    #Obtenemos el peso de la relación del vértice actual con su adyacencia
                    gValue=value['weight']
                    #Establecemos el costo total del camino f(n)=g(n) de acuerdo al algoritmo UCS Branch and bound
                    f=gValue+gPadre
                    #Verificamos que f(n) del camino de la adyacencia sea nulo o menor al que encontramos
                    if((vecino.f==0) or (f<vecino.f)):
                        #Agregamos la adyacencia a la lista de vértices por visitar
                        if(vecino not in abiertos):
                            abiertos.append(vecino)
                        #Asignamos los valores del camino encontrado al vertice
                        vecino.g=f
                        vecino.f=f
                        vecino.come_from=temp
            #Ordenamos la lista de visitados de acuerdo al costo total f(n) de los vértices
            abiertos.sort(key=Grafo.sort_by_f)         
        return False,iteraciones;

    def __str__(self):
        temp=''
        if(self.vertices.is_empty()):
            return'Sin Vertices'

        iterador=iter(self.vertices)
        while(iterador.has_next()):
            temp+=str(next(iterador))+'\n\n'
        return temp

    @classmethod
    def sort_by_f(cls,vertice):
        if(isinstance(vertice,Vertice)):
            return vertice.get_f()
        
    @classmethod
    def sort_by_first(cls,element):
        return element[0]

    @classmethod
    def reconstruct_path(cls,dest,path):
        if (dest==None):
            return
        
        cls.reconstruct_path(dest.come_from,path)
        path.append(dest)
    
    @classmethod 
    def set_default_values(cls, list):
        for i in list:
            i.set_f(0)
            i.set_g(0)
            i.set_come_from(None)

    @classmethod
    def heuristics(cls,node,goal):
        coor1=(node.latitud,node.longitud)
        coor2=(goal.latitud,goal.longitud)
        return round(Rutinas.haversine_function(coor1,coor2),2)
    
    @classmethod 
    def get_iteracion(cls, abiertos, cerrados,dest,count,is_informed):
            iteracion=''
            iteracion+=f'\nITERACIÓN #{count}\n'
            iteracion+='ABIERTOS:\n'

            if(is_informed):
                for i in abiertos:
                    iteracion+=f'{i.etiqueta}\nF(n):{str(round(i.f,2))} G(n):{i.g} H(n):{Grafo.heuristics(i,dest)}\n'
            else:
                for i in abiertos:
                    iteracion+=f'{i.etiqueta}\n'

            iteracion+='\nCERRADOS:\n'
            for i in cerrados:
                iteracion+=f'{i.etiqueta}\n'
            return iteracion
