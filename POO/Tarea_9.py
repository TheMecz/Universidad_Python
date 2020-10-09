class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.color = ruedas
    def __str__(self):
        return "El color es: " + self.color + "\nRuedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad
    

    def __str__(self):
        return super().__str__() + "\nLa velocidad es: " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo

    def __str__(self):
        return super().str__() + "\nEl tipo es: " + self.tipo

