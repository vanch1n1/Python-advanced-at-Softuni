n = int(input())
list_of_students = {}
def avg(values):
    return sum(values) / len(values)
for i in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in list_of_students:
        list_of_students[name] = []
    list_of_students[name].append(grade)
for (name, grades) in list_of_students.items():
    average = avg(grades)
    grades = ' '.join(map(str, grades))

    print(f"{name} - {grades} avg({average})")


