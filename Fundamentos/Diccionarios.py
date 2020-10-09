#Un diccionario está compuesto de llave, valor (key, value)
diccionario = {
    "IDE" : "Integrated Development Environment",
    "OOP" : "Object Oriented Programming",
    "DBMS" : "Database Management System"
}
print(diccionario)

#Largo
print(len(diccionario))

#Accediendo a un elemento
print(diccionario["IDE"])

#Otra forma, mismo resultado
print(diccionario.get("IDE"))

#Modificando Valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario)

#Iterar las llaves
for termino in diccionario:
    print(termino)
    
#Iterar los valalores
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
    
#Comprobando existencia de un elemento 
print("IDE" in diccionario)

#Agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#Remover elementos
diccionario.pop("DBMS")
print(diccionario)

#Limpiar
diccionario.clear()
print(diccionario)

#Eliminar el diccionario por completo
del diccionario
#print(diccionario)
