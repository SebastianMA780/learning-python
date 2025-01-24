# *args is used to pass a variable number of non-keyworded arguments to a function.
# **kwargs is used to pass a variable number of keyworded arguments to a function.
# args is a tuple, and kwargs is a dictionary.
# args y kwargs are just a convention. you can use any other name.

def test_args_kwargs(arg1, *args, **kwargs):
		print("arg1:", arg1)
		print("args:", args)
		print("kwargs:", kwargs)

test_args_kwargs(1.1, 1, 2, "a", 3, 4, 5, a=6, b=7)
