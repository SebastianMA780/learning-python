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

# Tuples: are similar to lists but they are immutable, meaning you can't change the values in a tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers)) # <class 'tuple'>

numbers_tuple_format = 1, 2, 3, 4, 5
print(numbers_tuple_format)
print(type(numbers_tuple_format)) # <class 'tuple'>

# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment
