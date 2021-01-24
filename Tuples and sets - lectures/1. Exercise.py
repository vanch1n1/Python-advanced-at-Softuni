values = tuple(map(float, '12 2132 14 34 23 12 1 1.2323'.split(' ')))
values_count = {}
for value in values:
    values_count[value] = values.count(value)
print(values_count)
values2 = ('192 2132 14 34 23 12 1 1.2323'.split(' '))
print(values2)