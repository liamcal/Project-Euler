import math


def gen_sieve(ceiling=None):
    if ceiling is not None:
        if ceiling % 2 == 0:
            ceiling -= 1
        highest_prime = math.ceil(math.sqrt(ceiling))
    last_val = 1
    found_primes = []
    yield 2
    while ceiling is None or ceiling > last_val:
        current_val = None
        while current_val is None:
            current_val = last_val = last_val + 2
            for prime, square in found_primes:
                if current_val < square: 
                    break
                if current_val % prime == 0:
                    current_val = None
                    break
        yield current_val
        if ceiling is None or highest_prime > last_val:
            found_primes.append((current_val, current_val ** 2))

def isprime(n):
    for fac in gen_sieve(int(math.ceil(math.sqrt(n)))):
        if n % fac == 0 and n != fac:
            return fac
    return 0
def is_prime(n):
    if n == 2 or n == 3: 
        return True
    elif n < 2 or n % 2 == 0: 
        return False
    elif n < 9:
        return True
    elif n % 3 == 0: 
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0: 
            return False
        else:
            f += 6
    return True

def rotate(n,t):
	for i in range(t):
		n = int(str(n)[1:] + str(n)[0])
	return n
def all_prime(n):
	for i in range(len(str(n))):	
		checked.add(rotate(n,i))	
	if all(is_prime((rotate(n,i))) for i in range(len(str(n)))):
		for i in range(len(str(n))):	
			primes.add(rotate(n,i))


primes = set(gen_sieve(100))
circular= set()
for n in primes:
	if all( rotate(n,i) in primes for i in range(len(str(n)))):
		circular.add(n)
print(primes) 
print(len(primes))