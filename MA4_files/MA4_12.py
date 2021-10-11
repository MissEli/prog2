""" MA4_12.py

Student: Elizaveta Yakovleva
Mail: elizveta.y@outlook.com
Reviewed by:
Date reviewed:
"""

import math
import random as rand
import numpy as np
import functools
# for 1.3
from time import perf_counter as pc

def hyper(n,d):
    nc = 0
    # X = [[rand.uniform(-1,1) for i in range(0,n)] for j in range(0,d)]

    for j in range(0,n):
        X = [rand.uniform(-1,1) for i in range(0,d)]
        
        f = lambda x: x**2
        if functools.reduce(lambda x,y: x+y, map(f,X)) <= 1:
            nc += 1
    
    V = nc/n*2**d
    Vd = math.pi**(d/2)*1/math.gamma(d/2+1)

    return V,Vd
    

def main():

    start = pc()
    for d in [11]:
        n = 10000000
        
        V = hyper(n,d)

        print('approximate: ', V[0])
        print('exact: ', V[1])
    end = pc()
    print(f"Process took {round(end-start,2)} seconds")
    # Process took 210.53 seconds

if __name__ == '__main__':
	main()