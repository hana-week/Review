import math

def a(n):
    if n<1:
        return 1
    else:
        return 1+n*a(n-1)

def b(n):
    return a(n)/math.factorial(n)

for i in range(1,10):
    print('(n=%d)'%i,b(i))
