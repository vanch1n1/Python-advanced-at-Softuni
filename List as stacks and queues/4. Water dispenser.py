from collections import deque
quantity_of_water = int(input())
queue = deque()
name = input()
while name != 'Start':
    queue.append(name)
    name = input()
liters = input()
while liters !=  'End':
    if liters.split()[0] != 'refill':
        liters = int(liters)
        if liters <= quantity_of_water:
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')
        quantity_of_water -= liters
    else:
        liters = liters.split()
        refill = liters[1]
        refill = int(refill)
        quantity_of_water += refill

    liters = input()

print(f'{quantity_of_water} liters left')