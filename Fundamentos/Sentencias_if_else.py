condicion = True
if condicion:
    print("La condición es verdadera.")
else:
    print("La condición es falsa.")

condicion = False
if condicion:
    print("La condición es verdadera.")
else:
    print("La condición es falsa.")

condicion = 10
if condicion == True:
    print("La condición es verdadera.")
elif condicion == False:
    print("La condición es falsa.")
else:
    print("Condición no reconocida.")

numero = int(input("Porporciona un número entre 1 y 3: "))
if numero == 1:
    numeroTexto = "Número uno."
elif numero == 2:
    numeroTexto = "Número dos."
elif numero == 3:
    numeroTexto = "Número tres."
else:
    numeroTexto = "Valor fuera de rango."
print("Número proporconado: ", numeroTexto)

