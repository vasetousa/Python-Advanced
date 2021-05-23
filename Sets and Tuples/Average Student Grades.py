number_students = int(input())
data = {}

for value in range(number_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in data:
        data[name] = [float(grade)]
    else:
        data[name].append(float(grade))

for key, value in data.items():
    avg = sum(value)/len(value)
    grades = ' '.join(map(lambda grade: f'{grade:.2f}', value))
    print(f"{key} -> {grades} (avg: {avg:.2f})")