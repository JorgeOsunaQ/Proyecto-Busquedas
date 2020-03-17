class Vertice:

    def __init__(self,nombre):
        self.__nombre=nombre
        self.__aristas=None

    def get_nombre(self): 
        return self.__nombre

    def get_next(self): 
        return self.__next

    def set_next(self,next):
        self.__next=next   

    def __str__(self):
        return self.__nombre

    nombre=property(get_nombre)
