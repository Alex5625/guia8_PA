from microorganismo import Microorganismo

class Celula(Microorganismo):

    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.__tipo = None
        self.__mutacion = False

    # metodos get y set propios para el tipo

    def set_tipoCel(self,tipo):
        if isinstance(tipo,str):
            self.__tipo = tipo


    def get_tipoCel(self):

        return self.__tipo
    
    # metodo de dividirse de la celula, "reproduccion", agrega
    # otra celula a la lista

    def dividirse(self):
        print(f"La célula {self.get_nombre()} está dividiéndose")

    def mutacionactiva(self):
        self.__mutacion = True
        print(f"{self.get_nombre()} ha sufrido una mutación y puede infectar a otras especies")
        