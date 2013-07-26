import math
import random
def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def miller_rabin(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


primes = 0
corners = 0
ratio = 0

d = 0
n = 3 
while True:
    d += 2
    primes += len([x for x in [n + d*i for i in range(4)]if miller_rabin(x)])
    corners += 4
    ratio = primes/corners
    if ratio < 0.1:
        break
    n = n + 4*d + 2
print(d-1)
