class Person:
    max_age = 150
    def __init__(self, name, age):
        self.validate_age(age) # here we can validate self attributes with static emthods
        self.name = name
        self.age = age


    @staticmethod
    def validate_age(age):
        if age < 0 or Person.max_age < age:
            raise ValueError('Age is invalid')

print(Person('Ivan', 28))
daci = Person('Dacyika', 29)
print(daci.max_age)
print(Person('bai Ivan', 151))
print(daci.max_age)
