

class Procesador:
    def proc(self, a, b, c):
        result = a * b + c
        return result

    def exe(self, d):
        return d ** 2

if __name__ == '__main__':
    procesador = Procesador()


    result_proc = procesador.proc(2, 3, 4)
    print(f"Resultado del proc(2, 3, 4): {result_proc}")


    result_exe = procesador.exe(3)
    print(f"Resultado del exe(3): {result_exe}")