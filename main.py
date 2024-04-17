# Nombres: Alexis Hernandez, Astrid Leon

from subanimal import Ave
from subanimal import Mamifero
from subanimal import Reptil
from subplanta import Flor
from subplanta import Arbol
from planta import Planta
from animal import Animal
from celula import Celula
from organismo import Organismo

    # organismo sera la clase padre, teniendo como hijas a Animal, Planta y Microorganismos
    # Posteriormente será | ave mamifero reptil | flor arbol | celula |

def main():


# ---------------------------------ave-----------------------------------------------------------------------------
    perico = Ave("pepito",5)
    perico.set_nPatas(2)


    # print(perico.__repr__())
    print(f"{perico.get_nombre()}, {perico.get_edad()}, {perico.get_nPatas()}, {perico.get_vivomuerto()}")
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
    rosa = Flor("Rosa",)
    

# -------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
    pass
