#Tupla mantiene el orden, pero ya no se puede modificar sus elementos (inmutable)
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#Largo de una tupla
print(len(frutas))

#Acceder a un elemento
print(frutas[1])

#Navegación inversa
print(frutas[-1])

#Rango
print(frutas[0:2]) #excluyendo el indice 2

#Modificar un valor
#frutas[0] = "Naranjita"
frutasLista = list(frutas)
frutasLista[0] = "Naranjita"
frutas = tuple(frutasLista)
print(frutas)

#Iterar una tupla
for fruta in frutas:
    print(fruta, end=" ")

#No podemos agregar ni eliminar elementos de una tupla
#Podemos eliminar una tupla
del frutas
#print(frutas)