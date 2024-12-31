# Description: Using __name__ == '__main__' to execute code only when the script is run as the main program
# this is useful when you want to run some code when the script is run as the main program, but not when it is imported as a module

def sum(a: int, b: int) -> int:
		return a + b

if __name__ == '__main__':
	print('executing as main program')
	print('sum(1, 2) =', sum(1, 2))
