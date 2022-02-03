my_list = [1, 3, 6, 10]  # the list

print([x**2 for x in my_list])  # using list comprehension

print((x**2 for x in my_list))  # using generator expression


def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

