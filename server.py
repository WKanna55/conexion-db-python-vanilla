from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os

from controllers.obtenerProductos import obtener_productos
from controllers.crearProducto import crear_producto
from controllers.actualizarProducto import actualizar_producto
from controllers.eliminarProducto import eliminar_producto
class MiServidor(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/productos":
            self.enviar_json({
                "productos": obtener_productos()
            })
            return

        super().do_GET()


    def do_POST(self):

        if self.path == "/api/productos":

            datos = self.leer_json()

            id_producto = crear_producto(
                datos["nombre"],
                datos["categoria"],
                datos["precio"],
                datos["stock"]
            )

            self.enviar_json({
                "mensaje": "Producto creado correctamente",
                "id": id_producto
            }, 201)

            return

        self.enviar_json({
            "error": "Ruta no encontrada"
        }, 404)


    def do_DELETE(self):

        if self.path.startswith("/api/productos/"):

            id_producto = self.obtener_id()

            filas_afectadas = eliminar_producto(id_producto)

            if filas_afectadas == 0:

                self.enviar_json({
                    "error": "Producto no encontrado"
                }, 404)

                return

            self.enviar_json({
                "mensaje": "Producto eliminado correctamente"
            })

            return

        self.enviar_json({
            "error": "Ruta no encontrada"
        }, 404)

    def do_PUT(self):

        if self.path.startswith("/api/productos/"):

            id_producto = self.obtener_id()

            datos = self.leer_json()

            filas_afectadas = actualizar_producto(
                id_producto,
                datos["nombre"],
                datos["categoria"],
                datos["precio"],
                datos["stock"]
            )

            if filas_afectadas == 0:

                self.enviar_json({
                    "error": "Producto no encontrado"
                }, 404)

                return

            self.enviar_json({
                "mensaje": "Producto actualizado correctamente"
            })

            return

        self.enviar_json({
            "error": "Ruta no encontrada"
        }, 404)



    def leer_json(self):

        longitud = int(self.headers.get("Content-Length", 0))

        cuerpo = self.rfile.read(longitud)

        return json.loads(cuerpo)


    def obtener_id(self):

        partes = self.path.split("/")

        return int(partes[-1])

    def enviar_json(self, datos, codigo=200):

        respuesta = json.dumps(datos).encode()

        self.send_response(codigo)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(respuesta)))
        self.end_headers()

        self.wfile.write(respuesta)


os.chdir("frontend") #poner frontend como directorio principal

servidor = HTTPServer(
    ("localhost", 8000),
    MiServidor
)

print("Servidor iniciado en http://localhost:8000")

servidor.serve_forever()