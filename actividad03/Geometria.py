class Geometria:
    def area_cuadrado(self, lado):
        return lado * lado

    def area_rectangulo(self, ancho, alto):
        return ancho * alto

    def perimetro_cuadrado(self, lado):
        return 4 * lado

    def perimetro_rectangulo(self, ancho, alto):
        return 2 * (ancho + alto)

if __name__ == '__main__':
    geometria = Geometria()


    result_area_cuadrado = geometria.area_cuadrado(4)
    print(f"Resultado del area_cuadrado(4): {result_area_cuadrado}")


    result_area_rectangulo = geometria.area_rectangulo(3, 4)
    print(f"Resultado del area_rectangulo(3, 4): {result_area_rectangulo}")


    result_perimetro_cuadrado = geometria.perimetro_cuadrado(4)
    print(f"Resultado del perimetro_cuadrado(4): {result_perimetro_cuadrado}")


    result_perimetro_rectangulo = geometria.perimetro_rectangulo(3, 4)
    print(f"Resultado del perimetro_rectangulo(3, 4): {result_perimetro_rectangulo}")