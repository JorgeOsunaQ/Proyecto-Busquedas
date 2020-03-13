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
                
