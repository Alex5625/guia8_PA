from organismo import Organismo
import random

class Microorganismo(Organismo):
    def __init__(self,nombre,edad):
        super().__init__(nombre, edad)
        self.__tipo = None

    # metodos get y set para el tipo

    def set_tipoMicro(self, tipo):
        if isinstance(tipo,str):
            self.__tipo = tipo

    def get_tipoMicro(self):
        return self.__tipo

    def reproducirse(self):
        pass

# interaccion con otras clases/objetos
    def infectar(self, otroorganismo):
        print(self.get_nombre(), " ha infectado a ", otroorganismo)

        num = random.randint(0,2)


# Un numero random para saber si el otro microorganismo muere o no
        # 0 = vive 
        # 1 = muere
        if num != 0:
            self.muere()
            print("vas a morir")
        else:
            print("viviste")
            self.vivo()


# con un random podemos decir si el otro microorganismo murio o no.


