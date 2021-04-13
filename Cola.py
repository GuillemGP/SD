class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")

    def es_vacia(self):
        return self.items == []
    
    def print_cola(self):
        print("Elementos de la cola: ")
        for i in self.items:
            print(i)

#Main temporal de pruebas
if __name__ == "__main__":
    q = Cola()
    q.es_vacia()

    q.encolar(1)
    q.encolar(2)
    q.encolar(3)

    q.print_cola()
    q.desencolar()
    q.print_cola()

    q.es_vacia()