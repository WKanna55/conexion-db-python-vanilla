from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os

class MiServidor(SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/libros":
            self.enviar_json({
                "libros": [
                    {"id": 1, "titulo": "El principito"},
                    {"id": 2, "titulo": "Don Quijote"}
                ]
            })
            return

        super().do_GET()

    def enviar_json(self, datos):

        respuesta = json.dumps(datos).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(respuesta))
        self.end_headers()

        self.wfile.write(respuesta)


os.chdir("frontend") #poner frontend como directorio principal

servidor = HTTPServer(
    ("localhost", 8000),
    MiServidor
)

print("Servidor iniciado en http://localhost:8000")

servidor.serve_forever()