import psycopg2

conexion = psycopg2.connect(user='postgres', password='@1b2c3d4e5', host='127.0.0.1', port='5432', database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
#id_persona = 1
id_persona = input("Porporciona la pk a buscar:")
llave_primaria = (id_persona,)
cursor.execute(sentencia, llave_primaria)
registro = cursor.fetchone() #Solo regresa un resgistro
print(registro)

cursor.close()
conexion.close()