import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def email_parse(email):
    found_info = EMAIL.findall(email)
    if found_info and found_info[0]:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    return f'username: "{name}", domain: "{addr}"'

print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))


from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=',')
        return func(*args)
    return wrapper

@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))

a = calc_cube(5, 3)

print(a)
print(calc_cube.__name__)


from functools import wraps

def val_checker(deco_func):
    def val_checker_2(calc_cube_func):
        @wraps(calc_cube_func)
        def wrapped(x):
            if deco_func(x):
                return calc_cube_func(x)
            else:
                raise ValueError(x)
        return wrapped
    return val_checker_2


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

a = calc_cube(5)

print(a)
print(calc_cube.__name__)

