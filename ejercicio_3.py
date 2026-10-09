
from enum import Enum


class TipoCombustible(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"


class TipoAutomovil(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"


class Color(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"


class Automovil:
    def __init__(self, marca, modelo, motor, tipoCombustible,
                 tipoAutomovil, numeroPuertas, cantidadAsientos,
                 velocidadMaxima, color, automatico):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMaxima = velocidadMaxima
        self.color = color
        self.velocidadActual = 0
        self.automatico = automatico
        self.multas = 0
        self.valorMultas = 0

    # Métodos get: consultar atributos
    def getMarca(self): return self.marca
    def getModelo(self): return self.modelo
    def getMotor(self): return self.motor
    def getTipoCombustible(self): return self.tipoCombustible
    def getTipoAutomovil(self): return self.tipoAutomovil
    def getNumeroPuertas(self): return self.numeroPuertas
    def getCantidadAsientos(self): return self.cantidadAsientos
    def getVelocidadMaxima(self): return self.velocidadMaxima
    def getColor(self): return self.color
    def getVelocidadActual(self): return self.velocidadActual
    def getAutomatico(self): return self.automatico
    def getMultas(self): return self.multas
    def getValorMultas(self): return self.valorMultas

    # Métodos set: cambiar atributos
    def setMarca(self, valor): self.marca = valor
    def setModelo(self, valor): self.modelo = valor
    def setMotor(self, valor): self.motor = valor
    def setTipoCombustible(self, valor): self.tipoCombustible = valor
    def setTipoAutomovil(self, valor): self.tipoAutomovil = valor
    def setNumeroPuertas(self, valor): self.numeroPuertas = valor
    def setCantidadAsientos(self, valor): self.cantidadAsientos = valor

    def setVelocidadMaxima(self, valor):
        if valor <= 0:
            raise ValueError("Velocidad máxima debe ser positiva")
        if valor < self.velocidadActual:
            raise ValueError("Máxima inferior a la velocidad actual")
        self.velocidadMaxima = valor

    def setColor(self, valor): self.color = valor

    def setVelocidadActual(self, valor):
        if not 0 <= valor <= self.velocidadMaxima:
            raise ValueError("Velocidad fuera del rango permitido")
        self.velocidadActual = valor

    def setAutomatico(self, valor): self.automatico = valor

    def setMultas(self, valor):
        if valor < 0:
            raise ValueError("Multas no pueden ser negativas")
        self.multas = valor

    def setValorMultas(self, valor):
        if valor < 0:
            raise ValueError("Valor no puede ser negativo")
        self.valorMultas = valor

    # Método para acelerar y generar multas
    def acelerar(self, incrementoVelocidad, valorMulta=100000):
        if incrementoVelocidad < 0:
            raise ValueError("El incremento no puede ser negativo")

        velocidadDeseada = self.velocidadActual + incrementoVelocidad

        if velocidadDeseada > self.velocidadMaxima:
            self.multas += 1
            self.valorMultas += valorMulta
            print("Multa: intento de superar la velocidad máxima")
        else:
            self.velocidadActual = velocidadDeseada

    # Método para desacelerar
    def desacelerar(self, decrementoVelocidad):
        if decrementoVelocidad < 0:
            raise ValueError("El decremento no puede ser negativo")

        if self.velocidadActual - decrementoVelocidad >= 0:
            self.velocidadActual -= decrementoVelocidad
        else:
            print("No se puede decrementar a velocidad negativa")

    # Método para frenar
    def frenar(self):
        self.velocidadActual = 0

    # Método para calcular el tiempo de llegada
    def calcularTiempoLlegada(self, distancia):
        if distancia < 0:
            raise ValueError("La distancia no puede ser negativa")
        if self.velocidadActual == 0:
            raise ValueError("No se calcula tiempo con velocidad cero")

        return distancia / self.velocidadActual

    # Método para determinar si tiene multas
    def tieneMultas(self):
        return self.multas > 0

    # Método para imprimir los atributos
    def imprimir(self):
        print("Marca =", self.marca)
        print("Modelo =", self.modelo)
        print("Motor =", self.motor)
        print("Combustible =", self.tipoCombustible.value)
        print("Tipo de automóvil =", self.tipoAutomovil.value)
        print("Número de puertas =", self.numeroPuertas)
        print("Cantidad de asientos =", self.cantidadAsientos)
        print("Velocidad máxima =", self.velocidadMaxima)
        print("Color =", self.color.value)
        print("Velocidad actual =", self.velocidadActual)
        print("Automático =", self.automatico)
        print("Número de multas =", self.multas)
        print("Valor total de multas =", self.valorMultas)


# Método principal
def main():
    auto1 = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL,
                      TipoAutomovil.EJECUTIVO, 5, 6, 250,
                      Color.NEGRO, True)

    auto1.imprimir()

    auto1.setVelocidadActual(100)
    print("Velocidad actual =", auto1.getVelocidadActual())

    auto1.acelerar(20)
    print("Velocidad actual =", auto1.getVelocidadActual())

    auto1.desacelerar(50)
    print("Velocidad actual =", auto1.getVelocidadActual())

    auto1.frenar()
    print("Velocidad actual =", auto1.getVelocidadActual())

    auto1.desacelerar(20)

    auto1.acelerar(260)
    print("¿Tiene multas? =", auto1.tieneMultas())
    print("Valor total multas =", auto1.getValorMultas())


if __name__ == "__main__":
    main()
