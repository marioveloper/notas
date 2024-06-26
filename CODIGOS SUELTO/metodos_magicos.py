class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)):
            result = other.cont[:index]+'>'+self.cont
            result += '>' + other.cont[index:]
            print(result)

spam = SpecialString('spam')
eggs = SpecialString('egss')
spam>eggs