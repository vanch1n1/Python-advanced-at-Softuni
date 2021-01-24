n = int(input())
names = []
for i in range(n):
    name = input()
    names.append(name)
names = (set(names))
for name in names:
    print(name)