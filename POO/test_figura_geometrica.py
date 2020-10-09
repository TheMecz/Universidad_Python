from Cuadrado import Cuadrado
from Clase_Rectangulo import Rectangulo
from Figura_Geometrica import FiguraGeometrica

#No es posible crear objetos de una clase abstracta
#figuraGeometrica = FiguraGeometrica()

cuadrado = Cuadrado(4, "Rojo")
print(cuadrado.area())
print(cuadrado.color)


#Metod Resolution Order
print(Cuadrado.mro())

rectangulo = Rectangulo(4, 5, "Azul")
print(rectangulo.area())
print(rectangulo.color)
print(Rectangulo.mro())