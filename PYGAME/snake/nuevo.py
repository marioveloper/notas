class Mario:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhello(self):
        return f'Hello my name is {self.name}'

mario = Mario('Mario Luis', 23)
print(mario.sayhello)