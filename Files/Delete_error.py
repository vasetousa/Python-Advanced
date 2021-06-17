import os
# create file
# file = open('try_to_delete_me.txt', 'w')

# delete file 2 tmes
try:
    os.remove('try_to_delete_me.txt')
except:
    print("File already deleted!")