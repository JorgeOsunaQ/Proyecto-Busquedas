import math
import pandas as pd
class Rutinas(object):

    E_Radius=6378

    @classmethod
    def haversine_function(cls,coor1,coor2):
        lat1=math.radians(coor1[0])
        lat2=math.radians(coor2[0])
        lon1=math.radians(coor1[1])
        lon2=math.radians(coor2[1])

        dlat=lat2-lat1
        dlon=lon2-lon1

        a=(math.sin(dlat/2)**2)+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        d=cls.E_Radius*c
        return d

    @staticmethod
    def get_datos_ciudades():
        return pd.read_csv('Grafo\CSV\ciudades.csv')

    @staticmethod
    def get_conexiones_ciudades():
        return pd.read_csv('Grafo\CSV\conexiones.csv')