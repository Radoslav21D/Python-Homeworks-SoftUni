def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        first_letter = name[0]
        result[name] = kwargs[first_letter]
    return result


print(age_assignment("Peter", "George", G=26, P=19))  # {'Peter': 19, 'George': 26}
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
