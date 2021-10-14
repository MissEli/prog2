#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

def main():
	for n in [30,32,35,37,40,43,45]:
		start = pc()
		f = Integer(n)
		print(f.fib())
		print(f.get())
		end = pc()
		print(f"Process took {round(end-start,2)} seconds")

if __name__ == '__main__':
	main()
