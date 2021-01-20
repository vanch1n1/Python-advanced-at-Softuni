line = (int(el)for el in input().split())
n, m = line
n_elements = set()
m_elements = set()
for i in range(n):
    element = input()
    n_elements.add(element)
for i in range(m):
    element = input()
    m_elements.add(element)
intersection_of_sets = (n_elements.intersection(m_elements))
for i in intersection_of_sets:
    print(i)

