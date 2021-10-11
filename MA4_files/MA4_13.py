""" MA4_12.py

Student: Elizaveta Yakovleva
Mail: elizveta.y@outlook.com
Reviewed by:
Date reviewed:
"""

# for multiprocessing
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
# from 1.2
import math
import random as rand
import numpy as np
import functools

def hyper(n,d):
    nc = 0

    for j in range(0,n):
        X = [rand.uniform(-1,1) for i in range(0,d)]
        
        f = lambda x: x**2
        if functools.reduce(lambda x,y: x+y, map(f,X)) <= 1:
            nc += 1
    
    V = nc/n*2**d
    Vd = math.pi**(d/2)*1/math.gamma(d/2+1)
    return V,Vd


if __name__ == "__main__":
    start = pc()
    print('(approximate, exact)')
    with future.ProcessPoolExecutor() as ex:     # parallellprogrammering
        
        n = [1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000]
        d = [11,11,11,11,11,11,11,11,11,11]
        results = ex.map(hyper, n, d)

        for r in results:
            print(r)
    end = pc()
    print(f"Process took {round(end-start,2)} seconds")
# Process took 65.66 seconds (multiprocessing)
# Process took 210.53 seconds (old code)
# 3 times faster with multiple processors because can split up work between three processors
