n = int(input())
even_numbers_set = set()
odd_numbers = set()
for i in range(1, n + 1):
    name = input()
    current_sum_of_name = sum([ord(el) for el in name]) // i
    if current_sum_of_name % 2 == 0:
        even_numbers_set.add(current_sum_of_name)
    else:
        odd_numbers.add(current_sum_of_name)
sum_evens = sum(even_numbers_set)
sum_odds = sum(odd_numbers)
if sum_evens == sum_odds:
    modified_set = (str(el) for el in even_numbers_set.union(odd_numbers))
    print(f'{"".join(modified_set)}')
elif sum_evens > sum_odds:
    modified_set = (str(el) for el in odd_numbers.difference(even_numbers_set))
    print(f'{"".join(modified_set)}')
else:
    modified_set = (str(el) for el in even_numbers_set.symmetric_difference(odd_numbers))
    print(f'{"".join(modified_set)}')