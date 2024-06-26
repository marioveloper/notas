class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pinneaple_allowed = False

    @property
    def pinneaple_allowed(self):
        return self._pinneaple_allowed

    @pinneaple_allowed.setter
    def pinneaple_allowed(self, value):
        if value:
            password = input('enter the password: ')
            if password == 'Sw0rdf1sh':
                self.pinneaple_allowed = value
            else:
                raise ValueError('alert intruder')

pizza = Pizza(['cheeze', 'tomato'])
print(pizza.pinneaple_allowed)
pizza.pinneaple_allowed = True
print(pizza.pinneaple_allowed)