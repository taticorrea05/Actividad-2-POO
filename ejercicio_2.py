
from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(self, nombre, cantidadSatelites, masa, volumen,
                 diametro, distanciaSol, tipo, esObservable,
                 periodoOrbital, periodoRotacion):
        self.nombre = nombre
        self.cantidadSatelites = cantidadSatelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distanciaSol = distanciaSol
        self.tipo = tipo
        self.esObservable = esObservable
        self.periodoOrbital = periodoOrbital  # años terrestres
        self.periodoRotacion = periodoRotacion  # días terrestres

    def imprimir(self):
        print("Nombre =", self.nombre)
        print("Satélites =", self.cantidadSatelites)
        print("Masa (kg) =", self.masa)
        print("Volumen (km³) =", self.volumen)
        print("Diámetro (km) =", self.diametro)
        print("Distancia al Sol (km) =", self.distanciaSol)
        print("Tipo =", self.tipo.value)
        print("Observable =", self.esObservable)
        print("Período orbital (años) =", self.periodoOrbital)
        print("Período de rotación (días) =", self.periodoRotacion)

    def calcularDensidad(self):
        if self.volumen <= 0:
            raise ValueError("El volumen debe ser positivo")
        return self.masa / self.volumen  # kg/km³

    def esPlanetaExterior(self):
        return self.distanciaSol > 149597870 * 3.4


def main():
    tierra = Planeta("Tierra", 1, 5.9736e24, 1.08321e12,
                     12742, 150000000, TipoPlaneta.TERRESTRE,
                     True, 1, 1)

    jupiter = Planeta("Júpiter", 79, 1.899e27, 1.4313e15,
                      139820, 750000000, TipoPlaneta.GASEOSO,
                      True, 11.86, 0.41)

    for planeta in (tierra, jupiter):
        planeta.imprimir()
        print("Densidad (kg/km³) =", planeta.calcularDensidad())
        print("¿Es exterior? =", planeta.esPlanetaExterior())
        print()


if __name__ == "__main__":
    main()
