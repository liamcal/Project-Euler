import math
import itertools
import time

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield int(divisor)

def isAbundant(n):
    s = (set(divisorGenerator(n)))
    s.remove(n)
    return sum(s) > n

# abundants = set(i for i in range(1,28123) if isAbundant(i))
# toCheck = set(i for i in range(1,28123))
# sums = set(i[0]+i[1] for i in itertools.combinations_with_replacement(abundants,2))
# print(sum(toCheck - sums))
t0 = time.clock()
print(sum(set(i for i in range(1,28123)) - set(i[0]+i[1] for i in itertools.combinations_with_replacement(set(i for i in range(1,28123) if isAbundant(i)),2))))
t1 = time.clock()
print(t1-t0)