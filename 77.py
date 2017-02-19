def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

n = 1000

coins = sieve_for_primes_to(n)

for t in range(5,n):
    target = t
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin,target+1):
            ways[i]+=ways[i-coin]
    if ways[target] > 5000:
        print(target, ways[target])
        break
