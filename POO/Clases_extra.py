class Persona:
    def __init__(this, n, e, *v, **d):
        this.nombre = n
        this.edad = e
        this.valores = v
        this.diccionario = d
    def desplegar(this):
        print("Nombre: ", this.nombre)
        print("Edad: ", this.edad)
        print("Valores (Tupla):", this.valores)
        print("Diccionario: ", this.diccionario)
persona1 = Persona("Juan", 28)
persona1.desplegar()

persona2 = Persona("José", 30, 2,3,4,5)
persona2.desplegar()

persona3 = Persona("María", 20, 2,4,5 , m="Manazana", p="Pera", j="Jicama")
persona3.desplegar()