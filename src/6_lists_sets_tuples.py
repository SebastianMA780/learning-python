### -- LISTS -- ###
# Lists are ordered collections of elements

to_do_list = ["Go to the gym", "Buy groceries", "Clean the house"]
print(to_do_list)

numbers = [1, 2, 3, 4, "five"]
print(numbers)
print(type(numbers)) # <class 'list'>

# Accessing elements in a list
print(numbers[0]) # 1
print(numbers[1]) # 2
print(numbers[-1]) # five , get the last element

# Matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix)) # <class 'list'>
print(matrix[0][2])



### -- TUPLES -- ###
# are similar to lists but they are immutable, meaning you can't change the values in a tuple

numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers)) # <class 'tuple'>

numbers_tuple_format = 1, 2, 3, 4, 5
print(numbers_tuple_format)
print(type(numbers_tuple_format)) # <class 'tuple'>
# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment



### -- SETS -- ###
# Sets are unordered collections of elements
# Sets cant have duplicates

numbers = {1, 2, 3, 4, 5, 5, 5, 5}
print(type(numbers)) # <class 'set'>
print(f'numbers set: {numbers}') # {1, 2, 3, 4, 5}

set_from_list = set([1, 2, 3, 4, 5, 5, 5, 5])
print(type(set_from_list)) # <class 'set'>
print(f'set_from_list: {set_from_list}') # {1, 2, 3, 4, 5}

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇
new_set = countries.union(northAm, centralAm, southAm)

print(new_set)



## -- COMPREHENSION LISTS -- ##
# List comprehensions are a way to create lists in a more concise way
# [expression for item in iterable if condition]
squares = [i**2 for i in range(10) if i % 2 == 0]
print(f'comprehensions list: {squares}') # [0, 4, 16, 36, 64]
