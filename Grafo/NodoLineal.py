class Nodo:

    def __init__(self, elemento=None):
        self.__element=elemento
        self.__next=None
    
    def get_element(self): 
        return self.__element

    def set_element(self,element): 
        self.__element=element

    def get_next(self): 
        return self.__next

    def set_next(self,next):
        self.__next=next    
    
    element=property(get_element)
    next=property(get_next, set_next)