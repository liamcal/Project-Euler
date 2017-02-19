import itertools
#Generate all primes <= n
def prime_sieve(n):
    a = [True for _ in range(n+1)]
    a[0] = a[1] = False
    for i, res in enumerate(a):
        if res:
            yield i
            for n in range(i*i, n, i):
                a[n] = False

primes = list(prime_sieve(10000))

prime_squares = [p ** 2 for p in primes if p ** 2 < 50000000]
prime_cubes = [p ** 3 for p in primes if p ** 3 < 50000000]
prime_quarts = [p ** 4 for p in primes if p ** 4 < 50000000]

can_make = map(sum,itertools.product(prime_squares, prime_cubes, prime_quarts))
valid = set(i for i in can_make if i < 50000000)
print(len(valid))
