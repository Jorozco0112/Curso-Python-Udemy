class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        self.balance -= monto
    
    def __str__(self):
        print(f'Cliente: {self.nombre} {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nSaldo: {self.balance}')   
    


def crear_cliente():
    print("Ingresa los datos del cliente: nombre, apellido, numero_cuenta, balance")
    global nombre
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = int(input("Numero de cuenta: "))
    balance = float(input("Saldo: "))
    nombre = Cliente(nombre, apellido, numero_cuenta, balance)
    return nombre


