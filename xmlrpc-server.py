from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

import CountingWords
import WordCount

def contarPalabrasFichero(fichero):
    return CountingWords.contar_palabras_fichero(fichero)

def diccionarioFichero(fichero):
    diccionario = WordCount.contar_palabras(fichero)
    WordCount.ver_palabras(diccionario)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")
server.register_function(contarPalabrasFichero, "contarPalabrasFichero")
server.register_function(diccionarioFichero, "diccionarioFichero")
server.serve_forever()