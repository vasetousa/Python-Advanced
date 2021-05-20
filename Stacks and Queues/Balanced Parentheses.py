string = list(input())
stack = []
dict_1 = {'{': "}",'[': "]", '(': ")"}
disrupted = False
for el in string:
    if el == "{" or el == '[' or el == '(':
        stack.append(el)
    else:
        if stack:
            last_element = stack.pop()
            if not el == dict_1[last_element]:
                disrupted = True
                break
        else:         # if string starts with closed parentheses -> end
            disrupted = True
            break
if stack:
    print("NO")
else:
    if disrupted:
        print("NO")
    else:
        print("YES")
