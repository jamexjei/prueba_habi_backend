from http.server import BaseHTTPRequestHandler
import json
from app.services.prueba_habi_service import ConsultarPropiedades

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith('/api/consultarPropiedades'):
            content_length = int(self.headers['Content-Length'])
            json_data = self.rfile.read(content_length)  
            try:
                
                data = json.loads(json_data)
                status = data.get('status')
                building_year = data.get('building_year')
                city=data.get('city')

                
                code,resultados = ConsultarPropiedades(status, building_year,city)

                # Respuesta JSON
                self.send_response(code)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(resultados).encode())
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'No encontrado'}).encode())
