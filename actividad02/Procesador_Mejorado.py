
class ProcesadorMej:

    def productoSuma(self, primervalor, segundovalor, tercervalor):
        return primervalor * segundovalor + tercervalor

    def cuadradodeunNumero(self, valor):
        return valor ** 2

if __name__ == '__main__':
    procesador = ProcesadorMej()

    # Call proc method and print the result
    result_productoSuma = procesador.productoSuma(2, 3, 4)
    print(f"Resultado del productoSuma(2, 3, 4): {result_productoSuma}")

    # Call exe method and print the result
    result_cuadradodeunNumero = procesador.cuadradodeunNumero(3)
    print(f"Resultado del cuadradodeunNumero(3): {result_cuadradodeunNumero}")