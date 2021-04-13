import xmlrpc.client

import worker

def mostrarMenu():
    print("Que opcion quieres?")
    print("Opcion 0: Salir")
    print("Opcion 1: CountingWords")
    print("Opcion 2: WordCount")
    opcion = int(input())
    return opcion

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

opcion = mostrarMenu()

while(opcion != 0):
    if opcion == 1: 
            print("Introducir nombre fichero: ")
            fichero1 = input()
            numPalabrasFichero = proxy.contarPalabrasFichero(fichero1)
            print("El fichero tiene %s palabras" %numPalabrasFichero)
        
    if opcion == 2: 
            print("Introducir nombre fichero: ")
            fichero = input()
            proxy.diccionarioFichero(fichero)

    opcion = mostrarMenu()

