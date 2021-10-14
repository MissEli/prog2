#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

def main():
	start = pc()
	f = Integer(30)
	f.fib()
	print(f.get())
	end = pc()
	print(f"Process took {round(end-start,2)} seconds")

if __name__ == '__main__':
	main()
