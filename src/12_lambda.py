# lambda is a small anonymous function
# lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a: a + 10
print(x(5))

even_numbers = list(filter(lambda x: x % 2 == 0, range(1, 11)))
print(even_numbers)
