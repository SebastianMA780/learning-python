import multiprocessing

def print_square(num):
		return num * num

if __name__ == "__main__":
        numbers = [1, 2, 3, 4, 5, 6]
	
        with multiprocessing.Pool() as pool:
                results = pool.map(print_square, numbers)
				
        print(results)