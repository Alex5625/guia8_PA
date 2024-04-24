from planta import Planta

class Flor(Planta):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__flores = 0

    def set_flores(self,florescantidad):
        if isinstance(florescantidad,int):

            self.__flores = florescantidad

    def get_flores(self):
        return self.__flores

# esto es la metodo reproduccion, propio del tipo flor
    def reproducirse(self):
        print(f"Una abeja está polinizando a {self.get_nombre()}")
        self.__flores =+ 1

