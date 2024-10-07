class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Has retirado {cantidad}. Saldo actual: {self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser mayor a 0.")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.saldo}")
cuenta1 = CuentaBancaria("Carlos", 1000)
cuenta1.consultar_saldo()      
cuenta1.depositar(500)        
cuenta1.retirar(200)           
cuenta1.retirar(2000)          
cuenta1.consultar_saldo()      