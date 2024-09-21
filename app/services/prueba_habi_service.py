import json
from app.services.database import CerrarConexion,ConectarBd
from datetime import datetime

def ConsultarPropiedades(status, building_year,city):
    today=datetime.now()
    connection = ConectarBd()
    if connection is None:
        mensaje=f"Can´t connect to data base , please contact your system administrator code:500"
        return 500,mensaje
    cursor = connection.cursor()
    validate_state =''
    validate_building_year=''
    validate_city=''

    if status:
        status=ValidarNumero(status)
        #nota aqui estoy esperando que el frontend envie el id del estado .
        # se hace entender que ya existe un microservicio que lista los estados
        validate_state=f"and sh.id={status}"
    if building_year:
        building_year=ValidarNumero(building_year)
        if building_year>today.year:
            mensaje="el año no puede ser mayor a la fecha actual"
            return 422,mensaje
        validate_building_year=f"and p.year={building_year}"
    
    if city:
        validar_string=(city)
        city=city.lower().strip
        validate_city=f"and p.city='{city}'"
        
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
    
    resultados = cursor.fetchall()
    cursor.close()
    CerrarConexion(connection)
    if not resultados:
        mensaje= "no encuentro informacion con esos criterios de busqueda"
        return 422,mensaje

    data = []
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
        return numero
    except ValueError:
        return "por favor ingrese un id valido code:422"
def validar_string(string_p):
    string_p=string_p.upper()
    palabras_prohibidas = {"SELECT", "UPDATE", "DELETE", "DROP", "USE"}
    
    if any(palabra in string_p.upper() for palabra in palabras_prohibidas):
        raise ValueError("No puede usar esas palabras en el parámetro. Código: 422")
    
    return True