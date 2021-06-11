def kwargs_length(**kwargs):
    el = len(kwargs.keys())
    return el


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))