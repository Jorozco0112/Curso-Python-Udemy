class Pajaro():
    alas = True
    
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie 
    def piar(self):
        if self.alas == True:
            print('Pajaro piando')
        else:
            print('Pajaro no piando')   
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()
    
    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es de color {self.color}")
    
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"El pajaro puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro esta mirando...")


piolin = Pajaro('amarillo', 'canario')

piolin.volar(50)
