""" MA4_11.py

Student: Elizaveta Yakovleva
Mail: elizveta.y@outlook.com
Reviewed by:
Date reviewed:
"""

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt


def spread(n):
    v = []
    for n in range(0,n):
        x = rand.uniform(-1,1)
        y = rand.uniform(-1,1)

        v.append([x,y])

    return v

# def in_circle(v):

#     nc = 0
#     vc = []
#     vo = []
#     for w in v:
#         x = w[0]
#         y = w[1]

#         if (x**2 + y**2 <= 1):
#             nc += 1
#             vc.append([x,y])
#         else:
#             vo.append([x,y])
        
#     return nc, vc, vo

    
    

def main():
    # n = int(input('Give an integer n: '))

    for n in [1000, 10000, 100000]:
        v = spread(n)

        nc = 0
        xc, yc, xo, yo = [], [], [], []

        for w in v:
            x = w[0]
            y = w[1]

            if (x**2 + y**2 <= 1):
                nc += 1
                xc.append(x)
                yc.append(y)
            else:
                xo.append(x)
                yo.append(y)

        pi_a = 4*(nc/n)

        print('approximate: ', pi_a)
        print('math pi: ', math.pi)
        
        
        plt.plot(xc,yc,'ro',xo,yo,'bo')
        plt.axis([-1,1,-1,1])
        # plt.show()

        fname = "n" + str(n) + ".png"
        plt.savefig(fname)

if __name__ == '__main__':
	main()