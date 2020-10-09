import psycopg2

conexion = psycopg2.connect(user='postgres', password='@1b2c3d4e5', host='127.0.0.1', port='5432', database='test_db')

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
valores = ('Carlos', 'Lara', 'clara@gmail.com')
cursor.execute(sentencia, valores)
cursor.close()

#Guardar la información en la base de datos
conexion.commit()
cursor.close()
conexion.close()