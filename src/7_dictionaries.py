# Dictionary is a collection of key-value pairs. Each key-value pair maps the key to its associated value.
numbers = {
	1: "one",
	2: "two",
	3: "three"
}
print(numbers)
print(type(numbers)) # <class 'dict'>
print(numbers[1]) # one

information = {
	"name": "John",
	"age": 30,
	"city": "New York",
}

print(information)
print(information["name"])
print(information["age"])

del information["city"]
print(information)

# Methods
keys = information.keys()
values = information.values()
print(keys) # dict_keys(['name', 'age'])
print(values) # dict_values(['John', 30]) 