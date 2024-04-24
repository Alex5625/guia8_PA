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
#     def infectar(self, otroorganismo):
#         print(f"{self.get_nombre()} ha infectado a {otroorganismo}")

# # Un numero random para saber si el otro microorganismo muere o no
#         # 0 = vive 
#         # 1 = muere
# # con un random podemos decir si el otro microorganismo murio o no.

#         num = random.randint(0,1)
#         if num == 0:
#             print(f"{self.get_nombre()} ha matado a {otroorganismo}", )
#             return False
#         elif num == 1:
#             print(f"{otroorganismo} ha sobrevivido a la infección")
#             return True






