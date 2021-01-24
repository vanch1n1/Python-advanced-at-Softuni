n = int(input())
guests_invited = []
for i in n:
    guests_invited.append(input())

guest_arrived = input().split()

guests_not_arrived = set(guests_invited).difference(guest_arrived)
print(guests_not_arrived)
