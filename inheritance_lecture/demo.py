class Person:
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print(f'Hello, I am {self.name}')

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        #super(Employee, self).__init__(name)  - na stari versii na python
        print(f'Hello, I  {self.name}')

emp = Employee('Ivan', 3500)
emp.say_hello()