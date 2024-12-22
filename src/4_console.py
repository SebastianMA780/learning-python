# get user input
name = input("Enter your name: ")
print("Hello, " + name)

age = input("Enter your age: ")
print(type(age)) # any value inserted by input will be <class 'str'>

age = int(age) # convert str to int
print(type(age)) # now age is <class 'int'>
