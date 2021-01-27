from _collections import deque

n = int(input())
stations = deque()
for i in range(n):
    stations.append(input())


for big_circle_iteration in range(n):
    is_valid = True
    tank_petrol = 0
    for small_small_circle_iteration in range(n):
        current_station = stations[big_circle_iteration]
        petrol, distance_to_next = current_station.split()
        petrol = int(petrol)
        distance_to_next = int(distance_to_next)
        tank_petrol += petrol
        if tank_petrol >= distance_to_next:
            tank_petrol -= distance_to_next
            stations.append(stations.popleft(current_station))


        else:
            is_valid = False
            break

    if is_valid:
        print(big_circle_iteration)
        break

