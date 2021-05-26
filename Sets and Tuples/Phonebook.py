phonebook = {}
command = input()

while not command[0].isdigit():
    name, number = command.split('-')
    phonebook[name] = number
    command = input()

command = int(command)
for i in range(command):
    search_name = input()
    if search_name not in phonebook:
        print(f"Contact {search_name} does not exist.")
    else:
        print(f"{search_name} -> {phonebook.get(search_name)}")
