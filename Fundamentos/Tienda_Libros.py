print("Proporcione los siguientes datos del libro: ")
nombre = input("Porporciona el nombre: ")
id = int(input("Porporciona el ID: "))
precio = float(input("Porporcione el precio: "))
envioGratuito = input("Indica si el envio es gratuito (True/False): ")

if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"

print("Nombre:", nombre)
print("ID:", id)
print("Precio:", precio)
print("Envio Gratuito:", envioGratuito)
print(type(envioGratuito))
