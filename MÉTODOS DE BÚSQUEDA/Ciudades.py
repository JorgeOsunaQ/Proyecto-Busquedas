class Ciudades:
    def __init__(self,ciudades):
        self.ciudades = ciudades

    def __getCiudad__(self,ciudad):
        for element in self.ciudades:
            if element.ciudad == ciudad:
                return element
        return None

    def __seeCiudadesYConexiones__(self):
        for i in self.ciudades:
            print(i.ciudad)
            for j in i.conexiones:
                print("     ", j.ciudad)
    
    def __auxProfundidad__(self,listaAbiertos,listaCerrados,destino,contador):
        nodo = listaAbiertos[0]
        conexiones=nodo.conexiones
        listaAbiertos.remove(nodo)
        listaCerrados.insert(0,nodo)
        self.__añadirConexionesProfundidad__(conexiones,listaAbiertos,listaCerrados)
        print('\nITERACIÓN : ', contador)
        print("\nABIERTOS :")
        self.__printLista__(listaAbiertos)
        print("\nCERRADOS: ")
        self.__printLista__(listaCerrados)
        print('\n-------------------------------')
        if nodo.ciudad == destino:
            return
        contador = contador + 1
        self.__auxProfundidad__(listaAbiertos,listaCerrados,destino,contador)

    def __auxAmplitud__(self,listaAbiertos,listaCerrados,destino,contador):
        nodo = listaAbiertos[0]
        conexiones=nodo.conexiones
        listaAbiertos.remove(nodo)
        listaCerrados.insert(0,nodo)
        self.__añadirConexionesAmplitud__(conexiones,listaAbiertos,listaCerrados)
        print('\nITERACIÓN : ', contador)
        print("\nABIERTOS :")
        self.__printLista__(listaAbiertos)
        print("\nCERRADOS: ")
        self.__printLista__(listaCerrados)
        print('\n-------------------------------')
        if nodo.ciudad == destino:
            return
        contador = contador + 1
        self.__auxAmplitud__(listaAbiertos,listaCerrados,destino,contador)

    def __trazarRutaProfundidad__(self,origen,destino):
        nodo = self.__getCiudad__(origen)
        nodoDestino = self.__getCiudad__(destino)
        if nodo == None:
            print('CAPITAL ORIGEN NO EXISTENTE')
            return
        if nodoDestino == None:
            print('CAPITAL DESTINO NO EXISTENTE')
            return
        listaAbiertos = []
        listaAbiertos.insert(0,nodo)
        listaCerrados = []
        self.__auxProfundidad__(listaAbiertos, listaCerrados,destino,1)
        print("\nRUTA TRAZADA")

    def __trazarRutaAmplitud__(self,origen,destino):
        nodo = self.__getCiudad__(origen)
        nodoDestino = self.__getCiudad__(destino)
        if nodo == None:
            print('CAPITAL ORIGEN NO EXISTENTE')
            return
        if nodoDestino == None:
            print('CAPITAL DESTINO NO EXISTENTE')
            return
        listaAbiertos = []
        listaAbiertos.insert(len(listaAbiertos)-1,nodo)
        listaCerrados = []
        self.__auxAmplitud__(listaAbiertos, listaCerrados,destino,1)
        print("\nRUTA TRAZADA")

    def __añadirConexionesProfundidad__(self,conexiones,listaAbiertos, listaCerrados):
        for conexion in conexiones:
            if conexion not in listaAbiertos and conexion not in listaCerrados :
                listaAbiertos.insert(0,conexion)
        return listaAbiertos
    
    def __añadirConexionesAmplitud__(self,conexiones,listaAbiertos, listaCerrados):
        for conexion in conexiones:
            if conexion not in listaAbiertos and conexion not in listaCerrados :
                listaAbiertos.insert(len(listaAbiertos),conexion)
        return listaAbiertos

    def __printLista__(self,lista):
        for element in lista:
            print(element.ciudad)