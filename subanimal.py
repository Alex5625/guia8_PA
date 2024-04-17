from animal import Animal

class Ave(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    # polimorfismo
    def moverse(self):
        print(f"{self.get_nombre()} está volando")


class Mamifero(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def lactar(self):
        print("El animal está lactando")
        

class Reptil(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def cambiardepiel(self):
        print(f"{self.get_nombre()} ha cambiado de piel")
        self.crecer()
        