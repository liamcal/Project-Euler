import math

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def rotate(n,t):
	for i in range(t):
		n = (str(n)[1:] + str(n)[0])
	return int(n)



primes = set(primes_sieve(1000000))
circular= set([2,5])
for n in primes:
	if(not any(i in str(n) for i in ['2','4','5','6','8','0']) and n not in circular):
		if all( rotate(n,i) in primes for i in range(len(str(n)))):
			circular.update([rotate(n,i) for i in range(len(str(n)))])
print(len(circular))
