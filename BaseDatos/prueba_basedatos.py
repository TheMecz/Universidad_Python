import psycopg2

conexion = psycopg2.connect(user='postgres', password='@1b2c3d4e5', host='127.0.0.1', port='5432', database='test_db')

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona ORDER BY id_persona'
cursor.execute(sentencia)
registro = cursor.fetchall()
print(registro)

cursor.close()
conexion.close()