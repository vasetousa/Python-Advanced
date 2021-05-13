string = input()
new_string = []

for el in string:
    new_string.append(el)

result = ''
while new_string:
    result += new_string.pop()
print(result)
