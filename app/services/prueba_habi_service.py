import json
#se llama al archivo database y se traen las funciones para crear la conexion y cerrar la conexion de la base de datos 
from app.services.database import CerrarConexion,ConectarBd
from datetime import datetime

# se crea funcion principal para consultar las propiedades (la funcion recibe tres parametros los cuales se validan mas adelante)
def ConsultarPropiedades(status, building_year,city):
    today=datetime.now()
    connection = ConectarBd()
    if connection is None:
        #mensaje que enviamos al front si no se puede conectar a la base de datos 
        mensaje=f"Can´t connect to data base , please contact your system administrator code:500"
        return 500,mensaje
    cursor = connection.cursor()
    validate_state =''
    validate_building_year=''
    validate_city=''
    #la funcion ValidarNumero tiene como objetivo  validar si el dato que envia el front es un numero  entero valido 
    if status:
        status=ValidarNumero(status)
        #nota aqui estoy esperando que el frontend envie el id del estado .
        # se hace entender que ya existe un microservicio que lista los estados
        #si gustan puedo hacer el servicio que reciba un string 
        validate_state=f"and sh.id={status}"
    if building_year:

        building_year=ValidarNumero(building_year)
        if building_year>today.year:
            mensaje="el año no puede ser mayor a la fecha actual"
            return 422,mensaje
        validate_building_year=f"and p.year={building_year}"
    
    if city:
        print(city)
        # se llama la funcion validar string para prevenir inyeccion sql en los string 
        codigo,dato=ValidarString(city)
        if codigo==1:
            city=city.lower().strip
            validate_city=f"and p.city='{city}'"
        else:
            return codigo,dato
    # query principal
    query = f"""SELECT 
        MAX(p.id) AS property_id,
        p.description,
        p.address,
        p.city,
        p.price,
        st.name
    FROM 
        property p
    INNER JOIN 
        status_history sh ON p.id = sh.property_id
    INNER JOIN 
        status st ON sh.status_id = st.id
    WHERE 
        st.id NOT IN (1, 2)
        {validate_building_year}
        {validate_city}
        {validate_state}
        AND sh.update_date = (
            SELECT MAX(sh2.update_date)
            FROM status_history sh2
            WHERE sh2.property_id = p.id
        )
    GROUP BY 
        p.id, p.description, p.address, p.city, p.price, st.name
    ORDER BY 
        sh.update_date DESC;"""
    
    cursor.execute(query)
    #traigo todos los dato de la consulta
    resultados = cursor.fetchall()
    cursor.close()
    CerrarConexion(connection)
    if not resultados:
        mensaje= "no encuentro informacion con esos criterios de busqueda"
        return 422,mensaje

    data = []
    # se construye una lista de diccionarios  que se  va a devolver 
    for row in resultados:
        data.append({
            "property_id": row[0],
            "description": row[1],
            "address": row[2],
            "city": row[3],
            "price": row[4],
            "status_name": row[5]
        })
    
    return 200,data


def ValidarNumero(numero):
    try:
        numero=int(numero)
        if isinstance(numero, int):
            return numero
    except ValueError:
        mensaje="por favor ingrese un id valido "
        return 422,mensaje
    
def ValidarString(string_p):
    string_p = string_p.upper()
    palabras_prohibidas = {"SELECT", "UPDATE", "DELETE", "DROP", "USE"}
    
    for palabra in palabras_prohibidas:
        if palabra in string_p:
            return 422, f"La palabra {palabra} no debe usarse en la solicitud"

    return 1,"success"