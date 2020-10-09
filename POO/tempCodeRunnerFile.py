class Aritmetica:
    """Clase Aritmetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operación con los atributos de la clase"""
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
#Creando un nuevo obejeto
aritmetica = Aritmetica(2,4)
print("Resultado suma:", aritmetica.sumar())
print("Resultado suma:", aritmetica.restar())
print("Resultado suma:", aritmetica.multiplicar())
print("Resultado suma:", aritmetica.dividir())

aritmetica2 = Aritmetica(5,4)
print("Resultado suma:", aritmetica2.sumar())
print("Resultado suma:", aritmetica2.restar())
print("Resultado suma:", aritmetica2.multiplicar())
print("Resultado suma:", aritmetica2.dividir())
