from multiprocessing import Process

WORKERS = {}
WORKER_ID = 0

def start_worker(WORKER_ID):
    print("Iniciando worker con ID: ", WORKER_ID)

def delete_worker(id):
    global WORKERS
    del WORKERS[id]
    print("Eliminado worker con ID: ", id)

def show_list_workers():
    global WORKERS
    print("Lista de workers: ")
    for worker in WORKERS:
        print(worker)

def create_worker():
    global WORKERS
    global WORKER_ID

    proc = Process(target=start_worker, args=(WORKER_ID, ))
    proc.start()
    WORKERS[WORKER_ID] = proc

    WORKER_ID += 1

def num_workers():
    global WORKER_ID
    return (WORKER_ID-1)

#Main temporal de pruebas
if __name__ == "__main__":
    create_worker()
    create_worker()
    create_worker()

    show_list_workers()
    delete_worker(1)
    show_list_workers()
