class Miclase:
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Método estático:")
        print(Miclase.variable_clase)
        #print(Miclase.variable_instancia) #Desde un método estátio no podemos acceder a una variable de instancia
        
    @classmethod
    def meotodo_clase(cls):
        print("Método de clase:" + str(cls))
        print(cls.variable_clase)
        #print(clc.variable_instancia) #No podemos acceder a una variable de instancia desde contexto estático
        
    def metodo_instanacia(self):
        self.meotodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)
        
Miclase.metodo_estatico()
Miclase.meotodo_clase()

print()
obejeto1 = Miclase()
obejeto1.metodo_instanacia()