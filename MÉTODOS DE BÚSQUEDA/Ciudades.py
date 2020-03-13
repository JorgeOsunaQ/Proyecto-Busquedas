class Ciudades:
    def __init__(self,ciudades):
        self.ciudades = ciudades

    def __getCiudad__(self,ciudad):
        for element in self.ciudades:
            if element.ciudad == ciudad:
                return element

    def __seeCiudadesYConexiones__(self):
        for i in self.ciudades:
            print(i.ciudad)
            for j in i.conexiones:
                print("     ", j.ciudad)
    
    def __auxProfundidad__(self,listaAbiertos,listaCerrados,destino):
        nodo = listaAbiertos[0]
        conexiones=nodo.conexiones
        listaAbiertos.remove(nodo)
        listaCerrados.insert(0,nodo)
        self.__añadirConexionesProfundidad__(conexiones,listaAbiertos,listaCerrados)
        print("\nABIERTOS :")
        self.__printLista__(listaAbiertos)
        print("\nCERRADOS: ")
        self.__printLista__(listaCerrados)
        if nodo.ciudad == destino:
            return
        self.__auxProfundidad__(listaAbiertos,listaCerrados,destino)

    def __auxAmplitud__(self,listaAbiertos,listaCerrados,destino):
        nodo = listaAbiertos[0]
        conexiones=nodo.conexiones
        listaAbiertos.remove(nodo)
        listaCerrados.insert(0,nodo)
        self.__añadirConexionesAmplitud__(conexiones,listaAbiertos,listaCerrados)
        print("\nABIERTOS :")
        self.__printLista__(listaAbiertos)
        print("\nCERRADOS: ")
        self.__printLista__(listaCerrados)
        if nodo.ciudad == destino:
            return
        self.__auxAmplitud__(listaAbiertos,listaCerrados,destino)

    def __trazarRutaProfundidad__(self,origen,destino):
        nodo = self.__getCiudad__(origen)
        listaAbiertos = []
        listaAbiertos.insert(0,nodo)
        listaCerrados = []
        self.__auxProfundidad__(listaAbiertos, listaCerrados,destino)
        print("\nRUTA TRAZADA")

    def __trazarRutaAmplitud__(self,origen,destino):
        nodo = self.__getCiudad__(origen)
        listaAbiertos = []
        listaAbiertos.insert(len(listaAbiertos)-1,nodo)
        listaCerrados = []
        self.__auxAmplitud__(listaAbiertos, listaCerrados,destino)
        print("\nRUTA TRAZADA")

    def __existeEnCola__(self,nodo,cola):
        for element in cola:
            if element == nodo:
                return True
        return False

    def __añadirConexionesProfundidad__(self,conexiones,listaAbiertos, listaCerrados):
        for conexion in conexiones:
            if self.__existeEnCola__(conexion,listaAbiertos) == False and self.__existeEnCola__(conexion,listaCerrados) == False :
                listaAbiertos.insert(0,conexion)
        return listaAbiertos
    
    def __añadirConexionesAmplitud__(self,conexiones,listaAbiertos, listaCerrados):
        for conexion in conexiones:
            if self.__existeEnCola__(conexion,listaAbiertos) == False and self.__existeEnCola__(conexion,listaCerrados) == False :
                listaAbiertos.insert(len(listaAbiertos)-1,conexion)
        return listaAbiertos

    def __printLista__(self,lista):
        for element in lista:
            print(element.ciudad)