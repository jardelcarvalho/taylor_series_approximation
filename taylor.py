""" 
2^64 < 21!
1 / k! = (1 / 1) * (1 / 2) * ... * (1 / (k - 1)) * (1 / k) 
"""

import math, sys

def taylor(x, x0, n):
    fx = math.e ** x0
    dx = lambda : -fx if x < 0 else fx
    fac = lambda k : 1 if k == 0 else (1 / k) * fac(k - 1)
    p = 0
    for k in range(0, n + 1):
        p += fx * ((x - x0) ** k) * fac(k)
        fx = dx()
    return p

x, x0, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
print('Pn(x): ' + str(taylor(x, x0, n)))
print('f(x):  ' + str(math.e ** x))