#Solo se quiere mostrar las instancias de una clase sencilla, sin funcionalidad en especifico 

class Pajaro():
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie 

mi_pajaro = Pajaro('negro', 'Tucan')  #Instancia de la clase pajaro
print(mi_pajaro.color, mi_pajaro.especie) 
