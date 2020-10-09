from Figura_Geometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color): #La preferencia va de izquierda a derecha
    def __init__(self, largo, ancho, color):

        FiguraGeometrica.__init__(self, largo, ancho)
        Color.__init__(self, color)
    

    def area(self):
        return self.alto * self.ancho
    

    
    