def age_assignment(*args, **kwargs):
    names = {}

    for name in args:
        names[name] = kwargs[name[0]]

    sorted_names = sorted(names.items(), key=lambda kvp: kvp[0])

    result = [f'{info[0]} is {info[1]} years old.' for info in sorted_names]

    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))