def age_assignment(*args, **kwargs):
    result = {}
    for x in args:
        first_l = x[0]
        if first_l in kwargs:
            result[x] = kwargs[first_l]
    return result



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))