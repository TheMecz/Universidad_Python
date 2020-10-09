#Set es una colección sin orden y sin índices, no permite elementos repetidos
#y los elmentos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Júpiter", "Venus"}
print(planetas)

#Largo
print(len(planetas))

#Revisar si un elemento está presente
print("Marte" in planetas)

#Agregar
planetas.add("Tierra")
print(planetas)

planetas.add("Tierra")#No se pueden agregar elementos duplicados
print(planetas)

#Eliminar con remove posiblemnte arroja excepción
planetas.remove("Tierra")
print(planetas)

#Eliminicar con discard no arroja excepción
planetas.discard("Jupiter")

#Limpiar el set
planetas.clear()
print(planetas)

#Eliminar el set
del planetas
#print(planetas)

