class Animal():
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print("Este animal acaba de nacer")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print("pio")
    
    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


pajaro = Pajaro(2, "rojo", 60)     
mi_animal = Animal()

