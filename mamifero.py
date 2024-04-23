from animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def lactar(self):
        print("El animal está lactando")
        