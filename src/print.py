#Basic usage of the print function
print("Hello World") #output: Hello World

# You can pass multiple arguments to the print function
print("Never", "Give", "Up") #output: Never Give Up

# sep argument is used to separate the arguments passed to the print function
print("Never", "Give", "Up", sep=", ") #output: Never, Give, Up

# end argument
print("Never", end=" ")
print("Give up") #output: Never Give up

# variables printing
name = "Python"
print("Amazing language:", name, ", Popular language:", name) #output: Amazing language: Python , Popular language: Python

# f-string formatting allows you to embed expressions inside string literals, using curly braces {}.
name = "Python"
print(f"Amazing language: {name}, Popular language: {name}") #output: Amazing language: Python, Popular language: Python

# format method
name = "Python"
print("Amazing language: {}, Popular language: {}".format(name, name)) #output: Amazing language: Python, Popular language: Python

# line break and special characters
print("Hello\nWorld") #output: Hello
											#        World

# escape characters
print("Hello \'World\'") #output: Hello    World
print("file path: C:\\Users\\Usuario\\Desktop\\archivo.txt") #output: file path: C:\Users\Usuario\Desktop\archivo.txt
