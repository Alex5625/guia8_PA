# Nombres: Alexis Hernandez, Astrid Leon

import random
import time
# -----------------------
from ave import Ave
from mamifero import Mamifero
from microorganismo import Microorganismo
from reptil import Reptil
from flor import Flor
from arbol import Arbol
from celula import Celula
# ------------------------
from planta import Planta
from animal import Animal
from organismo import Organismo

    # organismo sera la clase padre, teniendo como hijas a Animal, Planta y Microorganismos
    # Posteriormente será | ave mamifero reptil | flor arbol | celula |



def antidoto():
    # recorrer arreglo sobre arreglo y buscar la cantidad de frutos y flores que existan en la comunidad
    pass

def zombie():
    pass

def mutacion(mundo): # BACTERIAS 60%
    for i in mundo:
        for f in i:
            if isinstance(f,Celula) and isinstance(f,Microorganismo):
                mutado = random.randint(1,10)
                match mutado:
                    case 1 | 2 | 3 | 4 | 5 | 6: 
                        f.mutacionactiva()
                    case 7 | 8 | 9 | 10 | _: print(f"{f} no ha mutado")
                


def muertoporenfermo():
    pass



# PARA LLAMAR A LA CLASE HIJA Y ASIGNARLE AL OBJETO ES obj("nombre",edad)
def definircomunidad():
     
    comunidad = []
     
    #  random de cantidad de especies en la comunid
    for i in range(0,random.randint(6,8)):

        # buscar de manera random que especie se va a incluir
        n_especie = random.randint(1,6)
        # print(n_especie)
        match n_especie :
            case 1 : 
                especie = Ave("pajarito", 3)
                especie.set_nPatas(2)
            case 2 : 
                especie = Mamifero("mamut",30)
                especie.set_nPatas(4)
            case 3 : 
                especie = Reptil("iguana", 6)
                especie.set_nPatas(4)
            case 4 : 
                especie = Flor("rosita",3)
                especie.set_tipo("rosaceae")
                especie.set_flores(random.randint(0,3))
            
            case 5 :
                especie = Arbol("manzano",15)
                especie.set_tipo("malus")
                especie.set_frutos(random.randint(0,8))
        
            case 6 : 
                especie = Celula("covid",1)
                especie.set_tipoCel("virus")
                
            case _ : pass
            
        comunidad.append(especie)
    return comunidad
            
def crear_mundo():
    mundo = []
    for i in range(0,random.randint(3,5)):
        comunidad = definircomunidad()
        mundo.append(comunidad)

    return mundo
            


def main():
    mundo = crear_mundo()
    print(mundo)
    dia = 1
    while True:
# sintaxis para saber q hacer en la cantidad de día es con el MOD (%) dia % multiplo de dia == 0 
        """ if dia % 5 (q ocurra algo cada 5 dias) == 0:
        realizar acciones"""

        print(f"Día {dia} en Biótica")
        dia += 1
        time.sleep(1)
        mutacion(mundo)
    pass



if __name__ == "__main__":
    main()
    pass
