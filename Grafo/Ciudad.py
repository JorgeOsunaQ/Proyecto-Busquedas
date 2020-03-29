from Vertice import Vertice
class Ciudad(Vertice):
    
    def __init__(self,etiqueta,lat,lon):
        super().__init__(etiqueta)
        self.__latitud=lat
        self.__longitud=lon
     
    def get_latitud(self):
        return self.__latitud
    
    def get_longitud(self):
        return self.__longitud
    
    latitud=property(get_latitud)
    longitud=property(get_longitud)

    