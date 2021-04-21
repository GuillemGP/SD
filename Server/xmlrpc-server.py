from xmlrpc.server import SimpleXMLRPCServer
from redis import Redis
from rq import Queue, Worker, Connection
from multiprocessing import Process
import xmlrpc.client
import json
import CountingWords
import WordCount
import putResultTogether
import os
import redis
import time

def WordCountServer(fichero):
    numberOfWorkers = nWorkers()
    if numberOfWorkers > 0:                     #si tenemos workers creados (1 o mas)
        filesLength = len(fichero.split())
        if filesLength == 1:                    #si solo tenemos un fichero que tratar
            job = queue.enqueue(WordCount.contar_palabras,fichero)
            while job.result == None:
                time.sleep(0.1)
            result = str(job.result) + "\n"
            return result
        else:                                   #si tenemos mas de un fichero para tratar                
            jobResults = []
            for file in fichero.split():
                workerResult= []
                job = queue.enqueue(WordCount.contar_palabras,file)
                while job.result == None:
                    time.sleep(0.1)
                workerResult.append(file)       #ponemos en el resultado del worker el nombre del fichero
                workerResult.append(job.result) #ponemos en el resultado del worker el resultado obtenido
                jobResults.append(workerResult) #añadimos este objeto a la lista
            job = queue.enqueue(putResultTogether.putResultTogether, args=(jobResults,"WordCount"))
            while job.result == None:
                time.sleep(0.1)
            result = str(job.result) + "\n"
            return result
    else:                                       #si no tenemos ningun worker creado
        return("No hi ha cap worker actiu per encuar la tasca")

def CountingWordsServer(fichero):
    numberOfWorkers = nWorkers()
    if numberOfWorkers > 0:                     #si tenemos workers creados (1 o mas)
        result = ""
        filesLength = len(fichero.split())
        if filesLength == 1:                    #si solo tenemos un fichero que tratar          
            job = queue.enqueue(CountingWords.contar_palabras_fichero,fichero)
            while job.result == None:
                time.sleep(0.1)
            result = "El fichero tiene " + str(job.result) + " palabras\n"
            return result
        else:                                   #si tenemos mas de un fichero para tratar                
            jobResults = []
            for file in fichero.split():
                workerResult= []
                job = queue.enqueue(CountingWords.contar_palabras_fichero,file)
                while job.result == None:
                    time.sleep(0.1)
                workerResult.append(file)       #ponemos en el resultado del worker el nombre del fichero
                workerResult.append(job.result) #ponemos en el resultado del worker el resultado obtenido
                jobResults.append(workerResult) #añadimos este objeto a la lista
            job = queue.enqueue(putResultTogether.putResultTogether, args=(jobResults,"CountingWords"))
            while job.result == None:
                time.sleep(0.1)
            result = str(job.result) + "\n"
            return result
    else:                                       #si no tenemos ningun worker creado
        return("No hi ha cap worker actiu per encuar la tasca")    

#Inicializar worker
def startWorker(id):
    listen = ['default']

    redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

    conn = connection=Redis()

    if __name__ == '__main__':
        with Connection(conn):
            worker = Worker(list(map(Queue, listen)))
            worker.work()

#Crear worker
def createWorker():
    global WORKERS
    global WORKER_ID
    proc = Process(target=startWorker, args=(WORKER_ID,))
    proc.start()
    WORKERS.append(proc)

    WORKER_ID+=1
    return (WORKER_ID-1)

#Matar worker (pasandole su id)
def killWorker(id):
    WORKERS[int(id)].terminate()
    return "Worker " + id + " eliminat correctament"

#Numero de workers (devuelve un contador)
def nWorkers():
    i = 0
    for worker in WORKERS:
        poll = worker.is_alive()
        if poll is True:
            i+=1      
    return i

#Listar workers y su estado
def listWorkers():
    i = 0
    result = ""
    for worker in WORKERS:
        poll = worker.is_alive()
        if poll is True:
            result = result + "Worker " + str(i) + ": Actiu\n"
        else:
            result = result + "Worker " + str(i) + ": Eliminat\n"
        i+=1
    return result  

#Workers
WORKERS = []
WORKER_ID = 0

#Redis
queue = Queue(connection=Redis())

#Server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")
server.register_function(createWorker, "createWorker")
server.register_function(startWorker, "startWorker")
server.register_function(killWorker, "killWorker")
server.register_function(listWorkers, "listWorkers")
server.register_function(WordCountServer, "WordCountServer")
server.register_function(CountingWordsServer, "CountingWordsServer")
server.serve_forever()