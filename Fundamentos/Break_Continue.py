#Imprimir solo las letras a
for letra in "Holanda":
    if letra == 'a':
        print(letra)
else: 
    print("Fin ciclo for.")

#Break rompe todo el ciclo
for letra in "Holanda":
    if letra == 'a':
        print(letra)
        break
else: 
    print("Fin ciclo for.")

#Imprimir sólo números pares
for i in range(6):
    if i%2 == 0:
        print(i)

#Usando el continue
for i in range(6):
    if i%2 != 0:
        continue
    print(i)