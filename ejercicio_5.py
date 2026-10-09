
class CuentaBancaria:

    def __init__(self, nombresTitular, apellidosTitular,
                 numeroCuenta, tipoCuenta, porcentajeInteres):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.saldo = 0
        self.porcentajeInteres = porcentajeInteres

    def imprimir(self):
        print("Nombres del titular =", self.nombresTitular)
        print("Apellidos del titular =", self.apellidosTitular)
        print("Número de cuenta =", self.numeroCuenta)
        print("Tipo de cuenta =", self.tipoCuenta)
        print("Saldo =", self.saldo)
        print("Porcentaje de interés =", self.porcentajeInteres, "%")

    def consultarSaldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Se ha consignado $", valor,
                  "en la cuenta. El nuevo saldo es $", self.saldo)
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print("Se ha retirado $", valor,
                  "de la cuenta. El nuevo saldo es $", self.saldo)
            return True
        else:
            print("El valor a retirar debe ser positivo y no superar el saldo.")
            return False

    def aplicarInteres(self):
        interes = self.saldo * self.porcentajeInteres / 100
        self.saldo = self.saldo + interes

        print("Interés mensual aplicado = $", interes)
        print("Nuevo saldo con intereses = $", self.saldo)


def main():
    cuenta = CuentaBancaria("Pedro", "Pérez",
                            123456789, "AHORROS", 2)

    cuenta.imprimir()
    print()

    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)
    print()

    cuenta.consultarSaldo()
    print()

    cuenta.aplicarInteres()


main()
