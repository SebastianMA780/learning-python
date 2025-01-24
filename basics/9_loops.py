numbers = [1, 2, 3, 4, 5]
for i in numbers:
	print(i)

for i in range(10):
	print(i)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
	if fruit == "banana":
		print("I found the banana!")
		break


x = 0
while x < 10:
	if x == 5:
		break
	
	print(x)
	x += 1
	