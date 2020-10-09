class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    
altura = float(input("Digite el valor de la altura:"))
base = float(input("Digite el valor de base:"))
rectangulo = Rectangulo(altura, base)
print(rectangulo.area())
print(id(rectangulo))