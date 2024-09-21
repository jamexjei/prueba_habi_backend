import mysql.connector
from mysql.connector import Error
def ConectarBd():
    try:
        connection = mysql.connector.connect(
            host='18.221.137.98',
            port='3309',         
            database='habi_db',
            user='pruebas',
            password='VGbt3Day5R'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos habi")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def CerrarConexion(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")