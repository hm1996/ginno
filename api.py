# Importando las dependencias Flask y request
# de flask
from flask import Flask, request
# Importando las dependencias Resource y Api de
# flask_restful
from flask_restful import Resource, Api
import datetime

# Inicializar la api
app = Flask(__name__)
api = Api(app)

# Creamos el endpoint
class Server(Resource):
    # Defino el metodo http como post
    def post(self):
        # Obtengo la informacion desde el agente
        server_info = request.data
        server_ip = request.remote_addr
        fecha = datetime.datetime.now().strftime('%Y-%m-%d')
        
        #<IP de servidor>_<AAAA-MM-DD>
        # Abro el archivo informacion.txt
        f = open(server_ip + '_' + fecha + '.json', 'wb')
        # Escribo lo que mando el agente
        f.write(server_info)
        # Cierro el archivo
        f.close()
        # Devuelvo la respuesta al agente
        return 'OK'

# Integro el endpoint 'informacion' al API
api.add_resource(Server, '/informacion')

if __name__ == '__main__':
    # Inicio el servidor en el puerto 1234
    app.run(host = '0.0.0.0', port = 1234, debug = True)
        
