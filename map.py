def multiply_number(a):
    return a*a


x = map(multiply_number, (1, 2, 3, 4))  # x is the map object
# print(x)
print(list(x))


vowel = ("abc", "dcsgd", "hdkfn", "hdjdmfmf")
# vowel = tuple()
print(vowel)

const = {"dog", 'cat', "sheep", "ram"}
# const = set()
print(const)

def func(a, b):
    return a + b


a = map(func, [2, 4, 5], [1, 2, 3])
print(a)
print(list(a))


tup = (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = map(lambda x: x+3, tup)
print(tuple(newtuple))
