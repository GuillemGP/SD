import xmlrpc.client

import Cola
import worker

def mostrarMenu():
    print("Que opcion quieres?")
    print("Opcion 0: Salir")
    print("Opcion 1: CountingWords")
    print("Opcion 2: WordCount")
    print("Opcion 3: Crear worker")
    print("Opcion 4: Eliminar worker")
    print("Opcion 5: Listar workers")
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
            fichero1 = input()

            numPalabrasFichero = proxy.contarPalabrasFichero(fichero1)
            print("El fichero tiene %s palabras" %numPalabrasFichero)
        
    if opcion == 2: 
            print("Introducir nombre fichero: ")
            fichero = input()

            diccionario = proxy.diccionarioFichero(fichero)
            ver_palabras(diccionario)
    
    if opcion == 3: 
        worker.create_worker()

    if opcion == 4: 
        worker.delete_worker(worker.num_workers())

    if opcion == 5: 
        worker.show_list_workers()

    queue.print_cola()
    opcion = mostrarMenu()
    

