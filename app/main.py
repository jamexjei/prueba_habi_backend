# aqui se hacen las  importaciones de http server para la creacion de el servidor local 
from http.server import HTTPServer
# aqui se llama al archivo routes para llamar a la funcion request handler que es la que se encarga de recibir la peticion 
from app.routes import RequestHandler
# aqui se hace la configuracion de el servidor y el puerto de escucha, como no hemos definido una direccion , el servidor toma la ip local 
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en puerto {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()