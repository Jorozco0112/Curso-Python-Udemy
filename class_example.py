class Personaje:
    real = False
    
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
 
harry_potter = Personaje("humano", True, 17)

print(harry_potter.edad)  