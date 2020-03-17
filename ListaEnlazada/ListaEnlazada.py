from NodoLineal import Nodo
from ListaIterador import ListaIterador

class ListaEnlazada:
    
    def __init__(self):
        self.__inicio=None
        self.__fin=None
        self.__count=0

    def addToFront(self,elemento):
        if(elemento is None):
            return False

        nuevo=Nodo(elemento)
        if(self.isEmpty()):
            self.__inicio=self.__fin=nuevo
        else: 
            nuevo.next=self.__inicio
            self.__inicio=nuevo
        self.__count+=1
        return True

    def addToRear(self,elemento):
        if(elemento is None):
            return False

        nuevo=Nodo(elemento)
        if(self.isEmpty()):
            self.__inicio=self.__fin=nuevo
        else: 
            self.__fin.next=nuevo
            self.__fin=nuevo
        self.__count+=1
        return True

    def addSorted(self,elemento):
        pass

    def removeFirst(self):
        if self.isEmpty():
            return False
        temp=self.inicio.element
        self.__inicio=self.inicio.next

        self.__count-=1
        return temp
    
    def removeLast(self):
        if self.isEmpty():
            return False

        if(self.size()==1):
            return self.removeFirst()

        actual=self.inicio
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

        if(elem==self.inicio.element):
            return self.removeFirst()
        
        if(elem==self.fin.element):
            return self.removeLast()

        actual=self.inicio
        anterior=None

        while(elem!=actual.element):
            anterior=actual
            actual=actual.next
        
        temp=actual.element
        anterior.next=actual.next

        self.__count+=-1
        return temp
        
    def contains(self, elem):

        if(self.isEmpty()):
            return False
        
        iterador=self.iterator()

        while(iterador.hasNext()):
            if(elem is next(iterador)):
                return True

    def impr(self):
        if(self.isEmpty()):
            return 'No hay tortillas'

        impresion=''
        iterador=self.iterator()
        while(iterador.hasNext()):
                 impresion+='\n'+str(next(iterador))
        return impresion

    def iterator(self):
        return iter(ListaIterador(self.inicio))

    def isEmpty(self):
        return self.__count==0

    def size(self):
        return self.__count

    def get_inicio(self):
        return self.__inicio

    def get_fin(self):
        return self.__fin

    inicio=property(get_inicio)
    fin=property(get_fin)

#Pruebas vrgas
lista=ListaEnlazada()
lista.addToFront('Culiacan')
lista.addToFront('Durango')
lista.addToFront('Mazatlan')
lista.addToFront('Navolato')
lista.addToFront('Hermosillo')
lista.addToFront('Tijuana')

print(lista.impr())
lista.remove('Durango')
print(lista.impr())
lista.removeLast()
print(lista.impr())
lista.removeFirst()
print(lista.impr())