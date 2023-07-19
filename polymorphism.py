class Vaca():

    def __init__(self, name):
        self.name = name
    
    def hablar(self):
        print(self.name + " dice muuuu")

class Oveja():
    
    def __init__(self, name):
        self.name = name
    
    def hablar(self):
        print(self.name + " dice beeeeee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

def animal_hablar(animal):
    return animal.hablar()

animal_hablar(vaca1)
