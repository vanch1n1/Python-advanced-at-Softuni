class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

person = Person(25)

print(person.age)   