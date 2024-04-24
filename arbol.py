from planta import Planta

class Arbol(Planta):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.__cantidadfrutos = 0

    def get_frutos(self):
        return self.__cantidadfrutos

    def set_frutos(self,cantidadfrutos):
        if isinstance(cantidadfrutos, int):
            self.__cantidadfrutos = cantidadfrutos

    def crecer_fruto(self):
        self.__cantidadfrutos += 1
        

    
