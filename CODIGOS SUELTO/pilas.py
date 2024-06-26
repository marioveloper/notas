#ultimo en entrar es primero en salir
# push para anadir elementos
# pop para eliminar

class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.item.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)