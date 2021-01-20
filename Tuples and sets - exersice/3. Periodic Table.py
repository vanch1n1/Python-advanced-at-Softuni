n = int(input())
all_chemical_compunds = set()
for i in range(n):
    chemical_compounds = input().split()
    for i in chemical_compounds:
        all_chemical_compunds.add(i)
for i in all_chemical_compunds:
    print(i)

