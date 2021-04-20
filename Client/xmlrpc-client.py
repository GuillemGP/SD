import xmlrpc.client

import Cola
import worker

def mostrarMenu():
    print("Que opcion quieres?")
    print("Opcion 0: Salir")
    print("Opcion 1: Envia tasques WordCount al cluster")
    print("Opcion 2: Envia tasques CountinWords al cluster")
    print("Opcion 3: Afegeix worker")
    print("Opcion 4: Eliminar worker")
    print("Opcion 5: Llistar workers")
    opcion = int(input())
    return opcion

def ver_palabras(diccionario):
   for palabra in list(diccionario.keys()):
      print(palabra, ":", diccionario[palabra])

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
queue = Cola.Cola()

opcion = mostrarMenu()
while(opcion != 0):
    if opcion == 1: 
        print("Introducir nombre fichero: ")
        fichero = input()
        result = proxy.WordCountServer(fichero)
        print(result)

    if opcion == 2: 
        print("Introducir nombre fichero: ")
        fichero = input()
        result = proxy.CountingWordsServer(fichero)
        print(result)
        
    if opcion == 3: 
        id = proxy.createWorker()
        print("Worker " + str(id) + " creado")  
            
    if opcion == 4:
        print("Que worker quieres eliminar?")
        id = input()
        string = proxy.killWorker(id)
        print(string)
    if opcion == 5:
        result = proxy.listWorkers()
        print(result) 
    opcion = mostrarMenu()
    

