from animal import Animal

class Ave(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    
    # polimorfismo, propio de la clase
    def moverse(self):
        print(f"{self.get_nombre()} está volando")
