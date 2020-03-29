from Grafo import Grafo
from Ciudad import Ciudad
from Rutinas import Rutinas

class GrafoCiudades(Grafo): 
    def __init__(self):
        super(GrafoCiudades,self).__init__()
    
    def add_ciudad(self,etiqueta,latitud,longitud):
        ciudad=self.search_vertice(etiqueta)
        if(not ciudad):
            self.vertices.add_to_rear(Ciudad(etiqueta,latitud,longitud))
    
    def best_first_search(self,src,dst):
        pass

    def get_heuristics(self,node,goal):
        coor1=(node.latitud,node.longitud)
        coor2=(goal.latitud,goal.longitud)
        return Rutinas.haversine_function(coor1,coor2)