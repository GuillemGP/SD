import xmlrpc.client

def mostrarMenu():
    print("Que opcion quieres?")
    print("Opcion 0: Salir")
    print("Opcion 1: CountingWords")
    print("Opcion 2: WordCount")
    print("Opcion 3: Worker")
    opcion = int(input())
    return opcion

def ver_palabras(diccionario):
   for palabra in list(diccionario.keys()):
      print(palabra, ":", diccionario[palabra])

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
            diccionario = proxy.diccionarioFichero(fichero)
            ver_palabras(diccionario)
        
    if opcion == 3:
            print("worker")
            input = input()

    opcion = mostrarMenu()

