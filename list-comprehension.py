# You can use a for loop to create a list of elements in three steps:

#     1. Instantiate an empty list.
#    2.  Loop over an iterable or range of elements.
#     3. Append each element to the end of the list.

squares = []
for i in range(10):
    squares.append(i * i)
print(squares)


# List comprehension

# variable_name = [exoression for i in iterable_object]

square = [i * i for i in range(10)]
print(square)


language = "Javascripts"
list_lang = []
for n in language:
    list_lang.append(n)
print(list_lang)


program_language = [n for n in language]
print(program_language)


numbers = [i for i in range(11)]  # to generate number from 0 to 10
print(numbers)

# It is possible to do mathematical operation during iteration
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Generating even numbers
# to generate even number between 0 to 21
even_numbers = [m for m in range(21) if m % 2  == 0]
print(even_numbers)

# Filter numbers: let's filter positive and even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
print(len(numbers))


positive_event_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_event_numbers)


# Flattening two dimensional array
two_multi_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(two_multi_list[0][1])
flat_list = [number for x in two_multi_list for number in x]
print(flat_list)

sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant(sentence))

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)


def get_price(price):
    return price if price > 0 else 0

prices = [get_price(i) for i in original_prices]
print(prices)