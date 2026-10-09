
import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2

    def calcularPerimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

    def calcularPerimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularHipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcularPerimetro(self):
        return self.base + self.altura + self.calcularHipotenusa()

    def determinarTipoTriangulo(self):
        if self.base == self.altura:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")


class Rombo:
    def __init__(self, diagonalMayor, diagonalMenor, lado):
        self.diagonalMayor = diagonalMayor
        self.diagonalMenor = diagonalMenor
        self.lado = lado

    def calcularArea(self):
        return (self.diagonalMayor * self.diagonalMenor) / 2

    def calcularPerimetro(self):
        return 4 * self.lado


class Trapecio:
    def __init__(self, baseMayor, baseMenor, altura, lado1, lado2):
        self.baseMayor = baseMayor
        self.baseMenor = baseMenor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcularArea(self):
        return (self.baseMayor + self.baseMenor) * self.altura / 2

    def calcularPerimetro(self):
        return self.baseMayor + self.baseMenor + self.lado1 + self.lado2


class PruebaFiguras:
    @staticmethod
    def main():
        figura1 = Circulo(2)
        figura2 = Rectangulo(1, 2)
        figura3 = Cuadrado(3)
        figura4 = TrianguloRectangulo(3, 5)
        figura5 = Rombo(8, 6, 5)
        figura6 = Trapecio(10, 6, 3, 4, 4)

        figuras = [
            ("círculo", figura1),
            ("rectángulo", figura2),
            ("cuadrado", figura3),
            ("triángulo", figura4),
            ("rombo", figura5),
            ("trapecio", figura6)
        ]

        for nombre, figura in figuras:
            print("El área del", nombre, "es =", figura.calcularArea())
            print("El perímetro del", nombre, "es =", figura.calcularPerimetro())
            print()

        figura4.determinarTipoTriangulo()


PruebaFiguras.main()

