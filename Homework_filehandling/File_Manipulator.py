import os
new_file = None
data = input()
while not data == "End":
    if data.startswith("Create"):
        command, file_name = data.split("-")
        new_file = open(file_name, "w")
        print(new_file)
        new_file.close()
    elif data.startswith("Add"):
        command, file_name, content = data.split("-")
        if not os.path.exists(file_name):
            new_file = open(file_name, "w")
            print(content, "\n", file=new_file)
            new_file.close()
        else:
            new_file = open(file_name, "a")
            print(content, file=new_file)
            new_file.close()
    elif data.startswith("Replace"):
        command, file_name, old_string, new_string = data.split("-")
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            # reading info from the file
            with open(file_name, "r") as new_file:
                new_info = new_file.read()
            # writing new info in the file
            with open(file_name, "w") as new_file:
                new_info = new_info.replace(old_string, new_string)
                new_file.write(new_info)

    elif data.startswith("Delete"):
        command, file_name = data.split("-")
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            os.remove(file_name)
    data = input()