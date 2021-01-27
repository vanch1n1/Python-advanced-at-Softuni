number_of_clothes = list(map(int, input().split()))
capacity = int(input())
counter_racks = 1
current_capacity = capacity
while len(number_of_clothes) >0:
    current_cloth = number_of_clothes.pop()
    if current_cloth <= current_capacity:
        current_capacity -= current_cloth
    else:
        current_capacity = capacity
        counter_racks +=1
        current_capacity -= current_cloth

print(counter_racks)

