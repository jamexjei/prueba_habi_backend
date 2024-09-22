# se usa la dependencia mysqk connector para la conexion a la base de datos 
import mysql.connector
from mysql.connector import Error
#se crea funcion para conectar a la base de datos 
def ConectarBd():
    try:
        connection = mysql.connector.connect(
            #parametros de conexion 
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
    #cerrar conexion a la base de datos 
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada")