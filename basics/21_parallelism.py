# Parallelism means that multiple processes are running at the same time.
# This is posible by using multiple cores in the CPU, each core can run a process

import multiprocessing

def print_square(num):
		return num * num

if __name__ == "__main__":
        numbers = [1, 2, 3, 4]
	
        with multiprocessing.Pool(4) as pool:
                results = pool.map(print_square, numbers)
				
        print(results)