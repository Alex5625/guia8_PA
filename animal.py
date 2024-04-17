from organismo import Organismo

class Animal(Organismo):
    def __init__ (self, nombre, edad):
        super().__init__(nombre, edad)
        self.__numero_patas = None

    #metodos get y set
        
    def get_nPatas(self):
        return self.__numero_patas

    def set_nPatas(self,numero):
        if isinstance(numero, int):
            self.__numero_patas = numero
        else:
            print

    def moverse(self):
        print(f"{self.get_nombre()} está caminando")

    def hacersonido():
        pass

        