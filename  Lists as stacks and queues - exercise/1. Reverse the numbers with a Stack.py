command = input().split()
new_list = command.copy()
reversed_numbers = []
for i in command:
    reversed_numbers.append(new_list.pop())
print(f"{' '.join(reversed_numbers)}")


