def logged(func):
    def wrapper(*args):
        func_result = func(*args)
        result = f"you called {func.__name__}{args}\nit returned {func_result}"
        return result  # Връщаме резултат от функцията wrapper

    return wrapper     # Връщаме референция не резултат!


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# @logged
# def sum_func(a, b):
#    return a + b


# print(sum_func(1, 4))
