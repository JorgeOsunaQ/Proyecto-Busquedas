from NodoLineal import Nodo
from ListaIterador import ListaIterador

class ListaEnlazada:
    
    def __init__(self):
        self.__inicio=None
        self.__fin=None
        self.__count=0

    def get_inicio(self):
        return self.__inicio

    def get_fin(self):
        return self.__fin

    def add_to_front(self,elemento):
        if(elemento is None):
            return False

        nuevo=Nodo(elemento)
        if(self.is_empty()):
            self.__inicio=self.__fin=nuevo
        else: 
            nuevo.next=self.__inicio
            self.__inicio=nuevo
        self.__count+=1
        return True

    def add_to_rear(self,elemento):
        if(elemento is None):
            return False

        nuevo=Nodo(elemento)
        if(self.is_empty()):
            self.__inicio=self.__fin=nuevo
        else: 
            self.__fin.next=nuevo
            self.__fin=nuevo
        self.__count+=1
        return True

    def add_sorted(self,elemento):
        pass

    def remove_first(self):
        if self.is_empty():
            return False
        temp=self.__inicio.element
        self.__inicio=self.__inicio.next

        self.__count-=1
        return temp
    
    def remove_last(self):
        if self.is_empty():
            return False

        if(self.size()==1):
            return self.remove_first()

        actual=self.__inicio
        anterior=None

        while(actual.next!=None):
            anterior=actual
            actual=actual.next

        temp=actual.element
        anterior.set_next(None)
        self.__fin=anterior

        self.__count-=1
        return temp

    def remove(self,elem):
        if not self.contains(elem):
            return False

        if(elem==self.__inicio.element):
            return self.remove_first()
        
        if(elem==self.__fin.element):
            return self.remove_last()

        actual=self.__inicio
        anterior=None

        while(elem!=actual.element):
            anterior=actual
            actual=actual.next
        
        temp=actual.element
        anterior.next=actual.next

        self.__count+=-1
        return temp
        
    def contains(self, elem):

        if(self.is_empty()):
            return False
        
        iterador=self.iterator()

        while(iterador.has_next()):
            if(elem is next(iterador)):
                return True

    def iterator(self):
        return iter(ListaIterador(self.__inicio))

    def is_empty(self):
        return self.__count==0

    def size(self):
        return self.__count

    inicio=property(get_inicio)
    fin=property(get_fin)
