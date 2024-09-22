# prueba_habi_backend
para la prueba habi se van a implementar las siguientes tecnologias.

-- lenguaje : 
*python *Version : 3.9.13 
*framework: ninguno

--base de datos motor: 
*mysql 
*version: 5.7.12

para la implementacion del backend se planea realizar consultas con querys sin la necesidad de usar ORM , esto con el objetivo de que vean el uso y la sintaxis sql implementada en la prueba , 
la estructura del proyecto esta compuesta por diferentes subcarpetas y  comunicacion entre archivos como paquetes .

para las dependencias se planea usar :
-mysql-connector-python(para la conexion con la base de datos mysql)
-BaseHTTPRequestHandler(para crear un mini servidor y escuchar atraves de este mismi) 

para correr el proyecto se deben seguir los siguientes pasos. 
1- crear el entorno virtual 
2-correr el archivo requirements.txt
3-ejecutar el siguiente comando : python -m app.main
4 desde cualquier cliente que pueda consumir apis  llamar a la siguiente ruta : http://127.0.0.1:8000/api/consultarPropiedades
(method=POST)
json a enviar al servicio= 
{
    "city": "",
    "status": "",
    "building_year": 2011

}

-- para las pruebas unitarias se creo la carpeta test y se hizo la importacion de la dependencia unittest
comando para correr las pruebas :python -m unittest discover -s app/tests (debes estar ubicado en la ruta del proyecto)