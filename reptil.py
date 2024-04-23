from animal import Animal

class Reptil(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # implementado con el metodo de crecer()
    # al ser algo propio de la clase

    def cambiardepiel(self):
        print(f"{self.get_nombre()} ha cambiado de piel")
        self.crecer()
        