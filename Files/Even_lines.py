with open('text.txt', 'r') as file:
    data = file.readlines()
string = '-.,!?'
new_string = ''
new_list = []

for idx, row in enumerate(data):
        if not idx % 2 == 0:
            continue
        for el in row:
            if el in string:
                el = "@"
            new_string += el
        new_list.append(new_string)
        new_string = ''
for el in new_list:
    result = ' '.join(reversed(el.split()))
    print(result)
file.close()
