def outer(func):
    counter = 0
    def inner():
        nonlocal counter
        print("inner() wurde " + str(counter) + "x ausgeführt")
        counter = counter +1
        func()
    return inner


@outer
def do_something():
    print("do_something() wurde ausgeführt")

do_something()
do_something()
do_something()
do_something()
do_something()
