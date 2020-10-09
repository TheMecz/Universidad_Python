import psycopg2

conexion = psycopg2.connect(user='postgres', password='@1b2c3d4e5', host='127.0.0.1', port='5432', database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input("Proporciona las pk a buscar (separado por comas): ")
tupla = tuple(entrada.split(','))
llavez_primarias = (tupla,)
#id_persona = input("Porporciona la pk a buscar:")

cursor.execute(sentencia, llavez_primarias)
registros = cursor.fetchall() #Solo regresa un resgistro

for registro in registros:
    print(registro)

cursor.close()
conexion.close()

