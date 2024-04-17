from organismo import Organismo

class Planta(Organismo):

    def __init__(self, nombre, edad):

        super().__init__(nombre, edad)
        self.__tipo = None


##en organismo no hay npatas 
   
    def set_tipo(self, tipo):
        if isinstance(tipo,str):
            self.__tipo = tipo
        pass

    def get_tipo(self):
        return self.__tipo

# esto es la fotosintesis. Haciendo un polimorfismo
    def fotosintesis(self):
        print(f"{self.get_nombre()} está haciendo fotosíntesis")

    def reproducirse(self):
        print(f"{self.get_nombre()} se está reproduciendo")

    