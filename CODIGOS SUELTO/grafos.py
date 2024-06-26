# represantaciones con rutas redes etc

class Graph():
    def __init__(self, size):
        self.adj = [[0]*size for i in range(size)]
        self.size = size

    def add_edge(self, orig, dest):
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print('Invalid Edge')
        else:
            self.a