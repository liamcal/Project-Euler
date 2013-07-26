from math import sqrt
from itertools import permutations
import timeit

def is_prime(n):
    if n == 2 or n == 3: 
        return True
    elif n < 2 or n % 2 == 0: 
        return False
    elif n < 9:
        return True
    elif n % 3 == 0: 
        return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: 
            return False
        else:
            f += 6
    return True
pp = []
j = lambda x:int(''.join(str(i) for i in x))
for t in range(1000):
    start = timeit.default_timer()
    for p in sorted({j(i) for i in set(permutations([i for i in range(1,8)]))},reverse=True):
        if is_prime(p): 
            break
    stop = timeit.default_timer()
    pp.append(stop - start)
print(p)
print(sum(pp)/len(pp))
print(pp)