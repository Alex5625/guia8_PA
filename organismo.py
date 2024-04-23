class Organismo():
    
    def __init__(self,nombre,edad = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.vivo = None


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
    
    def get_vivomuerto(self):

        if self.vivo:
            return f"{self.get_nombre()} Está vivo"
        else:
            return f"{self.get_nombre() } esta muerto"
    # metodos de interaccion y comportamiento
    # de clase

    def nacer(self):
        print(f"{self.get_nombre()} esta naciendo")
        self.vivo = True
    
    def crecer(self):
        self.__edad = self.__edad + 1
    
    def reproducirse(self):
        pass

    def morir(self):
        self.vivo = False
