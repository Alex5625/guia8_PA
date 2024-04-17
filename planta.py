from organismo import Organismo

class Planta(Organismo):

    def __init__(self, nombre, edad):

        super().__init__(self, nombre ,edad)
        self.__tipos = str


##en organismo no hay npatas 
   
    def get_tipos(self, tipo):
        if isinstance(tipo,str):
            self.__tipos = tipo
        pass

    def set_tipos(self):
        return self.__tipos

# esto es la fotosintesis. Haciendo un polimorfismo
    def crecer(self):
        print(f"{self.get_nombre()} está haciendo fotosíntesis")
        self.crecer()

    