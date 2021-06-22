def input_error():
    """ checking for a proper input """
    integer_word = None
    while True:
        try:
            integer_word = input()
            if integer_word == 'Search':
                break
            integer = int(input())
            num_dict[integer_word] = integer
        except ValueError:
            print('The variable number must be an integer')
    search()

def search():
    """ Search for the key and print it from the dictionary if found """
    """ Print the error if not found """
    while True:
        try:
            key = input()
            if key == 'Remove':
                break
            print(f"{num_dict[key]}")
        except KeyError:
            print("Number does not exist in dictionary")
    remove()


def remove():
    """ Remove the key if found, print the error if not"""
    if not num_dict:
        print(num_dict)
    while True:
        try:
            key = input()
            if key == 'End':
                break
            del num_dict[key]
            print(num_dict)
        except KeyError:
            print("Number does not exist in dictionary")
            print(num_dict)


num_dict = {}
input_error()