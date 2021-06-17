import os

# data = open("/Users/Vasil/Desktop/Tier.txt", 'r')
# for line in data:
#     if "man" in line.lower():
#         print(line, end='')
# data.close()

# with open("/Users/Vasil/Desktop/Tier.txt", 'r') as data:
# no need to close the file

#     for line in data:
#         if 'tier' in line.lower():
#             print(line, end='')

# with open("/Users/Vasil/Desktop/Tier.txt", 'r') as data:
#     line = data.readline()
#     while line:
#         print(line, end='')
#         line = data.readline()

# using readlineS() -> returns the text as list. Using for cycle to print

with open("/Users/Vasil/Desktop/Tier.txt", 'r') as data:
    lines = data.readlines()

for line in lines:
    print(line, end='')


with open("/Users/Vasil/Desktop/Tier.txt", 'r') as data:
    lines = data.read()

for line in lines:
    print(line, end='')
