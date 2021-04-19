from xmlrpc.server import SimpleXMLRPCServer
from redis import Redis
from rq import Queue, Worker, Connection
from multiprocessing import Process
import xmlrpc.client
import json
import CountingWords
import WordCount
import os
import redis
import time

def WordCountServer(fichero):
    numberOfWorkers = nWorkers()
    if numberOfWorkers > 0:
        result = ""
        filesLength = len(fichero.split())
        if filesLength==1:
            job = queue.enqueue(CountingWords.contar_palabras_fichero,fichero)
            while job.result == None:
                time.sleep(0.1)
            result = result + "El fichero tiene " + str(job.result) + " palabras\n"
            job = queue.enqueue(WordCount.contar_palabras,fichero)
            while job.result == None:
                time.sleep(0.1)
            result = result + str(job.result) + "\n"
            return result
        else:
            return result
    else:
        return("No hi ha cap worker actiu per encuar la tasca")


def startWorker(id):
    listen = ['default']

    redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

    conn = connection=Redis()

    if __name__ == '__main__':
        with Connection(conn):
            worker = Worker(list(map(Queue, listen)))
            worker.work()

def createWorker():
    global WORKERS
    global WORKER_ID
    proc = Process(target=startWorker, args=(WORKER_ID,))
    proc.start()
    WORKERS.append(proc)

    WORKER_ID+=1
    return (WORKER_ID-1)

def killWorker(id):
    WORKERS[int(id)].terminate()
    return "Worker " + id + " eliminat correctament"

def nWorkers():
    i = 0
    result = ""
    for worker in WORKERS:
        poll = worker.is_alive()
        if poll is True:
            i+=1      
    return i

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

WORKERS = []
WORKER_ID = 0
queue = Queue(connection=Redis())
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")
server.register_function(createWorker, "createWorker")
server.register_function(startWorker, "startWorker")
server.register_function(killWorker, "killWorker")
server.register_function(listWorkers, "listWorkers")
server.register_function(WordCountServer, "WordCountServer")
server.serve_forever()