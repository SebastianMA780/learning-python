#### STRINGS
string = "New string"

#consult the type of the variable
print(type(string)) #output <class 'str'>

line_break = ''' This is a multiline string
and works with three single quote.
'''

print(line_break)

## string operations

# Concatenation
string1 = "Hello"
string2 = "World"
concatenation = string1 + " " + string2

# length of a string
print(len(concatenation))


##### NUMBERS

# integers
integer_number = 10
print(type(integer_number)) #output <class 'int'>

# float
float_number = 10.5
print(type(float_number)) #output <class 'float'>

# operations
print(integer_number + float_number) #output 20.5, the result is a float so for example a user can send a number that can lead to errors in the code if the code is not properly handled

#### BOOLEANS
is_true = True
is_false = False
print(type(is_true)) #output <class 'bool'>