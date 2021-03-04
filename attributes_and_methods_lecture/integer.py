import math

class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if type(value) != float:
            return "value is not a float"
        return cls(math.floor(value))

    @classmethod
    def from_roman(cls, value):
        pass # put  algotih from net

    @classmethod
    def from_string(cls, value):
        if type(value) !=str:
            return 'wrong type'
        return Integer(int(value))

    def add(self, integer):
        if type(integer) != int:
            return 'type is not an integer'
        return self.value + integer.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))