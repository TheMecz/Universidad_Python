class Persona:
    #Métodos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return "Nombre: " + self.nombre + "\nedad: " + str(self.edad)
    
#Herencia de la clase Persona
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #Llama al init de la clase persona
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + "\nsueldo: " + str(self.sueldo)
    
persona = Persona("Juan", 28)
print(persona)

empleado = Empleado("Karla", 30, 500.00)
print(empleado)

empleado.nombre = "Karla Ivone"
empleado.sueldo = 1000.00
print(empleado)