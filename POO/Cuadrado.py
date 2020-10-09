from Figura_Geometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color): #La preferencia va de izquierda a derecha
    def __init__(self, lado, color):

        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)


    def area(self):
        return self.alto * self.ancho
    

    
    