

class Organismo():
    
    def __init__(self,nombre,edad = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__vivo = True
        self.__zombie = False
        self.__infectado = False


    def __repr__(self):
            return f"{self.get_nombre()}"

#metodos get y set de los atributos

    def get_edad(self):
        return self.__edad
    
    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if isinstance(edad, int):
            if self.__edad == 0:

                self.__edad = self.nacer()

            else:
                self.__edad = edad
                
        else:
            # RAISE EXPECT INT
            pass
            
    def set_nombre(self,nombre):
        if isinstance(nombre,str):
            self.__nombre = nombre
        else:
            pass
    
    def set_infectado(self,sino):
        if isinstance(sino,bool):
            self.__infectado = sino
    
    def get_infectado(self):
        return self.__infectado
    
    def get_vivomuerto(self):

        if self.__vivo:
            return True
        else:
            return False
        
    def set_vivomuerto(self, estado):
        if isinstance(estado,bool):
            self.__vivo = estado

    def set_zombie(self,zombie):
        if isinstance(zombie,bool):
            self.__zombie = zombie

    def get_zombie(self):
        return self.__zombie

    # metodos de interaccion y comportamiento
    # de clase

    def nacer(self):
        print(f"{self.get_nombre()} esta naciendo")
        self.__vivo = True
    
    def crecer(self):
        self.__edad = self.__edad + 1

    def set_morir(self):
        self.__vivo = False
