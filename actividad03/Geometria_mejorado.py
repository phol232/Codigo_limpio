class GeometriaSimp:

    def area(self, *lados):
        if len(lados) == 1:
            return lados[0] ** 2
        elif len(lados) == 2:
            return lados[0] * lados[1]
        else:
            raise ValueError("Se requieren 1 o 2 argumentos para calcular el área.")

    def perimetro(self, *lados):
        if len(lados) == 1:
            return 4 * lados[0]
        elif len(lados) == 2:
            return 2 * (lados[0] + lados[1])
        else:
            raise ValueError("Se requieren 1 o 2 argumentos para calcular el perímetro.")

if __name__ == "__main__":
    geometria = GeometriaSimp()

    print("Área de un cuadrado de lado 4 es:", geometria.area(4))
    print("Área de un rectángulo de lados 4 y 5 es:", geometria.area(4, 5))
    print("Perímetro de un cuadrado de lado 4 es :", geometria.perimetro(4))
    print("Perímetro de un rectángulo de lados 4 y 5 es", geometria.perimetro(4, 5))