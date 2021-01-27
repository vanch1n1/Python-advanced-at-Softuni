a = '1 2 3 4 5 6'
listt = [int(i) for i in a.split()]
print(listt)

b = '1 2 3 4 5'
b_listt = list(map(int, b.split()))
print(b_listt)   