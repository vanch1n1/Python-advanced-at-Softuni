class Person:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.sex = sex

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

person = Person("George", 32, 'male')
print(person.sex)
print(person.get_age())
print(person.get_age())
print(person.__age)

