from planta import Planta

class Flor(Planta):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

# esto es la metodo reproduccion
    def reproducirse(self):
        print(f"Una abeja está polinizando a {self.get_nombre()}")


class Arbol(Planta):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)

# este es el metodo crecer, en arbol
# se puede considerar que crece con
# fotosintesis y produciendo un fruto
    def crecer_fruto(self):
        self.crecer()
        pass

    