def input_data_in_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def print_results(data):
    for e in data:
        print(e)

n = int(input())
names = input_data_in_list(n)

# names = [
# 'Lee',
# 'Joey',
# 'Lee',
# 'Joe',
# 'Alan',
# 'Alan',
# 'Peter',
# 'Joey'
# ]

new_list = set(names)
print_results(new_list)