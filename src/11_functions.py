def greet(name, greeting='Hello'):
		print(f'{greeting}, {name}!')

greet('Developer') # Hello, Developer!

def add(a, b):
		return a + b

result = add(2, 3)
print(result) # 5


#### 

def find_volume(length=1, width=1, height=1):
		return length * width * height , height

result = find_volume(width=10)

print(result) # returns a tuple (10, 1) 