import CountingWords
import WordCount

from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

print('Practica 1 SD\n')

#Servidor
def is_even(n):
    return n % 2 == 0

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
#server.register_function(is_even, "is_even")
server.register_function(CountingWords.contar_palabras_fichero, "contar_palabras_fichero")
server.serve_forever()

#Cliente
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    palabras=proxy.contar_palabras_fichero()
    print(palabras)

numPalabras=CountingWords.contar_palabras_fichero('ficheroPrueba.txt')
print(numPalabras)
print('\n')

diccionario = WordCount.contar_palabras('ficheroPrueba.txt')
WordCount.ver_palabras(diccionario)