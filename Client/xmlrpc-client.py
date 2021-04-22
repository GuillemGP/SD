import xmlrpc.client

#Menu para el cliente
def mostrarMenu():
    print("Quina opcio vols?")
    print("Opcio 0: Sortir")
    print("Opcio 1: Enviar tasques WordCount al cluster")
    print("         Si voleu enviar mes d'un fitxer introduiu un espai entre els noms dels fitxers")
    print("Opcio 2: Enviar tasques CountinWords al cluster")
    print("         Si voleu enviar mes d'un fitxer introduiu un espai entre els noms dels fitxers")
    print("Opcio 3: Afegeix worker")
    print("Opcio 4: Eliminar worker")
    print("Opcio 5: Llistar workers")
    opcion = int(input())
    return opcion

#Visualizar contenido del diccionario
def ver_palabras(diccionario):
   for palabra in list(diccionario.keys()):
      print(palabra, ":", diccionario[palabra])

#Server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

opcion = mostrarMenu()
while(opcion != 0):
    if opcion == 1: 
        print("Introduir el nom del fitxer: ")
        fichero = input()
        result = proxy.WordCountServer(fichero)
        print(result)

    if opcion == 2: 
        print("Introduir el nom del fitxer: ")
        fichero = input()
        result = proxy.CountingWordsServer(fichero)
        print(result)
        
    if opcion == 3: 
        id = proxy.createWorker()
        print("Worker " + str(id) + " creat")  
            
    if opcion == 4:
        print("Quin worker vols eliminar?")
        id = input()
        string = proxy.killWorker(id)
        print(string)

    if opcion == 5:
        result = proxy.listWorkers()
        print(result) 

    opcion = mostrarMenu()
    

