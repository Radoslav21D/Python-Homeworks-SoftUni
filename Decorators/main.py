# A Simple Python Decorator

def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$$$$$$$$")
    return wrap


def sayhello():
    print("Hello")


newfunc = decor(sayhello)
newfunc()
