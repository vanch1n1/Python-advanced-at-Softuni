numbers = input()
numbers = map(float, numbers.split(' '))
values = {}
for value in numbers:
    if value not in values:
        values[value] = 0
    values[value] += 1
for value, count in values.items():
    print(f"{int(value)} - {count} times")
