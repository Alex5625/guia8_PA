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
            raise TypeError("Tipo de caracter equivocado")

    # metodos que mas adelante seran implementados con
    # polimorfismo dependiendo de la especie

    def moverse(self):
        print(f"{self.get_nombre()} está caminando")

    def hacersonido(self):

        print(f"{self.get_nombre()} está haciendo un sonido")

        pass

        