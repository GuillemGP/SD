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

def contarPalabrasFichero(fichero):
    job = queue.enqueue(CountingWords.contar_palabras_fichero,fichero)
    time.sleep(0.5)
    return(job.result)

def diccionarioFichero(fichero):
    job = queue.enqueue(WordCount.contar_palabras,fichero)
    time.sleep(0.5)
    return(job.result)


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
    WORKERS[WORKER_ID]=proc

    WORKER_ID+=1
    return (WORKER_ID-1)

WORKERS ={}
WORKER_ID = 1
queue = Queue(connection=Redis())
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is listening on port 8000...")
server.register_function(contarPalabrasFichero, "contarPalabrasFichero")
server.register_function(diccionarioFichero, "diccionarioFichero")
server.register_function(createWorker, "createWorker")
server.register_function(startWorker, "startWorker")
server.serve_forever()