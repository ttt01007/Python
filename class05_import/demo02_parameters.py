def print_str_1(first, *second):
    print(first)
    print(second)


print_str_1(1, 2, 3, 4, 5, 6)


def print_str_2(first, *second, third):
    print(first)
    print(second)
    print(third)


print_str_2(1, third=3)


def print_str_3(first, **kwargs):
    print(first)
    print(kwargs)


print_str_3(1, second=2, third=3)


def print_str_4(first, *args, **kwargs):
    print(first)
    print(args)
    print(kwargs)


print_str_4(1, 2, 3, name='jianyu', age=18)
