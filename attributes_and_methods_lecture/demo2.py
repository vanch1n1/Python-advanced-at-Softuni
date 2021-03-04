class Person:
    def __init__(self, name):
        self.name = name
        self.age = 17


pesho = Person('Pesho')
print(pesho.name)
print(getattr(pesho, 'age'))