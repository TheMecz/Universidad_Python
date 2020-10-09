nombres = ['Juan', "Carla", "Ricardo", "María"]
#print(nombres)

for i in nombres:
    print(i)

#Conocer el rango de la lista
print(len(nombres))

#elemento 0 de la lista
print(nombres[0])
#Si salimos del rango de la lista marcará un error
#print(nombres[5])

#Navegación inversa
print(nombres[-1])
print(nombres[-2])

#Imprimir rango
print(nombres[0:2]) #sin incluir el indice 2

#Imprimir los elemntos de inicio hasta el infice proporcionado
print(nombres[:3])#sin incluir el indice 3

#Imprimir los elementos hasta el final hasta el indice proporcionado
print(nombres[1:])

#Cambiar los elementos de una lista
nombres[3] = "Ivone"
print(nombres)

#interar la lista

for nombre in nombres:
    print(nombre)

#Revisar si existe un elemento en la lista
if "Karla" in nombre:
    print("Karla si existe ne la lista")
else:
    print("El elemento buscado no existe en la lista")
    
#Agregar un nuevo elemento

nombres.append("Lorenzo")
print(nombres)

#insertar un nuevo elementos en el indice proporcionado
nombres.insert(1, "Octavio")
print(nombres)

#remover un elemento
nombres.remove("Octavio")
print( nombres )

#Remover el último elemento de nuestra lista
nombres.pop()
print(nombres)

#remover el indice indicado de la lista
del nombres[0]
print(nombres)

#limpiar los elementos de nuestra lista
nombres.clear()
print(nombres)

#eliminar por completo la lista
del nombres
#print(nombres) se elimino completamente la lista, entonces va a marcar error.