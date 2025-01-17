class X:
    def z(self, x, y):
        return x * y if y != 0 else x / y

if __name__ == '__main__':
    x = X()
    print(x.z(3, 4))
    print(x.z(3,0))