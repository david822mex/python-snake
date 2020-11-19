# 1. positional arguments, the order matters. -------------------------------------------
def function1(a, b, c):
    print(a, b, c)


# now to call it
function1(1, 2, 3)


# 2. keyword arguments, they have some default values.-----------------------------------
# so if we don't pass any arguments when we call the function, it still works.
def function2(name: str = "name", age: int = 2):
    print(name, age)


# now to call it
function2(name="David", age=10)


# 3.Many positional arguments *args.  args is of type "tuple" ---------------------------
# we can pass any number of arguments when we call the function.
def function3(*args: float):
    sum_of_args = 0
    for arg in args:
        sum_of_args += arg
    print(sum_of_args)
    print(type(args))


# now to call it
function3(1, 2, 4)


# 4.Many Keyword Arguments: **kwargs. kwargs is of type "dict" --------------------------
def function4(**kwargs):
    make = kwargs["make"]
    model = kwargs["model"]
    year = kwargs["year"]
    print(make, model, year)
    print(type(kwargs))


# now to call it
function4(make="Honda", model="E", year="2020")
