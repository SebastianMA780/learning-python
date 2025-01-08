# An Iterator is an object that can be iterated upon.
# But with the difference that it will be triggered manually. This is done through the next() function.
# The next() function will keep calling the next item until it reaches the end.
# This has the advantage of being more memory efficient, because it doesn't load all the items into memory at once.

my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
