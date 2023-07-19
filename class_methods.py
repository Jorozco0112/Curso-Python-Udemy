
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

piolin = Pajaro('amarillo', 'canario')  #Instancia de la clase pajaro
piolin.alas = False
piolin.piar()
piolin.volar(50)
