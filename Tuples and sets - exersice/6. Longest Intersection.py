n = int(input())
intersections = []
for i in range(n):
    data = input()
    first_seq_data, second_seq_data = data.split('-')
    start, stop = [int(el) for el in first_seq_data.split(',')]
    first_seq = range(start, stop + 1)
    start, stop = [int(el) for el in second_seq_data.split(',')]
    second_seq = range(start, stop + 1)
    intersection = set(first_seq).intersection(set(second_seq))
    intersections.append(intersection)
longest_intersection = sorted(intersections, key=lambda x: -len(x))
print(f'Longest intersection is {list(longest_intersection[0])} with length {len(longest_intersection[0])}')