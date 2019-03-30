from __future__ import print_function

import doctest


def fib(n):
	"""
	This is the block comment for the function!
	>>> fib(4)
	3
	>>> fib(2)
	1
	>>> fib(3)
	2
	"""
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def main():
	"""
	This is the doc-string for the main method!
	"""
	doctest.testmod() # puts in testing mode..
	print("Hello World!")
	# n = 5
	# res = fib(n)
	# print("Fibonacci function result for n=%d is %d"%(n, res))

if __name__ == '__main__':
	main()
