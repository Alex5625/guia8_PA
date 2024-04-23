from planta import Planta

class Arbol(Planta):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.__cantidadfrutos = int

    def get_frutos(self):
        return self.__cantidadfrutos

    def set_frutos(self,cantidadfrutos):
        self.__cantidadfrutos = cantidadfrutos

    def crecer_fruto(self,cantidadfrutos):
        self.__cantidadfrutos =+ 1
        

    
