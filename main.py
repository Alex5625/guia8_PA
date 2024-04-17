from subanimal import Ave
from subanimal import Mamifero
from planta import Planta
from animal import Animal
from celula import Celula
from organismo import Organismo

    # organismo sera la clase padre, teniendo como hijas a Animal, Planta y Microorganismos
    # Posteriormente será | ave mamifero reptil | flor arbol | celula |

def main():

    lista_animales = []

# ---------------------------------ave-----------------------------------------------------------------------------
    perico = Ave("pepito",5)
    perico.set_nPatas(2)

    lista_animales.append(perico.get_nombre()) 
    lista_animales.append(perico.get_edad())
    lista_animales.append(perico.get_nPatas())

    # print(perico.__repr__())
    print(f"{perico.get_nombre()}, {perico.get_edad()}, {perico.get_nPatas()}")
    # perico.volar()
# --------------------------------------------------------------------------------------------------------------

# ---------------------------------mamifero---------------------------------------------------------------------
    tigre = Mamifero("Toño",7)
    tigre.set_nPatas(4)

    print(f"{tigre.get_nombre()}, {tigre.get_edad()}, {tigre.get_nPatas()}")

# --------------------------------------------------------------------------------------------------------------

# --------------------------------------------celula------------------------------------------------------------------

    bacteritus = Celula("bacteriae", 0)
    bacteritus.set_tipoMicro("bacteria")
    bacteritus.set_tipoCel("caca")

    print(f"{bacteritus.get_nombre()}, {bacteritus.get_tipoMicro()}, {bacteritus.get_tipoCel()}")

# -------------------------------------------------------------------------------------------------------------------------
# ------------------------------------plantae------------------------------------------------------------------------------

    

# -------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    pass
