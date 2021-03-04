class School:
    def __init__(self, name, students):
        self.students = students
        self.name = name

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def from_string(cls, other_students, other_uni):
        return cls(other_uni, other_students)



print(School('Softuni',['Sofi, Marta, ivan']))
print(School.from_string('Ivan', 'UNSS'))


