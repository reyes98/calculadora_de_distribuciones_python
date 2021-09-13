from math import factorial,pi,e

def combinatoria(m, n): 
    return factorial(m) // (factorial(n) * factorial(m - n))

