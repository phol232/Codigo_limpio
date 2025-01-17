class X_mej:
    def z(self, x, y):
        if y == 0:
            return "Error: División por cero no permitida"
        return x * y

if __name__ == '__main__':
    x = X_mej()
    print(x.z(3, 4))
    print(x.z(3, 0))


