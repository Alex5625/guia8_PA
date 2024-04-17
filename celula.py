from microorganismo import Microorganismo

class Celula(Microorganismo):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__tipo = None


    def set_tipoCel(self,tipo):
        if isinstance(tipo,str):
            self.__tipo = tipo


    def get_tipoCel(self):

        return self.__tipo
    
    def dividirse(self):
        print(f"La célula {self.get_nombre} está dividiéndose")
        self.crecer()