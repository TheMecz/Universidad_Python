a = -1
valorMinimo = 0
valorMaximo = 5 

dentroRango = a >= valorMinimo and a <= valorMaximo
print(dentroRango)

if dentroRango:
    print("Dentro de rango.")
else:
    print("Fuerade rango")

vacaciones = False
diaDeDescanso = False
if not(vacaciones or diaDeDescanso):
    print("Puedes ir al parque.")
else:
    print("Tienes deberes que hacer")

print(not(vacaciones))