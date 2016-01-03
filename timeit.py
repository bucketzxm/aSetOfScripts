from __future__ import print_function
import time
from functools import wraps


def timeit(func):
	'''
	Decorator that reports the exec time
	'''

	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__, end-start)
		return result
	return wrapper 


if __name__ == "__main__":
	@timeit
	def test():
		for i in range(10):
			print(i)

	test()
