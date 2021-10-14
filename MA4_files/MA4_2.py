#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

def main():
	start = pc()
	n = 30
	f = Integer(n)
   	f.fib()
   	print(f.get())
    	end = pc()
    	print(f"Process took {round(end-start,2)} seconds")

if __name__ == '__main__':
	main()
