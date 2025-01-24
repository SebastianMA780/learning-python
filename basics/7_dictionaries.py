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


### -- Dictionary comprehensions -- ###
# {key: value for item in iterable if condition}
dict_v1 = {}
for i in range(10):
	if i % 2 == 0:
		dict_v1[i] = i**2


print('dict v1:', dict_v1)

dict_v2 = {i: i**2 for i in range(10) if i % 2 == 0}
print('dict v2:', dict_v2)
