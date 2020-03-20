from Nodo import Nodo
from Ciudades import Ciudades

La_Paz= Nodo('La paz')
Mexicali = Nodo('Mexicali')
Hermosillo = Nodo('Hermosillo')
Chihuahua = Nodo('Chihuahua')
Culiacan = Nodo('Culiacan')
Durango = Nodo('Durango')
Saltillo = Nodo('Saltillo')
Zacatecas = Nodo('Zacatecas')
Tepic= Nodo('Tepic')
Monterrey= Nodo('Monterrey')
Ciudad_Victoria= Nodo('Ciudad Victoria')
San_Luis= Nodo('San Luis')
Aguascalientes= Nodo('Aguascalientes')
Guadalajara= Nodo('Guadalajara')
Colima= Nodo('Colima')
Guanajuato= Nodo('Guanajuato')
Queretaro= Nodo('Queretaro')
Morelia= Nodo('Morelia')
Chilpancingo= Nodo('Chilpancingo')
Pachuca= Nodo('Pachuca')
Cuernavaca= Nodo('Cuernavaca')
Toluca= Nodo('Toluca')
CDMX= Nodo('CDMX')
Xalapa= Nodo('Xalapa')
Oaxaca= Nodo('Oaxaca')
Villahermosa= Nodo('Villahermosa')
Campeche= Nodo('Campeche')
Merida= Nodo('Merida')
Chetumal= Nodo('Chetumal')
Tlaxcala= Nodo('Tlaxcala')
Puebla= Nodo('Puebla')
Tuxla= Nodo('Tuxla')

#CONEXIONES
La_Paz.__conexiones__([Mexicali])
Mexicali.__conexiones__([La_Paz,Hermosillo])
Hermosillo.__conexiones__([Culiacan,Chihuahua, Mexicali])
Chihuahua.__conexiones__([Saltillo,Durango,Culiacan,Hermosillo])
Saltillo.__conexiones__([Chihuahua,Durango,Zacatecas,Monterrey])
Culiacan.__conexiones__([Hermosillo,Durango,Chihuahua,Tepic])
Durango.__conexiones__([Chihuahua,Saltillo,Zacatecas,Culiacan,Tepic])
Monterrey.__conexiones__([Saltillo,Zacatecas,San_Luis,Ciudad_Victoria])
Tepic.__conexiones__([Culiacan,Durango,Zacatecas,Guadalajara])
Zacatecas.__conexiones__([San_Luis,Monterrey,Saltillo,Durango,Aguascalientes,Tepic])
San_Luis.__conexiones__([Monterrey,Zacatecas,Ciudad_Victoria,Pachuca,Queretaro,Guadalajara,Guanajuato,Xalapa])
Guadalajara.__conexiones__([Tepic,Colima,Aguascalientes,Morelia,Guanajuato,San_Luis])
Aguascalientes.__conexiones__([Guadalajara,Zacatecas])
Ciudad_Victoria.__conexiones__([San_Luis,Monterrey,Xalapa])
Guanajuato.__conexiones__([San_Luis,Queretaro,Morelia,Guadalajara])
Colima.__conexiones__([Morelia,Guadalajara])
Morelia.__conexiones__([Guadalajara,Colima,Guanajuato,Queretaro,Toluca,Chilpancingo])
Queretaro.__conexiones__([San_Luis,Pachuca,Toluca,Guanajuato,Morelia])
Xalapa.__conexiones__([Ciudad_Victoria,San_Luis,Villahermosa,Tuxla,Oaxaca,Puebla])
Toluca.__conexiones__([Morelia,Queretaro,Pachuca,Tlaxcala,Cuernavaca,CDMX,Puebla])
Chilpancingo.__conexiones__([Morelia,Cuernavaca,Oaxaca,Puebla])
Tlaxcala.__conexiones__([Pachuca,Puebla,Toluca])
CDMX.__conexiones__([Toluca,Cuernavaca])
Puebla.__conexiones__([Xalapa,Tlaxcala,Oaxaca,Cuernavaca,Toluca,Chilpancingo])
Cuernavaca.__conexiones__([CDMX,Puebla,Chilpancingo,Toluca])
Oaxaca.__conexiones__([Chilpancingo,Puebla,Xalapa,Tuxla])
Tuxla.__conexiones__([Oaxaca,Xalapa,Villahermosa])
Villahermosa.__conexiones__([Tuxla,Xalapa,Campeche])
Campeche.__conexiones__([Merida,Villahermosa])
Merida.__conexiones__([Campeche,Chetumal])
Chetumal.__conexiones__([Merida,Campeche])
Pachuca.__conexiones__([Tlaxcala,Toluca,Queretaro,Xalapa,Puebla])

#INSERSION LIST
listCiudades = [La_Paz,Mexicali,Hermosillo,Chihuahua,Culiacan,Durango,
Saltillo,Zacatecas,Tepic,Monterrey,Ciudad_Victoria,San_Luis,Aguascalientes,
Guadalajara,Colima,Guanajuato,Queretaro,Morelia,Chilpancingo,Pachuca,
Cuernavaca,Toluca,CDMX,Xalapa,Oaxaca,Villahermosa,Campeche,Merida,
Chetumal,Tlaxcala,Puebla,Tuxla]

#CREACIÓN LIST CIUDADES
ciudades = Ciudades(listCiudades)

opcion = -1
while opcion != 3:
    print('\n--MENU--')
    print('1.- TRAZAR RUTA POR AMPLITUD\n2.- TRAZAR RUTA POR PROFUNDIDAD\n3.- SALIR')
    opcion = int(input())
    print('ORIGEN: ')
    origen = input()
    print('DESTINO: ')
    destino = input()
    if opcion == 1:
        ciudades.__trazarRutaAmplitud__(origen,destino)
    if opcion == 2:
        ciudades.__trazarRutaProfundidad__(origen,destino)
