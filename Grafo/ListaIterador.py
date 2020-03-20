class ListaIterador:

    def __init__(self, inicio):
        self.actual=inicio

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.has_next():
            raise StopIteration

        temp=self.actual.element
        self.actual=self.actual.next
        return temp

    def has_next(self):
        return self.actual!=None

    
        