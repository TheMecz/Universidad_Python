class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
    def volumen(self):
        return self.alto * self.ancho * self.largo
    
alto = float(input("Digite la altura: "))
ancho = float(input("Digite el ancho: "))
largo = float(input("Digite el largo: "))
caja1 = Caja(alto, ancho, largo)
print("El volumne de la caja es:", caja1.volumen())

