import Proyecto_Banco as bk

def inicio():
    bk.crear_cliente()

    while True:
      escogencia  = input("Ingrese 1 para depositar'\n Ingrese 2 para retirar'\n Ingrese 3 para salir del programa ") 
      if escogencia == "1":
        deposito = float(input("Ingrese el monto que quiere depositar a su cuenta: "))
        bk.nombre.depositar(deposito)
    
      elif escogencia == "2":
        retiro = float(input("Ingrese el monto que quiere retirar de su cuenta: "))
        if bk.nombre.balance < retiro:
          print("El monto del retiro que desea realizar es mayor al balance actual de su cuenta")
          print(f"El balance actual de su cuenta es: {bk.nombre.balance}")
        else:
          bk.nombre.retirar(retiro)
          print(f"El balance de su cuenta después de retirar es: {bk.nombre.balance}")
    
      elif escogencia == "3":
        break   


if __name__ == "__main__":
  inicio()       
          
    
      


