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

def outputzombieoinfectado(coso):
    if coso:
        return "Positivo"
    else:
        return "Negativo"

def muertoporenfermo():
    morirenfermo = random.randint(0,100)
    if morirenfermo <= 25 :
        return False
    else:
        return True

def zombie(mundo):
    for i in mundo:
        print("---cambio de comunidad---")

        for j in i:
            j.set_infectado(True)
            zombie = random.randint(0,100)
            if isinstance(j,Celula) and isinstance(j,Microorganismo):
                pass
            else:
                if zombie <= 45:
                    j.set_zombie(True)
                    print(f"{j} se ha convertido en zombie . . .")
                    if not muertoporenfermo():
                        j.set_morir()
                else:
                    j.set_zombie(False) 
                    print(f"{j} no se ha convertido en zombie")

        
# en la función de mutación se realiza una comparación
# con un valor aleatorio, dividiendo en un 60% las probabilidades
# de mutación o no de la célula. 
# seguido de eso, si la mutación existe, se va a hacer una condicional
# si existen suficientes materiales para el antidoto
# en caso de que no, se evalúa la probabilidad de convertirse en zombie

def mutacion(mundo): 
    # lista booleana se refiere a que si la comunidad de la posicion contador esta infectada o no
    lista_booleana = buscar_antidoto(mundo)
    contador = 0
    
    for i in mundo:
        antidoto_bool = lista_booleana[contador]
        for f in i:
            if isinstance(f,Celula) and isinstance(f,Microorganismo):
                mutado = random.randint(1,10)
                match mutado:
                    case 1 | 2 | 3 | 4 | 5 | 6: 
                        f.mutacionactiva()
                        if antidoto_bool:
                            print("TIENEN LA CURA, SE SALVÓ LA COMUNIDAD")
                        else:
                            print("NO SE PRODUJO UN ANTÍDOTO")
                            zombie(mundo)
                        # if buscar_antidoto(mundo):
                        #     pass
                        # else:
                        #     zombie(mundo)
                    case 7 | 8 | 9 | 10 | _: print(f"{f} no ha mutado")
                
                    
                    
        contador += 1
                


def buscar_antidoto(mundo):
    frutos_totales = 0
    flores_totales = 0
    frutos_necesarios = False
    flores_necesarias = False
    lista = []
    for i in mundo:

        for f in i:
            if isinstance(f,Arbol):
                frutos = f.get_frutos()
                print(f"LA CANTIDAD DE FRUTOS DEL ARBOL ES: {frutos}\n\n")

                #si encuentra los frutos necesarios para lograr el antidoto se eliminan de el objeto.
                if frutos >= 5:
                    print("tiene los frutos suficientes el arbol para crear el antidoto")
    
                    f.set_frutos(frutos-5)
                    print(f"La cantidad de frutos que le queda a ese arbol es de: {f.get_frutos()}\n")

                    frutos_necesarios = True
                else:
                    print("no tiene los frutos suficientes el arbol para crear el antidoto, debe crecer.")

            if isinstance(f,Flor):
                cantidad_flor = f.get_flores()
                print(f"LA CANTIDAD DE FLORES ES DE: {cantidad_flor}\n\n")

                if cantidad_flor >= 1:
                    print("esta la cantidad suficiente de flores")

                    f.set_flores(cantidad_flor-1)
                    print(f"La cantidad de flores que le quedan es de: {f.get_flores()}\n")
                    
                    flores_necesarias = True
            pass

            if frutos_necesarios and flores_necesarias: 
                break
            else:
                print("NO SE LOGRO FABRICAR ANTIDOTO")
        if frutos_necesarios and flores_necesarias:
            lista.append(True)
        else:
            lista.append(False)
    print(f"la lista es: {lista}")
    return lista


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
                especie.set_frutos(random.randint(5,9))
        
            case 6 : 
                especie = Celula("tardigrade",1)
                especie.set_tipoCel("microorganismo")
                
            case _ : pass
            
        comunidad.append(especie)
    return comunidad

# append de la mitosis ya que el objeto es diferente
# aumenta tamaño de la comunidad
def celulareproduccion(mundo):
    nuevo_mundo = mundo
    mitosis = random.randint(0,1)
    for i in nuevo_mundo:
        for j in i:
            if isinstance(j,Celula) and isinstance(j,Microorganismo):
                    if mitosis == 1:
                        gemelo = j
                        i.append(gemelo)

    return nuevo_mundo
            
def crear_mundo():
    mundo = []
    for i in range(0,random.randint(3,4)):
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

        # print(f"Día {dia} en Biótica")
        mutacion(mundo)
        
        # # Cada tres dias se reproducen
        # if dia % 3 == 0:
        #      mundo = celulareproduccion(mundo)
        
        # cada cinco dias crecen los frutos y las flores
        # if dia % 5 == 0:

        dia += 1

        for i in mundo:
            print("---cambio de comunidad---")
            for j in i:
                if isinstance(j,Animal):
                    print(f"- {j.get_nombre()}, Edad: {j.get_edad()}, Estado: {j.get_vivomuerto()}, Zombie: {outputzombieoinfectado(j.get_zombie())}, Infección: {outputzombieoinfectado(j.get_infectado())}")
                elif isinstance(j,Flor) and isinstance(j,Planta):
                    print(f"- {j.get_tipo()}, {j.get_flores()}, Zombie: {outputzombieoinfectado(j.get_zombie())}, Infección: {outputzombieoinfectado(j.get_infectado())}")
                elif isinstance(j,Arbol) and isinstance(j,Planta):
                    print(f"- {j.get_tipo()}, {j.get_frutos()}, Zombie: {outputzombieoinfectado(j.get_zombie())}, Infección: {outputzombieoinfectado(j.get_infectado())}")
                elif isinstance(j,Celula) and isinstance(j,Microorganismo):
                    print(f"- {j.get_nombre()}, Mutacion: {outputzombieoinfectado(j.get_mutacion())}")

        time.sleep(2)
    pass



if __name__ == "__main__":
    main()
    pass