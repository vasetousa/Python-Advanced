with open('text.txt') as file:
    data = file.readlines()
string = ",.!?-'"
lett_count = 0
punct_count = 0

with open("output", 'w') as output:
    for idx, row in enumerate(data):
        for el in row:
            if el in string:
                punct_count += 1
            elif 65 <= ord(el) <= 90 or 97 <= ord(el) <= 122:
                lett_count += 1

        print(f'Line {idx+1}: {row.strip()} ({lett_count})({punct_count})')
        print(f'Line {idx+1}: {row.strip()} ({lett_count})({punct_count})', file=output)

        punct_count = 0
        lett_count = 0