# You can use the try-except block to handle exceptions in Python.
# The try except contains the code that might throw an exception.
# then you can use the except block to handle the exception.
# You can use multiple except blocks to handle different exceptions.

try:
	dividend = int(input("Enter the dividend: "))
	result = 100 / dividend
	print("Result: ", result)
except ZeroDivisionError:
	print("Error: Division by zero")
except ValueError:
	print("Error: Invalid input")
except Exception as e:
	print("Input Error")


# Exceptions has a hierarchy in Python. following is the hierarchy of exceptions in Python.
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)
