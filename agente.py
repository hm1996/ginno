import os  # Importa la libreria Os de Python.
import sys # Importa la libreria Sys de Python.
import json # Importa la libreria Json de Python.
import http.client # Importa la libreria Httplib de Python.

# Configura la conexion con el API
conexion = http.client.HTTPConnection('localhost:1234')
endpoint = '/informacion'

# Obtiene la informacion de la plataforma.
sistema_operativo = sys.platform
comando_cpuinfo = ''
comando_procesos = ''
comando_usuarios = ''
so = ''
comando_version = ''

# Si el sistema operativo es windows.
if sistema_operativo == 'win32':
    comando_cpuinfo = 'wmic cpu get name /value'
    comando_procesos = 'tasklist'
    comando_usuarios = 'whoami'
    so = 'Windows'
    comando_version = 'wmic os get Caption /value'

# Si el sistema operativo es linux.
elif sistema_operativo == 'linux2':
    comando_cpuinfo = 'cat /proc/cpuinfo'
    comando_procesos = 'ps -a'
    comando_usuarios = 'w -h'
    so = 'Linux'
    comando_version = 'lsb_release -d'

# Si el sistema operativo es diferente a windows o linux
else:
    print('SISTEMA OPERATIVO NO COMPATIBLE')
    sys.exit() # OS no compatible, no corre el agente

# Ejecuta el comando en el terminal del SO:
#   read(), lee la respuesta del terminal.
#   strip(), elimina los espacios en la respuesta.
#   splitlines(), separa la informacion en lineas.
cpuinfo = os.popen(comando_cpuinfo).read().strip()
procesos = os.popen(comando_procesos).read().strip().splitlines()
usuarios = os.popen(comando_usuarios).read().strip()
version = os.popen(comando_version).read().strip()

# Enviar la informacion al API
informacion = {
    "cpu": str(cpuinfo),
    "procesos": procesos,
    "usuarios": str(usuarios),
    "so": str(so),
    "version": str(version)
}

conexion.request('POST', endpoint, json.dumps(informacion))
respuesta = conexion.getresponse()
print(respuesta.read())
conexion.close()
