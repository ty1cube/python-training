Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numb = filter(is_even, numbers)
# print(even_numb)
print(list(even_numb))       # [2, 4]


numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numb = filter(is_odd, numbers)
print(list(odd_numb))


# Filter long name
names = [ 'Noheemat', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

def add_two(x, y):
    return int(x) + int(y)


total = reduce(add_two, numbers_str)
print(total)
