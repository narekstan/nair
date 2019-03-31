from __future__ import print_function

import doctest


def fib(n):
	"""
	This is the block comment for the function!
	>>> fib(1)
	1
	>>> fib(2)
	1
	>>> fib(3)
	2
	>>> fib(6)
	8
	>>> fib(7)
	13
	>>> fib(8)
	21
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
