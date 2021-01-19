from _collections import deque

players = input().split()
step = int(input())
queue = deque(players)
n = 0
while len(queue) > 1:
    n += 1
    if n == step:
        print(f'Removed {queue.popleft()}')
        n = 0
    else:
        queue.append(queue.popleft())
print(f'Last is {queue.popleft()}')

