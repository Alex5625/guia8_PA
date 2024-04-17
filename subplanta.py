from planta import Planta

class Flor(Planta):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)


# esto es la metodo reproduccion
    def polinizar(self):
        print(f"Una abeja está polinizando a {self.get_nombre()}")


class Arbol(Planta):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)

# este es el metodo crecer
    def crecer_fruto(self):
        self.crecer()
        pass

    